"""Semantic quality gates for training targets.

Pydantic (`schema.py`) checks *shape*. These check whether a plan is actually
sensible. v1 had filters only for minute sums and schedule geometry, and every
defect that reached the shipped checkpoint slipped through the gaps:

  - 28% of `good_enough_criteria` demanded perfection or completeness — the one
    field the product exists for, and nothing validated it
  - the prompt asked for 2-6 subtasks; 28 examples had 7-11 and 27 had none
  - "File tax returns" appeared as step 1, before gathering any documents

Each function below returns a list of human-readable reasons, empty when clean,
so `repair.py` can report *why* an example was dropped rather than silently
losing it.
"""

import re

# Absolutist language that turns a stopping point into a perfectionist trap.
# "Complete the form" is fine; "all fields completed accurately" is not.
PERFECTIONIST = re.compile(
    r"\b(all|every|each|entire|complete(?:ly|d)?|perfect(?:ly)?|thorough(?:ly)?|"
    r"fully|flawless(?:ly)?|100%|no errors|error[- ]free|without any|"
    r"nothing (?:is )?(?:missed|missing|left)|exhaustive|comprehensive)\b",
    re.I,
)

# A "good enough" criterion must not be a deadline. v1 produced
# "submitted to the office by 10 AM" for a task that mentioned no such time.
CLOCK_TIME = re.compile(
    r"(\b\d{1,2}:\d{2}\b|\bby \d{1,2}\s*(?:am|pm)\b|\bdeadline\b|\bon time\b|"
    r"\bbefore \d|\bby (?:monday|tuesday|wednesday|thursday|friday|saturday|sunday)\b)",
    re.I,
)

MIN_SUBTASKS = 2
MAX_SUBTASKS = 6
# The first step is the one that has to beat inertia. v1 shipped a median of
# 15 min here by accident — nothing in its prompt asked for it — so the property
# needs a gate before a regenerated dataset quietly loses it.
MAX_FIRST_STEP_MINUTES = 15
# Repair is more forgiving than generation: a 20-minute opener is worth keeping,
# a 60-minute one is not a broken-down task at all.
MAX_FIRST_STEP_MINUTES_REPAIR = 30

# Steps that only make sense once something else has happened, and the step that
# must precede them. Catches the two concrete ordering bugs v1 shipped and the
# general shape of "acted before preparing".
PREREQUISITES: list[tuple[re.Pattern, re.Pattern, str]] = [
    (re.compile(r"\b(file|submit|e-?file|lodge)\b.*\b(return|taxes|tax)\b", re.I),
     re.compile(r"\b(gather|collect|assemble|find|locate|organi[sz]e|prepare|sort)\b", re.I),
     "files/submits before gathering documents"),
    (re.compile(r"\b(disassemble|dismantle|unscrew|open up|take apart|replace)\b.*"
                r"\b(tap|faucet|pipe|valve|cistern|toilet)\b", re.I),
     # "Turn the water off at the valve" puts words between turn and off, so
     # match the two halves independently rather than as a fixed phrase.
     re.compile(r"\b(?:turn|shut|switch)\b.{0,30}\boff\b|\bisolat", re.I),
     "opens plumbing before shutting off the water"),
    # Only decorating needs surface prep. Painting a picture does not, and an
    # earlier version of this rule failed a perfectly good "paint a small study"
    # example for not sanding first.
    (re.compile(r"\b(paint|prime|sand)\b.{0,40}"
                r"\b(wall|ceiling|room|door|fence|furniture|skirting|frame)\b", re.I),
     re.compile(r"\b(clean|wash|mask|cover|prep|prepare|sand|sugar soap)\b", re.I),
     "paints before preparing the surface"),
    (re.compile(r"\b(send|post|mail)\b.*\b(email|letter|application|form)\b", re.I),
     re.compile(r"\b(draft|write|compose|review|proofread|check)\b", re.I),
     "sends before drafting"),
]


def _norm_words(text: str) -> set[str]:
    return set(re.findall(r"[a-z]+", text.lower()))


# Tokens that mark a step as one *of a series* rather than a restatement of its
# neighbour: ordinals, counters, and part labels. When two titles differ only by
# one of these they are parallel or sequential work, not a duplicated step.
ENUMERATOR = re.compile(
    r"^\d+$|^(?:first|second|third|fourth|fifth|sixth|seventh|eighth|ninth|tenth|"
    r"next|another|final|last|remaining|other|part|module|section|chapter|day|week|"
    r"round|batch|phase|stage|[a-z])$", re.I)


