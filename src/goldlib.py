"""Shared machinery for hand-authored gold examples.

Authored examples live in `gold_*.py` modules, one per domain slice, each
exporting a `GOLD: list[Gold]`. `gold.py` discovers them, validates everything
and writes the JSONL. Splitting by module is what lets several authors (or
several agents) add examples at once without editing the same file.
"""

import json
import sys
from dataclasses import dataclass, field
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from prompts import SYSTEM_PLAN
from quality import check_plan
from schema import PlanResponse


@dataclass
class Gold:
    """One authored example.

    `steps` are (title, minutes) in the order they must actually happen.
    `estimated_duration` is always their sum — it is computed, never written by
    hand, so it cannot drift from the steps the way v1's did.
    """
    task: str                       # what the user types
    title: str
    desc: str
    pri: str                        # URGENT | HIGH | MEDIUM | LOW
    cat: str                        # WORK | PERSONAL | HEALTH | LEARNING | CREATIVE | ADMIN
    ge: str                         # good_enough_criteria
    steps: list[tuple[str, int]] = field(default_factory=list)
    #: Deadline words copied verbatim out of `task`, or None when it states no
    #: deadline. Validated as a literal span of the task — see
    #: `quality.check_due_phrase` for why this is extracted rather than computed.
    due: str | None = None

    def to_plan(self) -> dict:
        return {"task": {
            "title": self.title,
            "description": self.desc,
            "priority": self.pri,
            "category": self.cat,
            "estimated_duration": sum(m for _, m in self.steps),
            "good_enough_criteria": self.ge,
            "due_phrase": self.due,
            "subtasks": [
                {"title": t, "order": i, "estimated_minutes": m}
                for i, (t, m) in enumerate(self.steps, 1)
            ],
        }}


def validate(examples: list[Gold]) -> tuple[list[dict], list[tuple[str, str]]]:
    """Returns (chat rows for the valid ones, [(task, why) for the rest])."""
    rows, failures = [], []
    for g in examples:
        plan = g.to_plan()
        try:
            PlanResponse.model_validate(plan)
        except Exception as e:
            failures.append((g.task, f"schema: {e}"))
            continue
        problems = check_plan(plan, g.task, strict=True)
        if problems:
            failures.append((g.task, "; ".join(problems)))
            continue
        rows.append({"messages": [
            {"role": "system", "content": SYSTEM_PLAN},
            {"role": "user", "content": f"Plan this task: {g.task}"},
            {"role": "assistant", "content": json.dumps(plan, ensure_ascii=False)},
        ]})
    return rows, failures
