"""Generate training data by distilling from a local teacher model via Ollama.

Supports resuming: re-run the script and it picks up where it left off.
Descriptions are cached in data/descriptions.json so variations are stable across runs.
"""

import json
import random
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from ollama import Client
from tqdm import tqdm

from config import DATA_DIR, TEACHER_MODEL, PLAN_EXAMPLES_TARGET, SCHEDULE_EXAMPLES_TARGET
from prompts import build_plan_prompt, build_schedule_prompt, build_variation_prompt
from scenarios import TASK_SEEDS, ALL_SEEDS, NEW_TASK_SEEDS, generate_random_schedule
from schema import PlanResponse, ScheduleResponse


client = Client()


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def count_lines(path: Path) -> int:
    if not path.exists():
        return 0
    with open(path, encoding="utf-8") as f:
        return sum(1 for line in f if line.strip())


def extract_json(text: str) -> dict | None:
    """Pull the first valid JSON object from model output."""
    clean = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL).strip()
    # Try markdown fences first
    m = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", clean, re.DOTALL)
    if m:
        try:
            return json.loads(m.group(1))
        except json.JSONDecodeError:
            pass
    # Try raw JSON
    m = re.search(r"\{.*\}", clean, re.DOTALL)
    if m:
        try:
            return json.loads(m.group(0))
        except json.JSONDecodeError:
            pass
    return None


def call_teacher(messages: list[dict], retries: int = 2) -> str | None:
    """Call the teacher model with thinking enabled. Returns content with <think> tags."""
    for attempt in range(retries):
        try:
            resp = client.chat(model=TEACHER_MODEL, messages=messages)
            msg = resp.message
            content = msg.content or ""
            thinking = getattr(msg, "thinking", "") or ""
            if thinking and "<think>" not in content:
                content = f"<think>\n{thinking}\n</think>\n\n{content}"
            return content
        except Exception as e:
            print(f"  retry {attempt + 1}: {e}", file=sys.stderr, flush=True)
    return None


def extract_json_array(text: str) -> list[str]:
    """Extract a JSON array of strings from model output."""
    clean = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL).strip()
    m = re.search(r"\[.*\]", clean, re.DOTALL)
    if m:
        try:
            arr = json.loads(m.group(0))
            return [s for s in arr if isinstance(s, str)]
        except json.JSONDecodeError:
            pass
    return []


# ---------------------------------------------------------------------------
# Quality filters — Pydantic checks shape; these check that the teacher's
# output is actually *sensible*. Lenient: reject clear violations only.
# ---------------------------------------------------------------------------

def _to_min(hhmm: str) -> int:
    h, m = hhmm.split(":")
    return int(h) * 60 + int(m)


def valid_plan(parsed: dict) -> bool:
    task = parsed["task"]
    dur = task["estimated_duration"]
    subs = task.get("subtasks") or []
    # Rule from the prompt: tasks >30 min get broken into subtasks
    if dur > 30 and len(subs) < 2:
        return False
    # Subtask minutes should roughly track the estimate (+buffer), not be wild
    if subs:
        total = sum(s["estimated_minutes"] for s in subs)
        if not (0.5 * dur <= total <= 2.0 * dur):
            return False
    return True


def valid_schedule(parsed: dict) -> bool:
    blocks = parsed["schedule"].get("time_blocks") or []
    if not blocks:
        return False
    spans = []
    for b in blocks:
        try:
            s, e = _to_min(b["start_time"]), _to_min(b["end_time"])
        except (ValueError, KeyError):
            return False
        if s >= e or e > 17 * 60:          # zero-length/backwards, or past 17:00
            return False
        spans.append((s, e, b))
    spans.sort()
    for (_, prev_e, _), (next_s, _, _) in zip(spans, spans[1:]):
        if next_s < prev_e:                # overlap
            return False
    # Deferred tasks must actually be gone from the schedule
    titles = {b.get("title") for b in blocks} | {b.get("task_title") for b in blocks}
    if any(d in titles for d in parsed.get("deferred_tasks", [])):
        return False
    return True


# ---------------------------------------------------------------------------
# Phase 1: Expand seed scenarios (cached to disk)
# ---------------------------------------------------------------------------

