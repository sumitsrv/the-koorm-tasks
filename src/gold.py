"""Aggregate, validate and emit the hand-authored gold examples.

Discovers every `src/gold_*.py` module, concatenates their `GOLD` lists,
validates the lot against `quality.check_plan`, and writes
`data/gold/plan_gold.jsonl`. A failing example fails the build — it never reaches a
training run silently, which is precisely how v1's defects shipped.

    python src/gold.py            # validate + write data/gold/plan_gold.jsonl
    python src/gold.py --check    # validate only, write nothing
"""

import argparse
import importlib
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from config import DATA_GOLD_DIR
from goldlib import Gold, validate
from quality import coverage_report, label_distribution_report

SRC = Path(__file__).parent


def load_modules() -> list[tuple[str, list[Gold]]]:
    """Every gold_*.py module, in a stable order."""
    out = []
    for path in sorted(SRC.glob("gold_*.py")):
        mod = importlib.import_module(path.stem)
        examples = getattr(mod, "GOLD", None)
        if not examples:
            print(f"  warning: {path.name} exports no GOLD list — skipped")
            continue
        out.append((path.stem, examples))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="validate only")
    ap.add_argument("--only", help="validate a single gold_* module (use while "
                                   "authoring, so someone else's broken module "
                                   "doesn't fail your run)")
    args = ap.parse_args()

    modules = load_modules()
    if args.only:
        modules = [(n, e) for n, e in modules if n == args.only]
        if not modules:
            raise SystemExit(f"no module named {args.only}")
    if not modules:
        raise SystemExit("no gold_*.py modules found in src/")

    all_examples: list[Gold] = []
    print("gold modules:")
    for name, examples in modules:
        print(f"  {name:24s} {len(examples):4d} examples")
        all_examples.extend(examples)

    # Two modules describing the same task would double its weight in training.
    seen, dupes = set(), []
    unique = []
    for g in all_examples:
        key = g.task.strip().lower()
        if key in seen:
            dupes.append(g.task)
            continue
        seen.add(key)
        unique.append(g)
    if dupes:
        print(f"\ndropped {len(dupes)} duplicate task(s) across modules:")
        for d in dupes[:10]:
            print(f"  - {d[:70]}")

    rows, failures = validate(unique)

    if failures:
        print(f"\n{len(failures)} examples FAILED validation:")
        for task, why in failures:
            print(f"  - {task[:64]}\n      {why}")
        raise SystemExit("fix the examples above before building")

    tasks = [g.to_plan()["task"] for g in unique]
    print(f"\nvalidated {len(rows)} examples")
    print(label_distribution_report(tasks))
    print(coverage_report(tasks))

    if args.check or args.only:
        return

    out = DATA_GOLD_DIR / "plan_gold.jsonl"
    DATA_GOLD_DIR.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"\nwrote {len(rows)} examples -> {out}")


if __name__ == "__main__":
    main()
