"""Gold examples: home repair and maintenance, second pass (hand-authored).

`gold_core.py`'s REPAIR group already covers eight hands-on jobs: the leaking
kitchen tap, leaning shelves, a bike puncture, bleeding the radiators,
flat-pack wardrobe assembly, a car service, an unblocking washing machine and
repainting a damp-stained wall. This module deliberately covers different
concrete jobs rather than variations on those eight, while staying in exactly
the domain `quality.py`'s `PREREQUISITES` gate exists to police — physical
procedures with a real, get-it-wrong-and-you-flood-the-kitchen order to them.

Territory here: plumbing beyond the one tap (a running toilet, a slow drain,
a dripping shower mixer, an outside tap, a leak under a different sink,
descaling limescale out of taps); electrical work (a light fitting, a dead
socket, a breaker that keeps tripping, wiring a plug, a smoke alarm,
overloaded extension leads); appliance faults distinct from the one washing
machine example (a dishwasher, a fridge seal, a dryer, a kettle, a vacuum, an
oven); doors, windows and locks; walls, floors and fixtures (a floorboard, a
drywall patch, grout, a banister, a cabinet hinge); outdoor and structural
jobs including the "get a professional in and manage it" case for anything
not DIY-safe; seasonal maintenance that is one job at a time rather than
`gold_life.py`'s all-in-one "get the house ready for winter"; and the
landlord-adjacent admin of reporting a rental repair and working out what you
are and are not meant to fix yourself.

Every multi-step example that opens plumbing or wiring gets the prerequisite
order right: isolate the water or power and confirm it is off before you
open anything up, buy or check the part before you start rather than
discovering mid-job you have the wrong size, and test after the fix instead
of assuming it worked. Phrasing stays in the same informal, sometimes
procrastination-flavoured register as the rest of the corpus.

See `goldlib.Gold` for the format and `quality.py` for the rules every
example must pass.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from goldlib import Gold

G = Gold

# ---------------------------------------------------------------------------
# Plumbing beyond the kitchen tap
# ---------------------------------------------------------------------------
PLUMBING = [
    G("The toilet's been running non-stop since the weekend, it's driving me mad",
      "Fix the running toilet", "Stop the cistern refilling constantly",
      "MEDIUM", "PERSONAL",
      "The cistern stops filling and stays quiet once it's full, even if you fiddle with the float again later",
      [("Turn off the water at the isolation valve behind the toilet", 5),
       ("Lift the cistern lid and watch what happens as it fills", 5),
       ("Check the flapper or valve seal and float height, note what's worn", 10),
       ("Buy a matching fill valve or flapper if needed", 20),
       ("Fit the new part, turn the water back on and flush to test", 15)]),

    G("The bathroom sink's been draining dead slow for weeks now",
      "Unblock the slow bathroom sink drain", "Clear whatever's slowing the drain",
      "LOW", "PERSONAL",
      "The sink drains at a normal speed again, no more standing water while you brush your teeth",
      [("Clear the visible hair and gunk from the plughole by hand", 10),
       ("Try a sink plunger over the plug with the overflow covered", 10),
       ("Put a bucket under the trap in case it drips", 5),
       ("Undo the U-bend and clear out what's blocking it", 20),
       ("Reconnect the trap, run the tap and check underneath for leaks", 10)]),

    G("The shower mixer's been dripping non-stop after we turn it off",
      "Fix the dripping shower mixer", "Stop the shower mixer dripping when it's off",
      "MEDIUM", "PERSONAL",
      "The shower stops dripping within a minute of turning it off, and there's no water pooling under the tray",
      [("Turn the water off at the isolation valve under the bath panel", 5),
       ("Take the shower head off and check the washer inside", 10),
       ("Unscrew the mixer valve cartridge and inspect it", 20),
       ("Buy a matching replacement cartridge if it's worn", 20),
       ("Fit the new cartridge, turn the water back on and test for drips", 15)]),

    G("The outside tap's been dripping into the flowerbed all summer",
      "Fix the dripping outside tap", "Stop the garden tap dripping",
      "LOW", "PERSONAL",
      "The outside tap stops dripping once it's off, and the flowerbed underneath stays dry",
      [("Find the internal stopcock or isolation valve feeding the outside tap", 10),
       ("Turn it off and open the outside tap to drain what's left", 5),
       ("Unscrew the tap and check the washer or O-ring inside", 15),
       ("Buy a matching washer or O-ring kit", 20),
       ("Fit the new washer, reassemble and turn the water back on", 15)]),

    G("There's a small leak under the bathroom sink that's warping the cabinet floor",
      "Fix the leak under the bathroom sink", "Stop the pipe under the bathroom sink leaking",
      "HIGH", "PERSONAL",
      "The pipe joint stays dry after running the tap for a bit, and the cabinet floor isn't getting any wetter",
      [("Turn off the water at the isolation valve under the sink", 5),
       ("Clear out the cabinet and put a bowl under the pipe", 10),
       ("Loosen the slip nut and see exactly where it's leaking", 15),
       ("Buy a matching washer or replacement section of pipe", 20),
       ("Replace the leaking section and turn the water back on to check", 15)]),

    G("The taps around the house are covered in limescale and barely trickle now",
      "Descale the limescale-clogged taps", "Get the water flow back through the scaled-up taps",
      "LOW", "PERSONAL",
      "The taps run at a decent flow again, even if a couple of stubborn spots remain to attack another day",
      [("Buy a descaling solution or get white vinegar and bags", 10),
       ("Unscrew the aerators and showerheads and soak them in descaler", 15),
       ("Scrub off any visible scale on the tap bodies with a cloth and vinegar", 15),
       ("Rinse and refit the aerators, then run each tap to check the flow's improved", 15)]),
]

# ---------------------------------------------------------------------------
# Electrical — power off and test dead before opening anything
# ---------------------------------------------------------------------------
ELECTRICAL = [
    G("The hall light fitting's been hanging by its wires since the pendant cracked",
      "Replace the hall light fitting", "Swap the cracked pendant for a new fitting",
      "HIGH", "PERSONAL",
      "The new light works from the switch and nothing feels loose when you wiggle the fitting",
      [("Check the old fitting's fixing plate and cable type so you buy the right match", 10),
       ("Turn the power off at the consumer unit for that circuit", 5),
       ("Test the wires are dead with a voltage tester", 5),
       ("Buy the new fitting", 20),
       ("Disconnect the old fitting and wire in the new one", 25),
       ("Turn the power back on and test the switch", 10)]),

    G("One of the sockets in the kitchen has stopped working and half that wall's dead now",
      "Fix the dead kitchen socket", "Work out why the socket's stopped working",
      "MEDIUM", "PERSONAL",
      "The socket powers a lamp reliably again and the faceplate sits flush",
      [("Check if it's just tripped by looking at the consumer unit", 5),
       ("Reset any tripped breaker and see if power returns", 5),
       ("If not, turn that circuit off at the consumer unit before opening anything", 5),
       ("Test the socket is dead with a voltage tester", 5),
       ("Unscrew the faceplate and check the wiring connections are tight", 20),
       ("Screw it back together, turn the power on and test with a lamp", 10)]),

    G("The upstairs circuit breaker keeps tripping every couple of days and I've just been resetting it",
      "Find why the upstairs breaker keeps tripping", "Stop just resetting the breaker and find the cause",
      "HIGH", "PERSONAL",
      "You know whether it's one appliance or a wiring fault, and the breaker's staying up",
      [("Unplug everything on that circuit and reset the breaker", 10),
       ("Plug devices back in one at a time to find what trips it", 20),
       ("If nothing obvious trips it, leave that appliance unplugged and note it", 10),
       ("If it keeps tripping with nothing plugged in, call an electrician rather than keep resetting it", 15)]),

    G("The kettle's flex has a bare wire showing near the plug, needs sorting before someone gets a shock",
      "Fit a new plug on the kettle", "Replace the damaged plug on the kettle's flex",
      "HIGH", "PERSONAL",
      "The kettle powers on normally and the flex isn't hot to the touch after boiling",
      [("Unplug the kettle and buy a new plug that matches the flex", 15),
       ("Cut back the damaged end of the flex to good cable", 10),
       ("Strip the wires and wire them into the new plug: live, neutral, earth", 20),
       ("Check the fuse rating matches the appliance and close the plug up", 10),
       ("Plug it in and test the kettle works", 5)]),

    G("The smoke alarm's been chirping every few minutes for two nights and nobody's slept properly",
      "Fix the chirping smoke alarm", "Stop the smoke alarm's low-battery chirp",
      "HIGH", "PERSONAL",
      "The alarm's quiet and the test button gets a proper beep, even if you replace the other alarms another day",
      [("Check whether it's a battery model or hardwired with a backup battery", 5),
       ("Buy the right battery or a replacement alarm unit if it's old", 15),
       ("Turn off the power at the consumer unit if it's hardwired", 5),
       ("Swap the battery or unit and test the alarm button", 10),
       ("Turn the power back on and check the alarm's light is active", 5)]),

    G("There's an extension lead running to the desk with about six things plugged into it",
      "Sort out the overloaded desk extension lead", "Reduce the load on the desk's extension lead",
      "MEDIUM", "PERSONAL",
      "Nothing on the desk is overloaded and the cables aren't a trip hazard across the floor",
      [("List what's actually plugged in and add up the rough wattage", 10),
       ("Move anything high-draw, like a heater or kettle, off the extension entirely", 10),
       ("Buy a lead with a higher rating or a second circuit to split the load", 20),
       ("Reroute the cables so nothing's pinched under furniture or across a walkway", 15)]),
]

# ---------------------------------------------------------------------------
# Appliances beyond the washing machine
# ---------------------------------------------------------------------------
APPLIANCES = [
    G("The dishwasher's been leaving a pool of water in the bottom after every cycle",
      "Fix the dishwasher not draining", "Stop water pooling in the dishwasher after a cycle",
      "MEDIUM", "PERSONAL",
      "It drains with no standing water left in the bottom after a cycle, even if the pump sounds a bit different than before",
      [("Switch it off and unplug it before opening anything", 5),
       ("Bail out the standing water with a cup and towels", 10),
       ("Pull the filter out at the bottom and clean it", 15),
       ("Check the drain hose for a kink and the drain pump for debris", 20),
       ("Plug it back in and run a short cycle to check it drains", 15)]),

    G("The fridge door doesn't seem to be sealing properly and it's running non-stop",
      "Fix the fridge door seal", "Stop the fridge running constantly from a bad door seal",
      "MEDIUM", "PERSONAL",
      "The paper grips when you pull it out and the fridge stops running constantly",
      [("Check the seal for gaps by closing it on a piece of paper and pulling", 10),
       ("Clean the seal and the groove it sits in with warm soapy water", 15),
       ("See if a hairdryer softens and reshapes a warped section", 15),
       ("If it's cracked or too far gone, order a matching replacement seal", 20),
       ("Fit the new seal and repeat the paper test", 15)]),

    G("The tumble dryer's running but everything's coming out damp and cold now",
      "Fix the dryer not heating", "Work out why the dryer's stopped heating",
      "MEDIUM", "PERSONAL",
      "The towels come out properly warm at the end of a cycle, not just tumbled",
      [("Unplug the dryer before checking anything inside", 5),
       ("Clean the lint filter properly, it's an easy first fix", 10),
       ("Check the external vent hose isn't blocked or crushed", 15),
       ("If it's still not heating, check the thermal fuse hasn't tripped", 20),
       ("Plug it back in and run a short cycle with a couple of towels", 15)]),

    G("The kettle's got so much limescale in it the water's started tasting off",
      "Descale the kettle", "Clear the limescale build-up out of the kettle",
      "LOW", "PERSONAL",
      "The water doesn't taste of vinegar anymore and there's no visible scale floating in a fresh boil",
      [("Empty the kettle and check it's unplugged", 5),
       ("Fill it with a vinegar and water mix or a descaling sachet", 5),
       ("Let it sit for half an hour, then boil once", 15),
       ("Empty it out and rinse it a few times", 10),
       ("Boil a rinse batch and tip it away before using it for tea", 10)]),

    G("The hoover's basically just pushing dust around instead of picking it up",
      "Fix the vacuum losing suction", "Get the vacuum picking dirt up properly again",
      "LOW", "PERSONAL",
      "It's noticeably pulling dirt out of the carpet again, not just skating over it",
      [("Unplug it and check the bin or bag isn't full", 5),
       ("Pull the filter out and wash or replace it", 15),
       ("Check the hose and brush bar for a tangle or blockage", 15),
       ("Reassemble and run it over a small patch of carpet to test", 10)]),

    G("The oven's been baking things unevenly, one side always comes out darker",
      "Fix the oven's uneven heating", "Work out why the oven bakes unevenly",
      "LOW", "PERSONAL",
      "A tray of biscuits comes out roughly the same colour across the tray",
      [("Put an oven thermometer in and check the actual temperature against the dial", 15),
       ("Check the door seal isn't letting heat escape on one side", 10),
       ("Clean the fan and vents if it's a fan oven, they collect grease", 20),
       ("Recalibrate the dial if the manual explains how", 15),
       ("Bake something simple and check it browns more evenly", 20)]),
]

# ---------------------------------------------------------------------------
# Doors, windows, locks
# ---------------------------------------------------------------------------
DOORS_WINDOWS = [
    G("The bedroom door's been sticking on the frame for months, have to shoulder it open",
      "Fix the sticking bedroom door", "Stop the bedroom door catching on the frame",
      "LOW", "PERSONAL",
      "The door closes without catching and doesn't need a shove anymore",
      [("Work out where it's rubbing by opening and closing it slowly", 10),
       ("Tighten any loose hinge screws first, that's sometimes all it is", 15),
       ("If it's still tight, mark the high spot with chalk or pencil", 10),
       ("Take the door off and plane down the marked area a little at a time", 30),
       ("Rehang it and test it closes smoothly", 15)]),

    G("There's a cold draught coming through the bedroom window frame all winter",
      "Draught-proof the bedroom window", "Stop the draught coming through the window frame",
      "LOW", "PERSONAL",
      "You can't feel a draught with your hand held near the frame anymore",
      [("Find where the draught's coming from with a lit candle or the back of your hand", 10),
       ("Buy self-adhesive foam or brush strip in the right size", 15),
       ("Clean the frame where the strip will stick", 10),
       ("Cut and stick the strip around the frame", 20),
       ("Close the window and check the draught's gone", 5)]),

    G("The front door lock's been sticky and hard to turn, want it sorted before it seizes up completely",
      "Replace the sticky front door lock", "Swap the sticking front door lock for a new one",
      "HIGH", "PERSONAL",
      "The new lock turns smoothly and the spare key works in it too",
      [("Check the lock's make and size so you buy a matching replacement", 15),
       ("Buy a new lock cylinder or barrel", 20),
       ("Unlock and prop the door open before removing anything", 5),
       ("Unscrew the old lock and take it out", 15),
       ("Fit the new lock and cut a spare key", 20),
       ("Test it locks and unlocks smoothly from both sides", 10)]),

    G("The kitchen window won't stay open on its own anymore, the stay's snapped",
      "Fix the kitchen window that won't stay open", "Replace the broken window stay",
      "LOW", "PERSONAL",
      "The window stays open on its own at a couple of different angles",
      [("Check the broken stay and take the part number or a photo to match", 10),
       ("Buy a matching replacement stay", 15),
       ("Unscrew the broken stay from the frame and sash", 15),
       ("Fit the new stay and check the screws are tight", 15),
       ("Open and close the window a few times to check it holds", 5)]),

    G("The front door's letting the cold straight through around the edges",
      "Weatherstrip the front door", "Stop cold air coming through around the front door",
      "LOW", "PERSONAL",
      "No daylight or draught comes through around the closed door",
      [("Check where the gaps are all round the door with your hand", 10),
       ("Buy weatherstrip and a draught excluder brush for the bottom", 15),
       ("Clean the frame edges so the strip sticks properly", 10),
       ("Fit the strip around the frame and the brush along the bottom", 25),
       ("Close the door and check for gaps again", 5)]),
]

# ---------------------------------------------------------------------------
# Walls, floors, fixtures
# ---------------------------------------------------------------------------
WALLS_FLOORS = [
    G("There's a floorboard on the landing that squeaks every time someone walks over it at night",
      "Fix the squeaky landing floorboard", "Stop the landing floorboard squeaking",
      "LOW", "PERSONAL",
      "It doesn't squeak when you walk over it at normal speed anymore",
      [("Find the exact board and joist by walking over it and listening", 10),
       ("Sprinkle talc or a lubricant into the gap where it squeaks", 10),
       ("If that doesn't fix it, lift the edge of the carpet or find the board from below", 15),
       ("Screw the board down into the joist where it's moving", 20),
       ("Walk over it again to check the squeak's gone", 5)]),

    G("There's a fist-sized hole in the hallway wall from when we moved the sofa",
      "Patch the hole in the hallway wall", "Fill and finish the hole in the wall",
      "LOW", "PERSONAL",
      "The patch is solid to the touch and you can't see the hole from a normal distance, even if the paint's slightly different up close",
      [("Buy a patch kit or a scrap of drywall bigger than the hole", 15),
       ("Cut back any loose or crumbling edges around the hole", 10),
       ("Fit the patch and tape the edges", 20),
       ("Apply filler over the patch and let it dry", 30),
       ("Sand it smooth and touch up with matching paint", 25)]),

    G("The grout in the shower's gone black and crumbly in places",
      "Regrout the shower tiles", "Replace the mouldy shower grout",
      "LOW", "PERSONAL",
      "The grout lines look solid and even-ish, and there's nothing crumbling out when you run a nail along it",
      [("Buy a grout rake or multi-tool blade and matching grout", 15),
       ("Rake out the old crumbly grout between the tiles", 30),
       ("Wipe away the dust and leave it to dry", 15),
       ("Mix and apply the new grout, working it into the gaps", 30),
       ("Wipe off the excess before it sets and buff once dry", 20)]),

    G("The banister on the stairs wobbles when you grab it, kids use those stairs every day",
      "Fix the wobbly banister", "Stop the stair banister moving when it's grabbed",
      "HIGH", "PERSONAL",
      "The banister doesn't move when you lean your weight on it at any point along the stairs",
      [("Check whether it's the newel post, brackets or spindles that are loose", 10),
       ("Buy the right screws or a bracket if one's missing", 15),
       ("Tighten or replace the loose fixings", 25),
       ("Give it a firm shake test at the top and bottom of the run", 5)]),

    G("One of the kitchen cabinet doors has been hanging crooked for weeks, the hinge is stripped",
      "Fix the crooked kitchen cabinet door", "Sort out the stripped cabinet hinge",
      "LOW", "PERSONAL",
      "The door hangs straight and closes without catching on the frame",
      [("Open the door and see whether the hinge or the screw holes are stripped", 10),
       ("Buy matching hinges or wooden matchsticks and glue to pack the holes", 15),
       ("If packing the holes, glue matchsticks in and let them dry", 30),
       ("Screw the hinge back in, using the packed holes if needed", 15),
       ("Check the door sits flush and swings without dragging", 10)]),
]

# ---------------------------------------------------------------------------
# Outdoor and structural
# ---------------------------------------------------------------------------
OUTDOOR = [
    G("One of the fence panels blew down in the last storm, want it fixed before the next storm rolls in this weekend",
      "Replace the blown-down fence panel", "Fit a new panel where the fence blew down",
      "MEDIUM", "PERSONAL",
      "The new panel is solid when you push on it and there's no gap at the bottom letting the dog through",
      [("Measure the gap and check the post spacing before buying anything", 15),
       ("Buy a matching panel and any brackets or gravel boards needed", 30),
       ("Clear away the old broken panel", 15),
       ("Fit the new panel into the brackets and check it's level", 30),
       ("Screw or nail it in place and give it a shake test", 15)],
      due="this weekend"),

    G("One section of guttering's come away from the fascia and water's pouring down the wall when it rains",
      "Refix the loose gutter section", "Reattach the gutter section that's come away",
      "HIGH", "PERSONAL",
      "Water runs along the gutter and down the downpipe instead of over the edge next time it rains",
      [("Check from the ground whether it's a bracket, joint or a crack causing it", 10),
       ("Buy a matching bracket, joint seal or gutter section", 20),
       ("Set up a ladder safely on level ground with someone footing it", 10),
       ("Refit the bracket or seal the joint", 25),
       ("Run a hose through it to check water flows and nothing drips", 15)]),

    G("There's a damp patch spreading on the spare room ceiling after the last heavy rain, think it's the roof",
      "Deal with the roof leak on the spare room ceiling", "Get the roof leak looked at and managed",
      "URGENT", "ADMIN",
      "A roofer's booked in and the bucket's catching what comes through until then",
      [("Put a bucket under the patch and check the loft for the actual source", 15),
       ("Take photos of the damp patch and, if visible, the roof for the quote", 15),
       ("Get two or three roofers round to quote before picking one", 45),
       ("Book the one you trust and clear access to the loft and outside wall", 15),
       ("Keep an eye on the ceiling patch until the work's done", 10)]),

    G("The shed door's swollen with damp and doesn't shut properly, keeps sticking",
      "Fix the sticking shed door", "Stop the swollen shed door sticking",
      "LOW", "PERSONAL",
      "The door shuts and the latch catches without having to lean on it",
      [("Check whether it's swelling, a dropped hinge, or the frame that's the problem", 10),
       ("Tighten or reset the hinge screws first", 15),
       ("If it's swelling, plane down the rubbing edge a little at a time", 30),
       ("Treat the bare wood edge with a wood preserver so it doesn't keep swelling", 20),
       ("Test the door shuts and latches properly", 5)]),
]

# ---------------------------------------------------------------------------
# Seasonal maintenance — one job at a time, not gold_life's whole-house sweep
# ---------------------------------------------------------------------------
SEASONAL = [
    G("It's been over a year since the boiler was serviced and the pilot light's gone a funny colour",
      "Book the overdue boiler service", "Get the boiler properly serviced",
      "HIGH", "PERSONAL",
      "The boiler's been serviced, the pilot's back to normal, and there's a reminder set for next year",
      [("Check when it was last serviced and find the model number", 10),
       ("Book a Gas Safe registered engineer for a service", 15),
       ("Clear access around the boiler before they come", 10),
       ("Be in for the appointment and ask what they found", 60),
       ("Note the date and set a reminder for next year", 5)]),

    G("It's been ages since anyone tested the smoke alarms around the house",
      "Test the smoke alarms round the house", "Check every alarm in the house still works",
      "MEDIUM", "PERSONAL",
      "The alarms round the house give a proper test beep, and the tired ones have been swapped out",
      [("Find the test button on each alarm in the house", 5),
       ("Press and hold each one and listen for the test tone", 10),
       ("Note down any that are weak, silent, or way past their replacement date", 10),
       ("Buy replacements for any that failed or are out of date", 20),
       ("Fit the new ones and retest", 15)]),

    G("The silicone round the bath's gone black and mouldy and it's been bugging me for a while",
      "Reseal round the bath", "Replace the mouldy silicone sealant round the bath",
      "MEDIUM", "PERSONAL",
      "The new seal looks clean and there's no gap for water to get behind it",
      [("Buy a mould-resistant sealant and a sealant removal tool", 15),
       ("Cut and peel out the old silicone round the bath", 25),
       ("Clean the gap and let it dry out", 30),
       ("Apply the new sealant in one smooth line and tape the edges first", 30),
       ("Leave it to cure and avoid using the bath till then", 5)]),

    G("It's that time of year again, the gutters need clearing before it gets properly wet next month",
      "Do the annual gutter clear", "Clear the gutters before autumn sets in",
      "MEDIUM", "PERSONAL",
      "Water runs freely through the gutters and downpipes when you test them with the hose",
      [("Check the weather and pick a dry, calm day to do it", 10),
       ("Set up the ladder on firm, level ground", 10),
       ("Scoop the leaves and debris out working along each run", 60),
       ("Flush the gutters and downpipes through with a hose", 20),
       ("Check the downpipes run clear at the bottom", 10)],
      due="next month"),

    G("The lawnmower needs its yearly service before the grass starts growing properly",
      "Service the lawnmower for the season", "Get the mower ready before the grass takes off",
      "LOW", "PERSONAL",
      "It starts on the first or second pull and leaves an even cut on the test strip",
      [("Check the fuel's not old, drain and refill if it's been sitting since autumn", 15),
       ("Clean under the deck and check the blade for nicks", 20),
       ("Sharpen or replace the blade if it's dull or damaged", 30),
       ("Check the air filter and spark plug, clean or replace as needed", 20),
       ("Start it up and test cut a strip of lawn", 15)]),
]

# ---------------------------------------------------------------------------
# Landlord-adjacent: reporting and following up on rental repairs
# ---------------------------------------------------------------------------
RENTAL = [
    G("The landlord still hasn't fixed the broken extractor fan, I reported it three weeks ago and they said they'd sort it by Friday",
      "Chase the landlord about the extractor fan", "Follow up on the unfixed bathroom extractor fan",
      "MEDIUM", "ADMIN",
      "The landlord's had a proper written chase and there's a date noted to follow up again if nothing happens",
      [("Check your tenancy agreement for what the landlord's responsible for", 15),
       ("Find your original report and check what date it was sent", 5),
       ("Send a follow-up message to the landlord referencing the first report", 15),
       ("Note a date to chase again if there's still no response", 5),
       ("Keep photos and messages together in case it drags on", 10)],
      due="by Friday"),

    G("The boiler in the rented flat's stopped working and I don't know if I'm meant to fix it or tell the landlord",
      "Sort out the broken boiler in the rented flat", "Work out what to do about the dead boiler",
      "URGENT", "ADMIN",
      "The landlord knows about it with the details you've already checked, and you've got a timeframe noted",
      [("Check the tenancy agreement for who's responsible for the boiler", 10),
       ("Try the basics: check the pressure gauge and see if it's just lost pressure", 10),
       ("If it's not a simple pressure top-up, don't open it up yourself, it's not DIY-safe", 5),
       ("Message the landlord with what you've checked and photos of the pressure gauge", 15),
       ("Ask for a timeframe and note it down", 5)]),

    G("There's mould creeping up the wall behind the wardrobe in the rented room and I need to sort it before it gets worse",
      "Deal with the mould in the rented room", "Clean the mould and get the landlord involved",
      "HIGH", "ADMIN",
      "The wall's clean for now and the landlord's aware in writing, with photos to back it up",
      [("Pull the wardrobe away from the wall and check how bad it is", 10),
       ("Wipe down the visible mould with a mould spray and ventilate the room", 20),
       ("Take photos of the affected wall before and after cleaning", 10),
       ("Report it to the landlord in writing, mentioning ventilation or damp as a possible cause", 15),
       ("Keep an eye on it over the next couple of weeks to see if it comes back", 10)]),

    G("The catch on one of the rented flat's windows is broken and I don't know if I'm allowed to just fix it myself or need the landlord",
      "Sort out the broken window catch in the rental", "Fix or report the broken window catch",
      "MEDIUM", "ADMIN",
      "The window shuts securely and the landlord knows it's been dealt with, whichever way it went",
      [("Check the tenancy agreement for what you're allowed to alter or repair", 10),
       ("Take a photo of the broken catch", 5),
       ("Message the landlord asking whether you can fix it or they'll send someone", 15),
       ("If they say go ahead, buy a matching replacement catch", 20),
       ("Fit it and let the landlord know it's sorted", 15)]),
]

GOLD: list[Gold] = (
    PLUMBING + ELECTRICAL + APPLIANCES + DOORS_WINDOWS + WALLS_FLOORS + OUTDOOR
    + SEASONAL + RENTAL
)
