"""Held-out evaluation for a trained planner checkpoint.

v1 had no eval beyond training loss on a 90/10 split, which is why its defects
shipped: a loss curve cannot show you that `priority` has collapsed to HIGH on
nine tasks in ten, that every `due_date` lands in 2023, or that the "good enough"
criterion is quietly demanding perfection. Every number below is one of those
blind spots made visible.

The tasks in EVAL_TASKS are held out — none appears in `data/`. Keep it that way;
if you add one to training, remove it here.

    ollama create koorm-planner -f Modelfile      # or whatever you tagged it
    python src/evaluate.py koorm-planner
    python src/evaluate.py koorm-planner --baseline qwen2.5:0.5b   # compare two

Requires only the standard library plus a running Ollama.
"""

import argparse
import json
import re
import sys
import time
import urllib.request
from collections import Counter
from itertools import combinations
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from config import OUTPUT_DIR
from prompts import SYSTEM_PLAN
from quality import check_plan
from schema import PlanResponse, Priority, TaskCategory

OLLAMA_URL = "http://localhost:11434/api/chat"

# Held-out tasks. Deliberately weighted toward the shapes v1 failed on: physical
# procedures, progression over time, unglamorous admin, and the avoidance-
# flavoured phrasing real users type.
EVAL_TASKS = [
    "Write a quarterly sales report for the board meeting next Monday",
    "Fix the dripping shower head",
    "Get the boiler serviced before winter",
    "Sort out the spare room, it's become a dumping ground",
    "Finish chapter 3 of my thesis",
    "Reply to the backlog of unread work emails",
    "Do my taxes",
    "Learn enough Kotlin coroutines to refactor our networking layer",
    "Rewrite the landing page copy — I keep restarting it because it's never good enough",
    "Get back into swimming after a year off",
    "Replace the broken laptop battery",
    "Plan my father's retirement party",
    "Cancel the broadband contract and switch provider",
    "Put together a photo book from the holiday",
    "Prepare for the driving test I've already failed once",
    "Clear the gutters before the autumn storms",
    "Write the reference my old colleague asked for",
    "Sort out the recycling system in the kitchen",
    "Set up a budget I'll actually stick to",
    "Repot the houseplants that have outgrown their pots",
]


def call(model: str, task: str, max_tokens: int = 768) -> tuple[str, float]:
    body = json.dumps({
        "model": model,
        "messages": [
            {"role": "system", "content": SYSTEM_PLAN},
            {"role": "user", "content": f"Plan this task: {task}"},
        ],
        "stream": False,
        "options": {"temperature": 0.6, "top_p": 0.95, "top_k": 20,
                    "num_predict": max_tokens},
    }).encode()
    req = urllib.request.Request(OLLAMA_URL, data=body,
                                 headers={"Content-Type": "application/json"})
    t0 = time.time()
    with urllib.request.urlopen(req, timeout=600) as r:
        data = json.load(r)
    return data["message"]["content"], time.time() - t0


def extract_json(text: str) -> dict | None:
    """Mirror the app's parser: strip the thinking block, fences, then take the
    first balanced object. If this can't read it, neither can the app."""
    text = re.sub(r"<think>.*?</think>", "", text, flags=re.S).strip()
    if text.startswith("<think>"):
        return None                      # truncated inside the thinking block
    text = re.sub(r"^```(?:json)?|```$", "", text.strip(), flags=re.M).strip()
    start = text.find("{")
    if start < 0:
        return None
    depth, in_str, esc = 0, False, False
    for i in range(start, len(text)):
        c = text[i]
        if esc:
            esc = False
        elif c == "\\" and in_str:
            esc = True
        elif c == '"':
            in_str = not in_str
        elif in_str:
            continue
        elif c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                try:
                    return json.loads(text[start:i + 1])
                except json.JSONDecodeError:
                    return None
    return None


def content_words(text: str) -> set[str]:
    stop = set("""a an the and or of for to in on at by with my me i it its this that from
into about before after up out over under again more most some such no nor not only own
same so than too very can will just get got make made take need go new next back""".split())
    return {w for w in re.findall(r"[a-z]+", text.lower()) if len(w) > 2 and w not in stop}


