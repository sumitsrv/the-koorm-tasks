"""Task and schedule models mirroring the Koorm app's Kotlin models.

These MUST stay in sync with `core-domain/.../models/Task.kt` in the Koorm app.
They drifted once before, and it cost a training run: this file used to declare a
`SOCIAL` category the app has never had, while the app's `CREATIVE` and `ADMIN`
got zero training examples. 43 examples taught a label the app silently discards.
If you change an enum here, change it there in the same commit.
"""

from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field


class Priority(str, Enum):
    URGENT = "URGENT"
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"


class TaskCategory(str, Enum):
    """Exactly the app's `TaskCategory` enum — no more, no less."""
    WORK = "WORK"
    PERSONAL = "PERSONAL"
    HEALTH = "HEALTH"
    LEARNING = "LEARNING"
    CREATIVE = "CREATIVE"
    ADMIN = "ADMIN"


class TimeBlockType(str, Enum):
    DEEP_WORK = "DEEP_WORK"
    SHALLOW_WORK = "SHALLOW_WORK"
    BREAK = "BREAK"
    BUFFER = "BUFFER"
    MEETING = "MEETING"
    PERSONAL = "PERSONAL"
    EXERCISE = "EXERCISE"


class Subtask(BaseModel):
    title: str
    order: int
    estimated_minutes: int = Field(gt=0, le=480)


class TaskPlan(BaseModel):
    """A planned task.

    Note there is no `due_date`. The previous schema had one, and 73% of the
    generated examples carried a 2023 date because the teacher was asked for a
    date it had no way to know — the prompt never supplied "today". The student
    dutifully learned to answer "next Monday" with a date in 2023.

    `due_phrase` replaces it, and the difference is the whole design principle:
    the model **extracts** rather than **generates**. It copies the deadline
    words already present in the task ("before Saturday", "next Monday") and the
    app resolves them against the real clock with `DeadlineParser`. A span the
    model merely points at cannot be hallucinated — `quality.check_due_phrase`
    rejects any value that is not a literal substring of the task text — whereas
    a date it computes is wrong the moment its training data ages.

    The same split applies to anything else the model cannot know: the calling
    app supplies facts as context (see `prompts.plan_user`) or resolves them
    afterwards. A 0.6B model is a good extractor and a poor oracle; the schema
    should only ever ask it to be the former.
    """
    title: str
    description: str = ""
    priority: Priority = Priority.MEDIUM
    category: TaskCategory = TaskCategory.PERSONAL
    estimated_duration: int = Field(default=30, gt=0, le=2400, description="Total minutes")
    good_enough_criteria: Optional[str] = None
    #: Deadline words copied verbatim out of the task text, or null when the task
    #: states no deadline. Never a date — the app resolves this against today.
    due_phrase: Optional[str] = None
    subtasks: list[Subtask] = []


class TimeBlock(BaseModel):
    title: str
    start_time: str = Field(pattern=r"^\d{2}:\d{2}$")
    end_time: str = Field(pattern=r"^\d{2}:\d{2}$")
    type: TimeBlockType = TimeBlockType.DEEP_WORK
    task_title: Optional[str] = None
    notes: str = ""


class Schedule(BaseModel):
    date: str
    time_blocks: list[TimeBlock] = []


class PlanResponse(BaseModel):
    """Expected JSON output from the model for task planning."""
    task: TaskPlan


class ScheduleResponse(BaseModel):
    """Expected JSON output from the model for schedule adjustment."""
    schedule: Schedule
    deferred_tasks: list[str] = []
    notes: str = ""
