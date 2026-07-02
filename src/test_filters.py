"""Self-check for the data-quality filters. Run: python src/test_filters.py"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from generate import valid_plan, valid_schedule


def _plan(dur, subs):
    return {"task": {"estimated_duration": dur, "subtasks": subs}}


def _sched(blocks, deferred=()):
    return {"schedule": {"time_blocks": blocks}, "deferred_tasks": list(deferred)}


def _b(title, s, e):
    return {"title": title, "task_title": title, "start_time": s, "end_time": e}


# plans
assert valid_plan(_plan(20, []))                                  # short task, no subtasks ok
assert not valid_plan(_plan(90, []))                              # long task needs subtasks
assert valid_plan(_plan(60, [{"estimated_minutes": 30}, {"estimated_minutes": 30}]))
assert not valid_plan(_plan(60, [{"estimated_minutes": 5}, {"estimated_minutes": 5}]))  # sum too low

# schedules
assert valid_schedule(_sched([_b("A", "09:00", "10:00"), _b("B", "10:10", "11:00")]))
assert not valid_schedule(_sched([_b("A", "09:00", "10:00"), _b("B", "09:30", "10:30")]))  # overlap
assert not valid_schedule(_sched([_b("A", "16:30", "17:30")]))    # past 17:00
assert not valid_schedule(_sched([_b("A", "10:00", "09:00")]))    # backwards
assert not valid_schedule(_sched([_b("A", "09:00", "10:00")], deferred=["A"]))  # deferred still present
assert not valid_schedule(_sched([]))                             # empty

print("all filter checks passed")