def evaluate(model: str) -> dict:
    print(f"\n{'=' * 74}\n{model}\n{'=' * 74}")
    results = []
    for task in EVAL_TASKS:
        raw, secs = call(model, task)
        obj = extract_json(raw)
        plan = obj.get("task") if isinstance(obj, dict) else None
        schema_ok, problems = False, ["unparseable"]
        if obj is not None:
            try:
                PlanResponse.model_validate(obj)
                schema_ok = True
                problems = check_plan(obj, task, strict=True)
            except Exception as e:
                problems = [f"schema: {type(e).__name__}"]
        results.append({"task": task, "plan": plan, "raw": raw, "secs": secs,
                        "parsed": obj is not None, "schema_ok": schema_ok,
                        "problems": problems})
        flag = "ok  " if schema_ok and not problems else "FAIL"
        print(f"[{flag}] {secs:5.1f}s  {task[:56]}")
        if problems and problems != ["unparseable"]:
            print(f"         {'; '.join(problems[:3])}")
        elif not obj:
            print(f"         unparseable: {raw[:90]!r}")

    n = len(results)
    plans = [r["plan"] for r in results if r["plan"]]
    clean = [r for r in results if r["schema_ok"] and not r["problems"]]

    print(f"\n-- structure --")
    print(f"  parseable JSON         {sum(r['parsed'] for r in results)}/{n}")
    print(f"  valid against schema   {sum(r['schema_ok'] for r in results)}/{n}")
    print(f"  passes quality gates   {len(clean)}/{n}")
    if results:
        secs = sorted(r["secs"] for r in results)
        print(f"  median latency         {secs[len(secs) // 2]:.1f}s")

    # The blind spots that let v1 ship.
    print(f"\n-- label collapse (v1: HIGH on 9/10) --")
    for field, enum in (("priority", Priority), ("category", TaskCategory)):
        counts = Counter(p.get(field) for p in plans)
        total = sum(counts.values()) or 1
        print(f"  {field:9s} " + ", ".join(f"{k} {v}" for k, v in counts.most_common()))
        top = counts.most_common(1)
        if top and top[0][1] / total > 0.6:
            print(f"    ^^ COLLAPSED: {top[0][0]} on {top[0][1]/total:.0%} of tasks")
        unknown = {k for k in counts if k not in {e.value for e in enum}}
        if unknown:
            print(f"    ^^ emitted values the app has no enum for: {unknown}")

    print(f"\n-- decomposition quality --")
    all_steps = [(p, s.get("title", "")) for p in plans for s in (p.get("subtasks") or [])]
    if all_steps:
        # Templating: do unrelated tasks share steps? 0% means every task got its
        # own plan rather than a stock skeleton.
        shapes = {}
        for p, title in all_steps:
            shapes.setdefault(" ".join(sorted(content_words(title))), set()).add(p.get("title"))
        shared = {k: v for k, v in shapes.items() if len(v) > 1}
        reused = sum(len(v) for v in shared.values())
        print(f"  steps {len(all_steps)}, distinct shapes {len(shapes)}, "
              f"reused across tasks {reused} ({reused / len(all_steps):.0%})")

        firsts = [p["subtasks"][0].get("estimated_minutes") for p in plans
                  if p.get("subtasks") and isinstance(p["subtasks"][0].get("estimated_minutes"), int)]
        if firsts:
            fs = sorted(firsts)
            # Activation energy. v1 got a median of 15 by accident; a 60-minute
            # opening step is a failed breakdown for an overwhelmed user however
            # correct the rest of the plan is.
            print(f"  first step: median {fs[len(fs) // 2]} min, "
                  f"over 20 min on {sum(1 for f in fs if f > 20)}/{len(fs)}")

        sums = [(p.get("estimated_duration"), sum(s.get("estimated_minutes", 0)
                                                  for s in p.get("subtasks") or []))
                for p in plans if isinstance(p.get("estimated_duration"), int)]
        off = sum(1 for d, s in sums if s and d != s)
        print(f"  estimated_duration disagrees with its own steps: {off}/{len(sums)}")

    # The product-critical field.
    from quality import check_good_enough
    bad_ge = [(r["task"], r["plan"].get("good_enough_criteria"))
              for r in results if r["plan"] and check_good_enough(r["plan"].get("good_enough_criteria"))]
    print(f"\n-- good_enough_criteria (the field the product exists for) --")
    print(f"  perfectionist or deadline-bearing: {len(bad_ge)}/{len(plans)}")
    for task, ge in bad_ge[:4]:
        print(f"    [{task[:30]}] {ge}")

    return {"model": model, "results": results,
            "score": {"clean": len(clean), "total": n}}


def main():
    default_out = OUTPUT_DIR / "eval" / f"{time.strftime('%Y%m%d-%H%M%S')}.json"
    ap = argparse.ArgumentParser()
    ap.add_argument("model", help="Ollama tag of the checkpoint to evaluate")
    ap.add_argument("--baseline", help="second model to compare against")
    ap.add_argument("--out", default=str(default_out),
                    help="where to write full results (default: outputs/eval/<timestamp>.json)")
    args = ap.parse_args()

    runs = [evaluate(args.model)]
    if args.baseline:
        runs.append(evaluate(args.baseline))

    if len(runs) > 1:
        print(f"\n{'=' * 74}\nSUMMARY")
        for r in runs:
            print(f"  {r['model']:28s} {r['score']['clean']}/{r['score']['total']} clean")

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(runs, indent=2, ensure_ascii=False))
    print(f"\nfull output -> {out}")


if __name__ == "__main__":
    main()