def _dup_tokens(text: str) -> set[str]:
    """Tokens for near-duplicate comparison — digits included.

    `_norm_words` drops digits, which made "Get quote from provider 1" and
    "…provider 2" score a perfect 1.0 against each other: the only
    distinguishing character was thrown away before comparison. Every
    highest-scoring "duplicate" in the v1 data was this bug, not a real defect.
    """
    return set(re.findall(r"[a-z0-9]+", text.lower()))


# Word overlap alone turned out to be the wrong signal, at every threshold.
# Measured over the v1 corpus: the pairs it scored *highest* were legitimate
# parallel steps, while the real defect the shipped model produced — "Set up
# CI/CD pipeline" restated as "Set up CI/CD pipeline with environment variables"
# — scores 0.33 and was caught at no threshold at all.
#
# The distinction is structural rather than quantitative. A restated step is a
# **subset**: it says everything its twin said and adds only filler. Parallel and
# sequential steps each carry a token the other lacks (LinkedIn/Facebook,
# strengths/weaknesses, outline/write), so neither contains the other. That test
# catches the real shape and cannot fire on a well-formed plan.
JACCARD_CEILING = 0.85


def _is_restatement(a: set[str], b: set[str]) -> bool:
    """True when one step says nothing its neighbour didn't already say."""
    if a <= b or b <= a:
        return True
    # Belt and braces for titles that are near-identical without nesting
    # (a swapped article, a plural). Deliberately high: everything below this
    # in the corpus is a genuine parallel step.
    return len(a & b) / len(a | b) >= JACCARD_CEILING


def _is_sequence_pair(a: set[str], b: set[str]) -> bool:
    """True when two titles differ only by enumerators — a series, not a repeat.

    "Watch Module 1" / "Watch Module 2", "Review first 5 case studies" /
    "Review next 5 case studies", "Draft response to first urgent email" /
    "…second…". These are correct plans and must not be rejected.
    """
    diff = a ^ b
    return bool(diff) and all(ENUMERATOR.match(w) for w in diff)


def check_good_enough(criteria: str | None) -> list[str]:
    """Is this a permission-to-stop, or a perfectionist standard in disguise?"""
    problems = []
    if not criteria or not criteria.strip():
        return ["good_enough_criteria is missing"]
    if len(criteria.strip()) < 12:
        problems.append("good_enough_criteria too short to mean anything")
    m = PERFECTIONIST.search(criteria)
    if m:
        problems.append(f"good_enough_criteria is perfectionist ('{m.group(0)}')")
    m = CLOCK_TIME.search(criteria)
    if m:
        problems.append(f"good_enough_criteria contains a deadline ('{m.group(0)}')")
    return problems


def check_subtasks(task: dict, first_step_cap: int = MAX_FIRST_STEP_MINUTES) -> list[str]:
    problems = []
    subs = task.get("subtasks") or []
    n = len(subs)
    if not (MIN_SUBTASKS <= n <= MAX_SUBTASKS):
        problems.append(f"{n} subtasks (want {MIN_SUBTASKS}-{MAX_SUBTASKS})")
        if n == 0:
            return problems

    titles = [str(s.get("title", "")).strip() for s in subs]
    if any(not t for t in titles):
        problems.append("a subtask has no title")
    lowered = [t.lower() for t in titles]
    if len(set(lowered)) != len(lowered):
        problems.append("duplicate subtask titles")
    # Near-duplicates too: v1 emitted "Replace faucet assembly" and "Install new
    # faucet assembly" as separate steps of the same three-step plan.
    for i in range(len(titles)):
        for j in range(i + 1, len(titles)):
            a, b = _dup_tokens(titles[i]), _dup_tokens(titles[j])
            # Require two content words on each side: one-word titles ("Tidy",
            # "Bake") overlap trivially and would flag on nothing.
            if len(a) < 2 or len(b) < 2:
                continue
            # A step that differs from its neighbour only by an ordinal or
            # counter is part of a series, however high its word overlap.
            if _is_sequence_pair(a, b):
                continue
            if _is_restatement(a, b):
                problems.append(f"steps {i+1} and {j+1} are near-duplicates")
                break

    orders = [s.get("order") for s in subs]
    if orders != list(range(1, n + 1)):
        problems.append(f"subtask order is {orders}, want 1..{n}")

    first = subs[0].get("estimated_minutes")
    if isinstance(first, int) and first > first_step_cap:
        problems.append(f"first step is {first} min (want <= {first_step_cap})")
    return problems


