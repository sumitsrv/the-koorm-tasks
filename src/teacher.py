"""Teacher backends — chosen at runtime, not hard-coded.

v1 distilled from a local `qwen3:8b` over Ollama. That still works and is still
the zero-cost, fully-offline option, so it stays. What changed is that it is now
*a* choice rather than *the* pipeline: `generate.py --teacher claude` uses the
Anthropic API instead, for cases where the teacher's own quality is the limiting
factor.

Both backends implement the same two calls, so `generate.py` doesn't care which
is behind them:

    plan(description)   -> parsed plan dict, or None
    variations(axis, n) -> list of task description strings

Neither backend decides what lands in the training set. Whatever a teacher
returns is validated by `quality.check_plan` before it is written, so swapping
to a cheaper or weaker teacher lowers throughput and yield — never the floor.

Choosing:
  ollama  — free, offline, no API key. Bounded by what an 8B model can produce;
            that ceiling is exactly what produced v1's label collapse and its
            2023 dates. Needs `ollama pull qwen3:8b`.
  claude  — costs money and needs `ANTHROPIC_API_KEY` (or `ant auth login`).
            Schema is enforced server-side via structured outputs, so rejects
            are content problems rather than malformed JSON.
"""

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from config import TEACHER_MODEL
from prompts import SYSTEM_PLAN, SYSTEM_VARIATIONS, build_plan_prompt
from schema import PlanResponse

# Default model per backend. Sonnet is the Claude default because this is
# high-volume, structurally-constrained generation: the schema is enforced by
# `output_format` and the content gates live in quality.py, so an Opus-tier
# teacher buys little per dollar here. Pass --model to override either.
DEFAULT_MODELS = {
    "ollama": TEACHER_MODEL,       # qwen3:8b, from config.py
    "claude": "claude-sonnet-5",   # or claude-opus-5 for the hardest slices
}


def _extract_json_object(text: str) -> dict | None:
    """First JSON object in the text, thinking block and fences stripped."""
    clean = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL).strip()
    m = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", clean, re.DOTALL) or \
        re.search(r"\{.*\}", clean, re.DOTALL)
    if not m:
        return None
    try:
        return json.loads(m.group(1) if m.re.groups else m.group(0))
    except json.JSONDecodeError:
        return None


def _extract_json_array(text: str) -> list[str]:
    clean = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL).strip()
    start, end = clean.find("["), clean.rfind("]")
    if start < 0 or end <= start:
        return []
    try:
        arr = json.loads(clean[start:end + 1])
    except json.JSONDecodeError:
        return []
    return [s.strip() for s in arr if isinstance(s, str) and s.strip()]


# ---------------------------------------------------------------------------
# Ollama (local, free, offline) — the v1 path, kept intact
# ---------------------------------------------------------------------------

class OllamaTeacher:
    """Local model over Ollama. Requires `ollama pull <model>` first."""

    name = "ollama"

    def __init__(self, model: str, retries: int = 2):
        from ollama import Client  # imported lazily so the Claude path needs no ollama
        self.client = Client()
        self.model = model
        self.retries = retries

    def _chat(self, messages: list[dict]) -> str | None:
        for attempt in range(self.retries):
            try:
                resp = self.client.chat(model=self.model, messages=messages)
                content = resp.message.content or ""
                thinking = getattr(resp.message, "thinking", "") or ""
                # Keep the thinking trace out of the training target, but leave
                # it in the raw text so the JSON extractor sees the same shape
                # v1's did.
                if thinking and "<think>" not in content:
                    content = f"<think>\n{thinking}\n</think>\n\n{content}"
                return content
            except Exception as e:  # noqa: BLE001 — surface and retry, don't crash the run
                print(f"    retry {attempt + 1}: {e}", file=sys.stderr, flush=True)
        return None

    def plan(self, description: str) -> tuple[dict | None, str]:
        raw = self._chat(build_plan_prompt(description))
        if raw is None:
            return None, "teacher unreachable"
        parsed = _extract_json_object(raw)
        if parsed is None:
            return None, "no JSON in reply"
        try:
            return PlanResponse.model_validate(parsed).model_dump(mode="json"), ""
        except Exception as e:  # noqa: BLE001
            return None, f"schema: {type(e).__name__}"

    def variations(self, axis: str, n: int = 20) -> list[str]:
        raw = self._chat([
            {"role": "system", "content": SYSTEM_VARIATIONS.format(n=n, axis=axis)},
            {"role": "user", "content": "/think\nGenerate the tasks now."},
        ])
        return _extract_json_array(raw) if raw else []


# ---------------------------------------------------------------------------
# Claude (hosted) — structured outputs pin the schema server-side
# ---------------------------------------------------------------------------

class ClaudeTeacher:
    """Anthropic API. Resolves ANTHROPIC_API_KEY, ANTHROPIC_AUTH_TOKEN, or an
    `ant auth login` profile — nothing needs to be passed in or hardcoded."""

    name = "claude"

    def __init__(self, model: str, max_tokens: int = 2048):
        import anthropic  # imported lazily so the Ollama path needs no anthropic
        self.anthropic = anthropic
        self.client = anthropic.Anthropic()
        self.model = model
        self.max_tokens = max_tokens

    def _system(self, text: str) -> list[dict]:
        """Marked for prompt caching: identical on every call in a run, so after
        the first it is read at a fraction of the input price. A prompt below the
        model's cacheable minimum simply doesn't cache — no error either way."""
        return [{"type": "text", "text": text, "cache_control": {"type": "ephemeral"}}]

    def plan(self, description: str) -> tuple[dict | None, str]:
        msgs = build_plan_prompt(description)
        try:
            # output_format pins the reply to the Pydantic schema server-side,
            # so a malformed shape can't reach the content gates at all.
            resp = self.client.messages.parse(
                model=self.model,
                max_tokens=self.max_tokens,
                system=self._system(msgs[0]["content"]),
                messages=[msgs[1]],
                output_format=PlanResponse,
            )
        except self.anthropic.APIStatusError as e:
            return None, f"{type(e).__name__}: {e.message[:60]}"
        except self.anthropic.APIConnectionError:
            return None, "connection error"

        if resp.stop_reason == "refusal":
            return None, "refused"
        if resp.parsed_output is None:
            return None, "no parsed output (truncated?)"
        return resp.parsed_output.model_dump(mode="json"), ""

    def variations(self, axis: str, n: int = 20) -> list[str]:
        try:
            resp = self.client.messages.create(
                model=self.model,
                max_tokens=2048,
                system=self._system(SYSTEM_VARIATIONS.format(n=n, axis=axis)),
                messages=[{"role": "user", "content": "Generate the tasks now."}],
            )
        except (self.anthropic.APIStatusError, self.anthropic.APIConnectionError) as e:
            print(f"    ! {type(e).__name__} on '{axis[:34]}…'", file=sys.stderr)
            return []
        return _extract_json_array("".join(b.text for b in resp.content if b.type == "text"))


TEACHERS = {"ollama": OllamaTeacher, "claude": ClaudeTeacher}


def build(name: str, model: str | None = None):
    """Instantiate a teacher by name, with that backend's default model."""
    if name not in TEACHERS:
        raise SystemExit(f"unknown teacher {name!r} — choose from {sorted(TEACHERS)}")
    return TEACHERS[name](model or DEFAULT_MODELS[name])
