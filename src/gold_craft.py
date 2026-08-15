"""Gold examples: making, hobbies and gardening.

Hands-on craft with real physical procedures: sewing, woodwork, pottery,
brewing, darkroom work, gardening, instruments. This domain exists because a
prior model was catastrophically bad at prerequisite order in the physical
world (it "fixed" a leaking tap without turning the water off first) — so
every example here keeps the genuine order a knowledgeable person would use:
wash and dry fabric before you cut it, let glue cure before you sand it back,
baste a quilt before you quilt it, harden seedlings off before they go in the
ground, cut rotten roots off a plant before you repot it.

It also leans hard into two things the app's users actually do: they mostly
rate these projects LOW or MEDIUM priority (a half-finished quilt is not
urgent, however guilty it feels), and they describe them with real
perfectionism and avoidance ("I keep buying wool and not starting").

See `goldlib.Gold` for the format and `quality.py` for the rules every
example must pass.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from goldlib import Gold

G = Gold

# ---------------------------------------------------------------------------
# Textiles — sewing, knitting, quilting, mending
# ---------------------------------------------------------------------------
TEXTILE = [
    G("Take up the hem on the new trousers before they just sit in the wardrobe unworn",
      "Take up the trouser hem", "Shorten the new trousers to the right length",
      "LOW", "CREATIVE",
      "The hem sits level and clears your shoes - the stitching doesn't have to be invisible",
      [("Try the trousers on with the shoes you'll wear them with and pin the new length", 15),
       ("Take them off and mark the fold with tailor's chalk or pins", 10),
       ("Press a fold along the marked line with the iron", 10),
       ("Sew the new hem by hand or machine", 30),
       ("Try them on again and check both legs match", 10)]),

    G("I keep buying wool and not starting the jumper - I think I'm just scared of getting the tension wrong",
      "Start the avoided jumper", "Swatch and cast on the jumper instead of buying more wool",
      "LOW", "CREATIVE",
      "There's real knitted fabric on the needles and the tension matches the pattern's gauge "
      "- a dropped stitch here and there is fine",
      [("Find the pattern and check the needle size and yarn amount it calls for", 10),
       ("Knit a swatch and measure the stitches against the gauge", 20),
       ("Change needle size and swatch again if the gauge is off", 20),
       ("Cast on the first piece following the pattern", 15),
       ("Knit a few evenings until the piece is properly underway", 90)]),

    G("The quilt has been half-finished in a bag for two years because I'm scared of ruining it, "
      "and my sister's baby is due any day",
      "Finish the quilt for the baby", "Finish piecing, quilting and binding the half-made quilt",
      "HIGH", "CREATIVE",
      "It's a usable blanket-sized quilt that holds together in the wash - the quilting doesn't need to be even",
      [("Get the bag out and lay out what's already pieced", 15),
       ("Finish piecing whatever blocks are still missing", 60),
       ("Layer the top, wadding and backing and baste them together", 45),
       ("Quilt the layers, straight lines are fine", 90),
       ("Trim the edges and sew on the binding", 60)]),

    G("Darn the moth holes in my favourite jumper instead of throwing it out",
      "Darn the moth-eaten jumper", "Darn the holes so the jumper is wearable again",
      "LOW", "CREATIVE",
      "The holes are closed and it holds together in the wash - the darning doesn't have to be invisible",
      [("Turn the jumper inside out and find all the holes", 10),
       ("Trim any loose threads around each hole", 10),
       ("Weave a darning patch across each hole with matching wool", 40),
       ("Turn it right side out and check nothing pulls", 10)]),
]

# ---------------------------------------------------------------------------
# Wood and furniture — the domain where surface-prep ordering matters most
# ---------------------------------------------------------------------------
WOOD = [
    G("Build a bookshelf from timber for the alcove instead of buying another flat-pack one",
      "Build the alcove bookshelf", "Build and fit a timber bookshelf for the alcove",
      "MEDIUM", "CREATIVE",
      "It stands square in the alcove and holds books without flexing - the joints don't need to be cabinetmaker-tight",
      [("Measure the alcove and sketch the shelf dimensions", 15),
       ("Buy the timber, cut roughly to size at the yard", 30),
       ("Cut the pieces to their final lengths", 45),
       ("Sand the cut edges smooth", 30),
       ("Glue and screw the frame together", 60),
       ("Fix the finished shelf into the alcove", 30)]),

    G("The chair from the flea market still needs stripping and revarnishing - it's been sitting in the shed since spring",
      "Strip and revarnish the flea-market chair", "Strip the old finish and revarnish the chair",
      "MEDIUM", "CREATIVE",
      "The chair is sealed and safe to sit on without wobbling - a few brush marks are fine",
      [("Take the chair outside onto dust sheets somewhere ventilated", 10),
       ("Apply stripper to the old varnish and scrape it off once it bubbles", 45),
       ("Sand the bare wood smooth, working through the grits", 60),
       ("Wipe off the dust with a tack cloth", 10),
       ("Apply the first coat of varnish and let it dry", 40),
       ("Sand lightly between coats and apply the final coat", 35)]),

    G("The model kit's been in its box since my birthday - actually build it this weekend",
      "Build the model kit", "Assemble and paint the model kit instead of leaving it boxed",
      "MEDIUM", "CREATIVE",
      "It's assembled and painted enough to display - visible glue lines don't matter",
      [("Clear a table and lay out the sprues and instructions", 10),
       ("Cut the pieces from the sprues and dry-fit the main sections", 30),
       ("Glue the main assembly together and let it set", 45),
       ("Sand any rough seams once the glue has fully cured", 20),
       ("Paint the main colours, letting each dry before masking the next", 60),
       ("Add the final details and seal with a light varnish coat", 30)]),

    G("Upcycle the old dresser instead of taking it to the tip",
      "Upcycle the old dresser", "Prep and paint the dresser instead of throwing it out",
      "MEDIUM", "CREATIVE",
      "It's painted and the drawers still run smoothly - brush marks are part of the charm",
      [("Take the handles off and clean the dresser down", 15),
       ("Sand the furniture to key the surface for paint", 40),
       ("Fill any dents or gaps and sand them flush", 25),
       ("Apply a coat of primer and let it dry", 40),
       ("Paint two topcoats, sanding lightly between them", 60),
       ("Wax or seal the finish and refit the handles", 25)]),

    G("Build a birdhouse from the leftover fence timber",
      "Build a birdhouse", "Build and hang a simple birdhouse from scrap timber",
      "LOW", "CREATIVE",
      "It's put together solidly enough to survive outside and has a hole the right size - rough-cut edges are fine",
      [("Mark the cutting lines on the timber from the plan", 10),
       ("Cut the pieces to size", 30),
       ("Drill the entrance hole and ventilation gaps", 15),
       ("Screw or nail the box together, leaving one side hinged for cleaning", 40),
       ("Hang it somewhere sheltered out of direct sun", 15)]),

    G("Sand and revarnish the dining table, the top's gone dull and water-marked",
      "Sand and revarnish the dining table", "Strip back the dull, water-marked finish and revarnish the tabletop",
      "MEDIUM", "CREATIVE",
      "The top is smooth and sealed with an even sheen from normal viewing distance - a faint mark under raking light is fine",
      [("Clear the table and cover the surrounding floor", 10),
       ("Sand the tabletop back through the grits until the marks are gone", 60),
       ("Wipe away the dust with a tack cloth", 10),
       ("Apply the first coat of varnish thinly and let it dry", 45),
       ("Sand lightly between coats and apply the final coat", 40)]),
]

# ---------------------------------------------------------------------------
# Garden — most of the seasonal, prerequisite-heavy physical work lives here
# ---------------------------------------------------------------------------
GARDEN = [
    G("Lay the patio in the back garden before the summer gets away from us",
      "Lay the back garden patio", "Prepare the base and lay the patio slabs",
      "HIGH", "PERSONAL",
      "The patio is laid and doesn't rock underfoot - a few uneven joints are fine",
      [("Mark out the patio area and check it slopes away from the house", 15),
       ("Dig out the area to the right depth for the sub-base", 120),
       ("Compact a sub-base of hardcore and add a layer of sand", 90),
       ("Lay the slabs on mortar, checking each one with a spirit level", 180),
       ("Point the joints between the slabs once they've set", 60)]),

    G("The vegetable seedlings have gone leggy on the windowsill and need to get in the ground "
      "before they're beyond saving",
      "Plant out the leggy seedlings",
      "Harden off and plant the seedlings into the vegetable bed before they're past saving",
      "HIGH", "PERSONAL",
      "The seedlings are in the ground and upright - losing a few of the weaker ones is fine",
      [("Check the bed is weeded and the soil is workable", 15),
       ("Put the seedlings outside in a sheltered spot for a few hours to start hardening off", 15),
       ("Increase their time outside over the next couple of days", 30),
       ("Water the bed well before planting", 15),
       ("Plant them out at the right spacing and water them in", 45)]),

    G("Prune the fruit trees while they're still dormant",
      "Prune the dormant fruit trees", "Prune the apple and pear trees before they break bud",
      "LOW", "PERSONAL",
      "The trees have an open shape with the crossing branches gone - it doesn't need show-garden symmetry",
      [("Clean and sharpen the secateurs and loppers", 15),
       ("Stand back and look at each tree's shape before cutting anything", 10),
       ("Remove dead, damaged or crossing branches first", 30),
       ("Shape the remaining branches to open up the centre", 40),
       ("Clear the prunings away and check the cuts are clean", 20)]),

    G("Build a compost heap instead of putting kitchen scraps in the bin",
      "Build the compost heap", "Set up a compost heap or bin for garden and kitchen waste",
      "LOW", "PERSONAL",
      "There's a working heap taking scraps and garden waste - it doesn't need to be tidy",
      [("Pick a level spot, ideally in some shade", 10),
       ("Build or position the bin, with airflow at the base", 20),
       ("Lay a base layer of twigs or coarse material for drainage", 15),
       ("Add a mix of green and brown waste to get it started", 20)]),

    G("The orchid's roots are rotting in waterlogged compost and it needs repotting before it's beyond saving",
      "Repot the dying orchid", "Repot the orchid into fresh, better-draining compost",
      "HIGH", "PERSONAL",
      "The orchid is in fresh compost with the mushy roots gone - a few limp leaves can be left to recover on their own",
      [("Ease the orchid out of its pot and shake off the old compost", 15),
       ("Cut away any soft, mushy roots with clean scissors", 15),
       ("Rinse the remaining healthy roots", 10),
       ("Repot into fresh orchid compost in a pot with drainage holes", 20),
       ("Water lightly and put it somewhere with indirect light", 10)]),

    G("Build a raised bed for the garden before it's too late to get anything planted this year",
      "Build the raised bed", "Build and fill a raised bed ready for planting",
      "MEDIUM", "PERSONAL",
      "It's built, filled and ready to plant into - a slightly wonky corner is fine",
      [("Mark out the spot and check it gets enough sun", 15),
       ("Cut the timber to length for the sides", 40),
       ("Screw the frame together and level it in place", 45),
       ("Line the base with cardboard to suppress the grass beneath", 15),
       ("Fill it with topsoil and compost", 60)]),

    G("Take cuttings from the neighbour's plant before I forget again",
      "Propagate the cuttings", "Take and pot on cuttings from the neighbour's plant",
      "LOW", "PERSONAL",
      "The cuttings are potted and not wilting - losing one or two is normal",
      [("Ask for a few cuttings and snip them just below a leaf node", 15),
       ("Strip the lower leaves and dip the cut ends in rooting hormone", 10),
       ("Pot them into free-draining compost", 15),
       ("Water them in and cover loosely with a clear bag to keep humidity up", 10)]),

    G("Varnish the garden fence before the wood starts going grey",
      "Varnish the garden fence", "Clean and revarnish the garden fence panels",
      "MEDIUM", "PERSONAL",
      "The fence is coated and the colour is even from a normal viewing distance - a missed sliver at the base is fine",
      [("Sweep off loose dirt and check the fence is dry", 15),
       ("Brush or wash off any algae and let it dry fully", 30),
       ("Sand any rough or flaking patches", 30),
       ("Apply the first coat of fence varnish", 60),
       ("Apply a second coat once the first has dried", 60)]),
]

# ---------------------------------------------------------------------------
# Studio and darkroom — pottery, brewing, film, video, framing, printmaking,
# baking as decoration rather than food
# ---------------------------------------------------------------------------
STUDIO = [
    G("Finally use the pottery wheel that's been gathering dust in the garage and throw a bowl",
      "Throw and glaze a pottery bowl", "Throw a bowl on the wheel and glaze it once fired",
      "MEDIUM", "CREATIVE",
      "The bowl holds water and sits flat on the table - a slightly uneven rim is fine",
      [("Wedge the clay to knock the air bubbles out", 15),
       ("Centre and throw the bowl shape on the wheel", 30),
       ("Trim the base once it's leather-hard and firm enough to handle", 25),
       ("Let it dry out fully before the first firing", 20),
       ("Glaze it once it's back from the bisque fire", 30)]),

    G("Brew a batch of beer - the kit's been sitting unopened since Christmas",
      "Brew the beer kit", "Brew, ferment and bottle a batch of beer from the kit",
      "MEDIUM", "CREATIVE",
      "It ferments out and tastes drinkable - it doesn't need to taste like a brewery's",
      [("Clean and sanitise the brewing equipment", 15),
       ("Boil the malt extract with the hops for the bittering addition", 60),
       ("Cool the wort quickly and pour it into the fermenter with the yeast", 30),
       ("Leave it somewhere at a steady temperature to start fermenting", 15),
       ("Check the gravity reading and bottle it once fermentation has finished", 60)]),

    G("Develop the roll of black and white film that's been sitting in the camera for months",
      "Develop the black and white film", "Develop and dry the roll of black and white film",
      "MEDIUM", "CREATIVE",
      "The negatives are developed and you can see the frames against the light - a stray water mark won't ruin them",
      [("Gather the developing chemicals, tank and changing bag", 10),
       ("Load the film onto the reel inside the changing bag or darkroom", 20),
       ("Mix the chemicals to the right dilution and temperature", 15),
       ("Develop, stop and fix the film through the timed steps", 25),
       ("Wash and hang the film to dry", 20)]),

    G("Edit the holiday video before everyone's asking to see it and I keep putting it off",
      "Edit the holiday video", "Cut the holiday footage into a video people can actually watch",
      "MEDIUM", "CREATIVE",
      "There's a video that plays start to finish and captures the trip - plenty of clips can be left out",
      [("Import the clips onto the computer and back them up", 15),
       ("Watch through and note the timestamps worth using", 45),
       ("Cut a rough sequence in order, without polishing anything yet", 60),
       ("Add music and trim the cuts to the beat", 45),
       ("Export a version and watch it back on a bigger screen", 30)]),

    G("Frame the prints that have been rolled up in a tube for a year",
      "Frame the rolled-up prints", "Flatten and frame the prints that have been sitting in a tube",
      "LOW", "CREATIVE",
      "The prints are flat and hanging on the wall - a slightly off-centre mount is fine",
      [("Weight the prints flat under some books for a day to lose the curl", 10),
       ("Buy frames and mounts in the right sizes", 15),
       ("Cut the mounts to size and position the prints behind them", 30),
       ("Fit the prints into the frames and hang them", 25)]),

    G("Try lino-cut printmaking - I bought the kit ages ago and never opened it",
      "Try lino-cut printmaking", "Carve and pull a first lino print",
      "LOW", "CREATIVE",
      "There's a printed image you can recognise on paper - rough edges are part of the look",
      [("Sketch a simple design and transfer it onto the lino", 15),
       ("Carve away the areas that should stay white", 45),
       ("Roll out ink evenly on a plate or tile", 10),
       ("Ink the lino and pull a test print", 15),
       ("Adjust the carving and pull a few more prints", 40)]),

    G("Decorate the birthday cake - the party's this weekend and I still haven't started",
      "Decorate the birthday cake", "Bake, fill and decorate the cake for the party",
      "HIGH", "CREATIVE",
      "It tastes good and looks homemade rather than shop-bought - a wonky edge doesn't matter",
      [("Check the recipe and make sure you have the tins and ingredients", 15),
       ("Bake the sponges and let them cool completely before touching them", 75),
       ("Make the buttercream or filling", 30),
       ("Fill and crumb-coat the cake, then chill it", 30),
       ("Add the final coat of icing and decorate it", 60)]),
]

# ---------------------------------------------------------------------------
# Music, drawing, bikes, and the kitchen drawer of blunt knives
# ---------------------------------------------------------------------------
OTHER = [
    G("Restore the old bicycle that's been rusting in the shed since we moved in",
      "Restore the shed bicycle", "Strip, clean and rebuild the rusted bicycle",
      "HIGH", "CREATIVE",
      "It's rideable and stops safely - a few scuffs on the paint are fine",
      [("Wipe it down and take photos before taking anything apart", 15),
       ("Strip off the wheels, brakes and gears", 45),
       ("Clean the rust off the frame and treat any bare metal", 60),
       ("Clean, regrease and reassemble the moving parts", 90),
       ("Fit new brake pads and cables where the old ones are worn", 40),
       ("Test the brakes and gears on a short ride before going further", 20)]),

    G("Learn the piano piece for the recital - I can barely get through the first page",
      "Learn the recital piano piece", "Get the piece performance-ready for the recital",
      "MEDIUM", "LEARNING",
      "You can play it through without stopping, even if a few notes are shaky",
      [("Play through the first page slowly, marking the tricky bars", 15),
       ("Practise the tricky bars hands separately until they're steady", 30),
       ("Put hands together on the first page at a slow tempo", 30),
       ("Learn the rest of the piece the same way, page by page", 120),
       ("Play it through start to finish at a slower tempo than the target", 20)]),

    G("Take up drawing again - I haven't picked up a pencil in years",
      "Start drawing again", "Actually start drawing again instead of just thinking about it",
      "LOW", "CREATIVE",
      "Pencil has gone on paper and you sat with it for a while - the drawings don't need to be good",
      [("Get the sketchbook and pencils out somewhere you'll actually sit", 10),
       ("Do a few loose warm-up sketches of whatever is in front of you", 20),
       ("Spend a longer stretch on one drawing without rubbing out mistakes", 45),
       ("Leave the sketchbook out so it's easy to pick up again tomorrow", 5)]),

    G("Restring the guitar, the strings have gone dead",
      "Restring the guitar", "Replace the old strings and tune it back up",
      "LOW", "CREATIVE",
      "It's back in tune and holds pitch after a few minutes of playing - a slightly rough setup is fine",
      [("Loosen and remove the old strings one at a time", 10),
       ("Wipe down the fretboard while it's exposed", 10),
       ("Fit the new strings and wind them on", 20),
       ("Tune it up and stretch the strings to help them settle", 15)]),

    G("Sharpen the kitchen knives, they're barely cutting tomatoes anymore",
      "Sharpen the kitchen knives", "Get an edge back on the kitchen knives",
      "LOW", "PERSONAL",
      "The knives cut a tomato cleanly without sawing - a mirror edge isn't the point",
      [("Get the whetstone or sharpener out and soak the stone if it needs it", 10),
       ("Find the existing bevel angle on the first knife", 10),
       ("Draw the blade across the stone at a steady angle, both sides", 20),
       ("Strop or hone the edge to remove the burr", 10),
       ("Test on a tomato and repeat for the rest of the knives", 20)]),
]

GOLD: list[Gold] = TEXTILE + WOOD + GARDEN + STUDIO + OTHER