def check_duration(task: dict, tolerance: float = 0.0) -> list[str]:
    """Total must equal the sum of the steps.

    v1's prompt asked for both a 20% buffer *and* a sum-matching total, which
    cannot both hold; the student learned the incoherence and answered "24
    minutes" for a task whose own steps added up to 51.
    """
    subs = task.get("subtasks") or []
    dur = task.get("estimated_duration")
    if not subs or not isinstance(dur, int):
        return []
    total = sum(s.get("estimated_minutes", 0) for s in subs)
    if tolerance == 0.0:
        return [] if total == dur else [f"steps sum to {total}, estimated_duration is {dur}"]
    if not ((1 - tolerance) * dur <= total <= (1 + tolerance) * dur):
        return [f"steps sum to {total}, estimated_duration is {dur}"]
    return []


def check_ordering(task: dict) -> list[str]:
    """Catch a step that acts before its prerequisite exists in the plan."""
    subs = task.get("subtasks") or []
    titles = [str(s.get("title", "")) for s in subs]
    problems = []
    for act_re, prereq_re, why in PREREQUISITES:
        act_at = next((i for i, t in enumerate(titles) if act_re.search(t)), None)
        if act_at is None:
            continue
        prereq_at = next((i for i, t in enumerate(titles) if prereq_re.search(t)), None)
        if prereq_at is None or prereq_at > act_at:
            problems.append(f"ordering: {why}")
    return problems


def check_invention(task: dict, user_task: str) -> list[str]:
    """Flag third parties the task never mentioned.

    v1 invented a "travel agent" for a self-service flight booking and an
    "account manager's system" for cancelling a gym membership.
    """
    said = _norm_words(user_task) | _norm_words(str(task.get("description", "")))
    invented = {"agent", "assistant", "secretary", "manager", "team", "stakeholders",
                "client", "vendor", "contractor", "landlord", "hr"}
    problems = []
    for s in task.get("subtasks") or []:
        for w in _norm_words(str(s.get("title", ""))) & invented:
            if w not in said:
                problems.append(f"invents a third party ('{w}') the task never mentioned")
                return problems
    return problems


def check_due_phrase(task: dict, user_task: str) -> list[str]:
    """The extraction gate: a deadline must be *quoted*, never *computed*.

    This is the rule that makes the model an extractor rather than an oracle.
    v1 asked it for a `due_date` it had no way to know, and 73% of the training
    targets came back dated 2023. Here the model may only echo deadline words
    that already appear in the task text, and the app resolves them against the
    real clock. An invented deadline fails this check by construction, because
    invented text is not a substring of the input.
    """
    phrase = task.get("due_phrase")
    if phrase is None:
        return []
    if not isinstance(phrase, str) or not phrase.strip():
        return ["due_phrase present but empty — use null when there is no deadline"]
    phrase = phrase.strip()
    if ISO_DATE.search(phrase):
        return [f"due_phrase '{phrase}' is a computed date — quote the task's own words"]
    haystack = " ".join(user_task.lower().split())
    if " ".join(phrase.lower().split()) not in haystack:
        return [f"due_phrase '{phrase}' is not a span of the task text (invented)"]
    return []


# A due_phrase must never be a resolved date — that is the app's job.
ISO_DATE = re.compile(r"\b\d{4}-\d{2}-\d{2}\b|\b\d{1,2}/\d{1,2}/\d{2,4}\b")


def check_plan(parsed: dict, user_task: str = "", *, strict: bool = True) -> list[str]:
    """All gates for one plan. `strict=False` relaxes the caps used when
    repairing existing data, where dropping a third of the corpus costs more
    than a slightly loose first step."""
    task = parsed.get("task")
    if not isinstance(task, dict):
        return ["no task object"]
    cap = MAX_FIRST_STEP_MINUTES if strict else MAX_FIRST_STEP_MINUTES_REPAIR
    problems = []
    problems += check_subtasks(task, first_step_cap=cap)
    problems += check_duration(task, tolerance=0.0 if strict else 0.15)
    problems += check_good_enough(task.get("good_enough_criteria"))
    problems += check_ordering(task)
    if user_task:
        problems += check_invention(task, user_task)
        problems += check_due_phrase(task, user_task)
    return problems


