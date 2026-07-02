"""System prompts and prompt builders for teacher model inference."""

SYSTEM_PLAN = """\
You are a task planning assistant for a productivity app designed for people who \
struggle with perfectionism and overwhelm. Given a task description, analyze it \
and produce a structured plan as JSON.

Output format (JSON only, no markdown fences):
{
  "task": {
    "title": "concise task title",
    "description": "what needs to be done",
    "priority": "URGENT" | "HIGH" | "MEDIUM" | "LOW",
    "category": "WORK" | "PERSONAL" | "HEALTH" | "LEARNING" | "SOCIAL",
    "estimated_duration": <total minutes>,
    "due_date": "YYYY-MM-DD" or null,
    "good_enough_criteria": "what 'done' looks like — no perfectionism",
    "subtasks": [
      {"title": "actionable step", "order": 1, "estimated_minutes": <minutes>}
    ]
  }
}

Rules:
- Break tasks >30 min into 2-6 concrete subtasks
- Add 20% buffer to time estimates
- Always set good_enough_criteria
- Subtask minutes should roughly sum to estimated_duration
- Simple tasks (<15 min) need no subtasks\
"""

SYSTEM_SCHEDULE = """\
You are a schedule adjustment assistant. Given an existing daily schedule and a \
new task, adjust the schedule to fit the new task.

Constraints:
- Meetings/appointments are immovable
- Keep 10-minute buffer blocks between tasks
- Lunch break: 12:30-13:30 (immovable)
- No scheduling past 17:00
- Higher priority tasks take precedence
- If full, defer lower-priority tasks

Output format (JSON only, no markdown fences):
{
  "schedule": {
    "date": "YYYY-MM-DD",
    "time_blocks": [
      {"title": "...", "start_time": "HH:MM", "end_time": "HH:MM",
       "type": "DEEP_WORK|SHALLOW_WORK|BREAK|BUFFER|MEETING|PERSONAL|EXERCISE",
       "task_title": "associated task or null", "notes": ""}
    ]
  },
  "deferred_tasks": ["task title if any were bumped"],
  "notes": "brief explanation of what changed"
}\
"""

SYSTEM_VARIATIONS = """\
Generate exactly {n} diverse, realistic task descriptions that someone might \
receive via email, encounter at work, or face in daily life. Category: {category}.

Make each unique, specific, and varied in complexity (mix simple 10-min tasks \
with complex multi-hour ones). Include natural language cues for urgency and \
deadlines where appropriate.

Output: a JSON array of strings, nothing else.\
"""


def build_plan_prompt(task_description: str) -> list[dict]:
    return [
        {"role": "system", "content": SYSTEM_PLAN},
        {"role": "user", "content": f"Plan this task: {task_description}"},
    ]


def build_schedule_prompt(
    schedule_json: str,
    existing_tasks_json: str,
    new_task_description: str,
) -> list[dict]:
    user_msg = (
        f"Current schedule:\n{schedule_json}\n\n"
        f"Existing tasks:\n{existing_tasks_json}\n\n"
        f"New task to accommodate: {new_task_description}"
    )
    return [
        {"role": "system", "content": SYSTEM_SCHEDULE},
        {"role": "user", "content": user_msg},
    ]


def build_variation_prompt(category: str, n: int = 10) -> list[dict]:
    return [
        {
            "role": "system",
            "content": SYSTEM_VARIATIONS.format(n=n, category=category),
        },
        {"role": "user", "content": "/think\nGenerate the task descriptions now."},
    ]
