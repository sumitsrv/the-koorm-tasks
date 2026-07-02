"""Seed scenarios for training data generation."""

import json
import random
from schema import (
    Schedule, TimeBlock, TimeBlockType, TaskPlan, Priority, TaskCategory,
)

# ---------------------------------------------------------------------------
# Seed task descriptions (used directly + expanded via teacher model)
# ---------------------------------------------------------------------------

TASK_SEEDS: dict[str, list[str]] = {
    "WORK": [
        "Write a quarterly sales report for the board meeting next Monday",
        "Prepare slides for the product demo on Thursday",
        "Reply to the client email about the contract renewal",
        "Review and approve the new hire's onboarding documents",
        "Set up a 1:1 with the design team lead to discuss the homepage redesign",
        "Draft a project proposal for the new analytics dashboard",
        "Update the team wiki with the latest API changes",
        "Conduct code review on the authentication pull request",
        "Prepare talking points for tomorrow's standup",
        "Organize the shared drive — archive Q1 folders",
    ],
    "PERSONAL": [
        "Organize the garage this weekend",
        "Plan a birthday party for my daughter next Saturday",
        "File taxes before April 15th",
        "Get the car inspected and oil changed",
        "Pack for the vacation trip leaving in 3 days",
        "Return the Amazon package before the refund window closes Friday",
        "Call the electrician about the flickering kitchen light",
        "Declutter and donate clothes from the hall closet",
        "Set up automatic bill payments for utilities",
        "Renew passport — it expires in 3 months",
    ],
    "HEALTH": [
        "Schedule and attend annual physical checkup",
        "Start a 30-day morning yoga routine",
        "Meal prep healthy lunches for the week",
        "Find a new therapist and book initial appointment",
        "Refill prescriptions before they run out next Tuesday",
        "Research and sign up for a gym near the office",
        "Schedule a dentist cleaning appointment",
        "Track water intake daily for the next 2 weeks",
    ],
    "LEARNING": [
        "Complete chapter 5 of the machine learning course",
        "Practice Spanish for 30 minutes daily this week",
        "Read and take notes on 'Thinking, Fast and Slow'",
        "Watch and summarize the React conference talks from last week",
        "Finish the Kubernetes tutorial and deploy a test cluster",
        "Write a blog post about what I learned about RAG pipelines",
        "Take the AWS Solutions Architect practice exam",
        "Set up a personal Anki deck for the certification study material",
    ],
    "SOCIAL": [
        "Call mom and catch up — haven't talked in 2 weeks",
        "Organize a dinner with college friends next Friday",
        "Write a thank-you note to my mentor",
        "RSVP and prepare for the networking event Wednesday",
        "Plan a weekend hike with the running group",
        "Send a congratulations message to Sara on her promotion",
        "Coordinate carpool for the kids' soccer practice Thursday",
        "Buy a housewarming gift for Jake's party this Saturday",
    ],
}

ALL_SEEDS = [desc for descs in TASK_SEEDS.values() for desc in descs]

# ---------------------------------------------------------------------------
# Random schedule generator (for schedule-adjustment examples)
# ---------------------------------------------------------------------------

_SAMPLE_TASKS = [
    ("Review PRs", TimeBlockType.DEEP_WORK, Priority.HIGH, TaskCategory.WORK),
    ("Team standup", TimeBlockType.MEETING, Priority.HIGH, TaskCategory.WORK),
    ("Email triage", TimeBlockType.SHALLOW_WORK, Priority.MEDIUM, TaskCategory.WORK),
    ("Write docs", TimeBlockType.DEEP_WORK, Priority.MEDIUM, TaskCategory.WORK),
    ("Exercise", TimeBlockType.EXERCISE, Priority.MEDIUM, TaskCategory.HEALTH),
    ("1:1 with manager", TimeBlockType.MEETING, Priority.HIGH, TaskCategory.WORK),
    ("Study session", TimeBlockType.DEEP_WORK, Priority.MEDIUM, TaskCategory.LEARNING),
    ("Grocery list", TimeBlockType.SHALLOW_WORK, Priority.LOW, TaskCategory.PERSONAL),
    ("Sprint planning", TimeBlockType.MEETING, Priority.HIGH, TaskCategory.WORK),
    ("Read articles", TimeBlockType.SHALLOW_WORK, Priority.LOW, TaskCategory.LEARNING),
    ("Call dentist", TimeBlockType.SHALLOW_WORK, Priority.MEDIUM, TaskCategory.HEALTH),
    ("Client call", TimeBlockType.MEETING, Priority.URGENT, TaskCategory.WORK),
    ("Budget review", TimeBlockType.DEEP_WORK, Priority.MEDIUM, TaskCategory.PERSONAL),
    ("Design review", TimeBlockType.MEETING, Priority.HIGH, TaskCategory.WORK),
]


def _fmt(hour: int, minute: int) -> str:
    return f"{hour:02d}:{minute:02d}"


def generate_random_schedule(
    date: str = "2026-06-25",
    min_blocks: int = 3,
    max_blocks: int = 7,
) -> tuple[Schedule, list[TaskPlan]]:
    """Generate a realistic random schedule with associated tasks."""
    n_blocks = random.randint(min_blocks, max_blocks)
    chosen = random.sample(_SAMPLE_TASKS, min(n_blocks, len(_SAMPLE_TASKS)))

    blocks: list[TimeBlock] = []
    tasks: list[TaskPlan] = []
    cursor_h, cursor_m = 9, 0  # start at 09:00

    for title, block_type, priority, category in chosen:
        if cursor_h >= 17:
            break
        # lunch
        if cursor_h == 12 and cursor_m < 30:
            cursor_m = 30
        if cursor_h >= 12 and cursor_h < 13:
            blocks.append(TimeBlock(
                title="Lunch",
                start_time="12:30",
                end_time="13:30",
                type=TimeBlockType.BREAK,
            ))
            cursor_h, cursor_m = 13, 30

        duration = random.choice([30, 45, 60, 90])
        end_m = cursor_m + duration
        end_h = cursor_h + end_m // 60
        end_m = end_m % 60

        if end_h >= 17:
            break

        blocks.append(TimeBlock(
            title=title,
            start_time=_fmt(cursor_h, cursor_m),
            end_time=_fmt(end_h, end_m),
            type=block_type,
            task_title=title,
        ))
        tasks.append(TaskPlan(
            title=title,
            priority=priority,
            category=category,
            estimated_duration=duration,
        ))

        # buffer
        cursor_h, cursor_m = end_h, end_m + 10
        if cursor_m >= 60:
            cursor_h += 1
            cursor_m -= 60

    schedule = Schedule(date=date, time_blocks=blocks)
    return schedule, tasks


# New tasks to inject into existing schedules
NEW_TASK_SEEDS = [
    "Urgent: client escalation call needed within the hour",
    "Boss asked me to review the budget proposal before 3 PM",
    "Dentist called — appointment moved to today at 2 PM",
    "Need to pick up the kids early from school at 3:30",
    "Last-minute request: prepare a 5-min demo for the investor meeting at 4",
    "Teammate is sick — cover their code review this morning",
    "Forgot to submit the expense report — deadline is today",
    "Plumber can come today between 11-12, need to be home",
    "Got a study group invite for the cert exam, meeting at 1:30 PM today",
    "Quick errand: pharmacy closes at 5, need to pick up meds",
    "Manager wants a status update document by end of day",
    "Just remembered: Mom's birthday is today, need to order a gift",
    "HR needs my updated emergency contacts form by noon",
    "Car service appointment available today at 10 AM — should I take it?",
    "Conference talk proposal deadline is tonight — need to write abstract",
]
