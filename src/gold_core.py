"""Gold examples: core set (hand-authored).

Covers what distilling from Qwen3-8B demonstrably did not — measured on v1's 492
examples: 65% of tasks were arrange/schedule/email work and 1% hands-on, `LOW`
priority appeared exactly once, `CREATIVE` and `ADMIN` never appeared at all, and
nothing taught prerequisite ordering (hence "File tax returns" as step 1).

So this set leans deliberately toward physical procedures with real
prerequisites, unglamorous admin, creative work, caregiving, and the
avoidance-flavoured phrasing this app's users actually type.

See `goldlib.Gold` for the format and `quality.py` for the rules every example
must pass.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from goldlib import Gold

G = Gold

# ---------------------------------------------------------------------------
# Home repair & DIY — physical procedures with prerequisites. v1 had none.
# ---------------------------------------------------------------------------
REPAIR = [
    G("Fix the leaking kitchen tap",
      "Fix the leaking kitchen tap", "Stop the drip from the kitchen mixer tap",
      "MEDIUM", "PERSONAL",
      "The drip has stopped and the cupboard underneath stays dry overnight",
      [("Turn the water off at the isolation valve under the sink", 5),
       ("Plug the drain and lay a towel so nothing small disappears", 5),
       ("Unscrew the tap head and pull out the worn washer or cartridge", 20),
       ("Take the old part to the hardware shop and match it", 30),
       ("Fit the new part and reassemble the tap", 15),
       ("Turn the supply back on and watch the joint for seepage", 10)]),

    G("Put up the shelves that have been leaning against the wall since we moved",
      "Put up the leaning shelves", "Mount the shelf brackets and fit the boards",
      "LOW", "PERSONAL",
      "The shelves are level enough that nothing rolls, and hold the books you meant them for",
      [("Find the stud detector and the wall plugs", 10),
       ("Mark the bracket holes and check the line with a spirit level", 20),
       ("Drill and plug the holes", 25),
       ("Screw the brackets in and rest the boards on them", 20),
       ("Load the books on and check nothing sags", 10)]),

    G("The bike's been unrideable since the puncture in spring",
      "Repair the bike puncture", "Get the bike back on the road",
      "LOW", "HEALTH",
      "The bike holds air overnight and the brakes bite when you squeeze them",
      [("Find the tyre levers, patch kit and pump", 10),
       ("Take the wheel off and lever the tyre bead away", 15),
       ("Pull the tube out and find the hole by feel or in water", 15),
       ("Patch it, check the tyre for the thorn that caused it, refit", 25),
       ("Inflate, remount the wheel and test the brakes down the street", 15)]),

    G("Bleed the radiators, upstairs has been cold all week",
      "Bleed the radiators", "Clear trapped air from the upstairs radiators",
      "MEDIUM", "PERSONAL",
      "The upstairs radiators warm along their whole height instead of just the bottom",
      [("Find the bleed key and a cloth to catch drips", 5),
       ("Turn the heating off and let the system cool", 15),
       ("Open each upstairs valve until water replaces the hiss, then close it", 25),
       ("Top the boiler pressure back up if it dropped", 10),
       ("Turn the heating on and feel each radiator again", 15)]),

    G("Assemble the wardrobe that's been in a flat pack in the hall for a month",
      "Assemble the flat-pack wardrobe", "Build and stand the wardrobe",
      "LOW", "PERSONAL",
      "The doors close and it stands square, even if a spare dowel is left over",
      [("Clear a floor space wider than the wardrobe and open the box", 10),
       ("Sort the fittings into piles and find the instruction sheet", 15),
       ("Build the carcass flat on the floor", 60),
       ("Stand it up, fix it to the wall and hang the doors", 45),
       ("Adjust the hinges until the doors sit level", 20)]),

    G("Change the oil and check the tyres before the long drive",
      "Service the car before the trip", "Oil change and tyre check",
      "MEDIUM", "PERSONAL",
      "Fresh oil in, tyres at the pressure on the door sticker, and the spare is not flat",
      [("Buy the right oil grade and a new filter", 15),
       ("Park on level ground and let the engine cool", 15),
       ("Drain the old oil and swap the filter", 40),
       ("Refill, run the engine and check the level on the dipstick", 20),
       ("Set the tyre pressures including the spare", 15),
       ("Take the old oil to the recycling point", 20)]),

    G("The washing machine won't drain",
      "Unblock the washing machine", "Clear whatever is stopping the drain",
      "HIGH", "PERSONAL",
      "It drains within a normal cycle and there is no water on the floor",
      [("Switch it off at the wall and pull the plug", 5),
       ("Put a shallow tray and towels under the filter hatch", 10),
       ("Open the filter and let it drain out, clearing the trap", 20),
       ("Check the outlet hose for a kink or blockage", 15),
       ("Run a short rinse cycle and watch it empty", 25)]),

    G("Repaint the bedroom wall where the damp stain is",
      "Repaint the stained bedroom wall", "Cover the damp patch properly",
      "LOW", "PERSONAL",
      "The stain does not show through once it has dried, from normal standing distance",
      [("Check the damp source is actually fixed before painting over it", 15),
       ("Move the furniture back and put dust sheets down", 20),
       ("Sand the flaking area smooth and wipe the dust off", 25),
       ("Seal the stain with a stain-block primer and let it dry", 45),
       ("Roll two topcoats over the wall", 60)]),
]

# ---------------------------------------------------------------------------
# Cleaning, decluttering, organising
# ---------------------------------------------------------------------------
HOME = [
    G("Sort out the garage, it's been six months of avoiding it",
      "Sort out the garage", "Clear and organise the garage",
      "LOW", "PERSONAL",
      "You can walk from the door to the back wall and find the tools without moving boxes",
      [("Set a timer and clear one square metre by the door", 15),
       ("Put out four boxes: keep, donate, sell, rubbish", 10),
       ("Work along one wall at a time, sorting into the boxes", 90),
       ("Drive the donate and rubbish boxes away the same day", 45),
       ("Put the keep pile back on shelves grouped by how often you use it", 40)]),

    G("Clean the apartment before guests arrive on Saturday",
      "Clean the apartment before guests", "Get the flat presentable for visitors",
      "HIGH", "PERSONAL",
      "The rooms guests will actually see are tidy and the bathroom is fresh",
      [("Do a fast pass with a laundry basket, gathering anything out of place", 15),
       ("Clean the bathroom: sink, toilet, mirror, floor", 30),
       ("Wipe the kitchen surfaces and clear the sink", 25),
       ("Vacuum the rooms guests will be in", 25),
       ("Change the towels and take the bins out", 15)]),

    G("Declutter the wardrobe, I can't shut the door",
      "Declutter the wardrobe", "Thin out clothes until the wardrobe closes",
      "LOW", "PERSONAL",
      "The door shuts and the things you actually wear are the easiest to reach",
      [("Pull everything off one rail onto the bed", 15),
       ("Sort into keep, donate, and repair piles", 45),
       ("Bag the donations and put them by the front door", 15),
       ("Rehang the keepers with the most-worn at eye level", 30)]),

    G("Deep clean the fridge, something in there smells",
      "Deep clean the fridge", "Empty, clean and restock the fridge",
      "MEDIUM", "PERSONAL",
      "It smells neutral when you open it and you can see what is in there",
      [("Get a cool bag or box for anything that must stay cold", 10),
       ("Empty the shelves, binning anything past its date", 25),
       ("Take the shelves and drawers out and wash them", 30),
       ("Wipe the interior including the door seal", 20),
       ("Put things back grouped by type, oldest at the front", 15)]),

    G("Sort through the box of paperwork before it becomes a problem",
      "Sort the paperwork box", "Triage the accumulated post and documents",
      "MEDIUM", "ADMIN",
      "Anything needing action is in one pile with a date on it, and the rest is filed or shredded",
      [("Clear a table and get three trays: act, file, shred", 10),
       ("Open everything still sealed and sort by tray", 45),
       ("Deal with anything in the act tray that takes under two minutes", 30),
       ("File the keepers and shred the rest", 30)]),

    G("Wash the windows, they haven't been done in a year",
      "Wash the windows", "Clean the inside and reachable outside panes",
      "LOW", "PERSONAL",
      "The glass is clear looking out, even if a high corner is missed",
      [("Fill a bucket and find a squeegee and a dry cloth", 10),
       ("Do the inside of each window, top floor down", 45),
       ("Do the outside of the ground-floor windows", 40),
       ("Wipe the sills and frames while you are there", 20)]),
]

# ---------------------------------------------------------------------------
# Cooking & food
# ---------------------------------------------------------------------------
FOOD = [
    G("Plan meals and do a big grocery shop for the week",
      "Plan and shop for the week's meals", "Decide the week's meals and buy for them",
      "MEDIUM", "PERSONAL",
      "There is a plan for most evenings and the ingredients for them are in the house",
      [("Look in the fridge and cupboards and note what needs using", 15),
       ("Pick five evening meals, reusing ingredients where you can", 25),
       ("Write the list grouped by aisle", 15),
       ("Do the shop", 60),
       ("Put it away, prepping anything that will spoil first", 20)]),

    G("Batch cook lunches so I stop buying them",
      "Batch cook the week's lunches", "Cook and portion lunches in advance",
      "MEDIUM", "HEALTH",
      "There are enough portions in the fridge or freezer to cover most workdays",
      [("Pick one recipe that scales and check you have containers", 15),
       ("Buy the ingredients", 40),
       ("Cook the batch", 75),
       ("Cool it, portion into containers and label with the date", 25)]),

    G("Make my mum's birthday cake",
      "Bake the birthday cake", "Bake and decorate a cake for the party",
      "MEDIUM", "CREATIVE",
      "It tastes good and looks homemade rather than professional — that is the point",
      [("Choose the recipe and check the tin size you own", 15),
       ("Buy the ingredients you are missing", 30),
       ("Bake the sponges and let them cool", 75),
       ("Make the filling and icing", 30),
       ("Assemble and decorate it", 40)]),

    G("Learn to cook three dishes properly instead of the same pasta every night",
      "Learn three reliable dishes", "Build a small repertoire of meals you can cook well",
      "LOW", "LEARNING",
      "You can cook three dishes without reading the recipe line by line",
      [("Pick three dishes you actually want to eat often", 15),
       ("Shop for the first one and cook it following the recipe closely", 60),
       ("Cook the second, noting what you would change", 60),
       ("Cook the third, then repeat the one that went worst", 90)]),
]

# ---------------------------------------------------------------------------
# Admin, bureaucracy, money — the ADMIN category v1 never had
# ---------------------------------------------------------------------------
ADMIN = [
    G("Do my taxes",
      "File the tax return", "Prepare and submit the annual tax return",
      "HIGH", "ADMIN",
      "The return is submitted with the figures you can evidence, even if a small deduction is missed",
      [("Find last year's return to see what was needed", 15),
       ("Gather income statements, receipts and interest summaries into one folder", 60),
       ("Enter the income figures into the return", 45),
       ("Add the deductions you have paperwork for", 40),
       ("Read it back once, then submit and save the confirmation", 25)]),

    G("Cancel the gym membership",
      "Cancel the gym membership", "End the membership and stop the payments",
      "MEDIUM", "ADMIN",
      "The cancellation is confirmed in writing and the next payment does not leave your account",
      [("Find the membership number and the contract terms", 15),
       ("Check the notice period and any cancellation window", 15),
       ("Send the cancellation the way the contract requires", 20),
       ("Cancel the standing order once the confirmation arrives", 10)]),

    G("Switch banks, I've been meaning to for ages",
      "Switch to the new bank", "Move the current account across",
      "LOW", "ADMIN",
      "Salary and the main direct debits arrive at the new account and the old one is empty",
      [("List what actually pays into and out of the old account", 15),
       ("Open the new account", 30),
       ("Start the switch service and give it the old account details", 25),
       ("Update the salary details with payroll", 15),
       ("Watch both accounts for a full month before closing the old one", 30)]),

    G("Renew the passport, it expires in three months",
      "Renew the passport", "Get the passport renewed before it expires",
      "HIGH", "ADMIN",
      "The application is submitted with a photo that meets the rules and the fee paid",
      [("Check what the renewal needs and how long it is currently taking", 15),
       ("Get the photo taken to the official spec", 25),
       ("Fill in the application form", 35),
       ("Send it with the old passport and the fee, and note the tracking", 20)]),

    G("Sort out the insurance claim for the water damage",
      "File the water damage claim", "Get the claim submitted with evidence",
      "HIGH", "ADMIN",
      "The claim is lodged with photos and receipts attached and you have a reference number",
      [("Find the policy number and the claims contact", 15),
       ("Photograph the damage from several angles", 25),
       ("Gather receipts or valuations for what was damaged", 40),
       ("Fill in the claim form with what you have", 40),
       ("Submit it and write the reference number somewhere you will find it", 15)]),

    G("Chase the deposit my old landlord hasn't returned",
      "Chase the unreturned deposit", "Get the deposit back or escalate",
      "MEDIUM", "ADMIN",
      "A clear written request has gone out and you know the escalation route if it is ignored",
      [("Find the tenancy agreement and the deposit protection details", 15),
       ("Note the dates and the amount still outstanding", 15),
       ("Write a short factual request with those dates", 30),
       ("Send it and diary a follow-up two weeks out", 10),
       ("Look up the deposit scheme's dispute process so it is ready", 20)]),

    G("Set up automatic payments for the utility bills",
      "Automate the utility bills", "Put the recurring bills on automatic payment",
      "LOW", "ADMIN",
      "The regular bills leave automatically and you know roughly what date they go",
      [("List the bills that currently need manual payment", 15),
       ("Check the account has enough headroom around those dates", 15),
       ("Set up each direct debit through the provider", 40),
       ("Note the dates in one place so the balance is never a surprise", 10)]),

    G("Write the complaint letter about the broken delivery",
      "Complain about the broken delivery", "Get a refund or replacement",
      "MEDIUM", "ADMIN",
      "A factual complaint is sent with the order number and photos, asking for a specific outcome",
      [("Find the order number and the delivery date", 10),
       ("Photograph the damage and the packaging", 15),
       ("Write what happened, in order, and what you want done", 30),
       ("Send it through the retailer's complaints route and keep a copy", 15)]),
]

# ---------------------------------------------------------------------------
# Health, medical, fitness — v1's HEALTH seeds were all "book an appointment"
# ---------------------------------------------------------------------------
HEALTH = [
    G("Get back into running after two months off",
      "Restart running gently", "Rebuild a running habit without injury",
      "LOW", "HEALTH",
      "You have run three times in a fortnight without pain the next day",
      [("Dig out the shoes and check the soles are not worn through", 10),
       ("Pick three days in the week that realistically work", 15),
       ("Do the first outing as a walk-run, keeping it easy", 30),
       ("Repeat twice more at the same easy effort before adding anything", 60),
       ("Add five minutes to one run only once the others feel comfortable", 35)]),

    G("Sort out my sleep, I'm exhausted",
      "Improve the sleep routine", "Change the evening routine to sleep better",
      "MEDIUM", "HEALTH",
      "You are going to bed at a similar time most nights and waking less groggy",
      [("Note what time you actually went to bed for the last few nights", 10),
       ("Pick a realistic lights-out time, not an ideal one", 10),
       ("Move the phone charger out of the bedroom", 10),
       ("Keep the same wake time for a week, weekend included", 30),
       ("Review what changed and adjust one thing", 20)]),

    G("Book the dentist, it's been two years and I keep putting it off",
      "Book the dental appointment", "Get the overdue check-up booked",
      "MEDIUM", "HEALTH",
      "There is an appointment in the calendar, whatever date they could offer",
      [("Find the practice number or check you are still registered", 10),
       ("Call or book online", 15),
       ("Put it in the calendar with a reminder the day before", 5)]),

    G("Set up the medication reminders for dad",
      "Set up dad's medication reminders", "Make the daily medication routine reliable",
      "HIGH", "HEALTH",
      "The doses are laid out for the week and there is a reminder he will notice",
      [("Write out the current prescriptions and the times of day", 15),
       ("Buy a weekly pill organiser with day compartments", 25),
       ("Fill it for the coming week together, so he sees the system", 30),
       ("Set a repeating phone or clock alarm for each dose time", 20),
       ("Diary the repeat prescription order a week before it runs out", 10)]),

    G("Physio exercises for my back, I stopped doing them",
      "Restart the back exercises", "Get back to the physio routine",
      "MEDIUM", "HEALTH",
      "You have done the set on most days for a week, even shortened versions",
      [("Find the exercise sheet the physio gave you", 10),
       ("Pick a fixed time of day to attach them to", 10),
       ("Do a shortened set the first few days to rebuild the habit", 35),
       ("Build back to the full set", 40)]),
]

# ---------------------------------------------------------------------------
# Creative work — the CREATIVE category v1 never had, plus the perfectionism
# phrasing this app's users actually type
# ---------------------------------------------------------------------------
CREATIVE = [
    G("Rewrite the landing page copy — I keep restarting it because it's never good enough",
      "Rewrite the landing page copy", "Produce a usable draft of the page copy",
      "MEDIUM", "CREATIVE",
      "One draft exists end to end and says the main thing clearly — it can be improved later",
      [("Write down the single sentence the page has to land", 15),
       ("Draft the headline and opening paragraph without editing them", 25),
       ("Draft the rest straight through, leaving gaps where you get stuck", 40),
       ("Read it aloud once and fix only what trips you up", 25)]),

    G("Finish the short story I abandoned in chapter two",
      "Finish the abandoned short story", "Get the story to a finished draft",
      "LOW", "CREATIVE",
      "The story reaches an ending on the page, however rough that ending is",
      [("Reread what exists and note in one line where it was going", 15),
       ("Write the next scene without rereading the earlier ones", 45),
       ("Draft straight through to an ending, allowing it to be bad", 90),
       ("Leave it a day, then fix only what stops it making sense", 45)]),

    G("Put together a birthday photo album for my partner",
      "Make the birthday photo album", "Choose, order and assemble photos into an album",
      "MEDIUM", "CREATIVE",
      "The album is assembled and tells the story — a few blurry favourites are fine",
      [("Pick a rough number of photos and an album format", 15),
       ("Go through the camera roll and shortlist candidates", 45),
       ("Cut the shortlist down to the number that fits", 25),
       ("Order the prints", 20),
       ("Lay them out and mount them, writing dates on the backs", 60)]),

    G("Learn three songs on the guitar properly",
      "Learn three songs on guitar", "Get three songs playable start to finish",
      "LOW", "CREATIVE",
      "You can play them through at a slow tempo without stopping to look things up",
      [("Pick three songs within your current level", 15),
       ("Learn the chord shapes for the first and practise the changes slowly", 45),
       ("Play it through slowly until the changes stop breaking", 60),
       ("Repeat with the second and third", 120)]),

    G("Paint something, I haven't touched the paints since I bought them",
      "Start painting again", "Actually use the paints",
      "LOW", "CREATIVE",
      "Paint has gone on a surface and you enjoyed some of it — the result does not matter",
      [("Get the paints and a surface out and leave them out", 10),
       ("Mix a few colours just to see what they do", 20),
       ("Paint one small study without planning it", 45),
       ("Leave it up somewhere you will see it", 5)]),

    G("Record the podcast episode I keep rescheduling",
      "Record the podcast episode", "Get the episode recorded",
      "MEDIUM", "CREATIVE",
      "There is a recording end to end that is audible and roughly the right length",
      [("Write the running order as five bullet points", 15),
       ("Set the mic up and record a minute to check the levels", 15),
       ("Record it in one pass without restarting for stumbles", 45),
       ("Listen back and note only the cuts that genuinely matter", 30)]),
]

# ---------------------------------------------------------------------------
# Caregiving, family, social
# ---------------------------------------------------------------------------
PEOPLE = [
    G("Plan my mother's 60th birthday party",
      "Plan mum's 60th birthday party", "Organise the party",
      "HIGH", "PERSONAL",
      "The date, place, people and food are settled and everyone has been told",
      [("Agree the date and rough budget with whoever is sharing it", 15),
       ("Draw up the guest list", 25),
       ("Book the place, or decide it is at home", 40),
       ("Sort the food, whether cooked or ordered", 45),
       ("Send the invitations", 25),
       ("Sort decorations and a cake the week before", 45)]),

    G("Call mum, it's been three weeks and I feel bad about it",
      "Call mum", "Catch up properly by phone",
      "MEDIUM", "PERSONAL",
      "You had the call — length does not matter",
      [("Pick a time she is usually free and put it in the calendar", 10),
       ("Make the call", 30)]),

    G("Write the thank-you notes from the wedding",
      "Write the wedding thank-you notes", "Write and send the thank-you cards",
      "MEDIUM", "PERSONAL",
      "Everyone who gave something gets a note, even a short one",
      [("Make the list of who gave what from the gift record", 15),
       ("Buy or find the cards and stamps", 25),
       ("Write ten a sitting rather than trying to do them in one go", 90),
       ("Post them in batches as you finish each set", 15)]),

    G("Help my daughter with her science project without taking it over",
      "Support the science project", "Help her get the project done herself",
      "HIGH", "PERSONAL",
      "She has done the work and can explain it, even if it looks less polished than yours would",
      [("Ask her what the brief actually asks for", 15),
       ("Help her break it into steps she chooses", 20),
       ("Take her to buy the materials she needs", 40),
       ("Be nearby while she builds it, answering only when asked", 60),
       ("Have her talk you through it as practice", 20)]),

    G("Organise a dinner with the college friends we keep failing to meet",
      "Organise the friends' dinner", "Actually get the dinner in the diary",
      "LOW", "PERSONAL",
      "A date is set that most can make and somewhere is booked",
      [("Message the group with three candidate dates", 15),
       ("Pick whichever date gets the most yeses after a few days", 10),
       ("Book somewhere central and tell everyone", 20)]),

    G("Take the cat to the vet for the vaccination that's overdue",
      "Take the cat to the vet", "Get the overdue vaccination done",
      "MEDIUM", "PERSONAL",
      "The cat has been seen and the next booster is written down",
      [("Find the vaccination record and the vet's number", 10),
       ("Book the appointment", 15),
       ("Get the carrier out a day early so it stops being a warning sign", 10),
       ("Take her in", 60)]),
]

# ---------------------------------------------------------------------------
# Work & study
# ---------------------------------------------------------------------------
WORK = [
    G("Write a quarterly sales report for the board meeting next Monday",
      "Write the quarterly sales report", "Prepare the sales report for the board",
      "HIGH", "WORK",
      "The report covers the main numbers and the story behind them, and is readable",
      [("Pull the quarter's figures out of the dashboard", 15),
       ("Note the three things that actually changed and why", 30),
       ("Draft the summary around those three points", 45),
       ("Build the charts that support them", 40),
       ("Read it once for sense and tidy the formatting", 25)]),

    G("Migrate the database off the deprecated server",
      "Migrate the database", "Move the database to the new server",
      "HIGH", "WORK",
      "The application runs against the new database and the old one can be switched off safely",
      [("Take a verified backup and confirm you can restore it", 15),
       ("Stand up the new server and match the configuration", 60),
       ("Do a trial restore onto the new server", 45),
       ("Check row counts and spot-check a few tables against the old one", 40),
       ("Cut the application over during a quiet window", 40),
       ("Watch the logs, then retire the old server once it is clearly stable", 45)]),

    G("Prepare for my performance review on Thursday",
      "Prepare for the performance review", "Get ready to talk about the year",
      "HIGH", "WORK",
      "You can talk through several concrete things you did and what you want next",
      [("Skim the year's calendar and notes for what you actually shipped", 15),
       ("Write down four or five examples with the outcome next to them", 30),
       ("Note the two things you want to ask for", 15),
       ("Read it back and cut it to what you can say in ten minutes", 20)]),

    G("Learn enough Kotlin coroutines to refactor our networking layer",
      "Learn coroutines for the refactor", "Get to working knowledge of coroutines",
      "MEDIUM", "LEARNING",
      "You can explain structured concurrency and have converted one call successfully",
      [("Read the official coroutines basics page", 15),
       ("Write a throwaway example that runs two calls in parallel", 40),
       ("Read how cancellation and scopes work", 30),
       ("Convert one real network call in a branch", 60),
       ("Note what confused you and reread only that", 25)]),

    G("Set up CI for the mobile app repo",
      "Set up CI for the repo", "Get automated builds running on push",
      "MEDIUM", "WORK",
      "A push triggers a build that runs the tests and reports back on the pull request",
      [("Check what the build needs locally and write the steps down", 15),
       ("Add a workflow file that builds on push", 40),
       ("Get the secrets and signing config into the CI settings", 30),
       ("Push and fix the build until it passes", 60),
       ("Turn on the status check for pull requests", 15)]),

    G("Reply to the backlog of unread work emails",
      "Clear the email backlog", "Work through the unread mail",
      "MEDIUM", "WORK",
      "Anything needing a real reply has one, and the rest is archived — inbox zero is not the goal",
      [("Sort by sender and archive the newsletters in bulk", 15),
       ("Reply to anything that takes under two minutes", 40),
       ("Flag the ones needing a considered answer", 15),
       ("Write the considered replies one at a time", 60)]),

    G("Finish chapter 3 of my thesis",
      "Finish thesis chapter 3", "Get chapter three to a complete draft",
      "HIGH", "LEARNING",
      "The chapter has a beginning, middle and end and your supervisor can read it",
      [("Reread the outline and mark which sections are still missing", 15),
       ("Draft the missing sections without editing as you go", 90),
       ("Fill in the citations you left as placeholders", 45),
       ("Read it through once for argument, not for wording", 40)]),

    G("Back up everything properly, I've been meaning to since the last scare",
      "Set up proper backups", "Get an automatic backup running",
      "MEDIUM", "ADMIN",
      "The important folders copy automatically and you have restored one file to prove it works",
      [("List what would actually hurt to lose", 15),
       ("Pick a backup destination with room for it", 15),
       ("Set the backup to run on a schedule", 30),
       ("Run it once fully", 45),
       ("Restore a single file from the backup to check it really works", 15)]),
]

# ---------------------------------------------------------------------------
# Travel, moving, outdoors, errands
# ---------------------------------------------------------------------------
OUT = [
    G("Book flights and a hotel for the conference in October",
      "Book the conference travel", "Get flights and accommodation booked",
      "MEDIUM", "WORK",
      "Flights and a room are booked and the confirmations are saved somewhere you can find",
      [("Check the conference dates and which sessions you need to be there for", 15),
       ("Compare flights for those dates and book one", 40),
       ("Book a room near the venue", 30),
       ("Save the confirmations and add the trip to the calendar", 15)]),

    G("Pack for the trip, we leave in three days",
      "Pack for the trip", "Get packed without the last-night panic",
      "HIGH", "PERSONAL",
      "The bag is packed with what you need — anything forgotten can be bought there",
      [("Check the forecast for where you are going", 10),
       ("Write a short list by category: clothes, toiletries, documents, chargers", 15),
       ("Put the documents and chargers in the bag first", 15),
       ("Pack the clothes against the list", 35),
       ("Do one last pass for the things you use every morning", 15)]),

    G("Sort the garden out before it gets away from us completely",
      "Get the garden back under control", "Cut back and tidy the garden",
      "LOW", "PERSONAL",
      "The paths are clear and the beds are visible again — it does not need to be finished",
      [("Get the tools out and check the mower actually starts", 15),
       ("Cut the grass", 45),
       ("Cut back whatever is blocking the paths", 60),
       ("Bag the cuttings and take them to the tip or compost", 40)]),

    G("Find a new flat, our lease ends in two months",
      "Find a new flat", "Secure somewhere to live before the lease ends",
      "HIGH", "PERSONAL",
      "An offer is accepted on somewhere workable — it does not have to be the dream flat",
      [("Agree the budget and the two things you will not compromise on", 15),
       ("Set up alerts on the listing sites", 20),
       ("Book viewings in batches rather than one at a time", 40),
       ("Go to the viewings and note them down straight after", 120),
       ("Put an offer in on the best realistic option", 30)]),

    G("Return the parcel before the refund window closes",
      "Return the parcel", "Send the item back for a refund",
      "HIGH", "ADMIN",
      "The parcel is with the courier and you have the tracking receipt",
      [("Find the order and start the return online", 10),
       ("Print or save the return label", 10),
       ("Repack the item with everything it came with", 15),
       ("Drop it at the collection point and keep the receipt", 25)]),

    G("Get the Christmas shopping done without leaving it to the last week",
      "Do the Christmas shopping", "Buy and wrap the presents",
      "MEDIUM", "PERSONAL",
      "Everyone on the list has something and it is wrapped — thoughtful beats expensive",
      [("Write the list of who needs a present and a rough budget each", 15),
       ("Note one idea against each name, asking around where you are stuck", 30),
       ("Order the ones you can buy online", 45),
       ("Buy the rest in one trip", 90),
       ("Wrap them in a single sitting with something on in the background", 60)]),
]

GOLD: list[Gold] = REPAIR + HOME + FOOD + ADMIN + HEALTH + CREATIVE + PEOPLE + WORK + OUT