def expand_seeds(target: int = PLAN_EXAMPLES_TARGET) -> list[str]:
    """Expand seeds to `target` descriptions, topping up data/descriptions.json.

    Only ever appends (seeds stay at the front), so an existing cache and any
    plans already generated from it remain valid. Re-run to top up further.
    """
    cache = DATA_DIR / "descriptions.json"
    descs = json.loads(cache.read_text(encoding="utf-8")) if cache.exists() else list(ALL_SEEDS)
    seen = set(descs)

    if len(descs) >= target:
        print(f"Loaded {len(descs)} cached descriptions (target {target}) from {cache}")
        return descs

    print(f"Expanding {len(descs)} → {target} descriptions …", flush=True)
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    rounds = 0
    while len(descs) < target and rounds < 10:  # ponytail: cap rounds so a repeating teacher can't spin forever
        rounds += 1
        for category in TASK_SEEDS:
            if len(descs) >= target:
                break
            resp = call_teacher(build_variation_prompt(category, n=20))
            if not resp:
                continue
            fresh = [v for v in extract_json_array(resp) if v not in seen]
            seen.update(fresh)
            descs.extend(fresh)
            print(f"  {category}: +{len(fresh)} (total {len(descs)})", flush=True)
        cache.write_text(json.dumps(descs, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Total descriptions: {len(descs)}", flush=True)
    return descs


# ---------------------------------------------------------------------------
# Phase 2: Generate plan examples (resumable)
# ---------------------------------------------------------------------------

def generate_plan_examples(descriptions: list[str]) -> int:
    out = DATA_DIR / "plan_train.jsonl"
    out.parent.mkdir(parents=True, exist_ok=True)

    done = count_lines(out)
    if done >= len(descriptions):
        print(f"\nPlan examples already complete ({done}/{len(descriptions)})", flush=True)
        return done

    remaining = descriptions[done:]
    print(f"\nResuming plan generation from {done}/{len(descriptions)} …", flush=True)

    count = done
    with open(out, "a", encoding="utf-8") as f:
        for desc in tqdm(remaining, desc="plans", initial=done, total=len(descriptions)):
            msgs = build_plan_prompt(desc)
            resp = call_teacher(msgs)
            if not resp:
                continue
            parsed = extract_json(resp)
            if not parsed:
                continue
            try:
                PlanResponse.model_validate(parsed)
            except Exception:
                continue
            if not valid_plan(parsed):
                continue
            answer = json.dumps(parsed, ensure_ascii=False)  # JSON only — drops <think>
            example = {"messages": [msgs[0], msgs[1], {"role": "assistant", "content": answer}]}
            f.write(json.dumps(example, ensure_ascii=False) + "\n")
            f.flush()
            count += 1
    print(f"Saved {count} plan examples → {out}", flush=True)
    return count


# ---------------------------------------------------------------------------
# Phase 3: Generate schedule-adjustment examples (resumable)
# ---------------------------------------------------------------------------

def generate_schedule_examples() -> int:
    out = DATA_DIR / "schedule_train.jsonl"
    out.parent.mkdir(parents=True, exist_ok=True)

    done = count_lines(out)
    target = SCHEDULE_EXAMPLES_TARGET
    if done >= target:
        print(f"\nSchedule examples already complete ({done}/{target})", flush=True)
        return done

    remaining = target - done
    print(f"\nResuming schedule generation from {done}/{target} …", flush=True)

    count = done
    with open(out, "a", encoding="utf-8") as f:
        for _ in tqdm(range(remaining), desc="schedules", initial=done, total=target):
            date = f"2026-{random.randint(1,12):02d}-{random.randint(1,28):02d}"
            schedule, tasks = generate_random_schedule(date=date)
            new_task = random.choice(NEW_TASK_SEEDS)

            sched_json = schedule.model_dump_json(indent=2)
            tasks_json = json.dumps([t.model_dump() for t in tasks], indent=2)

            msgs = build_schedule_prompt(sched_json, tasks_json, new_task)
            resp = call_teacher(msgs)
            if not resp:
                continue
            parsed = extract_json(resp)
            if not parsed:
                continue
            try:
                ScheduleResponse.model_validate(parsed)
            except Exception:
                continue
            if not valid_schedule(parsed):
                continue
            answer = json.dumps(parsed, ensure_ascii=False)  # JSON only — drops <think>
            example = {"messages": [msgs[0], msgs[1], {"role": "assistant", "content": answer}]}
            f.write(json.dumps(example, ensure_ascii=False) + "\n")
            f.flush()
            count += 1
    print(f"Saved {count} schedule examples → {out}", flush=True)
    return count


# ---------------------------------------------------------------------------
# Phase 4: Combine into single training file
# ---------------------------------------------------------------------------

def combine():
    combined = DATA_DIR / "train.jsonl"
    examples = []
    for name in ["plan_train.jsonl", "schedule_train.jsonl"]:
        p = DATA_DIR / name
        if p.exists():
            with open(p, encoding="utf-8") as f:
                examples.extend(json.loads(line) for line in f if line.strip())
    random.shuffle(examples)
    with open(combined, "w", encoding="utf-8") as f:
        for ex in examples:
            f.write(json.dumps(ex, ensure_ascii=False) + "\n")
    print(f"\nCombined {len(examples)} examples → {combined}", flush=True)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    descriptions = expand_seeds()
    generate_plan_examples(descriptions)
    generate_schedule_examples()
    combine()
    print("\nDone. Training data is in data/train.jsonl")


if __name__ == "__main__":
    main()
