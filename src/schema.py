"""Task and schedule models mirroring the Koorm project's Kotlin models."""

from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field


class Priority(str, Enum):
    URGENT = "URGENT"
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"


class TaskCategory(str, Enum):
    PERSONAL = "PERSONAL"
    WORK = "WORK"
    HEALTH = "HEALTH"
    LEARNING = "LEARNING"
    SOCIAL = "SOCIAL"


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
    estimated_minutes: int = Field(gt=0)


class TaskPlan(BaseModel):
    title: str
    description: str = ""
    priority: Priority = Priority.MEDIUM
    category: TaskCategory = TaskCategory.PERSONAL
    estimated_duration: int = Field(default=30, gt=0, description="Total minutes")
    due_date: Optional[str] = None
    good_enough_criteria: Optional[str] = None
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