def coverage_report(tasks: list[dict]) -> str:
    """Warn when a field is present in the schema but absent from every target.

    This exists because of a real miss: `due_phrase` was added to the schema,
    the prompt, the gates, the app-side resolver and the tests — and then
    backfilled into exactly zero training examples. Trained that way the student
    would have learned "always emit null" and the feature would have been dead on
    arrival, with nothing in the pipeline saying so.

    A field the prompt asks for and no example demonstrates is not a feature.
    Run this before every training run.
    """
    lines = []
    total = len(tasks) or 1
    for field in ("due_phrase",):
        present = sum(1 for t in tasks if t.get(field) not in (None, "", []))
        pct = present / total
        lines.append(f"  {field:16s}: {present}/{total} non-null ({pct:.0%})")
        if present == 0:
            lines.append(f"    ^^ BLOCKER: the prompt asks for {field} and no example "
                         f"demonstrates it — the student will learn to always omit it")
        elif pct < 0.05:
            lines.append(f"    ^^ WARNING: only {pct:.0%} coverage; the student may "
                         f"treat {field} as always-null")

    # Second-order check: a faithfully-extracted phrase the app cannot turn into
    # a date populates the field without ever producing a due date. "next
    # Monday" resolves; "before he's discharged" is a correct extraction that
    # DeadlineParser will return null for.
    #
    # Both are legitimate *targets* — the model's job is to quote, not to
    # resolve — but that is NOT a reason to ignore a low ratio here. Keeping an
    # event-anchored phrase is right; writing a corpus that is mostly
    # event-anchored is not, because then the trained feature populates a field
    # the user never sees turn into a date. The fix is upstream of extraction:
    # write more *task texts* that state a datable deadline ("by Tuesday",
    # "in three weeks", "before the 14th"), so there is something datable to
    # quote. Do not relabel event-anchored phrases to make this number go up.
    phrases = [t["due_phrase"] for t in tasks if t.get("due_phrase")]
    if phrases:
        res = sum(1 for p in phrases if RESOLVABLE.search(p))
        share = res / len(phrases)
        lines.append(f"  {'  of which resolvable':16s}: {res}/{len(phrases)} ({share:.0%}) "
                     f"carry a token DeadlineParser can date")
        if share < 0.4:
            lines.append(f"    ^^ WARNING: only {share:.0%} resolve to an actual date. The "
                         f"field will populate but rarely set a due date — favour "
                         f"phrases with a weekday, a date, or an 'in N days' span")
    return "\n".join(lines)


# Tokens DeadlineParser can actually anchor to a calendar. Event-anchored
# phrases ("before the trip") are valid extractions but resolve to nothing.
RESOLVABLE = re.compile(
    r"\b(today|tonight|tomorrow|yesterday|monday|tuesday|wednesday|thursday|friday|"
    r"saturday|sunday|january|february|march|april|may|june|july|august|september|"
    r"october|november|december)\b|\bnext\s+\w+|\bin\s+(?:a|an|one|two|three|four|five|"
    r"six|seven|eight|nine|ten|\d+)\s+(?:day|week|month|hour)s?\b|"
    r"\bthis\s+(?:week|month|weekend|morning|afternoon|evening)\b|\d{1,2}(?:st|nd|rd|th)\b|"
    r"\d{4}-\d{2}-\d{2}", re.I)


def label_distribution_report(tasks: list[dict]) -> str:
    """v1's priority labels were HIGH 395 / URGENT 76 / MEDIUM 20 / LOW 1, so the
    student simply always said HIGH. Print this before every training run."""
    from collections import Counter
    lines = []
    for field in ("priority", "category"):
        counts = Counter(t.get(field) for t in tasks)
        total = sum(counts.values()) or 1
        parts = [f"{k} {v} ({v/total:.0%})" for k, v in counts.most_common()]
        lines.append(f"  {field:9s}: " + ", ".join(parts))
        top = counts.most_common(1)
        if top and top[0][1] / total > 0.5:
            lines.append(f"    ^^ WARNING: {top[0][0]} is {top[0][1]/total:.0%} of all"
                         f" examples — the student will collapse to it")
    return "\n".join(lines)


# Kept for backwards compatibility with generate.py / test_filters.py.
def valid_plan(parsed: dict) -> bool:
    return not check_plan(parsed, strict=False)
