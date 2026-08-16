"""Gold examples: healthcare-system logistics (hand-authored).

The niche here is narrow and deliberate: the *bureaucracy* that surrounds
healthcare, not the health habit and not the clinical content. `gold_body.py`
already owns booking a first-time or overdue appointment (GP check-up,
dentist, optician, smear test, health screening), the basic repeat-prescription
system, and physical habits; `gold_care.py` owns the caregiving relationship
itself (helping a parent through recovery, a child's allergy routine, the
conversations around it); `gold_core.py` has its own small set of "book the
dentist"-style seeds; `gold_admin2.py` owns registering with a new GP after a
move and generic insurance-claim appeals. This module deliberately steers
around all of that and covers what happens *after* the appointment exists, or
instead of a straightforward booking: chasing a referral that's gone quiet,
working out what a test result actually means and getting the follow-up
booked, pharmacy logistics beyond "set up a repeat", health-insurance paperwork
(claims, EOBs, pre-authorization, disputed charges), replacing medical
equipment, wrangling records and forms between providers, organizing someone
else's medical paperwork as a logistics problem rather than a caregiving one,
and the small admin glitches (double bookings, a clinic that rescheduled you
by text, a mystery appointment reminder) that eat an afternoon.

Every example stays in the administrative register: booking, chasing, filling
in forms, organizing paperwork. Nothing here diagnoses, gives symptom advice,
or makes a clinical call — that's out of scope for a productivity tool, and
where a decision is genuinely clinical the step is always "get it explained by
someone qualified," never an answer of its own.

See `goldlib.Gold` for the format and `quality.py` for the rules every example
must pass.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from goldlib import Gold

G = Gold

# ---------------------------------------------------------------------------
# Referrals — the ones that go quiet, and following up after a specialist
# ---------------------------------------------------------------------------
REFERRALS = [
    G("Chase up the referral to the specialist, the GP sent it three weeks ago and I've heard nothing",
      "Chase up the specialist referral", "Find out what happened to the referral and get it moving",
      "MEDIUM", "HEALTH",
      "You've spoken to someone about where the referral stands and know what happens next, even if there's still a wait",
      [("Find the GP surgery's number and check what info they'll need", 10),
       ("Call and ask them to confirm the referral actually went through", 15),
       ("Call the specialist's office directly to ask if they've received it", 15),
       ("Note down what you were told and when to chase again if nothing happens", 10)]),

    G("Follow up on the plan the specialist promised after my appointment, it's been two weeks of silence",
      "Follow up on the specialist's plan", "Chase the follow-up plan the specialist said they'd send",
      "MEDIUM", "HEALTH",
      "You've got an actual response about the plan, even if it's just a date for the next step",
      [("Check your notes or the letter for what exactly was promised", 10),
       ("Call the specialist's office and ask for an update", 15),
       ("Ask the GP practice to chase it if the specialist's office can't help", 15),
       ("Write down what happens next and when to check again", 10)]),

    G("The referral letter apparently never reached the specialist and I need to sort this out before I lose my place in the queue",
      "Sort out the lost referral letter", "Get the referral resent after it went missing",
      "HIGH", "HEALTH",
      "The referral is confirmed as received on the other end and you have something in writing or a reference",
      [("Call the GP surgery and confirm when and how it was sent", 10),
       ("Ask them to resend it and get a reference number", 15),
       ("Call the specialist's office to confirm it's now arrived", 15),
       ("Note the reference number somewhere you'll actually find it", 5)],
      due="before I lose my place in the queue"),

    G("Want a second opinion on this so I need my records sent over to another specialist",
      "Get records sent for a second opinion", "Request your file be sent to another specialist",
      "MEDIUM", "HEALTH",
      "The records have been requested and you know roughly when they'll reach the new specialist",
      [("Find the name of the new specialist and their office details", 10),
       ("Call your current specialist's office and ask about a records release", 15),
       ("Fill in whatever consent form they need to send it across", 15),
       ("Confirm with the new specialist's office that it's arrived", 10)]),

    G("Kid's referral to the paediatric clinic has gone completely quiet, it's been over a month now",
      "Chase the kid's paediatric referral", "Find out what's happening with a referral that's gone quiet",
      "MEDIUM", "HEALTH",
      "You know where the referral actually stands and roughly what the wait looks like",
      [("Find the referral date and reference from the GP letter", 10),
       ("Call the GP surgery to check it was actually sent", 15),
       ("Call the clinic directly to ask where it sits in the queue", 15),
       ("Note what you were told and when to check back", 10)]),
]

# ---------------------------------------------------------------------------
# Test results — working out what a result means and booking the follow-up,
# never diagnosing it yourself
# ---------------------------------------------------------------------------
RESULTS = [
    G("Results are up on the app and it just says 'abnormal', no idea what I'm supposed to do with that",
      "Follow up on the flagged test result", "Get a proper response about what the flagged result means",
      "HIGH", "HEALTH",
      "You've spoken to the surgery and there's an appointment booked or a plan for one, not just the app screen",
      [("Read exactly what the result and any notes on the app say", 10),
       ("Call the surgery and ask them to explain it or book you in", 15),
       ("Book the follow-up appointment they offer", 15),
       ("Write down the questions you want to ask at that appointment", 10)]),

    G("Blood test was over three weeks ago and I still haven't heard anything, starting to wonder if it's been lost",
      "Chase the overdue blood test results", "Find out what happened to results that should have come back weeks ago",
      "MEDIUM", "HEALTH",
      "You've got an actual answer about the results, even if it's just confirmation they're still on the way",
      [("Find the date the blood was taken and where", 5),
       ("Call the surgery or lab to ask where the results actually are", 15),
       ("Ask what to do if they've genuinely been delayed or lost", 10),
       ("Note when to check back if nothing's heard", 10)]),

    G("Got a letter with the scan results and it's full of jargon I don't understand, need to actually talk to someone about it",
      "Get the scan results explained", "Book time with someone who can explain what the scan letter means",
      "MEDIUM", "HEALTH",
      "You've got a call or appointment booked to go through it properly",
      [("Reread the letter and note the specific words you don't understand", 10),
       ("Call the GP surgery or the department that sent it", 15),
       ("Book a call or appointment to go through it", 15),
       ("Write down the questions so you don't forget them on the day", 10)]),

    G("Should have got my test results back by now and honestly not sure if I'm meant to chase this or just wait",
      "Find out the status of the test results", "Get clarity on when the results are expected and whether chasing is needed",
      "LOW", "HEALTH",
      "You know whether to wait or chase, and if chasing, exactly who to call",
      [("Check the paperwork from the test for a stated turnaround time", 10),
       ("Call the surgery or clinic and ask directly", 15),
       ("Note down what they said and when to follow up if nothing arrives", 10)]),
]

# ---------------------------------------------------------------------------
# Pharmacy logistics beyond the basic repeat-prescription system
# ---------------------------------------------------------------------------
PHARMACY = [
    G("Need to switch pharmacies now that the old one's miles from the new flat",
      "Switch to a pharmacy near the new flat", "Move the repeat prescriptions to a pharmacy that's actually convenient",
      "MEDIUM", "HEALTH",
      "The new pharmacy has your prescriptions and the old one's been cancelled",
      [("Find a pharmacy near the new flat that accepts transfers", 10),
       ("Ask the new pharmacy to request the transfer from the old one", 15),
       ("Confirm with the old pharmacy that the transfer's gone through", 10),
       ("Cancel or update any repeat order set up with the old pharmacy", 10)]),

    G("Pharmacy keeps saying my medication is out of stock and it's been two weeks of this now",
      "Chase the out-of-stock medication", "Find out what's actually going on with the delayed order",
      "HIGH", "HEALTH",
      "You've got an actual answer, whether that's a delivery date or an alternative sorted",
      [("Call the pharmacy and ask exactly what's out of stock and why", 10),
       ("Ask if another branch or pharmacy nearby has it in stock", 15),
       ("Ask the GP whether an alternative brand or dose can be prescribed instead", 15),
       ("Note the plan and when to check back if it's still not sorted", 10)]),

    G("Lost the paper prescription the GP printed out, need a replacement before the current supply runs out",
      "Get a replacement for the lost prescription", "Sort out a new copy after losing the paper prescription",
      "HIGH", "HEALTH",
      "The pharmacy has a valid prescription to work from, whatever happened to the original",
      [("Call the GP surgery and explain the paper copy is lost", 10),
       ("Ask them to reissue it or send it electronically instead", 15),
       ("Confirm with the pharmacy that they've received the new one", 10)],
      due="before the current supply runs out"),

    G("Want to set up prescription delivery instead of trekking to the pharmacy every month",
      "Set up prescription delivery", "Arrange a delivery service for the regular pharmacy order",
      "LOW", "HEALTH",
      "Delivery is set up and you know roughly when the next one will arrive",
      [("Ask the pharmacy whether they offer a delivery service", 10),
       ("Sign up and confirm the delivery address", 15),
       ("Check the delivery day actually lines up with when you'll be in", 10)]),

    G("GP switched my prescription to a new pharmacy without telling me and the old one had nothing left when I turned up",
      "Sort out the mixed-up pharmacy switch", "Get the prescription situation straightened out after the surgery moved it without warning",
      "HIGH", "HEALTH",
      "You know which pharmacy actually has the current prescription and can collect from it",
      [("Call the GP surgery and ask which pharmacy it was sent to", 10),
       ("Call that pharmacy to confirm they've got it ready", 15),
       ("Ask the surgery to note your preferred pharmacy for next time", 10)]),
]

# ---------------------------------------------------------------------------
# Health insurance and medical billing paperwork
# ---------------------------------------------------------------------------
INSURANCE_BILLING = [
    G("Open enrollment closes this Friday and I still haven't compared the health plans",
      "Compare and pick a health plan", "Get through open enrollment and actually choose a plan",
      "HIGH", "ADMIN",
      "A plan is chosen and enrolled in, even if it's not the ideal one on paper",
      [("Pull up the list of plan options and what's changed from last year", 15),
       ("Compare premiums, deductibles and whether your usual doctors are covered", 30),
       ("Pick the plan that fits best and note down the reasons", 15),
       ("Submit the enrollment before the window shuts", 15)],
      due="closes this Friday"),

    G("Insurance denied the claim for the ER visit and I think it's wrong",
      "Appeal the denied ER claim", "Challenge the insurance denial for the ER visit",
      "HIGH", "ADMIN",
      "The appeal is submitted with the paperwork they need, even if the decision takes weeks",
      [("Find the denial letter and read the stated reason", 10),
       ("Gather the ER paperwork and any referral or GP notes that support the claim", 20),
       ("Write the appeal explaining why the denial is wrong", 30),
       ("Submit the appeal with the supporting paperwork attached", 15)]),

    G("The medical bill doesn't match what I thought the insurance was supposed to cover, need to figure out what's going on",
      "Untangle the confusing medical bill", "Work out why the bill doesn't match what was expected",
      "MEDIUM", "ADMIN",
      "You understand why the bill is what it is, and it's either explained or a dispute is under way",
      [("Line up the bill next to the insurance explanation of benefits", 15),
       ("Note every charge that doesn't make sense", 10),
       ("Call the provider's billing office and ask them to explain the discrepancies", 20),
       ("Call the insurer if the provider can't explain it", 15),
       ("Note the outcome and any reference numbers", 10)]),

    G("Need pre-authorization sorted before the procedure or apparently insurance won't cover it",
      "Get the pre-authorization sorted", "Arrange insurance pre-authorization before the procedure goes ahead",
      "HIGH", "ADMIN",
      "The pre-authorization is confirmed in writing from the insurer, not just a verbal promise",
      [("Check with the provider's office what code needs pre-authorizing", 10),
       ("Confirm the provider has submitted the request to the insurer", 15),
       ("Call the insurer to check the request's been received", 15),
       ("Get written confirmation once it's approved", 10)],
      due="before the procedure"),

    G("Got a duplicate charge on the medical bill, definitely been billed for the same visit twice",
      "Dispute the duplicate medical charge", "Get the duplicate billing sorted with the provider",
      "MEDIUM", "ADMIN",
      "The duplicate is flagged with the provider and you have a reference number for the dispute",
      [("Compare the two bills and confirm they're for the same visit", 10),
       ("Call the billing office and point out the duplicate", 15),
       ("Ask for it to be corrected and get a reference number", 10),
       ("Check the next statement to confirm it's actually fixed", 15)]),

    G("Want to claim back the physio sessions through the FSA before the money expires at the end of December",
      "Claim the physio sessions through the FSA", "Get the physio costs reimbursed before the FSA money expires",
      "HIGH", "ADMIN",
      "The claim is submitted with receipts attached, even if reimbursement takes a while",
      [("Gather the receipts for the physio sessions", 10),
       ("Check what the FSA provider needs for a reimbursement claim", 10),
       ("Fill in the claim form with the receipt details", 20),
       ("Submit the claim through the FSA portal", 10)],
      due="before the money expires at the end of December"),

    G("Insurance sent an EOB that makes no sense, want to actually understand what I owe before paying anything",
      "Make sense of the EOB before paying", "Work out what's actually owed from the confusing explanation of benefits",
      "MEDIUM", "ADMIN",
      "You know what's actually owed and to whom, whatever the EOB's wording made it look like",
      [("Read through the EOB and note what's marked as patient responsibility", 15),
       ("Compare it against the actual bill from the provider", 15),
       ("Call the insurer if the numbers don't add up", 15),
       ("Pay or query the provider once it's clear what's owed", 15)]),
]

# ---------------------------------------------------------------------------
# Replacing and reordering medical equipment
# ---------------------------------------------------------------------------
EQUIPMENT = [
    G("Glasses snapped in half this morning and I genuinely can't see well enough to drive",
      "Replace the broken glasses", "Get new glasses sorted using the existing prescription",
      "URGENT", "HEALTH",
      "New glasses are ordered or an emergency pair sorted, even if the proper ones take a week",
      [("Find the current prescription, whether saved online or from the last optician", 10),
       ("Call the optician to ask about a rush order or loaner pair", 15),
       ("Order the replacement glasses", 20),
       ("Arrange to get by until they arrive, borrowed pair or an old prescription", 15)]),

    G("Hearing aid's been making a weird whistling noise for days and I keep putting off dealing with it",
      "Sort out the whistling hearing aid", "Get the hearing aid looked at or repaired",
      "MEDIUM", "HEALTH",
      "The hearing aid's booked in for a look or already fixed, whichever it needs",
      [("Check the battery and see if a fresh one clears the noise", 5),
       ("Call the audiologist or supplier if a fresh battery doesn't help", 15),
       ("Book a repair or check-up appointment", 15),
       ("Ask about a loaner while it's being fixed if it'll take a while", 10)]),

    G("Doctor said I need a walking stick and I have no idea where you even get one of those",
      "Get the walking stick sorted", "Work out where to get the walking stick the doctor recommended",
      "MEDIUM", "HEALTH",
      "A stick has been ordered or collected that's the right height, even if it's a basic one",
      [("Ask the doctor's office or a pharmacist where to get one locally", 10),
       ("Check whether it's available through the NHS or needs buying", 10),
       ("Get properly measured or fitted for the right height", 15),
       ("Order or collect it", 15)]),

    G("Need to order more test strips for the blood glucose monitor before I run out completely",
      "Reorder the blood glucose test strips", "Get more test strips ordered before the current box runs out",
      "HIGH", "HEALTH",
      "The order's placed and you know roughly when it'll arrive",
      [("Check how many strips are left and the brand needed", 5),
       ("Order more through the pharmacy or the prescription system", 15),
       ("Confirm when they'll be ready to collect or arrive", 10)]),

    G("CPAP supplies are due for a refresh and the mask's getting pretty worn out",
      "Reorder the CPAP supplies", "Get the mask and filters replaced",
      "MEDIUM", "HEALTH",
      "The new mask and filters are ordered and on the way",
      [("Check the supplier or DME company that handles the CPAP orders", 10),
       ("Confirm what insurance or the NHS covers for replacement parts", 15),
       ("Place the order for the mask and filters", 15),
       ("Note the next reorder date somewhere you'll actually see it", 5)]),
]

# ---------------------------------------------------------------------------
# Records and forms — moving information between providers, or producing it
# for someone who's asking
# ---------------------------------------------------------------------------
RECORDS_FORMS = [
    G("School needs proof of vaccinations before term starts next Monday and I have no idea where that paperwork even is",
      "Get the vaccination record for school", "Track down or request proof of vaccinations the school's asking for",
      "HIGH", "ADMIN",
      "The school has the proof they asked for, on paper or however they'll accept it",
      [("Check whether the record's saved anywhere at home first", 10),
       ("Call the GP surgery or health authority to request an official copy", 15),
       ("Confirm the format the school will actually accept", 10),
       ("Send it over to the school", 15)],
      due="before term starts next Monday"),

    G("New GP wants a full medical history form filled in and I don't have half of this information to hand",
      "Fill in the new GP's medical history form", "Track down the missing details and get the intake form filled in",
      "MEDIUM", "ADMIN",
      "The form's filled in with what you can find, even if a couple of dates are approximate",
      [("List what the form's actually asking for", 10),
       ("Check old letters, apps or the previous surgery for missing details", 20),
       ("Call the old GP surgery for anything you still can't find", 15),
       ("Fill in and submit the form", 20)]),

    G("Need my medical records transferred to the new surgery, we moved months ago and I still haven't sorted it",
      "Chase the medical records transfer", "Get your records actually moved over to the new surgery after registering",
      "MEDIUM", "HEALTH",
      "The new surgery confirms they've got your full records, not just your registration",
      [("Check whether you're properly registered at the new surgery", 10),
       ("Call the old surgery and ask them to send the records across", 15),
       ("Call the new surgery a couple of weeks later to confirm they've arrived", 10),
       ("Chase again if nothing's turned up", 10)]),

    G("New job wants proof of my immunizations from years ago and I don't even remember which ones I had",
      "Get proof of old immunizations for the new job", "Track down or reconstruct an immunization record for the employer",
      "HIGH", "ADMIN",
      "The employer has something they'll accept, even if it's a reconstructed record rather than the original",
      [("Check for any old vaccination booklet or app record", 10),
       ("Ask the GP surgery to pull whatever's on file", 15),
       ("Ask about a titer test if the records genuinely can't be found", 15),
       ("Send whatever's confirmed over to the employer", 15)]),

    G("Need a doctor's note for work explaining the time off last week",
      "Get the doctor's note for work", "Arrange a note covering last week's time off",
      "MEDIUM", "ADMIN",
      "The note is in hand and sent to work, whatever wording the doctor uses",
      [("Call the surgery and ask what's needed for a sick note", 10),
       ("Book the appointment or online request for the note", 15),
       ("Collect or download the note once it's issued", 10),
       ("Send it to work", 10)]),

    G("Need to apply for the medical leave paperwork before I can take the time off for the surgery",
      "Apply for medical leave paperwork", "Get the leave forms sorted with work before the surgery",
      "HIGH", "ADMIN",
      "The paperwork's submitted to work with what the doctor's given you",
      [("Check what your workplace needs for medical leave", 10),
       ("Ask the doctor's office for the certification or note it requires", 15),
       ("Fill in the leave request form", 20),
       ("Submit it to work with the medical certification attached", 15)],
      due="before I can take the time off for the surgery"),
]

# ---------------------------------------------------------------------------
# Organizing someone else's medical paperwork — the logistics, not the
# caregiving relationship itself (that's gold_care's territory)
# ---------------------------------------------------------------------------
OTHERS_PAPERWORK = [
    G("Dad's medical paperwork is just a shoebox of loose letters and I need to actually organize it before the specialist appointment",
      "Organize dad's medical paperwork", "Turn the shoebox of letters into something usable before the appointment",
      "MEDIUM", "PERSONAL",
      "The paperwork's sorted into something you can actually find things in, even if it's a rough system",
      [("Tip out the shoebox and sort into rough piles by type", 15),
       ("Put the most recent letters and test results at the front", 15),
       ("Buy or find a folder with dividers", 15),
       ("File everything in and label the sections", 30)],
      due="before the specialist appointment"),

    G("Need to set up proxy access to mum's patient portal so I can actually help her book things",
      "Set up proxy access to mum's patient portal", "Get authorized access so you can help manage her appointments online",
      "MEDIUM", "PERSONAL",
      "Proxy access is confirmed and you can actually see and book on her behalf",
      [("Check what the portal requires for proxy or delegate access", 10),
       ("Fill in the consent form with mum", 15),
       ("Submit it to the surgery or provider", 10),
       ("Log in and confirm you can see her appointments", 10)]),

    G("Putting together my son's medical history for the new pediatrician since we switched",
      "Put together the kid's medical history for the new pediatrician", "Get a summary ready so the new pediatrician has what they need",
      "MEDIUM", "HEALTH",
      "The new pediatrician has enough history to work from, even if a couple of early details are fuzzy",
      [("List what you remember: allergies, past issues, vaccination status", 15),
       ("Ask the old pediatrician's office to send the full record over", 15),
       ("Check the new pediatrician's office has received it before the first visit", 15)]),

    G("Years of mum's medical bills and EOBs are just piled up and I need to sort through them before she moves into the care home",
      "Sort through mum's old medical bills", "Work through the pile of bills and EOBs before the move",
      "MEDIUM", "PERSONAL",
      "The pile's sorted into paid, unresolved and can-be-shredded, even if a few are unclear",
      [("Sort the pile roughly by year", 15),
       ("Separate anything marked unpaid or with a balance due", 20),
       ("Call the provider's billing office about anything unclear", 20),
       ("Shred what's old and clearly settled", 15)],
      due="before she moves into the care home"),

    G("Need to find out who dad's actual GP is, he's been to three different practices and nobody's sure anymore",
      "Work out which practice dad's actually registered at", "Track down dad's current GP registration among the confusion",
      "MEDIUM", "PERSONAL",
      "You know which practice he's registered at and have their number saved",
      [("Check any recent letters or prescription labels for a practice name", 10),
       ("Call the health authority helpline to check his registration", 15),
       ("Confirm with that practice and save their details", 10)]),
]

# ---------------------------------------------------------------------------
# Small appointment admin glitches — reschedules, double bookings, mystery
# reminders, missed slots
# ---------------------------------------------------------------------------
APPOINTMENT_GLITCHES = [
    G("Clinic texted saying my appointment's been moved and I haven't actually done anything about finding a new time yet",
      "Rebook the appointment the clinic moved", "Sort out a new time after the clinic rescheduled without asking",
      "MEDIUM", "HEALTH",
      "A new time's confirmed that actually works, not just whatever slot they first offered",
      [("Check the text or email for the new details they gave", 5),
       ("Call and ask for a time that actually works if the given one doesn't", 15),
       ("Confirm the new time and update the calendar", 10)]),

    G("Double-booked the dentist and the optician for the same afternoon somehow, need to fix this",
      "Fix the double-booked appointments", "Sort out the clash between the dentist and optician",
      "MEDIUM", "ADMIN",
      "One's moved and both are confirmed at times that don't clash anymore",
      [("Decide which one's easier to move", 10),
       ("Call and reschedule the one you're moving", 15),
       ("Update the calendar with both confirmed times", 5)]),

    G("Missed the specialist appointment completely and need to find out if there's a fee before rebooking",
      "Deal with the missed specialist appointment", "Find out about the missed-appointment fee and get a new one booked",
      "MEDIUM", "HEALTH",
      "A new appointment's booked and you know whether a fee applies",
      [("Call the specialist's office and explain you missed it", 10),
       ("Ask whether a missed-appointment fee applies", 10),
       ("Book the next available slot", 15),
       ("Set a reminder this time so it doesn't happen again", 5)]),

    G("Need to set up an account on the hospital's patient portal, keep meaning to and never getting round to it",
      "Set up the hospital patient portal account", "Get registered on the portal so results and appointments are easier to manage",
      "LOW", "ADMIN",
      "The account's set up and logged into, even if you don't go poking around the rest of it",
      [("Find the portal registration link, usually on a letter or the hospital site", 10),
       ("Register with your patient or NHS number", 15),
       ("Verify the account, whether by email or a code", 10),
       ("Log in once to confirm it actually works", 5)]),

    G("Got a reminder text about an appointment I don't even remember booking, need to figure out what it's actually for",
      "Work out what the mystery appointment is for", "Figure out what the unexplained appointment reminder is actually about",
      "LOW", "HEALTH",
      "You know what the appointment's for and whether to keep or cancel it",
      [("Check the reminder for a department name or reference number", 5),
       ("Call the number on the text to ask what it's for", 15),
       ("Decide whether to keep it or cancel based on what they say", 10)]),
]

GOLD: list[Gold] = (
    REFERRALS + RESULTS + PHARMACY + INSURANCE_BILLING + EQUIPMENT
    + RECORDS_FORMS + OTHERS_PAPERWORK + APPOINTMENT_GLITCHES
)
