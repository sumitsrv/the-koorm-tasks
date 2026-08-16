"""Gold examples: money, paperwork and bureaucracy (hand-authored).

The unglamorous admin nobody wants to do: budgets, debt, disputed charges,
chasing invoices, benefits and tax, remortgaging, pensions, wills, vehicle
paperwork, visas, moving admin, warranty claims, and the letters people leave
on the table for weeks because opening them is the hard part.

See `goldlib.Gold` for the format and `quality.py` for the rules every
example must pass.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from goldlib import Gold

G = Gold

# ---------------------------------------------------------------------------
# Budgeting and debt
# ---------------------------------------------------------------------------
BUDGETING = [
    G("Sort out a proper monthly budget, I've been guessing for years",
      "Make a monthly budget", "Build a working monthly budget from actual income and spending",
      "LOW", "PERSONAL",
      "The budget covers the regular income and outgoings and roughly matches what actually happened last month",
      [("Download the last three months of bank statements", 10),
       ("List the regular income and fixed outgoings", 25),
       ("Add up the variable spending by category", 30),
       ("Set a realistic monthly figure for each category", 20),
       ("Put it in a spreadsheet or app you'll actually open again", 20)]),

    G("Get a proper plan going to pay down the credit card, it's not shrinking on its own",
      "Pay down the credit card balance", "Build and start a repayment plan for the card balance",
      "MEDIUM", "ADMIN",
      "A fixed monthly payment above the minimum is set up and the balance is smaller than when you started",
      [("Check the current balance, APR and minimum payment online", 10),
       ("Work out how much you can realistically put toward it each month", 15),
       ("Decide whether to pay it down as is or move it to a lower-rate card", 20),
       ("Set up a standing order or increased direct debit for the new amount", 15),
       ("Cut up or freeze the card so the balance stops growing", 10)]),

    G("There's a charge on the credit card I don't recognise and need to dispute",
      "Dispute the incorrect charge", "Get the unrecognised charge investigated and reversed",
      "MEDIUM", "ADMIN",
      "The dispute is logged with the bank and you have a reference number, even if the refund hasn't landed yet",
      [("Check the transaction details and the merchant name closely", 10),
       ("Look back through receipts and emails for anything that matches", 15),
       ("Note the date, amount and why it looks wrong", 10),
       ("Call or message the bank's disputes line to raise it", 25),
       ("Write down the reference number and the timeframe they gave you", 5)]),

    G("Ring up and negotiate the phone contract down before it renews at the full price",
      "Negotiate the phone contract down", "Get a better rate on the phone contract before renewal",
      "LOW", "ADMIN",
      "A better rate or deal is agreed and confirmed, even if it's not the cheapest one out there",
      [("Check the current contract price and when it renews", 10),
       ("Look up what competitors are charging for a similar deal", 20),
       ("Call the provider and ask for a loyalty or retention discount", 20),
       ("Get the new price confirmed in writing", 10)],
      due="before it renews"),

    G("Set up an emergency savings pot, we have literally nothing put aside",
      "Set up an emergency savings pot", "Open a separate savings pot and start funding it",
      "LOW", "PERSONAL",
      "A separate pot exists with a standing order feeding it, even if the balance starts small",
      [("Decide on a rough target, like one month's expenses", 15),
       ("Open a separate savings account or pot", 15),
       ("Set up a standing order for whatever you can spare monthly", 15),
       ("Move an initial amount in to get it started", 10)]),

    G("Set up a standing order to overpay the mortgage a bit each month",
      "Set up mortgage overpayments", "Start regular overpayments on the mortgage",
      "LOW", "ADMIN",
      "A regular overpayment is set up and within the lender's allowed limit, even if the amount is modest",
      [("Check the mortgage terms for the maximum allowed overpayment", 10),
       ("Decide how much extra you can realistically send each month", 15),
       ("Set up a standing order or ask the lender to apply it automatically", 20),
       ("Check next month's statement to see the overpayment applied", 10)]),
]

# ---------------------------------------------------------------------------
# Freelance admin: invoices, receipts, getting paid
# ---------------------------------------------------------------------------
FREELANCE = [
    G("Chase the invoice that's six weeks overdue, the client's gone quiet",
      "Chase the overdue invoice", "Get the unpaid invoice followed up and paid",
      "HIGH", "WORK",
      "A firm follow-up has gone out with a new payment date, even if the money hasn't arrived yet",
      [("Check the original invoice date and payment terms", 10),
       ("Confirm the invoice was actually received, not just sent", 15),
       ("Draft a short, firm follow-up chasing the payment", 20),
       ("Send the follow-up and set a reminder for a week from now", 15),
       ("Add a late payment note or fee if the terms allow it", 15)]),

    G("Sort out the shoebox of receipts before I can even start the expense claim",
      "Sort the receipts for the expense claim", "Organise receipts so the expense claim can be filled in",
      "LOW", "WORK",
      "The receipts are sorted by category and add up to a number you're confident in, even if a couple are missing",
      [("Tip the shoebox out and bin anything obviously not work-related", 10),
       ("Sort what's left into categories: travel, meals, supplies", 20),
       ("Photograph or scan each receipt before it fades", 30),
       ("Add up each category on a spreadsheet", 25)]),

    G("Set up a proper invoicing system now that I'm freelance, I'm just using ad hoc emails currently",
      "Set up an invoicing system", "Get a proper invoicing process running for freelance work",
      "MEDIUM", "WORK",
      "Invoices go out from a consistent template with your details and terms on them, even if old clients aren't added yet",
      [("Pick invoicing software or a simple template", 15),
       ("Add your business details, bank info and payment terms", 20),
       ("Set up a numbering system so invoices don't clash", 15),
       ("Create the first invoice from the template and send it", 20)]),
]

# ---------------------------------------------------------------------------
# Tax and benefits
# ---------------------------------------------------------------------------
TAX_BENEFITS = [
    G("Look into the council tax reduction we might actually qualify for",
      "Apply for the council tax reduction", "Check eligibility and submit the reduction application",
      "HIGH", "ADMIN",
      "The application is submitted with the evidence you have to hand, even if one document follows later",
      [("Check the eligibility rules on the council website", 15),
       ("Gather proof of income and the council tax bill", 30),
       ("Fill in the application form", 30),
       ("Attach the evidence and submit it", 15),
       ("Note the reference number and expected response time", 5)]),

    G("They've refused the benefit claim and I think the decision's wrong",
      "Appeal the benefit decision", "Challenge the incorrect benefit decision",
      "HIGH", "ADMIN",
      "The appeal is submitted with your reasons and any evidence, even if you're still waiting on one letter",
      [("Read the decision letter and note exactly what it says", 15),
       ("Check the appeal deadline and the process for this benefit", 15),
       ("Gather evidence that supports your case", 30),
       ("Write the appeal explaining why the decision is wrong", 30),
       ("Submit the appeal with the evidence attached", 15)]),

    G("Do the self-assessment for the freelance income before it becomes a panic",
      "Do the self-assessment tax return", "Prepare and submit the self-assessment for freelance income",
      "HIGH", "ADMIN",
      "The return is submitted with the income and expenses you can evidence, even if a small receipt is missing",
      [("Log into the self-assessment account and check what's needed", 15),
       ("Gather invoices, expense receipts and bank statements for the year", 60),
       ("Enter the income and allowable expenses into the return", 45),
       ("Check the tax owed calculation looks sensible", 20),
       ("Submit the return and save the confirmation", 15)]),

    G("I think I overpaid tax last year and never claimed it back",
      "Claim back the overpaid tax", "Work out and claim back tax you overpaid",
      "MEDIUM", "ADMIN",
      "The claim is submitted with the figures you can support, even if the refund takes a while to land",
      [("Check last year's payslips or tax statements for the overpayment", 15),
       ("Work out roughly how much was overpaid", 20),
       ("Fill in the online claim form or contact the tax office", 25),
       ("Submit the claim with the supporting figures", 15)]),

    G("Sort out the child benefit claim now the baby's arrived, we haven't touched it",
      "Claim child benefit for the new baby", "Get the child benefit claim submitted",
      "MEDIUM", "ADMIN",
      "The claim is submitted with the birth certificate details, even if the first payment takes a few weeks",
      [("Find the baby's birth certificate or registration reference", 10),
       ("Fill in the child benefit claim form", 25),
       ("Attach the required details and submit it", 15),
       ("Note when the first payment should arrive", 5)]),
]

# ---------------------------------------------------------------------------
# Mortgages and household costs
# ---------------------------------------------------------------------------
PROPERTY = [
    G("Sort out remortgaging before the fixed rate deal runs out",
      "Remortgage before the fixed rate ends", "Compare and apply for a new mortgage deal in time",
      "HIGH", "ADMIN",
      "A new deal is locked in with a lender, even if the paperwork is still being finalised",
      [("Check the current mortgage balance and when the fixed rate ends", 15),
       ("Use a comparison site or broker to see what rates are available", 30),
       ("Gather payslips, bank statements and ID for the application", 40),
       ("Apply for the deal that fits best", 30),
       ("Sign and return the offer documents once it arrives", 20)],
      due="before the fixed rate deal runs out"),

    G("Get a mortgage in principle sorted before we start looking at houses properly",
      "Get a mortgage in principle", "Get an agreement in principle sorted before house-hunting",
      "MEDIUM", "ADMIN",
      "An agreement in principle is in hand from at least one lender, even if the figure is provisional",
      [("Check your credit report for anything that might trip up an application", 15),
       ("Work out roughly what you can afford to borrow", 20),
       ("Gather payslips, ID and bank statements", 30),
       ("Apply for the agreement in principle online or with a broker", 25)]),

    G("Switch energy supplier before the new tariff kicks in, ours is about to get expensive",
      "Switch energy supplier", "Compare and switch to a better energy tariff",
      "MEDIUM", "ADMIN",
      "A new tariff is confirmed and the switch is underway, even if it takes a few weeks to go through",
      [("Get a recent meter reading and the current tariff details", 10),
       ("Compare tariffs on a comparison site", 25),
       ("Sign up with the new supplier", 20),
       ("Give the final meter reading when the old supplier asks for it", 10)],
      due="before the new tariff kicks in"),
]

# ---------------------------------------------------------------------------
# Pensions, wills, estates
# ---------------------------------------------------------------------------
PENSIONS_WILLS = [
    G("I'm nearly 30 and don't have a pension, need to just open one",
      "Open a pension", "Set up a pension and get contributions started",
      "LOW", "ADMIN",
      "A pension is open and the first contribution has gone in, even if the amount is small to start",
      [("Check whether a workplace pension is available and unused", 15),
       ("Compare a couple of low-fee personal pension providers", 25),
       ("Open the account online", 20),
       ("Set up a monthly contribution by direct debit", 15)]),

    G("I think I have a pension pot from the job before last and no idea where it is",
      "Track down the old workplace pension", "Find and confirm the old workplace pension",
      "MEDIUM", "ADMIN",
      "The pot is located and you know its value, even if you decide to leave it where it is for now",
      [("Check old payslips or P45s for the pension provider's name", 15),
       ("Use the government pension tracing service if the name isn't there", 20),
       ("Contact the provider with your details to confirm the pot", 20),
       ("Note the balance and provider details somewhere safe", 10)]),

    G("Finally get a will written, we keep saying we'll do it",
      "Write a will", "Get a basic will drafted and signed",
      "MEDIUM", "ADMIN",
      "A signed will exists that says who gets what, even if it gets updated again later",
      [("Jot down a rough list of what you own", 15),
       ("Decide on an executor and a guardian for the kids if relevant", 15),
       ("Use a solicitor or a reputable online will service to draft it", 45),
       ("Read the draft through and check it says what you meant", 20),
       ("Sign it with the required witnesses", 15)]),

    G("Start sorting out probate for my father's estate, I don't know where to begin",
      "Start probate for the estate", "Begin the probate process for your father's estate",
      "HIGH", "ADMIN",
      "The probate application is underway with the estate's value roughly worked out, even if some accounts are still being traced",
      [("Find the will if there is one", 15),
       ("List the assets, debts and accounts you already know about", 30),
       ("Get valuations for the property and any major assets", 45),
       ("Fill in the probate application", 40),
       ("Submit it with the death certificate and pay the fee", 20)]),
]

# ---------------------------------------------------------------------------
# Vehicles and fines
# ---------------------------------------------------------------------------
VEHICLES = [
    G("Register the car now it's actually mine",
      "Register the new car", "Get the car registered in your name",
      "MEDIUM", "ADMIN",
      "The registration is submitted and you have the reference or the new log book is on its way",
      [("Check the log book (V5C) the seller gave you", 10),
       ("Fill in the new keeper section", 15),
       ("Post or submit it online with your details", 20),
       ("Tax the car once the registration confirmation lands", 15)]),

    G("Renew the driving licence, the photo's about to expire",
      "Renew the driving licence", "Get the photocard licence renewed before the old one expires",
      "LOW", "ADMIN",
      "The renewal is submitted with a valid photo and fee paid, even if the new card takes a few weeks",
      [("Check the expiry date and what the renewal needs", 10),
       ("Get a new photo taken to the official spec", 20),
       ("Fill in the renewal application", 20),
       ("Submit it with the fee and note the confirmation", 15)]),

    G("There's a parking fine on the doormat and I need to sort it before it gets worse",
      "Sort out the parking fine", "Deal with the parking fine before the discount period lapses or it escalates",
      "HIGH", "ADMIN",
      "The fine is paid or formally challenged with a reference number, even if the outcome isn't known yet",
      [("Read the notice properly and check the amount and dates", 10),
       ("Decide whether it's worth challenging or just paying", 15),
       ("If challenging, write a short factual appeal with any evidence", 30),
       ("Pay it or submit the appeal", 15),
       ("Keep the confirmation somewhere you'll find it", 5)]),
]

# ---------------------------------------------------------------------------
# Visas, moving admin, warranties, subscriptions
# ---------------------------------------------------------------------------
MOVING_CLAIMS = [
    G("Sort the visa application before the work trip, it's more paperwork than I expected",
      "Apply for the visa", "Get the visa application submitted with the right documents",
      "HIGH", "ADMIN",
      "The application is submitted with the required documents and a receipt or tracking number",
      [("Check the visa type and document checklist for the destination", 15),
       ("Gather the passport, photos, itinerary and bank statements", 45),
       ("Fill in the online application form", 40),
       ("Book the biometrics appointment if one's required", 15),
       ("Submit the application and pay the fee", 20),
       ("Note the tracking number and expected processing time", 10)],
      due="before the work trip"),

    G("Update the address on every account and subscription now that we've actually moved",
      "Update the address everywhere", "Get the new address updated across banks, subscriptions and official bodies",
      "MEDIUM", "ADMIN",
      "The important accounts are updated — bank, DVLA, GP, work — and you've got a list for anything you think of later",
      [("Start a list of accounts tied to the old address", 15),
       ("Update the essential ones first: bank, employer, GP, DVLA", 30),
       ("Update subscriptions and delivery accounts", 30),
       ("Set up mail redirection for anything you miss", 20)]),

    G("The washing machine's broken and it should still be under warranty",
      "Claim on the washing machine warranty", "Get the warranty claim registered and the machine looked at",
      "MEDIUM", "ADMIN",
      "The claim is logged with the retailer or manufacturer and a repair or replacement is arranged",
      [("Find the receipt or proof of purchase and check the warranty terms", 15),
       ("Note what's actually wrong with the machine", 10),
       ("Contact the retailer or manufacturer to start the claim", 20),
       ("Book the repair or replacement slot they offer", 15)]),

    G("Cancel that subscription, they've buried the cancel button on purpose",
      "Cancel the hard-to-cancel subscription", "Actually get the subscription cancelled and confirmed",
      "LOW", "ADMIN",
      "The cancellation is confirmed in writing, even if you had to call rather than click a button",
      [("Check the account settings for a cancel option", 10),
       ("If there isn't one, search for how other people managed to cancel it", 15),
       ("Call or message support and ask directly to cancel", 20),
       ("Get cancellation confirmed in writing and check the next charge doesn't go through", 15)]),
]

# ---------------------------------------------------------------------------
# The letters people leave unopened on the table
# ---------------------------------------------------------------------------
DREADED_LETTERS = [
    G("I've had the letter from HMRC on the table for three weeks and haven't opened it",
      "Open and deal with the HMRC letter", "Open the letter and handle whatever it's asking for",
      "URGENT", "ADMIN",
      "The letter is opened and you know what it's actually asking for, even if you haven't finished responding yet",
      [("Open the letter", 5),
       ("Read it properly and note what it's asking for and by when", 15),
       ("Check if you need any documents to respond", 15),
       ("Gather anything you need or call HMRC if it's unclear", 30),
       ("Send the response or make the payment it's asking for", 20)]),

    G("There's a court letter about unpaid council tax and I've been too scared to open it",
      "Deal with the court letter about council tax", "Open the letter and respond before it escalates further",
      "URGENT", "ADMIN",
      "The letter is opened, you know what's actually owed, and a response or payment plan is underway",
      [("Open the letter", 5),
       ("Read it and note the amount owed and what it's asking you to do", 15),
       ("Call the council to ask about a payment plan", 25),
       ("Agree a plan or pay what you can afford now", 20),
       ("Write down the agreed terms somewhere safe", 10)]),
]

GOLD: list[Gold] = (
    BUDGETING + FREELANCE + TAX_BENEFITS + PROPERTY + PENSIONS_WILLS
    + VEHICLES + MOVING_CLAIMS + DREADED_LETTERS
)
