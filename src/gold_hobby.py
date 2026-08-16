"""Gold examples: hobbies and creative pursuits, non-physical-craft slice.

`gold_craft.py` already covers hands-on making with real physical procedures:
sewing, woodwork, pottery, brewing, darkroom photography, gardening, and
learning an instrument's technique. `gold_food2.py` covers baking as creative
cooking. `gold_core.py` has a handful of general CREATIVE seeds (rewriting
landing page copy, finishing an abandoned short story, a photo album, learning
three guitar songs, picking up painting again, recording a podcast episode).

This module deliberately steers around all of that and covers the rest of
what "a hobby" means for this app's users: pursuits that live mostly on a
screen or a page rather than at a workbench. Creative writing (poems, short
stories, a novel that's never got past an idea, journaling, a blog, fan
fiction, and the submission logistics for a magazine or contest — the
creative deadline, not `gold_admin2`'s paperwork framing), music composition
and songwriting (making new music, as distinct from practising an
instrument's technique), digital art and design, photography as editing,
culling and portfolio work rather than darkroom chemistry, video editing and
filmmaking, game design and tabletop RPG prep, performance (stand-up, sketch,
dance), and the long-running side projects that keep getting deprioritized —
a webcomic, a zine, a personal website.

Like the rest of the corpus, most of these carry LOW or MEDIUM priority and
avoidance-flavoured phrasing — a personal creative project rarely has
external urgency. A few carry a real deadline (a submission window, a show
date) and use `due_phrase` to quote it verbatim.

See `goldlib.Gold` for the format and `quality.py` for the rules every
example must pass.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from goldlib import Gold

G = Gold

# ---------------------------------------------------------------------------
# Creative writing — poems, stories, a novel, journaling, blogs, fan fiction,
# and the submission logistics that come with them
# ---------------------------------------------------------------------------
WRITING = [
    G("I want to start morning pages but I keep telling myself I'll begin properly on Monday",
      "Start the morning pages practice", "Begin a daily morning journaling practice instead of just planning to",
      "LOW", "CREATIVE",
      "You've written three mornings in a row, even if the pages ramble and go nowhere",
      [("Find a notebook or blank doc you'll actually use", 5),
       ("Write three pages by hand or typing without stopping to edit", 20),
       ("Do it again the next morning before checking your phone", 20),
       ("Do it a third morning and notice what keeps coming up", 20)]),

    G("The literary magazine's submission window closes at the end of the month and I still haven't sent the poem in",
      "Submit the poem before the window closes", "Get the poem revised and submitted to the literary magazine before submissions close",
      "HIGH", "CREATIVE",
      "The poem is submitted through their system with a reference or confirmation - it doesn't need to be the strongest thing you've written",
      [("Reread the poem and note the two or three lines that still feel weak", 10),
       ("Revise just those lines, leaving the rest alone", 20),
       ("Check the magazine's submission guidelines for format", 10),
       ("Submit the poem through their system and save the confirmation", 15)],
      due="closes at the end of the month"),

    G("I've had the idea for a novel in my head for years and never written a single page",
      "Start the novel that's only existed in your head", "Turn the idea into an outline and a first page instead of just thinking about it",
      "LOW", "CREATIVE",
      "There's a rough outline and an actual first page written - it doesn't need a finished plot",
      [("Write down the idea in a few loose sentences", 10),
       ("Sketch a rough outline of the beginning, middle and end", 30),
       ("Write the opening page without worrying if it's good", 30),
       ("Note where you got stuck so you know where to pick up next time", 10)]),

    G("The blog's had the same unfinished draft sitting there for two months and I keep meaning to publish something",
      "Publish the overdue blog post", "Finish and publish the blog post that's been sitting as a draft",
      "MEDIUM", "CREATIVE",
      "The post is published and makes sense start to finish - it doesn't need to be your best writing",
      [("Reread the draft and remind yourself what point it was making", 10),
       ("Write the missing sections straight through", 40),
       ("Read it once and fix only what actually confuses", 20),
       ("Add a title and image and hit publish", 10)]),

    G("I haven't updated the fan fiction in months and people keep commenting asking for the next chapter",
      "Write the next fan fiction chapter", "Get the next chapter written and posted for readers waiting on it",
      "LOW", "CREATIVE",
      "A new chapter is posted that moves the story forward - it doesn't need to resolve everything",
      [("Reread your own notes on what happens next", 10),
       ("Outline the scene in a few bullet points", 10),
       ("Draft the chapter straight through", 60),
       ("Skim it once for typos and post it", 15)]),

    G("The flash fiction contest closes on Friday and I still haven't written anything for it",
      "Write and enter the flash fiction contest", "Write a piece and get it submitted before the contest closes",
      "URGENT", "CREATIVE",
      "A story is submitted within the word limit - it doesn't need to be your strongest work to count as an entry",
      [("Check the contest's word limit and theme", 10),
       ("Freewrite a few possible ideas that fit the theme", 15),
       ("Draft the story straight through without editing", 60),
       ("Cut it down to the word limit and fix typos", 30),
       ("Submit it and save the confirmation", 10)],
      due="closes on Friday"),

    G("My cousin's wedding is in three weeks and I offered to write and read a poem but haven't started",
      "Write the wedding poem", "Write and practice the poem you offered to read at your cousin's wedding",
      "HIGH", "CREATIVE",
      "There's a poem you can read aloud without stumbling over the words - it doesn't need to be profound",
      [("Jot down a few memories or details about the couple", 15),
       ("Draft a rough version of the poem", 30),
       ("Read it aloud and adjust lines that trip you up", 20),
       ("Practice reading it out loud a few times so it's not the first time", 15)],
      due="is in three weeks"),
]

# ---------------------------------------------------------------------------
# Music — composing, arranging and recording, distinct from practising an
# instrument's existing technique
# ---------------------------------------------------------------------------
MUSIC = [
    G("I keep humming the same melody in the shower and never actually write it down",
      "Turn the shower melody into a real song", "Get the melody you keep humming written down and turned into an actual song",
      "LOW", "CREATIVE",
      "There's a recording of the melody with at least some lyrics or structure - it doesn't need a proper arrangement",
      [("Hum the melody into your phone before you forget it again", 5),
       ("Work out the chords that fit under it", 20),
       ("Write a verse and chorus of lyrics", 30),
       ("Record a rough version with your phone or a basic app", 20)]),

    G("The open mic night is next Thursday and the song I'm supposed to play still doesn't have a proper ending",
      "Finish arranging the song for Thursday's open mic", "Write an ending for the song and get the arrangement finished before the open mic",
      "HIGH", "CREATIVE",
      "The song has a full arrangement from start to end that you can play through - a rough ending is fine",
      [("Play through what you already have from the start", 10),
       ("Try a few different endings until one feels right", 30),
       ("Write out the final structure so you don't lose it", 15),
       ("Run through the whole song a few times to get it under your fingers", 30)],
      due="is next Thursday"),

    G("I've written a new song on guitar but never actually recorded a demo of it",
      "Record a demo of the new song", "Record a rough demo of the song you've written instead of just playing it live",
      "MEDIUM", "CREATIVE",
      "There's a listenable recording of the song from start to end - the vocals and playing don't need to be polished",
      [("Set up your phone or interface somewhere quiet", 10),
       ("Do a couple of practice run-throughs to warm up", 15),
       ("Record a few takes of the full song", 30),
       ("Listen back and pick the best take", 15)]),

    G("I offered to put together a short instrumental piece for my friend's wedding slideshow and the wedding is in a month",
      "Write the wedding slideshow music", "Compose a short instrumental piece for the wedding slideshow",
      "MEDIUM", "CREATIVE",
      "There's a finished piece of the right length that fits the mood of the slideshow - it doesn't need to sound professionally produced",
      [("Find out roughly how long the slideshow will run", 10),
       ("Sketch a simple chord progression and melody", 30),
       ("Build the arrangement out to fill the length needed", 40),
       ("Record or export a version and check the length against the slideshow", 20)],
      due="is in a month"),

    G("I've had a guitar riff saved as a voice memo for months and never written any lyrics for it",
      "Write lyrics for the saved riff", "Write lyrics for the riff you've been sitting on and turn it into a finished song",
      "LOW", "CREATIVE",
      "There's a full set of lyrics that fits the riff and a rough recording of it together - the rhymes don't need to be clever",
      [("Listen back to the voice memo and hum along a few times", 10),
       ("Freewrite some lines about whatever the riff makes you think of", 20),
       ("Shape the lines into a verse and chorus that fit the rhythm", 30),
       ("Record yourself playing and singing it together", 20)]),
]

# ---------------------------------------------------------------------------
# Digital art and design — illustration, logos, tablet painting, and the
# unglamorous graphics work behind a creative page
# ---------------------------------------------------------------------------
VISUAL = [
    G("I keep opening the digital illustration and closing it again without adding anything",
      "Make progress on the abandoned digital illustration", "Actually add to the illustration instead of just opening and closing the file",
      "LOW", "CREATIVE",
      "New work has actually been added to the piece - it doesn't need to be finished",
      [("Open the file and look at what's already there", 5),
       ("Block in one section you've been avoiding", 30),
       ("Add colour or shading to that section", 30),
       ("Save a version so today's progress isn't lost", 5)]),

    G("I want a proper logo for the little side project instead of the placeholder text I've been using",
      "Design a logo for the side project", "Design a proper logo instead of using placeholder text",
      "MEDIUM", "CREATIVE",
      "There's a usable logo file in a couple of sizes - it doesn't need to look like an agency made it",
      [("Sketch a few rough ideas on paper first", 15),
       ("Pick the sketch you like best and rebuild it digitally", 40),
       ("Try it in a couple of colour options", 20),
       ("Export it in the sizes you'll actually need", 15)]),

    G("I bought a drawing tablet six months ago and I've still never opened the box",
      "Actually try the unopened drawing tablet", "Set up the drawing tablet and use it for the first time instead of leaving it boxed",
      "LOW", "CREATIVE",
      "Something has actually been drawn with the tablet - the drawing itself doesn't need to be good",
      [("Unbox the tablet and plug it in", 10),
       ("Install the drivers and software it needs", 15),
       ("Do a few loose scribbles just to get used to the pressure", 15),
       ("Try drawing one simple thing all the way through", 30)]),

    G("I fell behind on the daily art challenge around day six and haven't opened the sketchbook since",
      "Catch up on the daily art challenge", "Get back into the art challenge instead of treating the gap as the end of it",
      "LOW", "CREATIVE",
      "A few new pieces exist and you're drawing again - skipping the missed days entirely is fine",
      [("Look at the prompt list and pick today's prompt", 5),
       ("Do a quick sketch for today's prompt", 25),
       ("Pick one or two missed prompts you actually like and sketch those too", 40),
       ("Post or save what you've done so the streak feels real again", 10)]),

    G("I want to redo the social media graphics for my art page, they're all different sizes and styles right now",
      "Redo the art page's social graphics", "Build a consistent set of graphics for the art page instead of the mismatched ones",
      "MEDIUM", "CREATIVE",
      "There's one template you actually reuse across the next few posts - it doesn't need to cover formats you rarely use",
      [("Look at what's currently posted and note what looks inconsistent", 10),
       ("Pick a colour palette and font pairing to stick with", 20),
       ("Build one template in the size you post most often", 40),
       ("Make two or three variations from that template", 30)]),
]

# ---------------------------------------------------------------------------
# Photography — culling, editing and portfolio work, not darkroom chemistry
# ---------------------------------------------------------------------------
PHOTO = [
    G("The photos from the trip are still sitting unedited on the memory card three months later",
      "Cull and edit the trip photos", "Go through the trip photos, pick the keepers and edit them",
      "MEDIUM", "CREATIVE",
      "The best shots are picked out and edited enough to share - the rest can stay unedited",
      [("Import the photos and back them up somewhere safe", 15),
       ("Go through and flag the shots worth keeping", 40),
       ("Edit the flagged shots - exposure, crop, colour", 60),
       ("Export a set to share or print", 15)]),

    G("My photography portfolio website still has work from three years ago on it",
      "Update the photography portfolio", "Replace the outdated work on the portfolio site with recent shots",
      "MEDIUM", "CREATIVE",
      "The site shows work you're actually proud of now - older shots can just come down without replacements yet",
      [("Shortlist a handful of the strongest recent images", 15),
       ("Edit the shortlisted images to a consistent look", 45),
       ("Remove the outdated images from the site", 15),
       ("Upload the new set and check it loads properly", 20)]),

    G("I started a 365-day photo project in January and stopped taking pictures around day forty",
      "Get back into the 365 photo project", "Pick the daily photo project back up instead of quietly abandoning it",
      "LOW", "CREATIVE",
      "You're taking a photo again most days - the gap in the middle doesn't need to be filled in",
      [("Look back at the last photo you actually took", 5),
       ("Take today's photo, whatever's in front of you", 10),
       ("Decide whether to renumber from where you stopped or just carry on", 10),
       ("Set a daily reminder so it's harder to quietly drop again", 10)]),

    G("I shot my friend's engagement photos and she needs a few edited ones before she announces it next weekend",
      "Edit the engagement photos before the announcement", "Edit and deliver a handful of the engagement photos before your friend announces the news",
      "HIGH", "CREATIVE",
      "A handful of shots are edited and sent over - the rest of the shoot can wait",
      [("Pick out a handful of the strongest shots from the shoot", 15),
       ("Edit exposure and colour on those shots", 45),
       ("Export them at a size she can post from", 15),
       ("Send them over with a quick message", 10)],
      due="before she announces it next weekend"),
]

# ---------------------------------------------------------------------------
# Video editing and filmmaking
# ---------------------------------------------------------------------------
VIDEO = [
    G("The tutorial footage has been sitting in the editing software for weeks and I keep putting off cutting it down",
      "Edit the tutorial footage into one video", "Cut the raw tutorial footage down into a single watchable video",
      "MEDIUM", "CREATIVE",
      "There's one video that plays start to finish and makes sense - some rough cuts are fine",
      [("Open the project and watch back what you already have", 15),
       ("Cut out the obvious mistakes and dead air", 45),
       ("Arrange what's left into a sensible order", 30),
       ("Add titles or captions where it needs them", 30),
       ("Export a version and watch it back", 20)]),

    G("I keep planning the YouTube channel and never actually filming the first video",
      "Film the first YouTube video", "Actually film and post a first video instead of continuing to plan the channel",
      "LOW", "CREATIVE",
      "One video exists and is posted - it doesn't need to represent the whole channel idea",
      [("Pick one small topic instead of the big idea for the channel", 10),
       ("Write a rough outline of what you'll say", 15),
       ("Film it in one or two takes", 30),
       ("Do a quick edit to cut the worst bits", 40),
       ("Post it, even quietly", 10)]),

    G("I want to storyboard and shoot the short scene I've been imagining for the film project",
      "Storyboard and shoot the short scene", "Storyboard the scene and actually shoot it instead of just picturing it",
      "MEDIUM", "CREATIVE",
      "The scene is shot and roughly matches what you pictured - a few camera angles can be simpler than planned",
      [("Sketch rough panels for the first few shots", 15),
       ("List what you'll need - location, people, props", 15),
       ("Shoot the scene following the storyboard loosely", 90),
       ("Back up the footage somewhere safe", 15)]),

    G("I filmed hours of gameplay for the channel and it's just sitting there unedited",
      "Edit the gameplay footage into a video", "Cut the hours of raw gameplay down into one video worth posting",
      "MEDIUM", "CREATIVE",
      "There's one edited video of a reasonable length - most of the raw footage can be left out",
      [("Skim through the footage and jot down promising moments", 15),
       ("Cut those moments into a rough sequence", 45),
       ("Trim it down to a length people will actually watch", 30),
       ("Add commentary or captions if it needs them", 30),
       ("Export and post it", 15)]),
]

# ---------------------------------------------------------------------------
# Game design, worldbuilding and tabletop RPG prep
# ---------------------------------------------------------------------------
GAMES = [
    G("I promised my group I'd have the next tabletop campaign arc planned before our session this weekend",
      "Plan the next campaign arc before the session", "Get the next arc of the tabletop campaign planned before the group's next session",
      "HIGH", "CREATIVE",
      "There's enough planned to run the next session - side branches the players might take can be improvised",
      [("Reread your notes on where the last session left off", 15),
       ("Decide the next major plot beat", 20),
       ("Sketch the encounters or scenes that get the players there", 40),
       ("Write brief notes for the NPCs involved", 20)],
      due="before our session this weekend"),

    G("I keep adding to the worldbuilding notes for the fantasy setting but never actually use any of it",
      "Organise the worldbuilding notes", "Pull the scattered worldbuilding notes into something usable instead of endless loose additions",
      "LOW", "CREATIVE",
      "The core of the setting is written somewhere organised - obscure details can stay scattered",
      [("Gather the notes from wherever they're currently scattered", 15),
       ("Group them into rough categories - places, people, history", 30),
       ("Write a short summary of the core setting from those groups", 40),
       ("File the rest under the categories for later", 20)]),

    G("I've had the idea for a board game for years and never built even a rough prototype",
      "Prototype the board game idea", "Build a rough playable prototype of the board game instead of leaving it as an idea",
      "MEDIUM", "CREATIVE",
      "There's a version you could actually play a round of - the components can be paper and cardboard",
      [("Write down the core rules in a few sentences", 15),
       ("Make rough components out of paper, card or whatever's around", 45),
       ("Play through a round by yourself to see what breaks", 30),
       ("Note the rules that need fixing before showing anyone", 20)]),

    G("The D&D session is on Friday and I still haven't written the dungeon the party's about to walk into",
      "Write Friday's dungeon before the session", "Get the dungeon written and ready before the party reaches it on Friday",
      "URGENT", "CREATIVE",
      "There's a playable dungeon with rooms, encounters and a way through - unexplored side corners don't need detail yet",
      [("Decide roughly how many rooms and what the goal is", 15),
       ("Sketch a rough map of the layout", 20),
       ("Write the key encounters and any traps or puzzles", 40),
       ("Note the loot and any important NPCs inside", 20)],
      due="is on Friday"),

    G("I want to write up a simple rules document for the tabletop game I made up so the group doesn't have to keep asking me",
      "Write up the tabletop game's rules", "Write down the rules for the homemade game so you're not explaining them from memory every time",
      "LOW", "CREATIVE",
      "The core rules are written down clearly enough that someone else could run a round - edge cases can wait",
      [("List the rules as you currently explain them out loud", 15),
       ("Write them up in a sensible order - setup, turns, winning", 30),
       ("Read it back as if you'd never played before", 15),
       ("Fix the parts that don't make sense on paper", 20)]),
]

# ---------------------------------------------------------------------------
# Performance — stand-up, sketch, dance, and the small showcases around them
# ---------------------------------------------------------------------------
PERFORMANCE = [
    G("There's an open mic on Tuesday and I haven't written any new stand-up material in months",
      "Write new material for Tuesday's open mic", "Write some new stand-up material before the open mic",
      "HIGH", "CREATIVE",
      "There's five minutes of material you can get through on stage - a joke or two falling flat is fine",
      [("Look through notes for things that made people laugh recently", 15),
       ("Pick two or three of those and write them out properly", 30),
       ("Say the set out loud a few times to check the timing", 20),
       ("Trim anything that runs long or falls flat when spoken aloud", 15)],
      due="on Tuesday"),

    G("The studio showcase is in three weeks and I haven't finished choreographing the piece",
      "Finish choreographing the showcase piece", "Finish choreographing the dance piece before the studio showcase",
      "HIGH", "CREATIVE",
      "The piece has movement worked out from start to end - some sections can stay rougher than others",
      [("Play the music through and mark where sections change", 10),
       ("Work out movement for the section you're stuck on", 40),
       ("Run the whole piece through to see how it flows together", 30),
       ("Film yourself running it and note what needs cleaning up", 20)],
      due="is in three weeks"),

    G("I want to plan a small house concert for friends instead of just talking about it",
      "Plan the small house concert", "Actually plan and set a date for a small house concert instead of just talking about it",
      "LOW", "PERSONAL",
      "A date is set and a handful of people are invited - it doesn't need a full setlist yet",
      [("Pick a rough date that could work", 10),
       ("Message a handful of people to gauge interest", 15),
       ("Sort out the space - seating, sound, where people put drinks", 30),
       ("Send the actual invite once the date's confirmed", 15)]),

    G("The sketch group's showcase is next month and our sketch still isn't rehearsed",
      "Rehearse the sketch before the showcase", "Get the sketch rehearsed and timed properly before the group's showcase",
      "MEDIUM", "CREATIVE",
      "You can run the sketch start to finish without checking the script - a flubbed line here and there is fine",
      [("Read through the script together once", 15),
       ("Run it without scripts, stopping only where you go blank", 30),
       ("Run it again focusing on timing and pauses", 30),
       ("Run it once more start to finish", 20)],
      due="is next month"),

    G("I've got a notes app full of one-liners and no actual set to perform at the open mic",
      "Turn the saved one-liners into a set", "Build an actual performable set out of the one-liners saved in your notes app",
      "LOW", "CREATIVE",
      "There's a short set that flows from one bit to the next - some one-liners can be left out",
      [("Read back through the notes app and copy out anything still funny", 15),
       ("Group the ones that fit a similar theme together", 20),
       ("Write short bridges between the groups so it flows", 30),
       ("Time yourself running through the set", 15)]),
]

# ---------------------------------------------------------------------------
# Long-running side projects that keep getting deprioritized
# ---------------------------------------------------------------------------
SIDE_PROJECTS = [
    G("My personal portfolio website still lists the job I left two years ago",
      "Update the outdated portfolio website", "Update the portfolio site instead of leaving old, incorrect information up",
      "MEDIUM", "CREATIVE",
      "The site reflects where you actually are now - it doesn't need a full redesign",
      [("Go through the site and note everything that's out of date", 15),
       ("Write updated text for the outdated sections", 30),
       ("Swap in a couple of more recent examples of your work", 30),
       ("Publish the changes and check it looks right on a phone", 15)]),

    G("I haven't updated the webcomic in months and I keep telling myself I'll catch up eventually",
      "Get back to the neglected webcomic", "Post a new page of the webcomic instead of leaving it indefinitely stalled",
      "LOW", "CREATIVE",
      "A new page is posted and the story has moved forward - the art doesn't need to match your best pages",
      [("Reread the last few pages to remember where the story was going", 15),
       ("Sketch the layout for the next page", 20),
       ("Ink and colour the page", 60),
       ("Post it with a short update for readers who are still around", 10)]),

    G("I keep talking about making a zine and never actually put one together",
      "Actually put the zine together", "Assemble the zine you keep talking about instead of just describing the idea",
      "MEDIUM", "CREATIVE",
      "There's a printable zine with a beginning and end - some pages can be simpler than others",
      [("Decide the theme and roughly how many pages", 15),
       ("Gather or make the content for each page", 60),
       ("Lay the pages out in a simple template", 40),
       ("Print a single copy and fold it to check it works", 15)]),

    G("I want to finally set up the newsletter for my writing that I've been meaning to start",
      "Set up the writing newsletter", "Set up the newsletter platform instead of continuing to just plan it",
      "LOW", "CREATIVE",
      "The newsletter exists and you could send an issue - the design doesn't need to be polished",
      [("Pick a newsletter platform and create an account", 15),
       ("Set the name and a short description", 10),
       ("Write a short welcome issue introducing what it'll be", 30),
       ("Send it to yourself as a test before sharing the signup link", 10)]),

    G("The small press fair is in two weeks and I haven't printed or priced any of my zine stock yet",
      "Prep the zine stock for the small press fair", "Get the zines printed, priced and packed before the fair",
      "HIGH", "ADMIN",
      "There's enough stock printed and priced to sell from - running low partway through the fair is fine",
      [("Decide which zines and how many copies of each to bring", 15),
       ("Print the copies", 60),
       ("Price each item and write up a simple price list", 20),
       ("Pack everything with a float of cash and a bag for the table", 20)],
      due="is in two weeks"),
]

GOLD: list[Gold] = WRITING + MUSIC + VISUAL + PHOTO + VIDEO + GAMES + PERFORMANCE + SIDE_PROJECTS
