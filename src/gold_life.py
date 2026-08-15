"""Gold examples: life logistics and big events (hand-authored).

Covers the multi-week projects people dread and put off: moving house,
weddings, funerals, buying and selling cars, mortgages, storage, travel prep,
seasonal admin, and the family logistics that never quite have an owner.

These are mostly PERSONAL and ADMIN, and several are genuinely multi-hour or
multi-day undertakings — that's fine within the 2-6 step cap as long as the
first step stays small and the six steps chosen are the ones that actually
matter, in the order they have to happen (measure before you buy, book the
venue before you announce the date, get the mortgage in principle before you
view houses).

See `goldlib.Gold` for the format and `quality.py` for the rules every example
must pass.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from goldlib import Gold

G = Gold

# ---------------------------------------------------------------------------
# Moving house — from panic to packed, one piece at a time
# ---------------------------------------------------------------------------
MOVE = [
    G("We complete on the house sale in six weeks and I haven't packed a single box, I don't know where to even start",
      "Get organised for the move", "Turn the six weeks left into an actual plan",
      "MEDIUM", "PERSONAL",
      "There's a written plan with the big bookings made — the boxes can still be empty",
      [("Write down the completion date and count backwards to what needs doing each week", 10),
       ("List the big jobs: removal, utilities, address changes, school if it applies", 15),
       ("Put the removal firm booking and any other fixed dates in the calendar", 20),
       ("Pick the first room to start on and put a date on it", 10)]),

    G("Find a removal firm for the house move, first time doing this and not sure what to look for",
      "Book a removal firm", "Compare firms and get one booked for moving day",
      "HIGH", "ADMIN",
      "A firm is booked with a written quote — it doesn't have to be the cheapest one you found",
      [("Measure roughly how much you're moving: rooms and any big items", 15),
       ("Get quotes from three removal firms, ideally with a video or in-person survey", 60),
       ("Compare the quotes for what's actually included: packing materials, insurance, access", 30),
       ("Book the one you want and pay any deposit", 20),
       ("Confirm the date, address and parking access with them in writing", 15)]),

    G("Pack up the whole flat before the move, there's more stuff than I remembered we owned",
      "Pack up the flat", "Get everything packed and labelled before moving day",
      "HIGH", "PERSONAL",
      "The flat is boxed and labelled by room — a few odds and ends can travel loose in the car",
      [("Order enough boxes, tape and a few thick marker pens", 15),
       ("Pack the things you won't need in the next six weeks first: books, spare bedding, decorations", 90),
       ("Pack the kitchen last apart from what you use daily, wrapping anything breakable", 90),
       ("Label every box with the room it's going to and roughly what's in it", 30),
       ("Pack a separate box of first-night essentials: kettle, chargers, bedding, toiletries", 20)]),

    G("Set up gas, electric, water and broadband at the new place before we move in",
      "Set up utilities at the new address", "Get the essential services live before move-in day",
      "HIGH", "ADMIN",
      "The essential services are set up to start around move-in day — a supplier switch for a better deal can wait",
      [("Note the meter types and the new address's postcode", 10),
       ("Call or go online to set up gas and electricity in your name from the move-in date", 40),
       ("Set up the water account with the local supplier", 20),
       ("Order broadband with enough lead time for the engineer visit", 30),
       ("Take meter readings on move-in day and send them to each supplier", 15)]),

    G("Redirect the post and update our address everywhere before we forget",
      "Redirect the post and update the address", "Get mail redirected and the important accounts updated",
      "MEDIUM", "ADMIN",
      "Post redirection is set up and the accounts that matter most are updated — a rarely used account can wait",
      [("Set up mail redirection for the move date", 15),
       ("List the accounts that actually matter: bank, GP, DVLA, insurance, employer payroll", 15),
       ("Update the address on each one, ticking them off the list", 60)]),

    G("Declutter before the move, no point paying to shift stuff we don't want",
      "Declutter before the move", "Cut down what you own before it gets packed and shipped",
      "HIGH", "PERSONAL",
      "Obvious clutter is gone and what's left is worth the cost of moving it — a few undecided boxes are fine",
      [("Set a timer and clear one drawer or shelf to get started", 15),
       ("Go room by room sorting into keep, donate, sell and bin", 120),
       ("List anything worth selling online and photograph it", 30),
       ("Book a charity collection or drop the donate pile off yourself", 30),
       ("Put the bin pile out or book a tip run", 20)]),
]

# ---------------------------------------------------------------------------
# Weddings, funerals, and other ceremonies — book the thing, then tell people
# ---------------------------------------------------------------------------
CEREMONY = [
    G("We're engaged and need to actually book a wedding venue before we can tell anyone a date",
      "Book the wedding venue", "Pin down a venue and date before announcing anything",
      "HIGH", "PERSONAL",
      "A venue and date are booked with a deposit paid — the rest of the planning can start from there",
      [("Agree a rough guest number and budget between you", 15),
       ("Shortlist a few venues that fit both", 30),
       ("Visit the shortlisted venues and ask about availability", 180),
       ("Pick one, check the contract terms and pay the deposit", 45),
       ("Only then tell family and close friends the date", 20)]),

    G("Sort the wedding invitations, we've had the venue booked for months and haven't sent a single one",
      "Sort the wedding invitations", "Finalise the guest list and get invitations out",
      "MEDIUM", "PERSONAL",
      "Invitations are out to the guest list you've agreed — a couple of late additions can follow separately",
      [("Check the venue's guest capacity again", 5),
       ("Pull together both families' guest lists into one spreadsheet", 30),
       ("Agree the final numbers against that capacity", 15),
       ("Choose or design the invitations and get them printed", 60),
       ("Write the addresses and post them out", 90)]),

    G("My dad died on Sunday and I need to organise the funeral, I don't know where to start",
      "Organise the funeral", "Get the funeral arranged",
      "URGENT", "PERSONAL",
      "The date, venue and funeral director are booked and the immediate family know the details — the rest can follow",
      [("Call a funeral director to register interest and get things moving", 15),
       ("Register the death and get the certificates you'll need", 60),
       ("Agree the date and venue with the funeral director", 30),
       ("Tell close family and friends the date once it's confirmed", 20),
       ("Decide the order of service and any music or readings with whoever's helping choose", 45)]),

    G("Sort out the christening for the baby, in-laws keep asking when",
      "Arrange the christening", "Get the christening booked and organised",
      "MEDIUM", "PERSONAL",
      "A date is booked with the church and the people who need to be there know it — the party can be kept simple",
      [("Check with the church about dates and what they need from you", 15),
       ("Pick godparents and ask them", 20),
       ("Book the date with the church once godparents have said yes", 15),
       ("Tell family the date and sort out a gathering afterwards", 45)]),

    G("Our son's bar mitzvah is coming up and there's a lot more to organise than I expected",
      "Arrange the bar mitzvah", "Get the service and celebration organised",
      "MEDIUM", "PERSONAL",
      "The service date is set with the synagogue and a venue is booked for afterwards — the finer details can follow",
      [("Confirm the date with the synagogue and what preparation it involves", 15),
       ("Check what your son still needs to prepare and set a practice schedule", 20),
       ("Book a venue for the celebration afterwards", 45),
       ("Send invitations once the date and venue are fixed", 40),
       ("Sort catering and music for the party", 60)]),
]

# ---------------------------------------------------------------------------
# Cars and property — measure/check before you buy, get the AIP before you view
# ---------------------------------------------------------------------------
VEHICLES_PROPERTY = [
    G("Need to buy a car, the old one finally died",
      "Buy a car", "Find and buy a replacement car",
      "MEDIUM", "PERSONAL",
      "A car that fits the budget and needs is bought and insured — it doesn't have to be the exact spec you pictured",
      [("Set a budget and the must-haves: seats, fuel type, rough age", 15),
       ("Shortlist a few for sale that fit and arrange to view them", 45),
       ("Check the history and take the best one for a test drive", 60),
       ("Negotiate the price and agree the sale", 30),
       ("Sort insurance before you drive it away, then complete the paperwork", 45)]),

    G("Selling the car now we don't need two, never done this before",
      "Sell the car", "Get the car sold safely and for a fair price",
      "MEDIUM", "PERSONAL",
      "The car is sold to someone who's paid properly and the paperwork is done — haggling a bit more wasn't worth it",
      [("Look up what similar cars are selling for", 15),
       ("Give it a clean and take decent photos", 45),
       ("List it with an honest description of any faults", 30),
       ("Meet buyers somewhere safe and let them view or drive it", 60),
       ("Take payment in a way you can verify before handing over the keys", 15),
       ("Notify the DVLA of the change of keeper", 10)]),

    G("We want to start looking at houses but apparently need a mortgage agreement in principle first",
      "Get a mortgage agreement in principle", "Get the AIP sorted before house hunting properly",
      "HIGH", "ADMIN",
      "An agreement in principle is in hand for a sensible amount — the actual lender can still change later",
      [("Pull together three months of bank statements and payslips", 15),
       ("Check your credit report for anything that might trip up the application", 20),
       ("Compare a few lenders' rates for your deposit size", 30),
       ("Apply for the agreement in principle with the one you've chosen", 30),
       ("Save the confirmation somewhere you can pull it up quickly when viewing", 10)]),

    G("Book some house viewings for the weekend, we've been putting it off",
      "Book house viewings", "Get viewings booked and actually go to them",
      "HIGH", "PERSONAL",
      "A few viewings are booked and been to, with notes jotted down afterwards — none of them has to be the one",
      [("Set your must-haves and hard no's so viewings don't waste time", 15),
       ("Shortlist listings that match and book viewings for a few", 30),
       ("Go to each viewing and note it down straight after while it's fresh", 150),
       ("Compare notes side by side and decide which to see again", 20)]),

    G("The van's booked for Friday and half our stuff still doesn't fit anywhere, need storage sorted fast",
      "Sort storage before the move", "Get a storage unit sorted for what won't fit",
      "URGENT", "ADMIN",
      "A storage unit big enough for the overflow is booked and paid for — the rest can be figured out after moving day",
      [("Estimate roughly how much overflow needs storing, in boxes or a van-load", 10),
       ("Call two or three storage places nearby for unit size and price", 30),
       ("Book the unit and pay the deposit", 15),
       ("Work out access times so you can drop things off around the move", 15)]),
]

# ---------------------------------------------------------------------------
# Travel — visas, jabs, insurance, and the group trips that need a plan
# ---------------------------------------------------------------------------
TRAVEL = [
    G("Sorting visas for the trip to India, apparently it needs doing weeks in advance",
      "Sort the travel visas", "Get the visas applied for with enough lead time",
      "HIGH", "ADMIN",
      "The visa applications are submitted with what they asked for — approval timing is out of your hands",
      [("Check the visa requirements and how long processing usually takes", 15),
       ("Get passport photos taken to the right spec", 20),
       ("Fill in the application forms and gather the supporting documents", 60),
       ("Submit the applications and pay the fee", 30),
       ("Note the tracking or reference numbers somewhere you'll find them", 10)]),

    G("Need to get travel vaccinations sorted before the trip, not sure which ones we actually need",
      "Get the travel vaccinations sorted", "Find out what's needed and get it done in time",
      "MEDIUM", "HEALTH",
      "The vaccinations that matter for the trip are booked or done — a very minor optional one can be skipped",
      [("Look up which vaccinations are recommended for the destination", 15),
       ("Book an appointment at the travel clinic or GP", 15),
       ("Get the vaccinations, checking which need a course over several weeks", 45),
       ("Note what was given and when the next dose is due if there is one", 10)]),

    G("Renew the travel insurance before it lapses",
      "Renew the travel insurance", "Get a new policy in place before the old one runs out",
      "LOW", "ADMIN",
      "A policy that actually covers the trip is in place — it doesn't have to be the cheapest quote found",
      [("Check what the current policy covers and when it expires", 10),
       ("Compare a few quotes for the same level of cover", 30),
       ("Buy the policy and save the documents somewhere you can find them travelling", 15)]),

    G("Planning a festival weekend with mates, need to get organised before tickets sell out",
      "Plan the festival weekend", "Get tickets, camping kit and logistics sorted",
      "LOW", "PERSONAL",
      "Tickets and a way to camp are sorted and everyone knows the plan — the packing list can happen closer to the time",
      [("Message the group to confirm who's actually in", 10),
       ("Buy tickets for everyone confirmed", 25),
       ("Sort camping gear: who owns what, what's missing", 30),
       ("Agree travel and split fuel or lift costs", 20),
       ("Share the final plan so everyone knows where and when to meet", 10)]),
]

# ---------------------------------------------------------------------------
# Household and seasonal — the recurring stuff that has no natural owner
# ---------------------------------------------------------------------------
HOUSEHOLD = [
    G("The house share cleaning rota has fallen apart again, need to sort it properly this time",
      "Sort the house share cleaning rota", "Get a fair cleaning rota that people actually stick to",
      "LOW", "PERSONAL",
      "There's an agreed rota on the wall or shared online — whether everyone sticks to it is another matter",
      [("List the jobs that actually need doing and how often", 15),
       ("Ask the housemates what they'd rather do and swap around", 20),
       ("Write the rota up and put it somewhere everyone will see it", 15),
       ("Agree what happens if someone misses their turn", 15)]),

    G("Due date's getting closer and we haven't got anything ready for the baby",
      "Get ready for the new baby", "Get the essentials sorted before the due date",
      "HIGH", "PERSONAL",
      "The essentials are ready — nursery, hospital bag, car seat — the nice-to-haves can wait",
      [("Write a list of what's actually needed versus nice to have", 15),
       ("Order or borrow the big items: cot, car seat, pram", 60),
       ("Set up the nursery or sleeping space", 90),
       ("Pack the hospital bag", 30),
       ("Fit the car seat and get it checked", 30)]),

    G("Get the house ready for winter before the cold really sets in, gutters and boiler and all that",
      "Get the house ready for winter", "Handle the jobs that stop winter becoming a crisis",
      "MEDIUM", "PERSONAL",
      "The boiler's serviced and the gutters are clear — smaller jobs can be picked off as the weather allows",
      [("Walk round the house and note anything obviously needed: gutters, drafts, leaks", 15),
       ("Book the boiler service", 15),
       ("Clear the gutters and check the downpipes run free", 60),
       ("Draught-proof the worst doors and windows", 45),
       ("Find the stopcock and check you can turn it in case a pipe freezes", 10)]),

    G("Put a snow kit together for the car before the first cold snap catches us out",
      "Put together a car snow kit", "Get the car ready for winter driving",
      "LOW", "PERSONAL",
      "The basics are in the boot — blanket, torch, shovel — it doesn't need to handle a full-on blizzard",
      [("Check the antifreeze and tyre tread are in decent shape", 15),
       ("Buy a scraper, de-icer and a torch", 20),
       ("Pack a blanket, a small shovel and some snacks in the boot", 15),
       ("Charge a power bank and keep it in the glovebox", 10)]),

    G("Do the spring clean, the flat needs a proper once-over after winter",
      "Do the spring clean", "Give the flat a proper clean after winter",
      "LOW", "PERSONAL",
      "The rooms feel noticeably fresher — a forgotten corner doesn't matter",
      [("Open the windows and pick the room to start in", 10),
       ("Clear surfaces and give everything a proper dust, including skirting and tops of frames", 45),
       ("Wash the floors and any rugs that need it", 60),
       ("Clean the windows inside and give curtains or blinds a wipe down", 45),
       ("Move on to the next room and repeat", 90)]),
]

# ---------------------------------------------------------------------------
# Family logistics — the admin nobody signs up for but somebody has to run
# ---------------------------------------------------------------------------
FAMILY_ADMIN = [
    G("It's our turn to host Christmas this year and I've never done the whole thing before",
      "Host Christmas this year", "Get the house and the day ready for everyone",
      "HIGH", "PERSONAL",
      "The food, sleeping arrangements and presents are sorted — a lopsided homemade decoration or two is fine",
      [("Confirm who's coming and how many are staying over", 15),
       ("Plan the menu and order what needs pre-ordering, like the turkey", 30),
       ("Sort sleeping arrangements: beds, sofa beds, air mattresses", 30),
       ("Do the food shop in stages so the fridge isn't overwhelmed at once", 90),
       ("Cook the day itself, working back from serving time", 300),
       ("Wrap the presents in the days before", 60)]),

    G("Sort a school run rota with the other parents on our street, doing it solo is killing me",
      "Sort the school run rota", "Share the school run with other parents nearby",
      "LOW", "PERSONAL",
      "A rota is agreed and everyone knows their days — an odd swap here and there is fine",
      [("Ask around which parents nearby might want to share the run", 15),
       ("Agree who can do which days and any car seat requirements", 20),
       ("Write the rota up and share it with everyone doing it", 15),
       ("Agree how swaps get sorted when someone can't make their day", 15)]),

    G("Put together a proper emergency kit for the house, we've got nothing if the power goes out",
      "Put together a home emergency kit", "Get basic supplies together for a power cut or similar",
      "MEDIUM", "ADMIN",
      "There's a torch, water, a way to charge a phone and basic first aid in one place — it's a starting point, not a bunker",
      [("Pick a cupboard or box to keep it all together in", 10),
       ("Buy torches, spare batteries and a battery radio or power bank", 30),
       ("Store bottled water and some tinned or dried food", 20),
       ("Put together a basic first aid kit", 20),
       ("Write down useful numbers and keep a copy in the box", 10)]),

    G("Trying to organise a family reunion, we haven't all been in the same place for years",
      "Organise a family reunion", "Get the wider family together in one place",
      "MEDIUM", "PERSONAL",
      "A date, place and headcount are settled and everyone's been told — the finer details can follow",
      [("Message the wider family to find a date that could work for most", 15),
       ("Settle on a date once you've heard back from enough people", 15),
       ("Book a venue or a big enough space to host everyone", 45),
       ("Sort food and let people know what to bring", 40),
       ("Send the final details out once everything's booked", 20)]),

    G("Write a will, we keep saying we'll get round to it",
      "Write a will", "Get a proper will in place",
      "HIGH", "ADMIN",
      "A signed, witnessed will exists that says what you actually want — it can be updated later as things change",
      [("Jot down roughly what you own and who matters most to leave it to", 15),
       ("Decide who'll be executor and guardians for the kids if that applies", 15),
       ("Use a solicitor or a reputable will-writing service to draft it", 60),
       ("Read the draft carefully and check it says what you meant", 30),
       ("Sign it with witnesses present and store it somewhere safe", 20)]),
]

GOLD: list[Gold] = MOVE + CEREMONY + VEHICLES_PROPERTY + TRAVEL + HOUSEHOLD + FAMILY_ADMIN
