"""Gold examples: body set (hand-authored).

Covers health, fitness, food and daily habits — the domain the previous model
handled worst. Asked to restart running after two months off, it prescribed
5-6 sessions a week and a "30-minute warm-up" that ran for 15 minutes: an
aggressive schedule and an internally contradictory step in the same plan.

So every example here that involves returning to or starting a physical habit
follows the same shape: a tiny first step, then two or three repeats at the
*same* easy effort, and only then a step that adds anything — never a jump
straight to an ambitious schedule. Nothing here gives medical advice, a
dosage or a diagnosis; anything clinical routes to a professional (write the
symptoms down for the GP, bring the questions to the appointment) rather than
substituting for one.

See `goldlib.Gold` for the format and `quality.py` for the rules every
example must pass.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from goldlib import Gold

G = Gold

# ---------------------------------------------------------------------------
# Fitness — starting from nothing, or restarting after a break. The gradual
# build is the whole point of this file existing.
# ---------------------------------------------------------------------------
FITNESS = [
    G("Start strength training, I've never lifted anything in my life",
      "Start strength training from scratch", "Build a beginner strength routine without overdoing it",
      "LOW", "HEALTH",
      "You've done the light routine twice this week and nothing feels wrecked the next day",
      [("Write down two days this week you can realistically train", 10),
       ("Find a simple beginner routine using just bodyweight or light dumbbells", 15),
       ("Do the first session, keeping every set light and stopping well short of failure", 30),
       ("Repeat the same light session on the second day", 30),
       ("Add a little more weight only once both sessions felt comfortable", 30)]),

    G("Get back into swimming, I haven't been to the pool in over a year",
      "Get back into swimming", "Ease back into regular pool sessions",
      "LOW", "HEALTH",
      "You've been to the pool twice this week and could still hold a conversation afterwards",
      [("Find your swimming costume and goggles and check they still fit", 10),
       ("Check the pool's opening times and quieter lane-swim slots", 10),
       ("Go for a short easy swim, however many lengths feels comfortable", 30),
       ("Go again a few days later at the same easy pace", 30),
       ("Add a few more lengths only once two sessions have felt easy", 25)]),

    G("I want to start running properly this time, using one of those couch to 5k plans",
      "Start couch to 5k", "Begin a structured walk-run programme from zero running fitness",
      "MEDIUM", "HEALTH",
      "You've finished week one's three sessions without your knees complaining",
      [("Download a couch to 5k plan and read what week one actually asks for", 10),
       ("Dig out trainers that don't hurt and pick three days that work", 10),
       ("Do week one's first walk-run session at an easy effort", 30),
       ("Do the second week-one session a couple of days later", 30),
       ("Do the third week-one session before even looking at week two", 30)]),

    G("My back's been stiff for weeks, I should actually stretch instead of just wincing about it",
      "Build a stretching habit for the stiff back", "Get a short daily stretch routine going",
      "LOW", "HEALTH",
      "You've stretched most days this week and the ache is duller by evening, not worse",
      [("Clear five minutes of floor space today", 5),
       ("Look up two or three gentle stretches for a stiff lower back", 10),
       ("Do the short routine once and note if anything felt sharp rather than tight", 10),
       ("Repeat the same short routine most days this week", 60)]),

    G("Meant to keep up the exercises for my sprained ankle and completely stopped",
      "Restart the ankle rehab exercises", "Get back to the exercises after stopping",
      "MEDIUM", "HEALTH",
      "You've done the gentle set daily for a week without new pain the next day",
      [("Find the exercise sheet or advice you were given for the ankle", 10),
       ("Pick a fixed time of day to attach the exercises to", 10),
       ("Do a shortened version of the set for the first couple of days", 15),
       ("Build back up to the full set once the shortened version feels easy", 30),
       ("Check with whoever prescribed them before adding anything new", 15)]),

    G("I sit at a desk all day and probably don't walk more than 500 steps, need to fix that",
      "Walk more during the work day", "Build in regular walking around a desk job",
      "MEDIUM", "HEALTH",
      "You've added the extra walk most days this week without having to think about it",
      [("Note how much you actually walk on a normal day right now", 10),
       ("Pick one small addition, like a lunchtime loop or getting off a stop early", 10),
       ("Do that one extra walk today", 15),
       ("Repeat it most days this week", 60),
       ("Add a second short walk only once the first feels automatic", 20)]),

    G("Bike's been in the shed all winter, want to start riding again before it gets warm",
      "Get back into cycling", "Ease back into regular rides after a winter off the bike",
      "MEDIUM", "HEALTH",
      "You've ridden twice this week at an easy pace and your legs aren't complaining the next day",
      [("Get the bike out and check the tyres still hold air", 10),
       ("Pick one easy, familiar route to start with", 10),
       ("Do a short ride at a pace you could hold a conversation through", 30),
       ("Do a similar short ride again later in the week", 30),
       ("Only make the next ride longer once both felt easy", 25)]),
]

# ---------------------------------------------------------------------------
# Food, drink and the habits around consuming less or better
# ---------------------------------------------------------------------------
FOOD = [
    G("Every morning is a scramble, want to get breakfasts sorted the night before instead",
      "Meal prep breakfasts for the week", "Set up a simple make-ahead breakfast routine",
      "MEDIUM", "PERSONAL",
      "There are ready breakfasts for most weekday mornings and mornings feel less rushed",
      [("Pick one simple make-ahead breakfast you'd actually eat", 10),
       ("Check you have containers and buy what's missing", 20),
       ("Make a batch big enough for most of the week", 45),
       ("Portion it into containers and put them somewhere obvious in the fridge", 15)]),

    G("I want to actually learn to cook, not just follow recipes blindly and hope",
      "Learn basic cooking and knife skills", "Build the underlying technique instead of just following recipes",
      "LOW", "LEARNING",
      "You can chop an onion and cook a simple dish without checking the recipe line by line",
      [("Watch one short video on basic knife grip and cutting technique", 15),
       ("Practise chopping an onion, carrot and pepper using what you watched", 20),
       ("Cook one simple recipe, paying attention to the technique rather than rushing", 45),
       ("Cook the same recipe again a few days later without checking every line", 40)]),

    G("We've ordered takeaway four times this week and I know exactly why the money's gone",
      "Cut down on takeaways", "Reduce how often food gets ordered in",
      "MEDIUM", "HEALTH",
      "You've cooked at home more nights than you've ordered in, two weeks running",
      [("Count how many takeaways you actually had last week", 10),
       ("Pick one night to swap for something quick to cook instead", 10),
       ("Stock the freezer or cupboard with two or three fast backup meals", 30),
       ("Cook at home on the night you picked instead of ordering", 30),
       ("Keep it to that one swap for a couple of weeks before adding another", 15)]),

    G("I basically only drink coffee all day, should probably have some actual water",
      "Drink more water through the day", "Build the habit of drinking water rather than just coffee",
      "LOW", "HEALTH",
      "You're getting through a bottle or two of water most days without having to force it",
      [("Find a water bottle you'll actually carry around", 5),
       ("Fill it and put it somewhere you'll see it first thing", 5),
       ("Refill it once during the day for the next few days", 30),
       ("Notice when you'd normally reach for coffee instead and swap one for water", 20)]),

    G("Want to actually cut back on drinking, it's crept up since last year",
      "Cut down on drinking", "Reduce how much and how often alcohol is being drunk",
      "MEDIUM", "HEALTH",
      "You've had two or three alcohol-free days this week without it feeling like a fight",
      [("Write down roughly how many drinks you actually had last week", 10),
       ("Pick one or two days this week to make alcohol-free", 10),
       ("Line up something else for the evenings you'd normally have a drink", 15),
       ("Get through the alcohol-free days you picked", 20),
       ("Notice how they felt and decide whether to add a third day", 15)]),

    G("Five coffees a day is clearly too many, need to bring it down",
      "Cut down on caffeine", "Reduce daily coffee intake gradually",
      "LOW", "HEALTH",
      "You're down by a cup or two a day without the headaches that come from stopping cold",
      [("Count how many coffees you actually had yesterday", 5),
       ("Cut just the last one of the day for a few days", 15),
       ("Swap one more cup for tea or water once that feels normal", 15),
       ("Hold at that level for a week before cutting further", 30)]),

    G("Trying to quit smoking again, this time I want an actual plan instead of just willpower",
      "Quit smoking", "Set up practical support for stopping smoking",
      "HIGH", "HEALTH",
      "You've gone a smoke-free week using the support in place, slip-ups noted rather than hidden",
      [("Pick the date you're actually starting from, not a vague 'soon'", 10),
       ("Book a stop-smoking service appointment or order nicotine replacement", 15),
       ("Clear cigarettes, lighters and ashtrays out of the house", 15),
       ("Tell one or two people so there's someone to be accountable to", 10),
       ("Get through the first smoke-free week, using the replacement when the urge hits", 60),
       ("Check in with the stop-smoking service and adjust what isn't working", 20)]),
]

# ---------------------------------------------------------------------------
# Medical admin — appointments, screenings, prescriptions. Concrete practical
# actions only: book it, prep the questions, lay the paperwork out. Nothing
# here diagnoses or advises; it routes to a professional.
# ---------------------------------------------------------------------------
MEDICAL = [
    G("I always realise I'm nearly out of my repeat prescription at the worst possible time, want a system",
      "Set up a repeat prescription system", "Stop running out of regular medication unexpectedly",
      "MEDIUM", "HEALTH",
      "The next two repeat orders are already set to go out with time to spare",
      [("List the medications you get on repeat and how long each lasts", 10),
       ("Check whether the surgery or pharmacy offers online repeat ordering", 15),
       ("Set up the online account or app if you haven't already", 20),
       ("Work out roughly how many days before running out you need to order", 10),
       ("Put a reminder in for the next order date", 10)]),

    G("Haven't had a proper check-up in years, keep telling myself I'll sort it next month",
      "Book the overdue GP check-up", "Get a general check-up booked after putting it off for years",
      "HIGH", "HEALTH",
      "There's an appointment in the calendar, whatever date they could offer",
      [("Check you're still registered at a GP practice", 10),
       ("Note anything that's been nagging you that you want to mention", 10),
       ("Call or book online for the next available appointment", 15),
       ("Put it in the calendar with a reminder the day before", 5)]),

    G("I've cancelled the smear test twice already, need to actually go this time",
      "Book the smear test", "Get the overdue screening actually booked and attended",
      "HIGH", "HEALTH",
      "The appointment is booked and in the calendar, not just thought about again",
      [("Find the invitation letter or the surgery's number", 10),
       ("Book the appointment for a time you're actually likely to keep", 15),
       ("Put it in the calendar with a reminder a day before", 5),
       ("Write down any questions you want to ask while you're there", 10)]),

    G("Can't remember the last time I had my eyes tested, everything's a bit blurry lately",
      "Book the overdue eye test", "Get an eye test booked after putting it off",
      "MEDIUM", "HEALTH",
      "The appointment is booked and you've noted the changes worth mentioning",
      [("Note down what's actually changed, like blur at distance or headaches", 10),
       ("Check if your current glasses or lenses prescription details are saved anywhere", 10),
       ("Book the appointment at an optician near you", 15),
       ("Put it in the calendar with a reminder the day before", 5)]),

    G("Got a hospital appointment coming up and last time I completely forgot everything I meant to ask",
      "Prepare for the hospital appointment", "Go in ready instead of forgetting everything on the day",
      "HIGH", "HEALTH",
      "You have the questions and the paperwork ready and know how you're getting there",
      [("Write down the symptoms and when they started, so you can describe them clearly", 15),
       ("List the questions you actually want answered", 10),
       ("Gather any letters, scan results or medication list they might ask for", 20),
       ("Check how you're getting there and how long parking or transport takes", 15),
       ("Pack the paperwork and questions somewhere you won't forget them", 5)]),

    G("Just found out I've got a nut allergy and have no idea how to actually live around it day to day",
      "Set up a routine around the nut allergy", "Build practical habits for living with a new allergy",
      "MEDIUM", "HEALTH",
      "You've got through a normal week of meals and shopping without a scare",
      [("Write down exactly what you were told to avoid and carry it with you", 10),
       ("Check what emergency medication you've been given and where to keep it", 15),
       ("Go through the kitchen cupboards and flag anything that's a risk", 30),
       ("Do one supermarket shop reading labels properly rather than guessing", 40),
       ("Tell the people you eat with regularly so they know too", 15)]),

    G("Got a letter months ago about a free health check and it's still sitting on the side unopened basically",
      "Book the health check", "Get the screening invitation actually followed up",
      "HIGH", "HEALTH",
      "The health check is booked, whatever date they could offer",
      [("Find the letter and read what the check actually involves", 10),
       ("Call or book online for an appointment", 15),
       ("Note anything you need to do beforehand, like fasting", 10),
       ("Put it in the calendar with a reminder the day before", 5)]),

    G("Been in bed with flu for a week, don't want to just leap back into normal life tomorrow",
      "Ease back in after the flu", "Return to normal activity gradually after being ill",
      "MEDIUM", "HEALTH",
      "You've had a couple of normal days without needing to stop and rest",
      [("Note how you're actually feeling today rather than how you think you should feel", 10),
       ("Do one short easy task today, like a walk round the block", 15),
       ("Go back to work or normal activity at a shortened pace for the first day", 60),
       ("Build back to the full routine only once a shortened day feels easy", 30)]),

    G("Just noticed I've only got two days of my prescription left and completely forgot to order more",
      "Order the prescription before it runs out", "Get the repeat prescription ordered before the current supply ends",
      "URGENT", "HEALTH",
      "The order is in and you know when it'll be ready to collect",
      [("Check exactly how many doses you've got left", 5),
       ("Order the repeat through the surgery, pharmacy or app", 15),
       ("Check when it'll be ready and note it somewhere you'll see", 10),
       ("Collect it before the current supply runs out", 20)]),
]

# ---------------------------------------------------------------------------
# Daily routines and small habit supports
# ---------------------------------------------------------------------------
ROUTINE = [
    G("Mornings are chaos, I want an actual routine instead of just panicking out the door",
      "Build a morning routine", "Put a simple, repeatable morning routine in place",
      "LOW", "PERSONAL",
      "You've followed roughly the same routine most mornings this week without rushing",
      [("Write down what actually needs to happen before you leave the house", 10),
       ("Put them in a realistic order and time roughly how long each takes", 10),
       ("Try the routine tomorrow morning as written", 30),
       ("Adjust the one step that went wrong and try again the next day", 15)]),

    G("I'm on my phone in bed until stupid o'clock every night and wondering why I feel awful",
      "Cut screen time before bed", "Reduce phone use in the hour before sleep",
      "LOW", "HEALTH",
      "You've had phone-free evenings a few nights this week and noticed you dropped off easier",
      [("Note what time you actually put the phone down the last few nights", 5),
       ("Pick a realistic cut-off time, not an ideal one", 5),
       ("Move the charger out of arm's reach of the bed", 10),
       ("Line up something else to do in that last half hour, like reading", 10),
       ("Try it for a few nights and see whether falling asleep gets easier", 30)]),

    G("I keep missing the morning gym session because I'm still packing the bag at 6am",
      "Pack the gym bag the night before", "Stop the morning scramble that's costing you the session",
      "LOW", "PERSONAL",
      "The bag's been ready the night before a few times running and you actually made it in",
      [("Find everything that usually goes in the bag: kit, shoes, water bottle, towel", 10),
       ("Pack it the evening before your next session", 10),
       ("Leave it by the door so it's the first thing you see", 5),
       ("Do this the night before each session for a couple of weeks", 30)]),

    G("I've signed up and quietly stopped going to that fitness class about four times now",
      "Actually stick with the fitness class", "Build consistency with the class instead of quietly dropping out again",
      "MEDIUM", "HEALTH",
      "You've been to the class two weeks running without cancelling on yourself",
      [("Look back at how many classes you've paid for and actually missed", 10),
       ("Pick just the one class a week to commit to, not an ambitious three", 10),
       ("Put it in the calendar and lay the kit out the night before", 10),
       ("Go to that one class", 60),
       ("Go to the same class again the following week before adding a second", 60)]),

    G("Realised I probably need jabs before the trip and haven't looked into it at all",
      "Sort out travel vaccinations", "Get travel vaccinations arranged before the trip",
      "HIGH", "HEALTH",
      "The appointment is booked with enough time left for the jabs to take effect",
      [("Check which vaccinations are recommended for where you're going", 15),
       ("Find a travel clinic or GP practice that offers them", 10),
       ("Book the appointment, checking it leaves enough time before you fly", 15),
       ("Go to the appointment and get the jabs done", 30),
       ("Note in the calendar if a booster or second dose is needed", 10)]),

    G("Dentist told me off about flossing again and I still haven't started",
      "Build a flossing habit", "Actually start flossing daily like the dentist keeps saying",
      "LOW", "HEALTH",
      "You've flossed most nights this week without having to remind yourself",
      [("Buy floss or interdental brushes and put them by the toothbrush", 10),
       ("Floss tonight, even if it's a rushed rough job", 5),
       ("Do it again each night this week straight after brushing", 30)]),

    G("I realised I sat completely still for four hours straight yesterday, that can't be good",
      "Add movement breaks to the work day", "Break up long stretches of sitting with short regular movement",
      "LOW", "HEALTH",
      "You've stood up roughly once an hour most of the day without setting constant alarms",
      [("Set a repeating reminder for roughly once an hour", 10),
       ("Decide on one simple move for the break, like a stretch or a lap of the room", 5),
       ("Do it when the first reminder goes off today", 5),
       ("Keep responding to the reminder for the rest of the day", 60)]),
]

GOLD: list[Gold] = FITNESS + FOOD + MEDICAL + ROUTINE
