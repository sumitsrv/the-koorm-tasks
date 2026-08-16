"""Repair the v1 training data in place, instead of throwing 492 examples away.

Most of what is wrong with `data/distilled/plan_train.jsonl` is mechanical and fixable: a
category the app doesn't have, a date field that should never have existed, a
total that disagrees with its own steps, and a priority label that is HIGH on 80%
of rows because the seed tasks were all urgency-flavoured and the teacher was
given no rubric. Those get rewritten. What can't be rewritten honestly — a plan
with no steps, a genuinely perfectionist stopping point that survives cleanup —
gets dropped, and the script says how many and why.

    python src/repair.py            # writes data/distilled/plan_train.repaired.jsonl
    python src/repair.py --apply    # also replaces data/distilled/plan_train.jsonl (backs up first)

The old system prompt is baked into every row's `messages[0]`, so it is replaced
with the current `SYSTEM_PLAN` too — otherwise the repaired rows would train the
student on a prompt the app no longer sends.
"""

import argparse
import json
import re
import shutil
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from config import DATA_DISTILLED_DIR
from prompts import SYSTEM_PLAN
from quality import PERFECTIONIST, check_plan, label_distribution_report
from schema import PlanResponse, TaskCategory

# The app has no SOCIAL category; 43 v1 examples used it. Social obligations are
# personal ones as far as the app's model is concerned.
CATEGORY_REMAP = {"SOCIAL": "PERSONAL"}

# --- priority relabelling -------------------------------------------------
# v1: HIGH 395, URGENT 76, MEDIUM 20, LOW 1. The label carried no information, so
# the student learned the constant function. Relabel from the task text against
# the same rubric the prompt now states, so the mapping is at least learnable.
URGENT_CUES = re.compile(
    r"\b(urgent|asap|right away|immediately|within the hour|today|tonight|"
    r"by (?:noon|end of day|eod)|this morning|this afternoon|emergency|"
    r"last[- ]minute|deadline is today)\b", re.I)
HIGH_CUES = re.compile(
    r"\b(tomorrow|this week|by (?:mon|tues|wednes|thurs|fri|satur|sun)day|"
    r"before (?:the )?(?:end of|deadline)|due |deadline|expires?|closing|"
    r"boss|manager|client|blocked|waiting on me|before it runs out)\b", re.I)
LOW_CUES = re.compile(
    r"\b(someday|eventually|at some point|when i (?:get|have) (?:a chance|time)|"
    r"would be nice|no rush|whenever|been meaning to|one of these days)\b", re.I)


def infer_priority(user_task: str, current: str) -> str:
    text = user_task
    if LOW_CUES.search(text):
        return "LOW"
    if URGENT_CUES.search(text):
        return "URGENT"
    if HIGH_CUES.search(text):
        return "HIGH"
    # No time signal at all. v1 said HIGH here ~80% of the time, which is exactly
    # the bias being corrected; the rubric's default is MEDIUM.
    return "MEDIUM"


# --- good_enough_criteria cleanup ----------------------------------------
# Conservative rewrites of the absolutist phrasings, tried before giving up on a
# row. Anything still tripping the perfectionism gate afterwards is dropped
# rather than mangled further.
SOFTENERS: list[tuple[re.Pattern, str]] = [
    (re.compile(r"^all\s+", re.I), "The main "),
    (re.compile(r"\ball of the\b", re.I), "the main"),
    (re.compile(r"\ball\s+(?=\w)", re.I), "the main "),
    (re.compile(r"\bevery\s+(?=\w)", re.I), "each main "),
    (re.compile(r"\bcompletely\b", re.I), "mostly"),
    (re.compile(r"\bthoroughly\b", re.I), "reasonably"),
    (re.compile(r"\bfully\b", re.I), "broadly"),
    (re.compile(r"\bperfectly\b", re.I), "well enough"),
    (re.compile(r"\bflawless(?:ly)?\b", re.I), "workable"),
    (re.compile(r"\bwith no errors\b", re.I), "without obvious mistakes"),
    (re.compile(r"\bwithout any errors\b", re.I), "without obvious mistakes"),
    (re.compile(r"\berror[- ]free\b", re.I), "free of obvious mistakes"),
    (re.compile(r"\b100%\s*", re.I), ""),
    (re.compile(r"\bcomprehensive\b", re.I), "adequate"),
    (re.compile(r"\bexhaustive\b", re.I), "adequate"),
    (re.compile(r"\baccurate(?:ly)?\b", re.I), "broadly correct"),
    (re.compile(r"\bcomplete(?:d|ly)?\b", re.I), "done"),
    (re.compile(r"\s{2,}"), " "),
]


def soften(criteria: str) -> str:
    out = criteria
    for pat, repl in SOFTENERS:
        out = pat.sub(repl, out)
    out = out.strip().strip(",;").strip()
    return out[0].upper() + out[1:] if out else out


