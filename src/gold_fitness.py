"""Gold examples: fitness and health, second pass (hand-authored).

`gold_body.py` already owns "returning to or starting a physical habit from
zero" — strength, running, swimming, cycling, and the food/drink habits that
sit next to them (water, caffeine, alcohol, smoking, screen time before bed).
Its whole design principle is the gradual-restart shape: tiny first step, two
or three repeats at the same easy effort, only then a step that adds
anything.

This module deliberately steers around all of that and covers the health
territory `gold_body` leaves alone:

  - rehab exercises a professional has already prescribed (following a given
    routine, not designing one) — physio sheets, post-surgery exercises,
    cardiac rehab walking plans
  - sleep — insomnia, jet lag, adjusting to a new shift pattern, a proper
    wind-down routine, waking in the night
  - tapering habits `gold_body` doesn't already cover — nail-biting, vaping,
    energy drinks, sugary desk snacking, late-night eating (not smoking,
    alcohol or caffeine, which are already there)
  - building a health habit from nothing that isn't a "restart" — posture,
    eye strain, a morning stretch, daylight, an ergonomic desk setup
  - the daily logistics of a chronic condition — home blood pressure or
    blood sugar monitoring, a headache diary, medication timing relative to
    food, a seasonal antihistamine routine, an inhaler routine — always
    routed to what a professional already asked for, never a diagnosis
  - getting physically ready for a specific one-off event by a date (a race,
    a hike, a house move's heavy lifting) rather than resuming a routine
  - the logistical mental load around health that is *not* therapeutic:
    fitting medications, meals and a shift pattern together. Logistics, not
    counseling — this app is a work-management tool, not a therapy app.

Nothing here diagnoses, doses or substitutes for a professional; anything
that needs one routes to what they already prescribed or to writing it down
for the next appointment. See `goldlib.Gold` for the format and `quality.py`
for the rules every example must pass.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from goldlib import Gold

G = Gold

# ---------------------------------------------------------------------------
# Rehab — following a routine a professional already handed over, not
# designing one from scratch.
# ---------------------------------------------------------------------------
REHAB = [
    G("Physio gave me exercises for my knee after the injury, actually need to start doing them",
      "Start the physio exercises for the knee", "Follow through on the knee exercises the physio actually prescribed",
      "LOW", "HEALTH",
      "You've done the set on the days the physio asked for, without pushing through sharp pain",
      [("Find the exercise sheet or app the physio gave you", 10),
       ("Set a fixed time or day to attach the exercises to", 10),
       ("Do the first session exactly as written, stopping short of sharp pain", 20),
       ("Do it again on the next day the physio specified", 20),
       ("Note anything that felt wrong to mention at the next appointment", 10)]),

    G("Just had shoulder surgery and the hospital gave me a rehab sheet I haven't looked at",
      "Start the post-surgery shoulder rehab", "Begin the shoulder exercises the hospital sent home with",
      "MEDIUM", "HEALTH",
      "You've done the gentle exercises on the days the sheet asks for and nothing feels worse the next day",
      [("Read through the rehab sheet properly", 15),
       ("Check which exercises are meant to start straight away versus later weeks", 10),
       ("Do the first week's exercises gently, stopping if anything sharpens", 15),
       ("Repeat them on the next scheduled day", 15),
       ("Flag anything that felt wrong at the follow-up appointment", 10)]),

    G("Physio wants me doing these hip exercises three times a week and I've done them once",
      "Get back on track with the hip exercises", "Actually hit the three-times-a-week routine the physio set",
      "MEDIUM", "HEALTH",
      "You've done the hip set on most of the days the physio asked for this week",
      [("Check the sheet for exactly which exercises and how many sets", 10),
       ("Pick three specific days this week and put them somewhere visible", 10),
       ("Do the set on the first picked day", 15),
       ("Do it again on the second picked day", 15),
       ("Do the third session before the week's out", 15)]),

    G("Got given a set of exercises for tennis elbow at the appointment, haven't touched them since",
      "Start the tennis elbow exercises", "Begin the exercises given at the appointment instead of leaving the sheet in a drawer",
      "LOW", "HEALTH",
      "You've done the set a couple of times this week without the elbow feeling worse after",
      [("Dig out the exercise sheet from the appointment", 5),
       ("Read through what it actually asks for", 10),
       ("Do the first gentle set today", 10),
       ("Do it again a couple of days later", 10)]),

    G("Discharged from physio for my back but told to keep doing the exercises at home, already slipping",
      "Keep up the back exercises after discharge", "Restart the home exercises now the supervised sessions have stopped",
      "MEDIUM", "HEALTH",
      "You've done the home set most days this week without the back feeling worse",
      [("Find the discharge sheet with the home exercises on it", 10),
       ("Pick a fixed time of day to do them", 10),
       ("Do the set today, keeping it gentle", 15),
       ("Do it again most days this week", 45)]),

    G("Cardiac rehab nurse gave me a walking plan to build up to after the surgery, feels daunting",
      "Start the cardiac rehab walking plan", "Begin the graded walking plan the cardiac rehab nurse set out",
      "MEDIUM", "HEALTH",
      "You've done the plan's first stage on the days it asks for without feeling wiped out after",
      [("Read through the walking plan properly", 15),
       ("Check what the very first stage actually asks for", 10),
       ("Do the first walk at the pace and distance the plan sets, not further", 20),
       ("Repeat it on the next day the plan specifies", 20),
       ("Note how it felt to mention at the next check-in", 10)]),
]

# ---------------------------------------------------------------------------
# Sleep — insomnia, jet lag, shift work, a wind-down routine.
# ---------------------------------------------------------------------------
SLEEP = [
    G("Been lying awake for hours most nights, need to actually do something about it",
      "Get a handle on not being able to sleep", "Build a wind-down routine instead of just lying awake worrying about it",
      "MEDIUM", "HEALTH",
      "You've had a couple of nights this week where you dropped off quicker than lying there for hours",
      [("Write down roughly what time you actually fall asleep most nights", 10),
       ("Look up two or three basic sleep hygiene changes worth trying", 15),
       ("Pick one small change to start with, like a fixed wind-down time", 10),
       ("Try it for a few nights and notice if falling asleep gets easier", 30),
       ("Write down the pattern to mention to the GP if it doesn't shift", 15)]),

    G("Flying to Tokyo for work next week and my sleep is going to be a disaster if I don't plan for it",
      "Plan for the jet lag before Tokyo", "Get ahead of the time difference instead of just arriving wrecked",
      "MEDIUM", "HEALTH",
      "You've got a rough plan for the flight and the first couple of days written down",
      [("Work out the time difference and how many hours you'll be shifting", 10),
       ("Look up whether shifting your sleep a little beforehand is worth doing", 15),
       ("Nudge bedtime slightly earlier or later for a couple of nights before flying", 20),
       ("Plan how you'll handle the flight itself, like when to sleep on board", 15),
       ("Decide how the first day there will go, easing in rather than a packed schedule", 15)],
      due="next week"),

    G("Just moved to night shifts and my sleep is completely backwards, feels awful",
      "Adjust sleep to the new night shift pattern", "Get a workable sleep schedule going around the new shifts",
      "MEDIUM", "HEALTH",
      "You've had a few shifts in a row where you slept a decent stretch during the day",
      [("Work out the block of hours you actually need to sleep around the shifts", 10),
       ("Sort the bedroom for daytime sleep, like blackout curtains or an eye mask", 20),
       ("Tell the people you live with the hours you'll be asleep", 10),
       ("Try the new sleep block after the next shift", 60),
       ("Adjust the timing if it didn't work and try again", 20)]),

    G("Keep going to bed at 1am even though I know it's wrecking me, need an actual wind-down routine",
      "Build an actual wind-down routine", "Put a proper wind-down in place instead of drifting to bed at 1am",
      "LOW", "HEALTH",
      "You've started winding down earlier most nights this week and bedtime's crept back a bit",
      [("Note what actually happens in the hour before you end up in bed", 10),
       ("Pick a realistic earlier target, not an ideal one", 5),
       ("Decide on two or three things to do in that wind-down hour", 10),
       ("Try the routine tonight", 30),
       ("Repeat it most nights this week and see if bedtime shifts", 60)]),

    G("Landing back from the states next Tuesday and last time the jet lag took me out for a week",
      "Plan for jet lag coming back from the states", "Get ahead of the return jet lag instead of losing a week to it again",
      "MEDIUM", "HEALTH",
      "You've got a plan for the first few days back and know what to keep light",
      [("Check how many time zones you'll be crossing on the way back", 10),
       ("Get some daylight and stay awake at the destination's daytime hours before flying", 15),
       ("Plan the first couple of days back to be light, nothing that needs sharp focus", 15),
       ("Decide roughly what time you'll aim to sleep the first night back", 10)],
      due="next Tuesday"),

    G("Alarm goes off at 5am for the new shift pattern and I'm still sleeping like it's 9am",
      "Shift the body clock earlier for the new alarm", "Get up-time and sleep-time actually lined up with the new shift start",
      "MEDIUM", "HEALTH",
      "You've woken up without a fight a few mornings in a row this week",
      [("Work out what time you'd need to fall asleep to get a proper night's sleep before the new alarm", 10),
       ("Shift bedtime 15 minutes earlier for a couple of nights", 10),
       ("Keep shifting it in small steps until it matches", 30),
       ("Get some morning light as soon as the alarm goes to help the shift stick", 10)]),

    G("Been waking up at 3am every night for weeks and just lying there watching the ceiling",
      "Deal with the 3am waking", "Work out what to do about waking at 3am most nights instead of just lying there",
      "MEDIUM", "HEALTH",
      "You've had a few nights this week where you dropped back off quicker than usual",
      [("Write down what's actually happening for a few nights: time you wake, how long it takes to drop off", 15),
       ("Look up what's actually recommended for middle-of-the-night waking", 15),
       ("Try getting up and doing something calm rather than lying there next time it happens", 20),
       ("Keep a note of the pattern to bring to the GP if it carries on", 15)]),
]

# ---------------------------------------------------------------------------
# Tapering habits `gold_body` doesn't already own (not smoking, alcohol or
# caffeine — those are covered there).
# ---------------------------------------------------------------------------
TAPERING = [
    G("Chewed my nails down to nothing again in that meeting, actually want to stop for good this time",
      "Stop biting my nails", "Build in something that actually gets in the way of the nail-biting habit",
      "LOW", "HEALTH",
      "You've caught yourself and stopped it a few times this week instead of never noticing",
      [("Notice the situations where it actually happens, like meetings or reading", 10),
       ("Buy a bitter-tasting nail polish or get a manicure as a physical deterrent", 15),
       ("Apply it today", 5),
       ("Top it up through the week as it wears off", 15)]),

    G("Vape's basically permanently in my hand now and I want to cut it out",
      "Cut down on vaping", "Start bringing the vaping down instead of it just being constant",
      "MEDIUM", "HEALTH",
      "You've gone a stretch of the day without it a few times this week, not just white-knuckling it",
      [("Notice roughly how often you actually reach for it in a normal day", 15),
       ("Pick one situation to cut it out of first, like first thing in the morning", 10),
       ("Get through today without it in that one situation", 30),
       ("Keep that one change going for a few days before picking another", 60)]),

    G("Living off energy drinks to get through afternoons at work, need to wean off them",
      "Wean off the afternoon energy drinks", "Bring the energy drink habit down instead of relying on it every afternoon",
      "LOW", "HEALTH",
      "You've swapped it for something else a few afternoons this week without the usual crash",
      [("Count how many you actually have on a normal day", 5),
       ("Cut one of them out this week, ideally the latest one", 10),
       ("Line up something else for that slot, like water or a short walk", 10),
       ("Hold at that level for a few days before cutting another", 30)]),

    G("Snacking on sugary stuff all afternoon at my desk and I know exactly why",
      "Cut back on the afternoon desk snacking", "Bring the sugary snacking down instead of grazing on it all afternoon",
      "LOW", "HEALTH",
      "You've swapped the snack for something else a few afternoons this week",
      [("Notice what time the craving actually hits", 10),
       ("Stock one better option nearby, like fruit or nuts", 15),
       ("Swap it in for the sugary snack tomorrow afternoon", 5),
       ("Keep doing the swap for the rest of the week", 30)]),

    G("Been eating a full meal at midnight most nights and know it's not helping my sleep",
      "Cut down on the midnight eating", "Bring the late-night eating earlier instead of a full meal at midnight",
      "LOW", "HEALTH",
      "You've eaten earlier a few nights this week without going to bed hungry",
      [("Notice what's actually driving it, like a late dinner or boredom", 10),
       ("Move dinner earlier by half an hour for a few nights", 15),
       ("Line up a small earlier snack for if hunger genuinely hits later", 10),
       ("Keep the earlier timing going for the rest of the week", 40)]),
]

# ---------------------------------------------------------------------------
# Building a health habit from nothing — not a "restart", there was never a
# routine here to begin with.
# ---------------------------------------------------------------------------
FOUNDATIONS = [
    G("Sit hunched over my laptop all day and my neck's constantly tight, should probably fix my posture",
      "Fix the desk posture", "Actually address the hunched-over posture instead of just noticing the tight neck",
      "LOW", "HEALTH",
      "You've caught and corrected the slouch a few times most days this week",
      [("Take a photo or video of how you actually sit right now", 10),
       ("Look up two or three basic fixes for laptop posture", 15),
       ("Adjust the screen height or chair using what's around already", 15),
       ("Set a reminder to check posture a couple of times a day", 5),
       ("Notice and correct the slouch when the reminder goes off", 30)]),

    G("Eyes are wrecked by the end of the day from staring at screens, need to actually do something about it",
      "Ease the screen strain on my eyes", "Build in regular screen breaks instead of staring straight through the day",
      "LOW", "HEALTH",
      "You've taken the short breaks most of the day without having to force it",
      [("Look up the 20-20-20 rule and what it actually asks for", 5),
       ("Set a repeating reminder for roughly every 20 minutes", 10),
       ("Look at something further away when the first reminder goes off", 5),
       ("Keep responding to it for the rest of the day", 60)]),

    G("Never stretch in the morning, just roll out of bed and go, want to build that in",
      "Build a morning stretch habit", "Add a short stretch before the day gets going instead of straight out of bed",
      "LOW", "HEALTH",
      "You've done the short stretch most mornings this week before checking your phone",
      [("Look up three or four easy morning stretches", 10),
       ("Clear a small bit of floor space by the bed", 5),
       ("Do the stretch tomorrow morning before anything else", 10),
       ("Repeat it most mornings this week", 50)]),

    G("Barely see daylight all winter working from this desk, should probably fix that",
      "Get more daylight during the work day", "Build in a bit of actual daylight instead of missing it all winter",
      "LOW", "HEALTH",
      "You've got outside or near a window most days this week, not just some",
      [("Check what daylight hours actually overlap with the work day right now", 10),
       ("Pick one point in the day to get outside, like a short walk at lunch", 10),
       ("Move the desk nearer a window if that's realistic", 15),
       ("Do the outside break today", 15),
       ("Keep it going most days this week", 60)]),

    G("Desk setup is a disaster, chair's wrong height and I'm hunched over the laptop all day",
      "Sort out the desk setup", "Fix the chair and screen height instead of hunching over the laptop all day",
      "LOW", "HEALTH",
      "The chair and screen are at a decent height and the neck ache isn't there by the end of the day",
      [("Check the current chair and screen height against basic ergonomic guidance", 15),
       ("Adjust the chair height first", 10),
       ("Raise the laptop or screen using books or a stand", 15),
       ("Work a normal day with the new setup and notice how the neck feels", 60)]),
]

# ---------------------------------------------------------------------------
# Chronic condition daily routines — always following what a professional
# already asked for; nothing here diagnoses or adjusts a dose.
# ---------------------------------------------------------------------------
CHRONIC = [
    G("Doctor wants me tracking my blood pressure at home for a few weeks, haven't started",
      "Start tracking blood pressure at home", "Get the home blood pressure monitoring actually going",
      "MEDIUM", "HEALTH",
      "You've logged a reading most days this week at roughly the same time",
      [("Find or buy a home blood pressure monitor", 15),
       ("Check the doctor's instructions for when and how often to measure", 10),
       ("Take the first reading and write it down", 10),
       ("Take readings at the same time most days this week", 30),
       ("Bring the log to the next appointment", 5)]),

    G("Meant to be logging my blood sugar readings properly since the diagnosis, keep forgetting",
      "Start logging blood sugar readings", "Get the blood sugar log actually going instead of forgetting",
      "MEDIUM", "HEALTH",
      "You've logged readings most days this week instead of skipping them",
      [("Find the meter and check it's got strips and is working", 10),
       ("Check what times you're actually meant to be testing", 10),
       ("Log the next reading straight after testing", 5),
       ("Keep logging at the same points most days this week", 30)]),

    G("GP wants me keeping a headache diary to spot what's triggering the migraines",
      "Start the headache diary", "Get the migraine trigger diary going the GP asked for",
      "MEDIUM", "HEALTH",
      "You've logged most of the headaches this week with roughly what came before them",
      [("Find or set up a simple template for the diary", 10),
       ("Log the next headache with what you'd eaten, slept and been doing", 10),
       ("Keep logging each one this week as it happens", 40),
       ("Bring the diary to the next GP appointment", 5)]),

    G("Thyroid medication has to be taken at a specific time relative to food and I keep getting it wrong",
      "Sort out the thyroid medication timing", "Get the timing relative to food actually right instead of guessing",
      "MEDIUM", "HEALTH",
      "You've taken it at the right gap from food most days this week",
      [("Check exactly what gap from food the instructions actually call for", 10),
       ("Work out where that fits around a normal day's meals", 10),
       ("Set a reminder for the right time", 10),
       ("Take it at that time tomorrow and notice if it fits", 5),
       ("Keep it going for the rest of the week", 30)]),

    G("Hay fever's already bad and I know I'll forget to start the antihistamines again like every year",
      "Start the hay fever antihistamines early this year", "Get ahead of the hay fever instead of starting late again",
      "LOW", "HEALTH",
      "You've taken it most days this week instead of only when it's already bad",
      [("Check what's actually in the cupboard or needs buying", 10),
       ("Take the first dose today", 5),
       ("Put a daily reminder in for the rest of the season", 10),
       ("Keep taking it most days this week", 30)]),

    G("Asthma nurse wants me using the inhaler properly twice a day, keep forgetting the evening one",
      "Fix the evening inhaler routine", "Actually get the evening dose in instead of just forgetting it",
      "MEDIUM", "HEALTH",
      "You've taken the evening dose most nights this week without having to remember at the last second",
      [("Check what time the evening dose is actually meant to happen", 5),
       ("Attach it to something you already do every evening, like brushing teeth", 10),
       ("Take it tonight at that point", 5),
       ("Keep attaching it to the same routine for the rest of the week", 30)]),
]

# ---------------------------------------------------------------------------
# Getting physically ready for a specific one-off event by a date — the
# shape is "get ready for X", not "resume a routine".
# ---------------------------------------------------------------------------
EVENT_PREP = [
    G("Signed up for a charity 10k in eight weeks and haven't run further than the bus stop in months",
      "Get ready for the charity 10k", "Build up to the 10k from close to zero running fitness",
      "MEDIUM", "HEALTH",
      "You've done the first couple of weeks of a plan without your knees complaining",
      [("Find a beginner 10k training plan that fits eight weeks", 15),
       ("Pick three days a week you can realistically train", 10),
       ("Do the first easy run or walk-run session", 30),
       ("Do the second session a couple of days later", 30),
       ("Check in after week one and adjust if anything hurt", 15)],
      due="in eight weeks"),

    G("We're doing a big coastal hike in three weeks and my legs are nowhere near ready",
      "Get ready for the coastal hike", "Build up leg fitness before the hike instead of arriving cold",
      "MEDIUM", "HEALTH",
      "You've done a couple of longer walks this week and your legs held up the next day",
      [("Check how far and how hilly the actual route is", 10),
       ("Break in or check the boots you'll be wearing", 15),
       ("Do one longer walk this week, ideally on hills if any are nearby", 45),
       ("Do a second longer walk a few days later", 45)],
      due="in three weeks"),

    G("Moving house ourselves next month, going to be lifting boxes all weekend and my back's not exactly strong",
      "Get ready for the lifting-heavy move", "Build a bit of back and leg strength before a weekend of carrying boxes",
      "MEDIUM", "PERSONAL",
      "You've done a couple of short strength sessions and know how to lift without wrecking your back",
      [("Look up how to lift boxes properly without straining the back", 10),
       ("Do a short session of simple strength moves, like squats and step-ups", 20),
       ("Repeat it a few days later", 20),
       ("Sort a back brace or gloves if the move looks like it needs them", 15)],
      due="next month"),

    G("Ski trip's in six weeks and my legs always die on the first day if I don't prep",
      "Get the legs ready before the ski trip", "Build up leg strength so the first day on the slopes isn't a write-off",
      "MEDIUM", "HEALTH",
      "You've done a couple of sessions this week and your legs felt less wrecked than usual after",
      [("Look up a couple of simple ski-prep exercises like squats and lunges", 10),
       ("Do the first short session", 20),
       ("Do a second session a few days later", 20),
       ("Add a bit more as the trip gets closer", 20)],
      due="in six weeks"),

    G("Signed up for a charity walk in five weeks and I've done zero training so far",
      "Get ready for the charity walk", "Start building up to the walk instead of showing up completely unprepared",
      "MEDIUM", "HEALTH",
      "You've done a couple of longer walks this week without needing to stop and rest",
      [("Check exactly how far the walk actually is", 5),
       ("Do one walk this week at roughly a third of that distance", 40),
       ("Do a second, slightly longer walk a few days later", 45),
       ("Sort shoes and anything you'll need to carry on the day", 15)],
      due="in five weeks"),

    G("First triathlon try in ten weeks, still haven't started training and panicking a bit",
      "Start training for the first triathlon", "Get a beginner plan going across swim, bike and run instead of panicking",
      "MEDIUM", "HEALTH",
      "You've done one swim, bike and run session this week without anything feeling wrecked after",
      [("Find a beginner triathlon plan that fits ten weeks", 15),
       ("Check what kit you actually have and what's missing", 15),
       ("Do one easy swim, bike or run session, whichever fits today", 30),
       ("Do the other two disciplines later in the week at an easy effort", 60),
       ("Check in after week one and adjust the plan if anything hurt", 15)],
      due="in ten weeks"),

    G("Doing a big charity bike ride in seven weeks and haven't been on the bike since last summer",
      "Get ready for the charity bike ride", "Build back up to the distance before the ride instead of starting cold on the day",
      "MEDIUM", "HEALTH",
      "You've ridden a couple of times this week and your legs weren't wrecked the next day",
      [("Check the actual distance and route of the ride", 10),
       ("Get the bike out and check it's roadworthy", 15),
       ("Do one easy ride this week at a fraction of the distance", 40),
       ("Do a second, slightly longer ride a few days later", 40)],
      due="in seven weeks"),
]

# ---------------------------------------------------------------------------
# The mental load of fitting medications, meals and a schedule together —
# logistics, not counseling.
# ---------------------------------------------------------------------------
SCHEDULE = [
    G("Got three different medications to take at different times now and keep just guessing",
      "Sort out a proper medication schedule", "Build an actual schedule for the three medications instead of guessing",
      "MEDIUM", "HEALTH",
      "You've taken them at roughly the right times most days this week",
      [("Write down each medication and when it's actually meant to be taken", 15),
       ("Work out a realistic order that fits round meals and the day", 10),
       ("Set reminders for each one", 10),
       ("Follow the schedule today and notice what didn't fit", 5),
       ("Adjust the timing for the rest of the week", 20)]),

    G("New shift pattern means my meal times are all over the place and I'm just eating whenever",
      "Sort out meal times around the new shift pattern", "Build a workable eating schedule instead of eating whenever it happens",
      "MEDIUM", "PERSONAL",
      "You've eaten at roughly planned times for a few shifts in a row",
      [("Map out roughly when you're actually awake and working now", 10),
       ("Pick three points in that stretch to actually eat", 10),
       ("Prep or buy something for the first shift's meal times", 30),
       ("Try the new timing on the next shift", 60),
       ("Adjust anything that didn't fit and try again", 20)]),

    G("Kids' dinner, my own meals and evening meds all need to happen and none of it fits together right now",
      "Get the evening routine actually fitting together", "Line up kids' dinner, your own meals and the evening meds so they don't clash",
      "MEDIUM", "PERSONAL",
      "The evening's gone smoothly a few nights this week without a last-minute scramble",
      [("Write down what actually needs to happen and roughly when", 15),
       ("Put them in a realistic order for a normal evening", 10),
       ("Try the order tonight as written", 45),
       ("Adjust whatever clashed and try again tomorrow", 20)]),

    G("Working from home now but somehow eating lunch at 4pm most days, need an actual schedule",
      "Fix the lunch schedule working from home", "Get lunch happening at a sane time instead of drifting to 4pm",
      "LOW", "PERSONAL",
      "You've eaten lunch at roughly the planned time most days this week",
      [("Notice what's actually pushing lunch back so late", 10),
       ("Pick a realistic lunch time and put a reminder in", 5),
       ("Prep something quick to grab at that time tomorrow", 15),
       ("Eat at the new time for the rest of the week", 30)]),
]

GOLD: list[Gold] = REHAB + SLEEP + TAPERING + FOUNDATIONS + CHRONIC + EVENT_PREP + SCHEDULE
