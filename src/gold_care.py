"""Gold examples: caring for people and animals, and relationships.

Covers the caregiving and relational side of the app's users: getting kids
ready for school, looking after elderly parents, taking care of pets, and the
conversations people put off — apologising, reconnecting, sorting out a
falling-out with a neighbour. Mostly PERSONAL, some HEALTH where the task is
genuinely medical or physical, with ADMIN only where the task is actually a
form.

These are practical plans, not therapeutic ones: the steps are things like
"write down the one thing you need to say," never "process your feelings." See
`goldlib.Gold` for the format and `quality.py` for the rules every example
must pass.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from goldlib import Gold

G = Gold

# ---------------------------------------------------------------------------
# Kids
# ---------------------------------------------------------------------------
KIDS = [
    G("Get the kids ready for the new school term, it's crept up on me again",
      "Get the kids ready for the new school term", "Sort uniform, kit and supplies before school goes back",
      "MEDIUM", "PERSONAL",
      "The uniform fits, the bag's packed and the big supply list is covered — a couple of small items can wait",
      [("Try the old uniform on both kids to see what still fits", 15),
       ("Order or buy whatever's outgrown", 30),
       ("Label the new items with their names", 15),
       ("Work through the stationery and kit list", 25),
       ("Pack the bags together the night before term starts", 15)]),

    G("Help with the maths homework without just doing it for her",
      "Help with the maths homework", "Support her through it without taking it over",
      "MEDIUM", "PERSONAL",
      "She got through the homework understanding it, even if you had to nudge her more than once",
      [("Ask her to show you what she's tried so far", 10),
       ("Work through one example together, talking through each step", 15),
       ("Let her attempt the next one alone while you watch", 15),
       ("Check her answer only once she asks you to", 10)]),

    G("Sort out childcare now I'm going back to work three days a week",
      "Arrange the childcare", "Get regular childcare in place for the working days",
      "HIGH", "PERSONAL",
      "A place is booked for the days you need — it doesn't have to be the ideal setup on day one",
      [("Work out exactly which days need covering", 15),
       ("Call round the local nurseries and childminders for availability", 30),
       ("Visit the two options that could actually work", 60),
       ("Book a place and pay the deposit", 20),
       ("Tell work the confirmed start date", 10)]),

    G("Start potty training now the health visitor says he's ready",
      "Start potty training", "Begin potty training now he's showing signs of readiness",
      "MEDIUM", "HEALTH",
      "He's using the potty some of the time and you know roughly what helps — accidents are still normal at this stage",
      [("Buy a potty and some easy-off trousers", 15),
       ("Clear a few days with no long outings planned", 10),
       ("Put him in pants and offer the potty every hour or so", 60),
       ("Praise every attempt, not just the successes", 15),
       ("Drop the daytime nappy once he's dry a few days running", 20)]),

    G("Plan my son's 7th birthday party",
      "Plan the 7th birthday party", "Organise the party for his birthday",
      "HIGH", "PERSONAL",
      "The date, food and guests are sorted and everyone's been told, even if the theme is a bit thrown together",
      [("Agree a guest list with him", 15),
       ("Pick a date and book a venue or clear the house", 30),
       ("Send the invites out", 20),
       ("Sort the food and order a cake", 40),
       ("Buy party bags and a couple of games", 30)]),

    G("Teach her to ride her bike without stabilisers",
      "Teach her to ride without stabilisers", "Get her riding a two-wheeler on her own",
      "LOW", "HEALTH",
      "She's managed a few wobbly metres unaided — smoothing it out can happen over the following weeks",
      [("Take the stabilisers off and lower the seat so her feet reach", 15),
       ("Find a flat, traffic-free spot to practise", 10),
       ("Hold the saddle and jog alongside while she pedals", 30),
       ("Let go for a few seconds at a time once she has balance", 30)]),
]

# ---------------------------------------------------------------------------
# Elderly parents
# ---------------------------------------------------------------------------
ELDERCARE = [
    G("Get mum's care needs properly looked at, she's been struggling more than she admits",
      "Arrange mum's care assessment", "Get a needs assessment organised through social services",
      "HIGH", "PERSONAL",
      "The assessment is booked or done and you know what support she's entitled to — sorting the funding can follow",
      [("Call social services and ask for a needs assessment", 15),
       ("Write down what's actually become difficult for her day to day", 20),
       ("Be there for the assessment visit", 60),
       ("Read through what they recommend once it arrives", 20),
       ("Look into next steps for anything they won't fund", 30)]),

    G("Fit grab rails in dad's bathroom before he's discharged",
      "Fit grab rails in dad's bathroom", "Get grab rails installed before he comes home from hospital",
      "HIGH", "PERSONAL",
      "The rails are fitted and solid to lean on — the grouting round them can be tidied up later",
      [("Work out where he'll need support getting in and out of the bath", 15),
       ("Buy grab rails rated for the wall type", 25),
       ("Find the studs, or the right fixings for a stud-free wall", 15),
       ("Drill and fit the rails", 40),
       ("Put your full weight on each one to check it holds", 5)]),

    G("Sort mum's medication now she's got pills from three different doctors",
      "Sort out mum's medication", "Get her different prescriptions organised into one system",
      "HIGH", "HEALTH",
      "Everything's in one organiser with the times written down — you don't need to have memorised it yourself",
      [("Lay out every box and blister pack on the table", 15),
       ("Write down what each one is for and when it's taken", 25),
       ("Check with the pharmacist for anything that shouldn't be mixed", 20),
       ("Buy a pill organiser with day and time slots", 20),
       ("Fill it for the week ahead together", 25)]),

    G("Actually visit dad more than once a month like I keep meaning to",
      "Visit dad more regularly", "Get into a habit of seeing him more often",
      "LOW", "PERSONAL",
      "You've been once this week without waiting for an occasion — keeping it up matters more than the frequency",
      [("Pick a day that's realistically free most weeks", 10),
       ("Put a standing note in the calendar for it", 5),
       ("Go this week rather than waiting for a reason", 60)]),

    G("Look after my partner for the first week after his knee surgery",
      "Look after him after the knee surgery", "Get him through the first week of recovery at home",
      "HIGH", "HEALTH",
      "He's managing at home and getting what he needs — he doesn't have to be back on his feet yet",
      [("Set up a downstairs spot with everything he'll need in reach", 15),
       ("Collect him from the hospital and get his prescriptions on the way", 90),
       ("Handle the cooking and stairs for the first few days", 120),
       ("Help him keep up with the physio exercises he's been given", 20),
       ("Step back gradually as he manages more himself", 15)]),

    G("Agree a fair rota with my brother for who does what for mum",
      "Agree a caring rota with my brother", "Split mum's care fairly between the two of you",
      "MEDIUM", "PERSONAL",
      "You've got a rough split you've both agreed to — it can be adjusted once you see how it actually works",
      [("List everything mum currently needs help with", 15),
       ("Work out what each of you can realistically manage", 20),
       ("Talk it through with him and propose a split", 30),
       ("Write down who does what and when", 15)]),

    G("Help mum apply for attendance allowance now she needs more support",
      "Help mum apply for attendance allowance", "Get the application submitted for her",
      "MEDIUM", "ADMIN",
      "The form is sent off describing a genuinely bad day — you don't need the ideal wording",
      [("Find the application form and check she's eligible", 15),
       ("Note down her diagnoses and what she needs help with", 25),
       ("Fill in the form describing a typical hard day", 40),
       ("Ask her GP or a support worker to check it over", 20),
       ("Send it off and note when to expect a decision", 10)]),
]

# ---------------------------------------------------------------------------
# Pets
# ---------------------------------------------------------------------------
ANIMALS = [
    G("Get the dog's limp checked out, it's been three days now",
      "Get the dog's limp checked out", "Get the vet to look at the limp that hasn't cleared up",
      "HIGH", "HEALTH",
      "He's been seen and you've got a plan to follow — it doesn't mean he's already back to normal",
      [("Call the vet and describe the limp to see how soon he needs to be seen", 15),
       ("Keep him rested and off it until the appointment", 20),
       ("Take him in for the appointment", 45),
       ("Follow whatever they recommend for the days after", 15)]),

    G("House-train the new puppy",
      "House-train the puppy", "Get her reliably toileting outside",
      "MEDIUM", "PERSONAL",
      "She's mostly going outside with the odd accident — a full week without one isn't realistic yet",
      [("Pick a spot outside as her toilet area", 10),
       ("Take her out first thing, after meals and after naps", 60),
       ("Praise and treat her the second she goes in the right spot", 15),
       ("Clean any accidents with something that kills the smell", 15),
       ("Keep the routine going for a couple of weeks", 30)]),

    G("Puppy-proof the house before he arrives on Saturday",
      "Puppy-proof the house", "Make the house safe before the puppy comes home",
      "LOW", "PERSONAL",
      "The obvious hazards are dealt with — you'll spot more once he's actually exploring",
      [("Walk round at floor level and spot anything chewable or dangerous", 15),
       ("Move or tape down loose wires", 20),
       ("Put a stair gate across any rooms that are off limits", 15),
       ("Set up a crate with bedding in a quiet corner", 15)]),

    G("Rehome the rabbits, we can't keep them after the move",
      "Rehome the rabbits", "Find them a good new home before the move",
      "MEDIUM", "PERSONAL",
      "They've gone somewhere that can actually look after them properly — it doesn't have to be the ideal setup",
      [("Write an honest description of them and their setup", 15),
       ("Ask the local rescue or rabbit groups if they can help place them", 20),
       ("Take clear photos of them and their hutch", 15),
       ("Meet anyone interested before agreeing to anything", 45),
       ("Hand over the hutch, food and vet record together", 20)]),

    G("The cat hasn't eaten since yesterday morning",
      "Get the cat seen, she's not eating", "Get her checked out after a day of not eating",
      "URGENT", "HEALTH",
      "She's been seen by a vet and you know what to watch for — she doesn't have to be eating normally again yet",
      [("Check her gums and see if she's drinking or hiding more than usual", 10),
       ("Call the vet and describe exactly what's changed", 15),
       ("Get her into the carrier", 10),
       ("Take her in", 45),
       ("Follow whatever they recommend for feeding once you're home", 15)]),
]

# ---------------------------------------------------------------------------
# Relationships — the conversations people put off
# ---------------------------------------------------------------------------
RELATIONSHIPS = [
    G("Have the conversation with my flatmate about the mess before I lose it",
      "Talk to my flatmate about the mess", "Raise it calmly before it turns into a blow-up",
      "MEDIUM", "PERSONAL",
      "You said the specific thing that's bothering you — it doesn't have to have landed smoothly",
      [("Write down the one or two things that actually bother you", 10),
       ("Pick a calm moment rather than mid-annoyance", 5),
       ("Say the specific thing without listing the whole backlog", 20),
       ("Agree one concrete change to try", 15)]),

    G("Sort things out with my partner about money, we keep avoiding it",
      "Talk to my partner about money", "Have the conversation you've both been putting off",
      "HIGH", "PERSONAL",
      "You had the conversation and said the main thing — it doesn't have to have gone smoothly",
      [("Write down what's actually worrying you about it", 15),
       ("Pick an evening with no other distractions", 10),
       ("Say the specific thing you need to say without dredging up old arguments", 30),
       ("Agree one concrete next step together", 15)]),

    G("Apologise to my sister properly, not just a text",
      "Apologise to my sister properly", "Make the apology properly instead of a quick text",
      "MEDIUM", "PERSONAL",
      "You said it plainly and she knows you mean it — it doesn't have to fix things immediately",
      [("Work out exactly what you're apologising for, not the vague version", 15),
       ("Decide to say it in person or on a call rather than by text", 5),
       ("Say it plainly without immediately explaining yourself", 20),
       ("Ask what would actually help and do that", 20)]),

    G("I keep meaning to call my grandmother and now it's been so long it feels awkward",
      "Call my grandmother", "Get past the awkwardness and just make the call",
      "LOW", "PERSONAL",
      "You spoke to her — it doesn't need to have been a long call",
      [("Pick a time she's usually free and put it in the diary", 5),
       ("Make the call without over-planning how to open it", 20)]),

    G("Reconnect with my old uni friend, we've drifted apart these past couple of years",
      "Reconnect with my old uni friend", "Get back in touch properly rather than just liking a photo",
      "LOW", "PERSONAL",
      "You've messaged and suggested meeting up — whether she takes you up on it is out of your hands",
      [("Send a message referencing something specific you remember", 15),
       ("Suggest an actual date to meet or call, not just 'we should catch up'", 10),
       ("Put it in the diary once she replies", 5)]),

    G("Support my friend after her dad died, I don't know what to actually do",
      "Support my friend after her dad died", "Do something practical rather than just saying you're there",
      "MEDIUM", "PERSONAL",
      "You've done one concrete useful thing for her — you don't have to have found the right words",
      [("Text her to say you're thinking of her rather than waiting for the right words", 5),
       ("Offer one specific practical thing rather than 'let me know if you need anything'", 10),
       ("Follow through on whatever she says would help", 40),
       ("Check in again the following week, not just now", 10)]),

    G("Sort out the fence dispute with next door before it gets worse",
      "Sort out the fence dispute with next door", "Deal with the boundary argument before it escalates",
      "HIGH", "PERSONAL",
      "You've raised it calmly and agreed a way forward — it doesn't have to be resolved to your exact liking",
      [("Check the deeds or boundary plan to see whose fence it is", 15),
       ("Write down what's actually happened so far", 15),
       ("Knock on their door and raise it calmly rather than by note", 20),
       ("Agree who pays for what in writing", 20),
       ("Get quotes and book the work once you've agreed", 30)]),
]

# ---------------------------------------------------------------------------
# Community — showing up for people beyond the immediate household
# ---------------------------------------------------------------------------
COMMUNITY = [
    G("Start volunteering at the food bank like I keep saying I will",
      "Start volunteering at the food bank", "Actually get signed up and turn up",
      "LOW", "PERSONAL",
      "You've done the first shift and it's in the diary again — you don't have to commit to a fixed pattern yet",
      [("Look up the local food bank's volunteering page", 10),
       ("Sign up for an induction slot", 10),
       ("Go to the induction", 90),
       ("Put a recurring shift in the calendar", 10)]),

    G("Plan the visit to see my parents, we haven't been in ages",
      "Plan the visit to my parents", "Get an actual visit organised rather than talking about it",
      "MEDIUM", "PERSONAL",
      "Dates are agreed and travel's booked — the itinerary can stay loose",
      [("Check dates that work for both households", 15),
       ("Book the travel or block out the driving time", 30),
       ("Tell them roughly how long you're staying", 5),
       ("Sort cover for the dog or whatever's keeping you home", 20)]),

    G("Get properly involved with the school PTA instead of just paying the sub",
      "Get involved with the school PTA", "Take on one actual role rather than staying on the sidelines",
      "LOW", "PERSONAL",
      "You've been to a meeting and taken on one job — you don't need to run the whole thing",
      [("Message the PTA to say you'd like to help with one specific job", 10),
       ("Go along to the next meeting to confirm it", 60),
       ("Do that job for the coming event", 90)]),

    G("Sign up to be a regular blood donor",
      "Sign up to donate blood", "Get registered and give the first donation",
      "LOW", "HEALTH",
      "You've given the first donation and booked the next — that's the habit started",
      [("Check you're eligible to give blood", 10),
       ("Register on the donor service's site", 15),
       ("Book the first appointment", 10),
       ("Go and give the first donation", 45),
       ("Book the next one before you leave", 5)]),

    G("Sort out visiting my aunt in the care home, I haven't been since she moved in",
      "Visit my aunt in the care home", "Get the first visit done and a pattern started",
      "MEDIUM", "PERSONAL",
      "You've made the first visit — settling into a regular pattern can follow",
      [("Check the home's visiting hours and any booking system", 10),
       ("Pick a day and put it in the diary", 5),
       ("Think of one or two things to bring or talk about", 10),
       ("Go for the first visit", 60),
       ("Agree a rough regular pattern with her afterwards", 10)]),
]

GOLD: list[Gold] = KIDS + ELDERCARE + ANIMALS + RELATIONSHIPS + COMMUNITY