def repair_task(task: dict, user_task: str) -> tuple[dict, list[str]]:
    """Returns (repaired task, list of changes made)."""
    changes = []

    old_cat = task.get("category")
    if old_cat in CATEGORY_REMAP:
        task["category"] = CATEGORY_REMAP[old_cat]
        changes.append(f"category {old_cat}->{task['category']}")
    elif old_cat not in {c.value for c in TaskCategory}:
        task["category"] = "PERSONAL"
        changes.append(f"category {old_cat!r}->PERSONAL")

    if "due_date" in task:
        task.pop("due_date")
        changes.append("dropped due_date")
    # Set the key explicitly rather than omitting it: the prompt describes
    # `due_phrase`, so a target that lacks the key teaches the student to drop
    # it. v1's dates were computed and unrecoverable, so null is the honest
    # value — the gold set and fresh generation teach the positive case.
    task.setdefault("due_phrase", None)

    old_pri = task.get("priority")
    new_pri = infer_priority(user_task, old_pri)
    if new_pri != old_pri:
        task["priority"] = new_pri
        changes.append(f"priority {old_pri}->{new_pri}")

    subs = task.get("subtasks") or []
    if len(subs) > 6:
        task["subtasks"] = subs[:6]
        changes.append(f"trimmed {len(subs)} subtasks to 6")
        subs = task["subtasks"]
    for i, s in enumerate(subs, 1):
        if s.get("order") != i:
            s["order"] = i
            changes.append("renumbered subtask order")

    # Make the total honest rather than dropping the row over a mismatch.
    if subs:
        total = sum(s.get("estimated_minutes", 0) for s in subs)
        if total and task.get("estimated_duration") != total:
            changes.append(f"estimated_duration {task.get('estimated_duration')}->{total}")
            task["estimated_duration"] = total

    crit = task.get("good_enough_criteria") or ""
    if crit and PERFECTIONIST.search(crit):
        softened = soften(crit)
        if not PERFECTIONIST.search(softened):
            task["good_enough_criteria"] = softened
            changes.append("softened good_enough_criteria")

    return task, changes


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true",
                    help="replace data/distilled/plan_train.jsonl (backs up to .v1.bak)")
    ap.add_argument("--infile", default=str(DATA_DISTILLED_DIR / "plan_train.jsonl"))
    args = ap.parse_args()

    src = Path(args.infile)
    rows = [json.loads(l) for l in src.open(encoding="utf-8") if l.strip()]
    print(f"read {len(rows)} examples from {src}\n")

    kept, dropped = [], Counter()
    change_counts = Counter()
    repaired_tasks = []

    for row in rows:
        msgs = row.get("messages", [])
        user = next((m["content"] for m in msgs if m["role"] == "user"), "")
        assistant = next((m["content"] for m in msgs if m["role"] == "assistant"), None)
        if not assistant:
            dropped["no assistant turn"] += 1
            continue
        try:
            parsed = json.loads(assistant)
            task = parsed["task"]
        except Exception:
            dropped["unparseable target"] += 1
            continue

        user_task = user.replace("Plan this task:", "").strip()
        task, changes = repair_task(task, user_task)
        for c in changes:
            change_counts[c.split(" ")[0]] += 1
        parsed["task"] = task

        try:
            PlanResponse.model_validate(parsed)
        except Exception as e:
            dropped[f"schema: {type(e).__name__}"] += 1
            continue

        problems = check_plan(parsed, user_task, strict=False)
        if problems:
            dropped[problems[0].split("(")[0].strip()] += 1
            continue

        repaired_tasks.append(task)
        kept.append({"messages": [
            {"role": "system", "content": SYSTEM_PLAN},
            {"role": "user", "content": f"Plan this task: {user_task}"},
            {"role": "assistant", "content": json.dumps(parsed, ensure_ascii=False)},
        ]})

    print("REPAIRS APPLIED")
    for c, n in change_counts.most_common():
        print(f"  {n:4d}  {c}")
    print(f"\nKEPT {len(kept)} / {len(rows)}   DROPPED {len(rows) - len(kept)}")
    for reason, n in dropped.most_common():
        print(f"  {n:4d}  {reason}")

    print("\nLABEL DISTRIBUTION AFTER REPAIR")
    print(label_distribution_report(repaired_tasks))

    DATA_DISTILLED_DIR.mkdir(parents=True, exist_ok=True)
    out = DATA_DISTILLED_DIR / "plan_train.repaired.jsonl"
    with out.open("w", encoding="utf-8") as f:
        for ex in kept:
            f.write(json.dumps(ex, ensure_ascii=False) + "\n")
    print(f"\nwrote {out}")

    if args.apply:
        backup = src.with_suffix(".v1.bak")
        shutil.copy2(src, backup)
        shutil.copy2(out, src)
        print(f"applied: {src} replaced (v1 backed up to {backup})")


if __name__ == "__main__":
    main()
