"""Self-check for the data-quality gates. Run: python src/test_filters.py

Each case below is a defect that actually reached the v1 checkpoint, encoded so
it can never reach another one silently. The gates are the only thing standing
between a teacher's output and the training set, so they get tested like code.

Note the deliberate contract change from v1: a plan with **no** subtasks is no
longer valid at any duration. v1 accepted it for short tasks and 27 examples
came through with an empty `subtasks` array — a "breakdown" that breaks nothing
down, which is the one thing this model exists to do.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from generate import valid_schedule
from quality import (
    check_due_phrase,
    check_good_enough,
    check_ordering,
    check_plan,
    check_subtasks,
    label_distribution_report,
)


def _task(**kw):
    task = {
        "title": "T",
        "estimated_duration": 30,
        "good_enough_criteria": "The main thing is done and it works",
        "subtasks": [
            {"title": "First small step", "order": 1, "estimated_minutes": 10},
            {"title": "Second step", "order": 2, "estimated_minutes": 20},
        ],
    }
    task.update(kw)
    return {"task": task}


# Distinct multi-word titles: the near-duplicate check needs two content words
# a side, and placeholder titles like "Step 1"/"Step 2" would trip it on nothing.
_TITLES = ["Gather the paperwork", "Draft the opening", "Check the figures",
           "Print and sign", "Post the envelope", "File your copy", "Update the log"]


def _steps(*mins):
    return [{"title": _TITLES[i - 1], "order": i, "estimated_minutes": m}
            for i, m in enumerate(mins, 1)]


def _sched(blocks, deferred=()):
    return {"schedule": {"time_blocks": blocks}, "deferred_tasks": list(deferred)}


def _b(title, s, e):
    return {"title": title, "task_title": title, "start_time": s, "end_time": e}


# --- plans: the happy path -------------------------------------------------
assert not check_plan(_task(), "T"), check_plan(_task(), "T")

# --- subtask count ---------------------------------------------------------
# A plan with no steps is not a breakdown, whatever the duration. v1 let 27 of
# these through.
assert check_subtasks({"subtasks": []})
assert check_subtasks({"subtasks": _steps(10)})                     # 1 step: too few
assert check_subtasks({"subtasks": _steps(*([10] * 7))})            # 7 steps: too many
assert not check_subtasks({"subtasks": _steps(10, 20)})

# --- activation energy -----------------------------------------------------
# The opening step has to beat inertia. v1 got a 15-min median by accident,
# with nothing asking for it.
assert check_subtasks({"subtasks": _steps(60, 10)})
assert not check_subtasks({"subtasks": _steps(15, 60)})

# --- restated steps --------------------------------------------------------
# A restatement is a SUBSET: it says everything its twin said and adds only
# filler. This is the exact shape the shipped model produced — "Set up CI/CD
# pipeline" appearing again as step 5 with a trailing qualifier.
def _pair(x, y):
    return {"subtasks": [{"title": x, "order": 1, "estimated_minutes": 10},
                         {"title": y, "order": 2, "estimated_minutes": 20}]}


def _flags(x, y):
    return any("near-duplicate" in p for p in check_subtasks(_pair(x, y)))


assert _flags("Set up the CI/CD pipeline",
              "Set up the CI/CD pipeline with environment variables")
assert _flags("Draft the covering letter", "Draft the covering letter")

# Everything below is a well-formed plan and must NOT be flagged. Each of these
# is a real pair from the corpus that a word-overlap threshold rejected:
#
#   parallel work — differ by their object
assert not _flags("Upload to LinkedIn", "Upload to Facebook")
assert not _flags("Identify internal strengths", "Identify internal weaknesses")
assert not _flags("Forecast income categories", "Forecast expense categories")
#   progression — differ by their verb
assert not _flags("Schedule the team sync-up call", "Attend the team sync-up call")
assert not _flags("Outline the reflection essay", "Write the reflection essay")
#   a series — differ only by an ordinal or counter. These scored a *perfect*
#   1.0 under the old tokeniser, which discarded the digits that distinguish
#   them, making the highest-confidence "duplicates" the clearest false ones.
assert not _flags("Watch Module 1 (30 mins)", "Watch Module 2 (30 mins)")
assert not _flags("Get quote from provider 1", "Get quote from provider 2")
assert not _flags("Review first 5 case studies", "Review next 5 case studies")
assert not _flags("Write introduction paragraph", "Write conclusion paragraph")

# --- totals must match their own steps -------------------------------------
# v1 answered "24 minutes" for a task whose steps summed to 51.
assert check_plan(_task(estimated_duration=24, subtasks=_steps(15, 36)), "T")
assert not check_plan(_task(estimated_duration=51, subtasks=_steps(15, 36)), "T")

# --- good_enough_criteria: the field the product exists for -----------------
assert check_good_enough(None)
assert check_good_enough("")
assert check_good_enough("All fields completed accurately")          # perfectionist
assert check_good_enough("Every room is spotless")                   # perfectionist
assert check_good_enough("Submitted to the office by 10 AM")         # a deadline
assert not check_good_enough("The main points are covered and it reads clearly")

# --- prerequisite ordering -------------------------------------------------
# Both of these shipped in v1: filing before gathering, and opening a tap
# without shutting the water off.
assert check_ordering({"subtasks": [
    {"title": "File tax returns"}, {"title": "Gather the documents"}]})
assert not check_ordering({"subtasks": [
    {"title": "Gather the documents"}, {"title": "File tax returns"}]})
assert check_ordering({"subtasks": [
    {"title": "Unscrew the tap head"}, {"title": "Fit the new washer"}]})
assert not check_ordering({"subtasks": [
    {"title": "Turn the water off at the valve"}, {"title": "Unscrew the tap head"}]})

# --- the extraction gate ---------------------------------------------------
# A deadline must be quoted from the task, never computed. This is what stops
# the model inventing dates the way v1 did (73% of its targets were 2023).
task_text = "Clean the apartment before guests arrive on Saturday"
assert not check_due_phrase({"due_phrase": "before guests arrive on Saturday"}, task_text)
assert not check_due_phrase({"due_phrase": None}, task_text)          # no deadline is fine
assert check_due_phrase({"due_phrase": "next Tuesday"}, task_text)    # invented
assert check_due_phrase({"due_phrase": "2023-10-14"}, task_text)      # computed
assert check_due_phrase({"due_phrase": "   "}, task_text)             # empty but present

# --- invented third parties ------------------------------------------------
# v1 invented a "travel agent" for a self-service booking.
assert check_plan(_task(subtasks=[
    {"title": "Confirm details with the travel agent", "order": 1, "estimated_minutes": 10},
    {"title": "Book the flight", "order": 2, "estimated_minutes": 20},
]), "Book flights for the conference")

# --- schedules (unchanged from v1) -----------------------------------------
assert valid_schedule(_sched([_b("A", "09:00", "10:00"), _b("B", "10:10", "11:00")]))
assert not valid_schedule(_sched([_b("A", "09:00", "10:00"), _b("B", "09:30", "10:30")]))  # overlap
assert not valid_schedule(_sched([_b("A", "16:30", "17:30")]))    # past 17:00
assert not valid_schedule(_sched([_b("A", "10:00", "09:00")]))    # backwards
assert not valid_schedule(_sched([_b("A", "09:00", "10:00")], deferred=["A"]))  # still present
assert not valid_schedule(_sched([]))

# --- the collapse warning ---------------------------------------------------
# The report has to actually fire on v1-shaped label distributions, or it is
# decoration. v1 was HIGH on 80% of rows and nothing said so.
collapsed = [{"priority": "HIGH", "category": "WORK"} for _ in range(9)]
collapsed.append({"priority": "LOW", "category": "PERSONAL"})
assert "WARNING" in label_distribution_report(collapsed)
balanced = [{"priority": p, "category": "WORK"} for p in ("LOW", "MEDIUM", "HIGH", "URGENT")]
assert "WARNING" not in label_distribution_report(balanced).split("category")[0]

print("all filter checks passed")
