"""Gold examples: food, cooking and hosting (second slice).

`gold_core.py` already covers weekly meal planning, batch-cooking lunches, a
birthday cake, and learning three dishes. This module covers the rest of the
domain: hosting occasions with real stakes (a dinner for six, Christmas
dinner cooked for the first time, catering round a serious allergy), the
physical procedures that have a real prerequisite order (bread that has to
prove before it bakes, jars that have to be sterilised before they're filled,
meat that has to defrost and marinate before it hits the grill, stock that
has to cool before it's frozen), and the unglamorous everyday version of
feeding people (budget weeks, packed lunches, a veg box nobody keeps up with).

See `goldlib.Gold` for the format and `quality.py` for the rules every
example must pass.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from goldlib import Gold

G = Gold

# ---------------------------------------------------------------------------
# Hosting — dinners with real stakes: numbers, allergies, people to impress
# ---------------------------------------------------------------------------
HOSTING = [
    G("Hosting a dinner for six on Saturday and I've never cooked for that many people before",
      "Host the dinner for six", "Cook and serve a sit-down dinner for six guests",
      "HIGH", "PERSONAL",
      "Everyone's fed, the timing didn't fall apart, and you got to sit down for most of it",
      [("Decide the menu, keeping at least one course fully make-ahead", 15),
       ("Write the shopping list and do the big shop", 60),
       ("Prep whatever can be made a day ahead and get it in the fridge", 90),
       ("Cook the parts that need last-minute attention", 60),
       ("Lay the table and serve", 20)],
      due="on Saturday"),

    G("Having friends round for dinner next month, want to actually enjoy it instead of stressing in the kitchen all evening",
      "Have friends round for dinner", "Cook dinner for friends without spending the evening in the kitchen",
      "MEDIUM", "PERSONAL",
      "You spent most of the evening at the table with everyone instead of at the stove",
      [("Pick a menu where most of it can be prepped ahead", 15),
       ("Shop for everything a couple of days before", 45),
       ("Prep the make-ahead parts the day before", 60),
       ("Finish the last-minute bits once everyone's arrived", 40)],
      due="next month"),

    G("Friend with a severe nut allergy is coming for dinner tonight and I want to get this right",
      "Cook dinner for a friend with a severe nut allergy", "Cater safely for a guest with a severe nut allergy",
      "URGENT", "PERSONAL",
      "She's eaten safely and you didn't have to guess about anything on her plate",
      [("Ask her directly what she can't have and how severe it is", 10),
       ("Plan a menu that's naturally free of it rather than working round it", 15),
       ("Shop, reading every label instead of assuming", 40),
       ("Use a separate board and utensils for her food", 10),
       ("Cook her plate first, before anything else touches the kitchen", 30)],
      due="tonight"),

    G("Cooking a dinner party where one guest has a serious dairy allergy and I don't want to mess it up",
      "Cater the dinner party for a guest with a dairy allergy", "Plan and cook a dinner party safely for a guest with a serious dairy allergy",
      "MEDIUM", "PERSONAL",
      "Everyone ate the same meal and nothing on her plate came near dairy",
      [("Ask her exactly what to avoid and how strict she needs it", 10),
       ("Plan a menu that's naturally free of dairy for the whole table", 20),
       ("Shop, checking labels rather than assuming a product is safe", 35),
       ("Cook it through, keeping dairy out of every pan and utensil", 30),
       ("Plate hers first and label it before serving the rest", 15)]),

    G("Cooking a dinner to impress for our anniversary, want it to actually go well this time",
      "Cook a dinner to impress for the anniversary", "Cook an ambitious dinner to mark an anniversary",
      "HIGH", "PERSONAL",
      "The food came out well and you got to enjoy the evening instead of firefighting in the kitchen",
      [("Pick a menu with nothing you haven't cooked before", 15),
       ("Do a full shop a day ahead so nothing's missing", 45),
       ("Prep everything that can be done in advance the day before", 90),
       ("Cook the parts that need last-minute attention while you can focus", 60),
       ("Plate it up and serve while it's hot", 15)]),

    G("Want to cook something properly impressive for the in-laws coming Saturday, first time hosting them",
      "Cook an impressive dinner for the in-laws", "Cook an ambitious dinner for the in-laws' first visit",
      "HIGH", "PERSONAL",
      "The meal came together without a last-minute scramble and you got to sit at the table instead of hiding in the kitchen",
      [("Choose a menu that's ambitious but within what you can actually pull off", 15),
       ("Shop for everything, including a backup for anything niche", 45),
       ("Prep the parts that can be made ahead the day before", 75),
       ("Work out a timing plan for the day so nothing's cold", 15),
       ("Cook and plate it, working backwards from serving time", 60)],
      due="Saturday"),
]

# ---------------------------------------------------------------------------
# Occasions — Christmas, a kid's birthday party, a big barbecue
# ---------------------------------------------------------------------------
OCCASIONS = [
    G("Cooking Christmas dinner for the whole family tomorrow and I've never done a turkey before, panicking about the timings",
      "Cook the first Christmas dinner", "Cook Christmas dinner for the family for the first time, turkey included",
      "URGENT", "PERSONAL",
      "Everything's cooked through and lands on the table at roughly the same time",
      [("Work out the oven timings backwards from when you want to eat", 15),
       ("Prep the vegetables and stuffing tonight so tomorrow isn't a scramble", 60),
       ("Get the turkey into the oven first thing, timed off its weight", 20),
       ("Get the potatoes and vegetables timed to finish with the turkey", 45),
       ("Rest the turkey properly before carving", 20),
       ("Make gravy from the tin juices while it rests", 15)],
      due="tomorrow"),

    G("Hosting a vegetarian option alongside Christmas dinner next week for a guest who doesn't eat meat, want it to feel like a proper part of the meal not an afterthought",
      "Plan a vegetarian Christmas main", "Cook a proper vegetarian main to go alongside Christmas dinner",
      "MEDIUM", "PERSONAL",
      "There's a hot vegetarian main that isn't just the side vegetables on a plate",
      [("Ask what she actually likes rather than guessing", 10),
       ("Pick a vegetarian main that can be prepped ahead", 15),
       ("Shop for it alongside the usual Christmas shop", 30),
       ("Prep what can be done the day before", 40),
       ("Cook it to finish alongside the rest of the meal", 30)],
      due="next week"),

    G("Sorting the food for my son's 6th birthday party, fifteen kids coming on Saturday",
      "Sort the food for the birthday party", "Plan and prepare food for a children's birthday party",
      "HIGH", "PERSONAL",
      "There's enough simple food out that no one's hungry and nothing needs last-minute rescuing",
      [("Check with the other parents for any allergies first", 15),
       ("Plan a simple finger-food menu that doesn't need cutlery", 20),
       ("Shop for everything", 45),
       ("Prep whatever can be made the day before", 60),
       ("Set it all out once the party starts", 20)],
      due="on Saturday"),

    G("Doing the food for my daughter's birthday party at home next weekend, want it easy rather than Pinterest-perfect",
      "Do the birthday party food", "Prepare food for a children's birthday party at home",
      "MEDIUM", "PERSONAL",
      "Everyone's fed something they'll actually eat and you weren't stuck in the kitchen the whole time",
      [("Ask around for any allergies among the kids coming", 10),
       ("Pick a short menu of things kids actually eat", 15),
       ("Shop for it a couple of days ahead", 30),
       ("Prep what freezes or keeps overnight the day before", 45),
       ("Lay it out once everyone arrives", 15)],
      due="next weekend"),

    G("Doing a barbecue for twenty people at the weekend, more food than I've ever cooked outdoors",
      "Cook the barbecue for twenty", "Plan, prep and cook a barbecue for twenty people",
      "HIGH", "PERSONAL",
      "Everyone's fed and nothing came off the grill raw or stone cold",
      [("Work out quantities for twenty and write the shopping list", 15),
       ("Shop for the food plus enough charcoal or gas", 45),
       ("Marinate the meat the day before", 20),
       ("Get the barbecue cleaned and preheated before anyone arrives", 30),
       ("Cook it in batches, keeping cooked food warm while the rest finishes", 90)],
      due="at the weekend"),

    G("Hosting a big barbecue for the extended family next month, twenty-odd people",
      "Host the family barbecue", "Plan and cook a barbecue for the extended family",
      "MEDIUM", "PERSONAL",
      "There's enough food including a proper vegetarian option and nothing's still raw in the middle",
      [("Confirm numbers and check for any dietary needs", 15),
       ("Plan a menu that covers meat and a decent vegetarian option", 20),
       ("Defrost anything frozen well ahead of the day", 15),
       ("Shop and marinate what needs it the day before", 45),
       ("Preheat the barbecue and get the sides ready", 30),
       ("Cook in batches, keeping everything warm as it comes off", 90)],
      due="next month"),
]

# ---------------------------------------------------------------------------
# Baking — bread that has to prove before it bakes, a cake for an occasion
# ---------------------------------------------------------------------------
BAKING = [
    G("Finally making a proper loaf of bread from scratch instead of always using the bread maker",
      "Bake a proper loaf of bread from scratch", "Make and bake a loaf of bread by hand from scratch",
      "MEDIUM", "CREATIVE",
      "It's risen properly, holds together when sliced, and tastes better than shop bread",
      [("Weigh out the flour, water, yeast and salt", 10),
       ("Mix and knead the dough properly", 15),
       ("Let it prove somewhere warm until it's doubled in size", 90),
       ("Knock it back and shape the loaf", 15),
       ("Prove it again briefly before it goes in", 30),
       ("Bake it until it sounds hollow when tapped", 35)]),

    G("Want to get into sourdough properly, tired of buying it every week",
      "Start making sourdough bread", "Build a starter and bake a first sourdough loaf",
      "LOW", "CREATIVE",
      "You've got a loaf out of the oven that actually rose, even if the shaping is rough",
      [("Feed the starter daily until it's reliably doubling", 15),
       ("Mix the dough and let it rest before working it", 20),
       ("Stretch and fold the dough every half hour over a few hours", 45),
       ("Shape it and prove it in the fridge overnight", 30),
       ("Bake it in a hot pot with the lid on", 45)]),

    G("Decorating a cake for my parents' 40th wedding anniversary and want it to look properly done",
      "Decorate the anniversary cake", "Bake, fill and decorate a cake for a wedding anniversary",
      "HIGH", "CREATIVE",
      "It tastes good and looks properly finished, even if the piping isn't dead straight",
      [("Check the recipe and confirm you have the right tins", 15),
       ("Bake the sponges and let them cool completely", 75),
       ("Make the buttercream or ganache", 25),
       ("Level, fill and crumb-coat it, then chill", 30),
       ("Add the final coat and decorate it", 60)]),

    G("First time doing a naked cake for a friend's engagement party and I'm nervous about it",
      "Make the naked cake for the engagement party", "Bake and assemble a naked cake for an engagement party",
      "LOW", "CREATIVE",
      "The layers are stacked straight and the filling shows through evenly enough to look intentional",
      [("Pick a simple design that actually suits a naked finish", 15),
       ("Bake the layers and let them cool fully", 75),
       ("Make the filling and stack the layers", 30),
       ("Apply a thin final layer so the sponge still shows through", 20),
       ("Decorate with fruit or flowers just before it needs to travel", 20)]),
]

# ---------------------------------------------------------------------------
# Preserving — jars that have to be sterilised before they're filled
# ---------------------------------------------------------------------------
PRESERVING = [
    G("Tomato plants have gone mad and I don't want them all rotting on the vine",
      "Use up the tomato glut", "Turn a glut of tomatoes into a sauce before they spoil",
      "MEDIUM", "PERSONAL",
      "The ripe ones are picked and turned into something you can actually use, even if a few soft ones get binned",
      [("Pick the ripe tomatoes before they split", 15),
       ("Wash and sort them, setting aside any that are past it", 15),
       ("Sterilise the jars while the sauce cooks down", 20),
       ("Cook the tomatoes down into a sauce", 60),
       ("Ladle it into the sterilised jars while hot and seal", 20)]),

    G("Need to freeze and jar the tomato glut from the allotment before they all turn at once",
      "Freeze and jar the tomato glut", "Preserve a large glut of tomatoes by freezing some and jarring the rest",
      "HIGH", "PERSONAL",
      "Most of the glut is dealt with one way or another instead of rotting on the side",
      [("Sort which tomatoes go in the freezer whole and which get cooked down", 15),
       ("Wash and freeze the ones going straight in", 20),
       ("Sterilise jars for the rest", 20),
       ("Cook the rest down into a sauce", 60),
       ("Jar it while hot and seal", 20)],
      due="before they all turn at once"),

    G("Make proper stock from the chicken carcass instead of just binning it",
      "Make chicken stock from the carcass", "Turn a leftover chicken carcass into proper stock",
      "MEDIUM", "PERSONAL",
      "There's stock in the freezer that tastes like something, not just seasoned water",
      [("Save the carcass and any vegetable scraps instead of binning them", 5),
       ("Put them in a pot with water and bring it to a simmer", 10),
       ("Simmer it low for a few hours, skimming the fat off", 45),
       ("Strain it and let it cool before doing anything else with it", 20),
       ("Portion it into containers or bags and freeze", 15)]),

    G("Learn to make a proper vegetable stock instead of always reaching for the cubes",
      "Make vegetable stock from scratch", "Make a batch of vegetable stock instead of using cubes",
      "LOW", "PERSONAL",
      "There's a batch of stock in the freezer that actually tastes of something",
      [("Save vegetable peelings and offcuts in the freezer until there's enough", 10),
       ("Put them in a pot with water and simmer gently", 15),
       ("Strain out the solids", 10),
       ("Let it cool before portioning it into the freezer", 20)]),

    G("Try fermenting vegetables properly, I keep meaning to and never start",
      "Ferment a first batch of vegetables", "Make a first batch of fermented vegetables from scratch",
      "MEDIUM", "CREATIVE",
      "There's a jar actively fermenting on the side and it tastes right when you check it",
      [("Pick a simple first ferment like sauerkraut", 15),
       ("Wash and shred the vegetables", 20),
       ("Weigh out the right ratio of salt", 10),
       ("Sterilise a jar and pack it tightly under its own brine", 25),
       ("Check it daily and burp the jar until it tastes right", 15)]),

    G("Get into fermenting properly and make my own kimchi instead of buying it",
      "Make a batch of kimchi", "Make a first batch of kimchi from scratch",
      "MEDIUM", "CREATIVE",
      "There's kimchi fermenting on the side that tastes properly sour when you check it",
      [("Read up on a basic kimchi recipe", 15),
       ("Buy the napa cabbage and other ingredients", 25),
       ("Salt the cabbage and let it wilt down", 40),
       ("Sterilise a jar large enough for it", 15),
       ("Mix the paste and pack it tightly into the jar", 30),
       ("Leave it out to ferment, tasting it every couple of days", 15)]),
]

# ---------------------------------------------------------------------------
# The Sunday roast
# ---------------------------------------------------------------------------
ROAST = [
    G("Do a proper Sunday roast for the family this weekend",
      "Cook the Sunday roast", "Cook a full Sunday roast for the family",
      "MEDIUM", "PERSONAL",
      "Everything landed on the table roughly together and hot",
      [("Season the meat and prep the vegetables", 15),
       ("Get the meat into the oven with enough time before anything else goes in", 60),
       ("Get the potatoes and vegetables roasting, timed to finish together", 45),
       ("Rest the meat before carving", 15),
       ("Make gravy from the pan juices while it rests", 15)],
      due="this weekend"),

    G("Get back into doing a Sunday roast every week instead of always ordering in",
      "Start a weekly Sunday roast habit", "Get back into cooking a Sunday roast most weeks",
      "LOW", "PERSONAL",
      "You've cooked one properly and have a rough plan for doing it again next week",
      [("Plan a simple rotation of three roasts you actually like", 15),
       ("Do a shop for the first one", 45),
       ("Cook it properly, timing the sides to finish with the meat", 90),
       ("Rest the meat, carve it and keep any leftovers for the week", 20)]),
]

# ---------------------------------------------------------------------------
# Everyday cooking — budget weeks, packed lunches, a veg box, a cookbook,
# curry made properly instead of from a jar
# ---------------------------------------------------------------------------
EVERYDAY = [
    G("Kids' packed lunches keep coming home a soggy mess by lunchtime and I want to actually sort it",
      "Fix the soggy packed lunches", "Work out why packed lunches are soggy by lunchtime and fix it",
      "MEDIUM", "HEALTH",
      "A trial lunch came home in decent shape at the end of the day",
      [("Work out what's actually going wrong - the containers or the ingredients", 15),
       ("Buy proper insulated containers and an ice pack", 30),
       ("Pack wet and dry things in separate containers", 15),
       ("Do a trial pack and check how it's held up by the end of the day", 15)]),

    G("Sort out my own packed lunch so it's not a soggy sandwich by midday",
      "Fix my own packed lunch", "Set up a packed lunch routine that survives to midday",
      "LOW", "HEALTH",
      "Lunch is still in decent shape when you actually get to eat it",
      [("Buy a proper lunch box with separate compartments", 15),
       ("Batch prep a few days of fillings at the weekend", 45),
       ("Pack it the night before instead of in the morning rush", 10),
       ("Keep an ice pack in the freezer ready to grab", 5)]),

    G("Feed us properly this week on a tight budget, money's tight until payday",
      "Feed the household on a tight budget this week", "Plan and cook a week of meals on a tight budget",
      "MEDIUM", "PERSONAL",
      "There's a meal planned for most nights and the shop didn't blow the budget",
      [("Check what's already in the cupboards and freezer", 15),
       ("Plan meals around that plus a few cheap staples", 20),
       ("Write a list and do one shop, sticking to it", 60),
       ("Batch cook the cheaper meals so nothing goes to waste", 60)],
      due="until payday"),

    G("Cut the food bill down properly instead of just complaining about it every week",
      "Cut down the food bill", "Change how the household shops and cooks to cut the food bill",
      "LOW", "PERSONAL",
      "This week's shop cost less than the last few and nothing important got missed",
      [("Track what actually got bought and thrown out last week", 15),
       ("Plan meals around what's on offer and what's already in", 25),
       ("Do one proper shop instead of several top-up trips", 60),
       ("Batch cook a couple of meals to stretch the cheaper ingredients", 60)]),

    G("Half of every veg box goes to waste and I'm sick of throwing money away",
      "Stop wasting the veg box", "Use up a vegetable box properly instead of letting it spoil",
      "MEDIUM", "PERSONAL",
      "Most of this week's box got eaten or frozen instead of binned",
      [("Check what's actually in this week's box before anything wilts", 10),
       ("Plan meals around the box first, buying round it rather than the other way", 20),
       ("Cook whatever spoils fastest first", 45),
       ("Freeze whatever won't get used in time", 15)]),

    G("Use up the veg box properly instead of it turning to compost every week",
      "Use up the veg box before it spoils", "Get into the habit of using up a vegetable box before it spoils",
      "LOW", "PERSONAL",
      "This week's box got used up instead of composted",
      [("Sort the box into what spoils fast and what keeps", 10),
       ("Cook the fast-spoiling stuff first in whatever's for dinner", 30),
       ("Turn anything left over by midweek into a soup or stew", 45),
       ("Freeze portions of that for later", 15)]),

    G("Was given a cookbook for Christmas and it's just sat on the shelf, want to actually cook from it",
      "Actually cook from the cookbook", "Work through a cookbook that's been sitting unused",
      "LOW", "PERSONAL",
      "You've cooked a few recipes from it properly rather than it just sitting there",
      [("Flick through it and mark five recipes that actually appeal", 15),
       ("Check which ingredients you don't already have", 10),
       ("Cook the first one, following it properly", 60),
       ("Cook a second one the same week", 60),
       ("Keep going until most of the marked recipes are done", 90)]),

    G("Actually work through the cookbook mum gave me instead of it gathering dust",
      "Work through mum's cookbook", "Cook a run of recipes from a cookbook given as a gift",
      "MEDIUM", "PERSONAL",
      "You've cooked several recipes from it and have a couple of new favourites",
      [("Go through it and flag the recipes that actually appeal", 15),
       ("Check what's missing from the cupboard for the first few", 15),
       ("Cook one a week rather than trying to do it all at once", 60),
       ("Note which ones are worth repeating", 10)]),

    G("Make a proper curry from scratch instead of always reaching for the jar",
      "Make curry from scratch", "Cook a curry from scratch using whole spices instead of a jar",
      "MEDIUM", "CREATIVE",
      "It tastes properly of the spices you used, not like the jar",
      [("Check what spices are already in the cupboard against the recipe", 10),
       ("Buy what's missing, including anything you need whole", 25),
       ("Toast and grind the whole spices", 15),
       ("Fry the onion, garlic and ginger properly until it's softened right down", 20),
       ("Build the sauce and let it cook down slowly", 30),
       ("Add the meat or vegetables and simmer until it's done", 35)]),

    G("Learn to make a curry that doesn't taste like the jar, sick of relying on it",
      "Learn to make curry properly", "Learn a scratch-made curry recipe well enough to repeat it",
      "LOW", "CREATIVE",
      "You've made it twice without needing the recipe open the whole way through",
      [("Pick one curry recipe that uses whole spices rather than a paste", 10),
       ("Buy the spices and other ingredients you're missing", 25),
       ("Cook it slowly, following the recipe properly", 60),
       ("Make it again the following week without checking every line", 60)]),
]

# ---------------------------------------------------------------------------
# Family and caregiving food — a new baby, a bereaved friend, a day out
# ---------------------------------------------------------------------------
FAMILY = [
    G("Baby's due in six weeks and I want the freezer stocked with meals before things get chaotic",
      "Stock the freezer before the baby arrives", "Cook and freeze a stock of meals ahead of a baby's arrival",
      "HIGH", "PERSONAL",
      "There's a decent stack of labelled meals in the freezer ready to grab",
      [("Plan a list of freezer-friendly meals", 15),
       ("Shop for the ingredients", 60),
       ("Cook each batch and let it cool properly before freezing", 120),
       ("Portion it into labelled containers with the date", 30),
       ("Stack the freezer so things are easy to find one-handed", 15)],
      due="in six weeks"),

    G("Want to take a cooked meal round to a friend who just lost her mum, not sure what's right",
      "Take a meal round to a grieving friend", "Cook and deliver a meal for a friend who's just been bereaved",
      "MEDIUM", "PERSONAL",
      "The meal's dropped off and she doesn't have to think about cooking for a night",
      [("Check with someone close to her what she can actually manage to eat right now", 10),
       ("Cook something simple that reheats well", 60),
       ("Portion it into containers she can microwave straight from", 15),
       ("Drop it round without expecting to stay long", 20)]),

    G("Pack a picnic for the day out on Sunday",
      "Pack the picnic", "Plan and pack food for a picnic day out",
      "MEDIUM", "PERSONAL",
      "There's enough food that travels well and nobody's hungry by the afternoon",
      [("Check the forecast and pick a spot", 10),
       ("Plan food that travels well without needing reheating", 15),
       ("Shop for it the day before", 30),
       ("Pack it in a cool bag with ice packs", 15),
       ("Load the blanket and plates in with it", 10)],
      due="on Sunday"),

    G("Starting to wean the baby onto solids and I've got no idea where to begin",
      "Start weaning the baby onto solids", "Begin introducing solid food to a baby",
      "MEDIUM", "HEALTH",
      "She's taken to a few different first foods without much fuss",
      [("Read up on what to start with and what to avoid at this age", 15),
       ("Buy a highchair and some simple first spoons", 30),
       ("Offer a first taste of one simple food", 15),
       ("Watch how she takes to it over a few days before trying anything new", 20),
       ("Build up to a mix of textures over the following weeks", 30)]),

    G("Sorting the food for the road trip, we leave Friday and I don't want it to just be service station rubbish the whole way",
      "Sort the road trip food", "Plan and pack food for a road trip",
      "HIGH", "PERSONAL",
      "There's enough proper food for most of the drive instead of relying on service stations",
      [("Work out roughly what meals happen on the road versus at stops", 15),
       ("Make a list of snacks and things that travel without spoiling", 15),
       ("Shop for it the day before", 30),
       ("Pack perishables in a cool bag with an ice pack", 15),
       ("Load it within reach of the front seat", 5)],
      due="Friday"),

    G("Planning proper food for the drive up to Scotland next week instead of living off garage snacks",
      "Plan food for the drive to Scotland", "Plan and pack food for a long drive",
      "LOW", "PERSONAL",
      "There's enough decent food packed that the garage stops are only for fuel",
      [("Work out roughly how long each leg of the drive is", 10),
       ("Make a list of food that travels well and isn't too messy to eat moving", 15),
       ("Shop for it the day before", 30),
       ("Pack the perishables in a cool bag with an ice pack", 15)],
      due="next week"),
]

GOLD: list[Gold] = HOSTING + OCCASIONS + BAKING + PRESERVING + ROAST + EVERYDAY + FAMILY
