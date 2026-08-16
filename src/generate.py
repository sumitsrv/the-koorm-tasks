"""Generate training data by distilling from a teacher model.

The teacher is chosen at runtime — both backends are first-class:

    python src/generate.py --teacher ollama    # local qwen3:8b, free, offline
    python src/generate.py --teacher claude    # Anthropic API, needs a key

See `teacher.py` for what each costs you and what it buys. Everything else in
this pipeline is identical either way, including the gates: whatever a teacher
returns must pass `quality.check_plan` before it is written, so the teacher
affects yield and content quality, never the schema floor.

Output is per-teacher (`data/distilled/plan_<teacher>.jsonl`), so runs from different
teachers accumulate side by side instead of overwriting each other — and
`combine` merges whichever ones exist along with the repaired v1 data and the
hand-authored gold set.

Resumable: re-run the same command and it picks up where it left off. Run only
one instance per teacher at a time.
"""

import argparse
import json
import random
import sys
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from tqdm import tqdm

from config import DATA_DIR, DATA_DISTILLED_DIR, DATA_GOLD_DIR, PLAN_EXAMPLES_TARGET, SCHEDULE_EXAMPLES_TARGET
from prompts import SYSTEM_PLAN, SYSTEM_SCHEDULE, build_schedule_prompt
from quality import check_plan, label_distribution_report
from scenarios import ALL_SEEDS, DIVERSITY_AXES, NEW_TASK_SEEDS, generate_random_schedule
from schema import ScheduleResponse
import teacher as teachers

_write_lock = threading.Lock()


def count_lines(path: Path) -> int:
    if not path.exists():
        return 0
    with path.open(encoding="utf-8") as f:
        return sum(1 for line in f if line.strip())


# ---------------------------------------------------------------------------
# Quality filters — kept here for backwards compatibility; the real gates live
# in quality.py so the same rules apply to distilled and hand-authored data.
# ---------------------------------------------------------------------------

def _to_min(hhmm: str) -> int:
    h, m = hhmm.split(":")
    return int(h) * 60 + int(m)


def valid_plan(parsed: dict) -> bool:
    return not check_plan(parsed, strict=False)


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
    titles = {b.get("title") for b in blocks} | {b.get("task_title") for b in blocks}
    if any(d in titles for d in parsed.get("deferred_tasks", [])):
        return False
    return True


# ---------------------------------------------------------------------------
# Phase 1: expand seeds into diverse descriptions (cached to disk)
# ---------------------------------------------------------------------------

