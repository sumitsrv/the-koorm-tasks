"""Gold examples: bureaucracy and paperwork, second pass (hand-authored).

`gold_core.py` and `gold_money.py` already cover the tax return, cancelling a
gym membership, switching banks, renewing a passport, a water-damage claim,
chasing a deposit, automating bills, a delivery complaint, budgeting, debt,
invoices, self-assessment, benefits appeals, remortgaging, pensions, wills,
probate, vehicle registration, visas for a trip, warranty claims and the
hard-to-cancel subscription. This module deliberately steers around all of
that and covers the next layer of everyday admin: registering with services,
disputing decisions, life-event paperwork, and the deadline-heavy claims and
appeals that make up so much of this domain.

See `goldlib.Gold` for the format and `quality.py` for the rules every
example must pass.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from goldlib import Gold

G = Gold

# ---------------------------------------------------------------------------
# Registering with services and challenging local/civic decisions
# ---------------------------------------------------------------------------
CIVIC = [
    G("Register with a new GP now that we've moved across town",
      "Register with a new GP", "Get set up with a GP practice near the new house",
      "MEDIUM", "ADMIN",
      "You're registered with a practice nearby and have your NHS number sorted, even if the first appointment is weeks off",
      [("Find the nearest practices taking new patients", 10),
       ("Fill in the registration form online or in person", 20),
       ("Attach proof of address and ID and submit it", 15),
       ("Wait for confirmation and note the new practice's number", 10)]),

    G("Apply for a residents' parking permit before the new restrictions start next month",
      "Apply for the residents' parking permit", "Get a permit sorted before the new restrictions start",
      "LOW", "ADMIN",
      "The permit application is submitted with proof of address and the car details, whatever happens to the wait time",
      [("Check the council's eligibility rules and permit zones", 10),
       ("Gather proof of address and the vehicle logbook", 15),
       ("Fill in the online application and upload the documents", 20),
       ("Pay the fee and note the reference number", 10)],
      due="before the new restrictions start next month"),

    G("Dispute the council tax band before the six-month window since we moved in runs out",
      "Dispute the council tax band", "Challenge the band the property was given",
      "MEDIUM", "ADMIN",
      "The challenge is submitted with the comparison evidence, even if the valuation office takes a while to respond",
      [("Check neighbouring properties' bands on the valuation office website", 10),
       ("Note the sale price and floor area evidence for your own property", 20),
       ("Fill in the band challenge form with the comparisons", 25),
       ("Submit it and save the reference number", 10)],
      due="before the six-month window since we moved in runs out"),

    G("Apply for a Blue Badge now dad's hip has got so much worse",
      "Apply for dad's Blue Badge", "Get the disabled parking permit application in",
      "HIGH", "ADMIN",
      "The application is submitted with the medical evidence you have, even if a follow-up assessment gets booked later",
      [("Check the eligibility criteria on the council's page", 10),
       ("Gather the medical evidence and a recent photo", 20),
       ("Fill in the application form with his details", 25),
       ("Submit it with the evidence and pay the fee", 15)]),

    G("Register to vote at the new address before the election in May",
      "Register to vote at the new address", "Get onto the electoral roll before the election",
      "HIGH", "ADMIN",
      "The registration is submitted with the new address and confirmed, even if the polling card arrives closer to the date",
      [("Find your National Insurance number", 5),
       ("Fill in the online voter registration form", 10),
       ("Submit it with the new address details", 10),
       ("Check for the confirmation email or letter", 5)],
      due="before the election in May"),

    G("Apply for planning permission for the garden office before we order the timber",
      "Apply for planning permission for the garden office", "Get permission sorted before ordering materials",
      "MEDIUM", "ADMIN",
      "The application is submitted with the drawings and fee, even if the decision takes the full eight weeks",
      [("Check whether permitted development rights actually cover it", 15),
       ("Get the site plan and drawings prepared", 60),
       ("Fill in the planning application form", 30),
       ("Submit it with the drawings and pay the fee", 20)],
      due="before we order the timber"),

    G("Apply for the council tax single-person discount now I'm living alone",
      "Apply for the council tax single-person discount", "Get the discount applied now the household's just you",
      "LOW", "ADMIN",
      "The application is submitted with proof you live alone, even if the adjusted bill takes a cycle to show up",
      [("Check the council's eligibility page for the discount", 10),
       ("Fill in the online discount application", 15),
       ("Submit it and note the reference number", 10)]),
]

# ---------------------------------------------------------------------------
# Life-event paperwork: names, certificates, power of attorney, bereavement
# ---------------------------------------------------------------------------
LIFE_EVENTS = [
    G("Get a certified copy of the marriage certificate for the name-change form",
      "Get a certified copy of the marriage certificate", "Order a certified copy for the name-change paperwork",
      "LOW", "ADMIN",
      "A certified copy is ordered and on its way, even if it takes a couple of weeks to arrive",
      [("Find the date and register office where you married", 10),
       ("Fill in the certificate order form online", 10),
       ("Pay the fee for a certified copy", 10)]),

    G("Change my name on everything now the marriage certificate's finally arrived",
      "Change my name on the important accounts", "Update your name across the accounts that matter most",
      "MEDIUM", "ADMIN",
      "The name is updated on the accounts that matter most, bank and passport included, a rarely used account can wait",
      [("List which accounts actually need the name change first", 10),
       ("Update passport and driving licence details", 30),
       ("Update the bank and payroll records", 25),
       ("Work through the rest of the list as they come up", 30)]),

    G("Notify all the organisations after mum passed, apparently there's a service that does it in one go",
      "Notify the organisations after mum's death", "Use the single notification service to tell the relevant organisations",
      "HIGH", "ADMIN",
      "The main organisations are notified through the service, anything it doesn't cover can be chased separately",
      [("Find the death certificate reference number", 10),
       ("Register for the single notification service", 15),
       ("Enter the organisations to notify: bank, pension, council", 20),
       ("Confirm the notifications went through", 10)]),

    G("Sort out lasting power of attorney for dad before things get any harder for him",
      "Sort out lasting power of attorney for dad", "Get the power of attorney paperwork done while he can still decide",
      "HIGH", "ADMIN",
      "The forms are filled in and ready to register, even if the registration itself takes weeks",
      [("Talk to dad about who he wants as attorney and confirm he's willing", 15),
       ("Download the power of attorney forms for finance and health", 10),
       ("Fill in the forms together", 60),
       ("Get a certificate provider to countersign them", 30),
       ("Submit the forms and pay the registration fee", 20)]),

    G("Order a replacement birth certificate, need it for the passport application",
      "Order a replacement birth certificate", "Get a copy ordered for the passport application",
      "MEDIUM", "ADMIN",
      "The certificate is ordered and paid for, even if it takes the standard few days to arrive",
      [("Find the district and approximate date of birth for the search", 10),
       ("Fill in the online certificate order form", 15),
       ("Pay the certificate fee", 10)]),
]

# ---------------------------------------------------------------------------
# Registering to work, checks and licences
# ---------------------------------------------------------------------------
WORK_ADMIN = [
    G("Register as a sole trader before the 5th of October deadline for this tax year",
      "Register as a sole trader", "Get registered before the self-employment deadline",
      "MEDIUM", "ADMIN",
      "The registration is submitted with your details, even if the confirmation letter takes a couple of weeks",
      [("Check you actually need to register this tax year", 10),
       ("Gather your National Insurance number and business details", 15),
       ("Fill in the online registration form", 20),
       ("Submit it and save the confirmation reference", 10)],
      due="before the 5th of October deadline for this tax year"),

    G("Get a police check done for the school volunteering role before the placement starts",
      "Get the police check done for the volunteering role", "Get the criminal record check sorted before the placement starts",
      "MEDIUM", "ADMIN",
      "The check has been submitted with the ID verified, even if the certificate itself takes a few weeks",
      [("Confirm which level of check the role needs", 10),
       ("Gather the ID documents it asks for", 15),
       ("Fill in the application online", 20),
       ("Get the ID verified at the checking point", 25),
       ("Submit it and note the application reference", 10)],
      due="before the placement starts"),

    G("Renew the food hygiene certificate before it lapses next week",
      "Renew the food hygiene certificate", "Get the certificate renewed before it lapses",
      "HIGH", "ADMIN",
      "The renewal course or exam is booked and paid for, even if the new certificate takes a few days to arrive",
      [("Check when the current certificate actually expires", 5),
       ("Find a course or exam slot before then", 15),
       ("Book and pay for it", 15),
       ("Complete the course or exam", 120)],
      due="before it lapses next week"),

    G("Query the balance on the student loan statement, the numbers don't add up",
      "Query the student loan balance", "Get the mismatched balance looked into",
      "MEDIUM", "ADMIN",
      "The query is logged with the loan company and you have a reference number, even if the answer takes a few weeks",
      [("Pull up the last two years of statements", 10),
       ("Note exactly where the figures stop matching", 15),
       ("Fill in the online query form or call them", 20),
       ("Save the reference number they give you", 5)]),

    G("Send a subject access request to get everything the company holds on me",
      "Send the subject access request", "Request a copy of the data the company holds on you",
      "MEDIUM", "ADMIN",
      "The request is submitted with proof of identity, even if the response takes the full statutory month",
      [("Find the company's data protection contact details", 10),
       ("Write a short request naming the data you want", 15),
       ("Attach proof of identity", 10),
       ("Submit it through their official channel", 10)]),
]

# ---------------------------------------------------------------------------
# Claims, appeals and disputes — the deadline-dense heart of this domain
# ---------------------------------------------------------------------------
CLAIMS_APPEALS = [
    G("Appeal the rejected insurance claim within the 20 working days they've given us",
      "Appeal the rejected insurance claim", "Challenge the decision with the evidence they missed",
      "HIGH", "ADMIN",
      "The appeal is submitted with the extra evidence attached, even if the outcome takes a while to come back",
      [("Read the rejection letter and note their exact reasons", 15),
       ("Gather the evidence that addresses those reasons", 30),
       ("Write the appeal referencing the policy and the evidence", 30),
       ("Submit it before the window closes", 15)],
      due="within the 20 working days they've given us"),

    G("Apply for the primary school place before the January admissions deadline",
      "Apply for the primary school place", "Get the application in before the admissions deadline",
      "HIGH", "ADMIN",
      "The application is submitted with the schools ranked in order, even if the first choice is never guaranteed",
      [("Check the catchment areas and admission criteria", 15),
       ("Visit or shortlist the schools you'd rank", 60),
       ("Fill in the online application form", 25),
       ("Submit it before the deadline and save the confirmation", 10)],
      due="before the January admissions deadline"),

    G("Appeal the rejected school place offer within the ten working days we've got",
      "Appeal the rejected school place offer", "Get the appeal in within the short window",
      "URGENT", "ADMIN",
      "The appeal is submitted with your grounds and any evidence, even if the panel date is weeks away",
      [("Read the refusal letter and note the reason given", 10),
       ("Gather evidence that challenges that specific reason", 30),
       ("Write the appeal letter setting out your grounds", 30),
       ("Submit it within the window and keep a copy", 15)],
      due="within the ten working days we've got"),

    G("Dispute the wrong entry on the credit file before it causes any more problems",
      "Dispute the wrong entry on the credit file", "Get the incorrect entry corrected",
      "HIGH", "ADMIN",
      "The dispute is logged with the credit reference agency and you have a case reference, even if the correction takes a few weeks",
      [("Pull the credit report and find the exact entry that's wrong", 15),
       ("Gather evidence that shows it's incorrect", 20),
       ("Fill in the dispute form with the agency", 25),
       ("Submit it and note the case reference", 10)]),

    G("Claim back the emergency tax that came off the first payslip",
      "Claim back the emergency tax", "Get the overcharged tax refunded",
      "MEDIUM", "ADMIN",
      "The claim is submitted with the payslip details, even if the refund takes a few weeks to land",
      [("Check the payslip to see the tax code that was used", 10),
       ("Confirm your correct tax code online", 15),
       ("Fill in the online refund claim form", 20),
       ("Submit it with the payslip reference", 10)]),

    G("Claim delay repay on yesterday's train within the 28-day window",
      "Claim delay repay on yesterday's train", "Get compensation for the delayed journey submitted",
      "LOW", "ADMIN",
      "The claim is submitted with the ticket details, even if the payout takes a couple of weeks",
      [("Find the ticket or booking reference", 5),
       ("Note the scheduled and actual arrival times", 5),
       ("Fill in the online delay repay form", 15),
       ("Submit it with the ticket details", 10)],
      due="within the 28-day window"),

    G("Sort out the stamp duty refund before the three-year window closes",
      "Sort out the stamp duty refund", "Claim back the surcharge before the window closes",
      "HIGH", "ADMIN",
      "The claim is submitted with the sale dates and figures, even if the tax office takes a while to process it",
      [("Check the exact dates that make you eligible for the refund", 15),
       ("Gather the completion statements for both sales", 25),
       ("Fill in the online refund claim form", 25),
       ("Submit it with the figures and save the reference", 10)],
      due="before the three-year window closes"),

    G("Challenge the wrongly issued bus lane fine within the 28-day deadline",
      "Challenge the wrongly issued bus lane fine", "Get the incorrect fine formally challenged in time",
      "URGENT", "ADMIN",
      "The challenge is submitted with the evidence attached, even if the council takes weeks to respond",
      [("Read the notice and check the exact date and location", 10),
       ("Gather evidence that the entry wasn't a breach: photos, signage, timing", 25),
       ("Write the formal challenge referencing the evidence", 25),
       ("Submit it within the 28 days and keep a copy", 15)],
      due="within the 28-day deadline"),
]

# ---------------------------------------------------------------------------
# Travel and vehicle paperwork
# ---------------------------------------------------------------------------
TRAVEL_VEHICLES = [
    G("Apply to extend the visa before the current one expires next month",
      "Apply to extend the visa", "Submit the extension application before the current visa runs out",
      "URGENT", "ADMIN",
      "The extension application is submitted with the evidence they ask for, even if the decision takes a while",
      [("Check the extension route and evidence checklist", 15),
       ("Gather the documents and payslips it asks for", 40),
       ("Fill in the online extension application", 45),
       ("Pay the fee and submit it before the current visa expires", 20)],
      due="before the current one expires next month"),

    G("Claim back the road tax now the car's been scrapped",
      "Claim back the road tax", "Get the remaining months of tax refunded",
      "LOW", "ADMIN",
      "The refund request is submitted with the scrap confirmation, even if the money takes a few weeks to land",
      [("Find the scrap certificate the yard gave you", 10),
       ("Check whether the refund is automatic or needs a form", 10),
       ("Fill in the refund form if one's needed", 15),
       ("Submit it with the certificate details", 10)]),

    G("Get an International Driving Permit sorted before the trip in three weeks",
      "Get the International Driving Permit", "Sort the permit before the trip",
      "MEDIUM", "ADMIN",
      "The permit is applied for with a valid photo and licence details, even if collection means a trip to the post office",
      [("Check which permit type the destination needs", 10),
       ("Get a passport photo to the right spec", 15),
       ("Fill in the application with your licence details", 15),
       ("Submit it and pay the fee", 10)],
      due="before the trip in three weeks"),

    G("Renew the GHIC card before the ski trip in December",
      "Renew the GHIC card", "Get a new card sorted before the ski trip",
      "LOW", "ADMIN",
      "The renewal is submitted through the official site, even if the new card takes a couple of weeks to arrive",
      [("Check the current card's expiry date", 5),
       ("Fill in the renewal form on the official site", 10),
       ("Submit it and note when the new card should arrive", 10)],
      due="before the ski trip in December"),
]

# ---------------------------------------------------------------------------
# Consumer rights
# ---------------------------------------------------------------------------
CONSUMER = [
    G("Claim a Section 75 chargeback on the faulty sofa from the credit card company",
      "Claim the Section 75 chargeback on the sofa", "Get the credit card company to refund the faulty purchase",
      "MEDIUM", "ADMIN",
      "The claim is submitted with the purchase and fault details, even if it takes a few weeks to resolve",
      [("Gather the purchase receipt and card statement showing the payment", 15),
       ("Photograph the fault and note when it appeared", 20),
       ("Fill in the chargeback claim with the card company", 25),
       ("Submit it with the evidence attached", 10)]),

    G("Cancel the subscription that only accepts cancellation by recorded-delivery letter",
      "Cancel the subscription by recorded-delivery letter", "Get the awkward subscription actually cancelled",
      "MEDIUM", "ADMIN",
      "The cancellation letter has been posted and you have proof of postage, even if the confirmation takes weeks",
      [("Find the account number and the exact cancellation address", 10),
       ("Write a short letter giving notice to cancel", 15),
       ("Post it recorded delivery and keep the receipt", 15),
       ("Cancel the payment once the notice period ends", 10)]),
]

# ---------------------------------------------------------------------------
# Estate and probate follow-on admin
# ---------------------------------------------------------------------------
ESTATE = [
    G("Get the house valued for probate before the six-month inheritance tax deadline",
      "Get the house valued for probate", "Get a formal valuation done for the estate before the tax deadline",
      "HIGH", "ADMIN",
      "A formal valuation is obtained and passed to whoever's handling probate, even if other assets are still being valued",
      [("Find the property details and any recent valuations", 15),
       ("Book a valuer to assess the house", 20),
       ("Have the valuation carried out", 60),
       ("Pass the figure to whoever's handling the probate application", 15)],
      due="before the six-month inheritance tax deadline"),

    G("Close the accounts now probate's finally come through",
      "Close the deceased's bank accounts", "Wind down the accounts now probate has been granted",
      "MEDIUM", "ADMIN",
      "The accounts have been notified and closure requested, even if the final payouts take a little longer",
      [("Gather the grant of probate and a list of the accounts", 15),
       ("Contact each bank with the grant of probate", 30),
       ("Fill in each bank's closure form", 30),
       ("Confirm the balance has been paid out before closing", 15)]),
]

# ---------------------------------------------------------------------------
# Everything else — the odd, specific bits of paperwork that pile up
# ---------------------------------------------------------------------------
MISC_ADMIN = [
    G("Consolidate the old pensions from the last two jobs into one pot",
      "Consolidate the old pensions", "Combine the old workplace pensions into one pot",
      "LOW", "ADMIN",
      "The transfer requests are submitted for both pots, even if the move itself then takes weeks",
      [("Find the provider and policy number for each old pension", 15),
       ("Compare the fees on each against a single consolidated option", 25),
       ("Fill in the transfer request for each pot", 30),
       ("Submit the requests and note the reference numbers", 10)]),

    G("Resubmit the passport application before the flight next month, the photo got rejected",
      "Resubmit the passport application", "Get a compliant photo and resend the application before the flight",
      "URGENT", "ADMIN",
      "The resubmission goes off with a photo that meets the spec, even if it's a tight turnaround",
      [("Read exactly why the photo was rejected", 10),
       ("Get a new photo taken to the official spec", 20),
       ("Check the rest of the form is still correct", 10),
       ("Submit the resubmission with the new photo", 15)],
      due="before the flight next month"),

    G("Get a copy of an old P60 for the mortgage application",
      "Get a copy of the old P60", "Request a duplicate P60 for the mortgage application",
      "HIGH", "ADMIN",
      "The request is submitted to the right place, even if the copy takes a few days to arrive",
      [("Work out which tax year and employer it's from", 10),
       ("Contact the employer's records line, or the tax office if the employer is gone", 15),
       ("Request the duplicate copy", 10),
       ("Pass it on to the mortgage application once it arrives", 10)]),

    G("Complain to the ombudsman after the company ignored the complaint for months",
      "Complain to the ombudsman", "Escalate the ignored complaint to the ombudsman",
      "HIGH", "ADMIN",
      "The complaint is submitted with the timeline and evidence, even if the ombudsman takes weeks to respond",
      [("Check you've waited the required time and are eligible to escalate", 10),
       ("Gather the original complaint and every reply, or lack of one", 20),
       ("Write a timeline of what happened and what you want", 30),
       ("Submit it to the ombudsman with the evidence attached", 15)]),

    G("Get a copy of the credit report before viewing the flat on Friday",
      "Get a copy of the credit report", "Pull a copy before the rental viewing",
      "MEDIUM", "ADMIN",
      "The report is downloaded and you've checked the score and any obvious errors, whatever it turns out to say",
      [("Sign up with a free credit checking service", 10),
       ("Request the full report", 10),
       ("Download it and skim it once before Friday", 15)],
      due="before viewing the flat on Friday"),

    G("Get replacement exam certificates reissued before the job application closes",
      "Get the exam certificates reissued", "Request replacements before the application closes",
      "MEDIUM", "ADMIN",
      "The replacement request is submitted with the right reference numbers, even if the reissue takes a couple of weeks",
      [("Find which awarding body issued each certificate", 10),
       ("Locate your candidate number or exam year for each", 15),
       ("Fill in each awarding body's replacement request form", 25),
       ("Submit them and pay the reissue fee", 15)],
      due="before the job application closes"),

    G("File a freedom of information request to the council about the missed bin collections",
      "File a freedom of information request about the bin collections", "Ask the council formally why collections keep being missed",
      "LOW", "ADMIN",
      "The request is submitted in writing with a clear, specific question, even if the statutory reply takes weeks",
      [("Check the council's FOI request page for how to submit it", 10),
       ("Write a clear, specific question about the missed collections", 15),
       ("Submit it through the official FOI channel", 10)]),
]

GOLD: list[Gold] = (
    CIVIC + LIFE_EVENTS + WORK_ADMIN + CLAIMS_APPEALS + TRAVEL_VEHICLES
    + CONSUMER + ESTATE + MISC_ADMIN
)