def expand_seeds(teacher, target: int, workers: int) -> list[str]:
    """Top up data/distilled/descriptions.json toward `target`. Only ever
    appends, so an existing cache — and any plans already generated from it —
    stay valid.

    Expansion is nudged along `DIVERSITY_AXES` rather than v1's five fixed
    category buckets, which produced 65% arrange/schedule/email work and 1%
    anything hands-on.
    """
    cache = DATA_DISTILLED_DIR / "descriptions.json"
    descs = json.loads(cache.read_text(encoding="utf-8")) if cache.exists() else list(ALL_SEEDS)
    seen = {d.strip().lower() for d in descs}

    if len(descs) >= target:
        print(f"Loaded {len(descs)} cached descriptions (target {target})")
        return descs

    print(f"Expanding {len(descs)} → {target} descriptions …", flush=True)
    DATA_DISTILLED_DIR.mkdir(parents=True, exist_ok=True)
    rounds = 0
    while len(descs) < target and rounds < 20:   # cap rounds so a repeating teacher can't spin
        rounds += 1
        axes = random.sample(DIVERSITY_AXES, min(workers, len(DIVERSITY_AXES)))
        with ThreadPoolExecutor(max_workers=workers) as pool:
            futures = {pool.submit(teacher.variations, axis): axis for axis in axes}
            for fut in as_completed(futures):
                fresh = [d for d in fut.result() if d.strip().lower() not in seen]
                seen.update(d.strip().lower() for d in fresh)
                descs.extend(fresh)
                print(f"  +{len(fresh):2d}  {futures[fut][:46]}…  (total {len(descs)})", flush=True)
        cache.write_text(json.dumps(descs, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"Total descriptions: {len(descs)}", flush=True)
    return descs


# ---------------------------------------------------------------------------
# Phase 2: plan every description (resumable, concurrent)
# ---------------------------------------------------------------------------

def generate_plan_examples(teacher, descriptions: list[str], workers: int) -> int:
    out = DATA_DISTILLED_DIR / f"plan_{teacher.name}.jsonl"
    out.parent.mkdir(parents=True, exist_ok=True)

    done: set[str] = set()
    if out.exists():
        for line in out.open(encoding="utf-8"):
            if not line.strip():
                continue
            user = next((m["content"] for m in json.loads(line)["messages"]
                         if m["role"] == "user"), "")
            done.add(user.replace("Plan this task:", "").strip().lower())

    todo = [d for d in descriptions if d.strip().lower() not in done]
    print(f"\nPlans ({teacher.name}): {len(done)} done, {len(todo)} to go", flush=True)
    if not todo:
        return len(done)

    written, rejects = 0, {}
    tasks: list[dict] = []
    with out.open("a", encoding="utf-8") as f, \
            ThreadPoolExecutor(max_workers=workers) as pool:
        futures = {pool.submit(_plan_one, teacher, d): d for d in todo}
        for fut in tqdm(as_completed(futures), total=len(todo), desc="plans"):
            row, task, why = fut.result()
            if row is None:
                rejects[why] = rejects.get(why, 0) + 1
                continue
            with _write_lock:
                f.write(json.dumps(row, ensure_ascii=False) + "\n")
                f.flush()
            tasks.append(task)
            written += 1

    print(f"Saved {written} plan examples → {out}")
    if rejects:
        print("Rejected:")
        for why, n in sorted(rejects.items(), key=lambda kv: -kv[1])[:10]:
            print(f"  {n:4d}  {why}")
    if tasks:
        print("\nLabel distribution of this run:")
        print(label_distribution_report(tasks))
    return len(done) + written


def _plan_one(teacher, description: str):
    """Returns (chat row, task dict, reject reason). Row is None when rejected."""
    parsed, err = teacher.plan(description)
    if parsed is None:
        return None, None, err
    problems = check_plan(parsed, description, strict=True)
    if problems:
        return None, None, problems[0].split("(")[0].strip()
    row = {"messages": [
        {"role": "system", "content": SYSTEM_PLAN},
        {"role": "user", "content": f"Plan this task: {description}"},
        {"role": "assistant", "content": json.dumps(parsed, ensure_ascii=False)},
    ]}
    return row, parsed["task"], ""


# ---------------------------------------------------------------------------
# Phase 3: schedule-adjustment examples (resumable)
# ---------------------------------------------------------------------------

def generate_schedule_examples(teacher, target: int, workers: int) -> int:
    out = DATA_DISTILLED_DIR / f"schedule_{teacher.name}.jsonl"
    out.parent.mkdir(parents=True, exist_ok=True)

    done = count_lines(out)
    if done >= target:
        print(f"\nSchedule examples already complete ({done}/{target})")
        return done

    print(f"\nSchedules ({teacher.name}): resuming from {done}/{target} …", flush=True)
    count = done
    with out.open("a", encoding="utf-8") as f, \
            ThreadPoolExecutor(max_workers=workers) as pool:
        futures = [pool.submit(_schedule_one, teacher) for _ in range(target - done)]
        for fut in tqdm(as_completed(futures), total=target - done, desc="schedules"):
            row = fut.result()
            if row is None:
                continue
            with _write_lock:
                f.write(json.dumps(row, ensure_ascii=False) + "\n")
                f.flush()
            count += 1
    print(f"Saved {count} schedule examples → {out}", flush=True)
    return count


def _schedule_one(teacher):
    date = f"2026-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}"
    schedule, tasks = generate_random_schedule(date=date)
    new_task = random.choice(NEW_TASK_SEEDS)
    msgs = build_schedule_prompt(
        schedule.model_dump_json(indent=2),
        json.dumps([t.model_dump() for t in tasks], indent=2),
        new_task,
    )
    # Schedules aren't covered by the plan schema, so both backends go through
    # their generic text path here.
    raw = getattr(teacher, "_chat", None)
    if raw is not None:                       # ollama
        text = teacher._chat(msgs)
        parsed = teachers._extract_json_object(text) if text else None
    else:                                     # claude
        try:
            resp = teacher.client.messages.create(
                model=teacher.model, max_tokens=2048,
                system=teacher._system(SYSTEM_SCHEDULE),
                messages=[msgs[1]],
            )
            parsed = teachers._extract_json_object(
                "".join(b.text for b in resp.content if b.type == "text"))
        except Exception:  # noqa: BLE001
            parsed = None
    if not parsed:
        return None
    try:
        ScheduleResponse.model_validate(parsed)
    except Exception:  # noqa: BLE001
        return None
    if not valid_schedule(parsed):
        return None
    return {"messages": [msgs[0], msgs[1],
                         {"role": "assistant", "content": json.dumps(parsed, ensure_ascii=False)}]}


# ---------------------------------------------------------------------------
# Phase 4: combine everything into one training file
# ---------------------------------------------------------------------------

def combine():
    """Merge every available source into data/train.jsonl.

    Sources are optional — whichever exist get used, so you can train on the
    repaired v1 data plus the gold set without running a teacher at all.
    """
    combined = DATA_DIR / "train.jsonl"
    sources = [
        (DATA_DISTILLED_DIR, "plan_train.jsonl"),       # v1 distilled data (run repair.py --apply first)
        (DATA_DISTILLED_DIR, "plan_ollama.jsonl"),      # this pipeline, local teacher
        (DATA_DISTILLED_DIR, "plan_claude.jsonl"),      # this pipeline, hosted teacher
        (DATA_GOLD_DIR, "plan_gold.jsonl"),             # hand-authored (python src/gold.py)
        (DATA_DISTILLED_DIR, "schedule_train.jsonl"),
        (DATA_DISTILLED_DIR, "schedule_ollama.jsonl"),
        (DATA_DISTILLED_DIR, "schedule_claude.jsonl"),
    ]
    examples, used = [], []
    for folder, name in sources:
        p = folder / name
        if not p.exists():
            continue
        rows = [json.loads(line) for line in p.open(encoding="utf-8") if line.strip()]
        examples.extend(rows)
        used.append(f"{name} ({len(rows)})")

    if not examples:
        raise SystemExit("no data to combine — run a teacher, gold.py, or repair.py first")

    random.shuffle(examples)
    with combined.open("w", encoding="utf-8") as f:
        for ex in examples:
            f.write(json.dumps(ex, ensure_ascii=False) + "\n")
    print(f"\nCombined {len(examples)} examples → {combined}")
    for u in used:
        print(f"  from {u}")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--teacher", choices=sorted(teachers.TEACHERS), default="ollama",
                    help="which teacher to distil from (default: ollama — local and free)")
    ap.add_argument("--model", help="override that teacher's default model")
    ap.add_argument("--workers", type=int, default=1,
                    help="concurrent requests (default 1; raise for the hosted teacher, "
                         "keep at 1 for Ollama — parallel calls to one local model "
                         "just serialise)")
    ap.add_argument("--plans", type=int, default=PLAN_EXAMPLES_TARGET,
                    help="target number of plan examples")
    ap.add_argument("--schedules", type=int, default=SCHEDULE_EXAMPLES_TARGET,
                    help="target number of schedule examples")
    ap.add_argument("--skip-schedules", action="store_true",
                    help="plans only — the schedule head isn't wired into the app yet")
    ap.add_argument("--combine-only", action="store_true",
                    help="just merge existing data into train.jsonl")
    args = ap.parse_args()

    if args.combine_only:
        combine()
        return

    teacher = teachers.build(args.teacher, args.model)
    print(f"teacher: {teacher.name} / {teacher.model}, {args.workers} worker(s)")

    descriptions = expand_seeds(teacher, args.plans, args.workers)
    generate_plan_examples(teacher, descriptions, args.workers)
    if not args.skip_schedules:
        generate_schedule_examples(teacher, args.schedules, args.workers)
    combine()
    print("\nDone. Training data is in data/train.jsonl")


if __name__ == "__main__":
    main()
