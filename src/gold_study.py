"""Gold examples: personal learning and open-ended study (hand-authored).

gold_learn.py already covers exam and test revision with a real sitting
attached (GCSE resits, driving theory, citizenship tests, the bar exam),
language learning tied to a trip or a family occasion, reading through a
stalled hard book, a paid course you stalled on and statistics from scratch,
deliberate-practice skills like typing, piano theory and chess, work-adjacent
CAREER learning (an AWS or PRINCE2 certification your employer wants, a
literature review for a dissertation built from papers you've already read,
rehearsing a talk you've already prepared, ramping up on a new codebase,
building a study routine around a job), and hands-on LIFE_SKILLS (learning to
swim, first aid pre-reading, cooking a cuisine, memorising lines or vows).
gold_core.py separately covers finishing thesis chapter 3 from an existing
outline and learning Kotlin coroutines for a work refactor. gold_dev.py's own
LEARNING slice covers programming languages, profilers and garbage collectors
learned through a personal coding project — always tied to the job.
gold_craft.py covers hands-on physical hobbies and instruments. gold_tech.py
covers setting up and migrating consumer devices and accounts.

This module is what's left over: learning driven by curiosity or an itch
rather than an exam, a job, or a due literature review — going down a rabbit
hole on a topic out of genuine interest, not to pass anything or satisfy
anyone; academic writing as a from-scratch project (a personal statement, a
thesis proposal, a philosophy essay written purely for yourself) rather than
finishing an existing draft or synthesising already-read sources into a lit
review; learning a piece of creative or personal software for its own sake
(Blender, GIMP, a DAW, genealogy software, Lightroom, a video editor,
spreadsheets) rather than a programming language or a work tool; building a
personal knowledge system (an out-of-control reading list, notes scattered
across apps, a podcast backlog, a someday-learn list); learning something
well enough to teach it to someone else (a curious kid, a work
lunch-and-learn, a study group you're meant to be ahead of); and open-ended
hobby learning projects with no deadline and no employer behind them
(astronomy, birdwatching, wine, DNA ancestry results, genealogy research,
mushroom identification, map reading).

Keeps gold_learn.py's realistic-progression rule: every multi-session plan
starts from wherever the person actually is, repeats an easy rep before
adding difficulty, and assumes a job that eats evenings.

See `goldlib.Gold` for the format and `quality.py` for the rules every
example must pass.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from goldlib import Gold

G = Gold

# ---------------------------------------------------------------------------
# Curiosity-driven research — no exam, no job, just an itch to understand
# ---------------------------------------------------------------------------
CURIOSITY_RESEARCH = [
    G("Fell down a rabbit hole about the Chernobyl disaster after watching the documentary and want to actually understand what happened",
      "Actually understand what happened at Chernobyl", "Turn documentary curiosity into a real understanding of the event",
      "LOW", "LEARNING",
      "You can explain the causes and the timeline of what happened in your own words, not just repeat the documentary's version",
      [("Write down what you actually want to know beyond the documentary", 10),
       ("Read one solid overview article or book chapter on the disaster", 40),
       ("Look up the two things that still don't add up for you", 30),
       ("Explain the sequence of events out loud to yourself or someone else", 20)]),

    G("I've bookmarked about forty articles about the 2008 financial crisis and read precisely none of them, want to actually understand what happened",
      "Actually understand the 2008 financial crisis", "Turn the bookmark pile into real understanding instead of more open tabs",
      "LOW", "PERSONAL",
      "You can explain what actually caused the crash to someone else without checking your notes",
      [("Delete the tabs you'll never read and pick two or three bookmarked articles to actually start with", 15),
       ("Read the clearest overview one first, ignoring the rest for now", 35),
       ("Read a second article that covers a part the first one skipped", 35),
       ("Write a few sentences summarising the chain of events in your own words", 25)]),

    G("Want to actually understand how vaccines work instead of just repeating what I've heard secondhand",
      "Actually understand how vaccines work", "Replace secondhand talking points with a real grasp of the mechanism",
      "LOW", "LEARNING",
      "You can explain how a vaccine trains the immune system without leaning on a phrase you memorised",
      [("Write down what you currently think you know and where the gaps are", 10),
       ("Read one solid explainer on how the immune system responds to a vaccine", 30),
       ("Look up the one part of the mechanism that's still fuzzy", 20),
       ("Explain the whole process out loud without looking at your notes", 20)]),

    G("Thinking about buying an electric car and want to actually understand the technology properly, not just compare prices",
      "Understand EV technology before buying one", "Learn how the technology actually works instead of only comparing spec sheets",
      "MEDIUM", "LEARNING",
      "You can explain how range, charging speed and battery degradation actually work to someone else",
      [("List the three things about EVs you don't actually understand yet", 10),
       ("Read a solid explainer on how EV batteries and charging actually work", 35),
       ("Read about battery degradation and what actually affects it", 30),
       ("Compare what you've learned against the two models you're actually considering", 30)]),

    G("Started reading about the fall of the Roman Empire and keep following side links on Wikipedia, want to turn it into something I actually understand",
      "Turn the Roman Empire wiki-hole into real understanding", "Stop wandering the side links and build an actual grasp of the collapse",
      "LOW", "LEARNING",
      "You can explain the main causes of the collapse in a rough order, not just isolated facts",
      [("Pick one decent overview source instead of following more side links", 15),
       ("Read it through once without chasing every link that looks interesting", 40),
       ("Note the three or four causes it points to", 20),
       ("Look up the one cause that's still unclear", 25)]),

    G("Curious how the stock market actually works beyond 'number go up'",
      "Actually understand how the stock market works", "Get past the headline version and understand the actual mechanism",
      "LOW", "LEARNING",
      "You can explain what a share price actually reflects and why it moves, in your own words",
      [("Write down what 'number go up' actually leaves unexplained for you", 10),
       ("Read a beginner explainer on what a share and an exchange actually are", 30),
       ("Read about what actually moves a price day to day", 30),
       ("Explain it back in your own words without the article open", 20)]),

    G("Got obsessed with a true crime case after the podcast and want to actually read the primary sources instead of the recap",
      "Read the primary sources behind the true crime case", "Go past the podcast's retelling to what the original documents actually say",
      "LOW", "PERSONAL",
      "You've read at least one primary source yourself and know where the podcast's version simplified it",
      [("Note the specific claims the podcast made that you want to check", 15),
       ("Track down the court documents or news reports the case was actually based on", 30),
       ("Read the primary source and compare it to the podcast's version", 40),
       ("Write down where the two accounts actually differ", 20)]),
]

# ---------------------------------------------------------------------------
# Academic writing as its own project — from a blank page, not an outline
# or a pile of already-read sources
# ---------------------------------------------------------------------------
ACADEMIC_WRITING = [
    G("Personal statement for the grad school application is due in three weeks and I haven't written a word",
      "Write the grad school personal statement", "Get from a blank document to a real draft before the deadline",
      "HIGH", "LEARNING",
      "There's a full draft that says something specific about you, even if the wording still needs polishing",
      [("Jot down two or three real reasons you want to do this, not the ones that sound good", 15),
       ("Write a rough opening paragraph straight through without editing", 30),
       ("Write the middle section connecting your actual experience to the reasons", 45),
       ("Write a short closing paragraph", 20),
       ("Read it back once and cut whatever doesn't sound like you", 25)],
      due="in three weeks"),

    G("Scholarship essay needs to be in by the end of the month and the prompt still just says 'notes' underneath it",
      "Write the scholarship essay", "Turn the empty notes section into an actual essay before the deadline",
      "HIGH", "LEARNING",
      "There's a full draft answering the actual prompt, even if a sentence or two still needs smoothing",
      [("Reread the prompt properly and note exactly what it's asking", 10),
       ("Brainstorm two or three real examples that answer it", 20),
       ("Write a rough draft straight through without editing", 40),
       ("Read it back against the prompt and cut anything that doesn't answer it", 30)],
      due="by the end of the month"),

    G("Want to write a philosophy essay on free will just to work the argument out properly, no deadline, just for myself",
      "Write the free will essay for yourself", "Use the writing to actually work the argument out, not to hand it in anywhere",
      "LOW", "LEARNING",
      "The essay states a clear position and defends it, even if you'd still argue with parts of it",
      [("Write down the position you actually hold before reading anyone else's", 15),
       ("Read one counter-argument to your position properly", 30),
       ("Draft the essay straight through, addressing that counter-argument", 45),
       ("Read it back and tighten the weakest paragraph", 25)]),

    G("Thesis proposal is still a blank document and my first supervisor meeting is in two weeks",
      "Draft the thesis proposal", "Get a real proposal down before the first supervisor meeting",
      "HIGH", "LEARNING",
      "There's a draft with a research question and a rough plan, even if the scope will change after feedback",
      [("Write down the research question in one sentence, however rough", 15),
       ("List the two or three papers your idea builds on", 20),
       ("Draft the background section from those papers", 40),
       ("Draft a rough plan for how you'd actually answer the question", 40),
       ("Read it through once and note what you'll ask your supervisor about", 20)],
      due="in two weeks"),

    G("Want to start a personal essay for the blog I never post on, the draft's been an empty document for months",
      "Start the personal essay for the blog", "Get an actual draft going instead of an empty document",
      "LOW", "CREATIVE",
      "There's a rough draft down, even if it's not something you'd publish yet",
      [("Pick the one idea you keep coming back to and write it as a single sentence", 10),
       ("Write a rough opening paragraph without editing as you go", 25),
       ("Keep writing until you've got the shape of the whole thing down", 40),
       ("Read it back once and mark the parts that actually sound like you", 20)]),

    G("College application essay prompt has been open in a tab for two weeks and I still don't have an angle",
      "Find an angle for the college application essay", "Get past the blank tab and into an actual draft",
      "MEDIUM", "LEARNING",
      "There's a rough draft built around one real angle, even if the ending still needs work",
      [("Reread the prompt and write down three moments from your life that might answer it", 15),
       ("Pick the one that actually has something to say and outline it in a few bullet points", 15),
       ("Draft the essay straight through from the outline", 40),
       ("Read it back and check it actually answers the prompt", 20)]),

    G("Want to write up the research I did out of curiosity into something more like a proper essay instead of scattered notes",
      "Turn the scattered research notes into an essay", "Give the curiosity-driven reading an actual shape instead of loose notes",
      "LOW", "LEARNING",
      "There's a draft with a clear thread through it, even if a section or two is still thin",
      [("Reread your notes and group them into two or three themes", 15),
       ("Write a rough paragraph for the first theme straight from the notes", 30),
       ("Write the paragraph for the second theme", 30),
       ("Write a short link between the two and a rough ending", 25)]),
]

# ---------------------------------------------------------------------------
# Learning a piece of creative or personal software for its own sake —
# not a programming language, not a work tool, not an instrument
# ---------------------------------------------------------------------------
NEW_SOFTWARE = [
    G("Got Blender to make a 3D model of the house we're renovating and have no idea where to start",
      "Learn Blender for the house model", "Get from a blank Blender window to a basic model of the house",
      "MEDIUM", "LEARNING",
      "You've built one basic room shape yourself, even if it's rough and the textures aren't touched yet",
      [("Watch one beginner tutorial on the basic navigation and tools", 15),
       ("Follow along and build one simple shape from scratch", 30),
       ("Redo the same shape without the tutorial playing, just from memory", 25),
       ("Try blocking out one actual room of the house", 45)]),

    G("Downloaded GIMP to edit the old family photos and it might as well be a spaceship cockpit",
      "Learn the basics of GIMP", "Get comfortable enough with GIMP to actually edit the family photos",
      "LOW", "LEARNING",
      "You can crop, straighten and adjust the brightness on a photo without hunting through menus",
      [("Watch a short beginner tour of where the main tools live", 15),
       ("Open one photo and practise cropping and straightening it", 20),
       ("Practise adjusting brightness and contrast on the same photo", 20),
       ("Edit a second, different photo using only what you just learned", 25)]),

    G("Want to actually learn the DAW properly instead of just dragging loops around",
      "Learn the DAW properly", "Move past dragging loops into actually understanding the software",
      "MEDIUM", "LEARNING",
      "You've built one short track using at least one feature beyond dragging loops",
      [("Watch a beginner walkthrough of the interface and the main panels", 15),
       ("Practise recording or programming one simple track from scratch", 30),
       ("Learn how to use at least one effect or automation properly", 30),
       ("Put together a short piece using what you just learned instead of only loops", 40)]),

    G("Inherited grandad's genealogy software files and want to learn the program well enough to actually use them",
      "Learn grandad's genealogy software", "Get comfortable enough with the program to actually use what he left behind",
      "MEDIUM", "PERSONAL",
      "You can open the file, find a person in it and add a new one yourself",
      [("Open the software and just look around at what's already in there", 15),
       ("Find the tutorial or help section and skim how the basics work", 20),
       ("Practise finding one relative you already know is in there", 20),
       ("Try adding one new person and connecting them correctly", 30)]),

    G("Want to learn Lightroom properly instead of just using the auto button on every photo",
      "Learn Lightroom properly", "Get past the auto button and into actually editing photos",
      "LOW", "LEARNING",
      "You've edited one photo manually using at least two tools beyond the auto button",
      [("Watch a short beginner tutorial on the main editing panel", 15),
       ("Pick one photo and adjust exposure and white balance manually", 20),
       ("Try one more tool, like cropping or a local adjustment", 25),
       ("Edit a second photo without touching the auto button at all", 25)]),

    G("Bought a video editing program for the holiday footage and haven't got past the free trial popup",
      "Learn the video editing software", "Get past the trial popup and into actually cutting the holiday footage",
      "LOW", "CREATIVE",
      "You've cut one short clip together, even if it's rough around the edges",
      [("Watch a short beginner tutorial on importing and trimming clips", 15),
       ("Import the holiday footage and just get familiar with the timeline", 20),
       ("Trim and arrange a handful of clips into a rough order", 35),
       ("Add one transition or piece of music and export a short clip", 30)]),

    G("Want to actually learn spreadsheets properly instead of googling the same formula every time",
      "Actually learn spreadsheets properly", "Build real spreadsheet skills instead of relooking up the same formula each time",
      "LOW", "LEARNING",
      "You can build a simple formula from memory without searching for it first",
      [("List the three formulas you always end up googling", 10),
       ("Read how each of those three actually works, not just the syntax", 30),
       ("Build a small practice sheet using all three from memory", 30),
       ("Redo one of them the next day without looking anything up, to check it stuck", 15)]),
]

# ---------------------------------------------------------------------------
# Building a personal knowledge system — the backlog has gotten unwieldy
# ---------------------------------------------------------------------------
KNOWLEDGE_SYSTEM = [
    G("Reading list has about two hundred books on it and I add to it faster than I ever take anything off",
      "Get the reading list under control", "Turn an endlessly growing list into something you'll actually work through",
      "LOW", "PERSONAL",
      "The list is trimmed to books you'd actually read next, with a rough order, not everything you've ever heard of",
      [("Go through the list and cut anything you know you'll never actually read", 15),
       ("Sort what's left into a rough order of what you actually want next", 20),
       ("Pick the top three and note why you want to read them", 15),
       ("Start the first one this week instead of adding another book to the list", 20)]),

    G("Notes are scattered across four different apps and a stack of notebooks and I can never find anything",
      "Consolidate the scattered notes", "Get the notes into one place you can actually search",
      "MEDIUM", "LEARNING",
      "The notes that actually mattered are in one place, even if a couple of the old notebooks are still just sitting in a drawer",
      [("List the four apps and the notebooks and roughly what's in each", 15),
       ("Pick one app to be the actual home for notes going forward", 10),
       ("Move over the notes you still actually reference", 40),
       ("Skim the notebooks and copy over anything worth keeping", 40)]),

    G("Podcast backlog is over three hundred episodes deep and it just keeps growing",
      "Get the podcast backlog under control", "Turn an endless queue into something you'll actually listen to",
      "LOW", "PERSONAL",
      "The queue only has episodes you'd actually choose to listen to next, not everything you ever added",
      [("Go through the queue and remove anything you know you'll never get to", 15),
       ("Unsubscribe from the shows adding more than you'll ever hear", 15),
       ("Pick the three episodes you actually want to hear next", 10),
       ("Listen to the first one instead of adding a new one", 30)]),

    G("Saved articles pile in the browser is embarrassing and I want an actual system instead of more tabs",
      "Build a real system for saved articles", "Replace the tab pile with somewhere articles actually get read",
      "LOW", "LEARNING",
      "There's a system with a small number of articles actually queued, not a hundred open tabs",
      [("Close the tabs you'll genuinely never read", 15),
       ("Pick one read-it-later tool and save the rest into it", 20),
       ("Sort what's left into two or three rough categories", 20),
       ("Read the first article from the pile before saving anything new", 25)]),

    G("Started five different note-taking apps this year looking for the perfect system and use none of them properly",
      "Actually settle on one note-taking system", "Stop app-hopping and get one system properly working",
      "LOW", "LEARNING",
      "You've picked one app and used it for a real note this week, without starting a sixth one",
      [("List what actually annoyed you about each of the five apps", 15),
       ("Pick the one that annoyed you least instead of searching for a sixth", 10),
       ("Set up the basic structure you'll actually use", 25),
       ("Move this week's notes into it instead of a new app", 25)]),

    G("The 'things I want to learn someday' list has forty items on it and I've never opened half the links",
      "Get the someday-learn list under control", "Turn a forty-item wishlist into something you'll actually start",
      "LOW", "LEARNING",
      "The list is down to a handful of things you'd actually start next, not everything you've ever been curious about",
      [("Go through the list and cut anything you're not actually curious about anymore", 15),
       ("Check the dead links and remove whatever's gone", 15),
       ("Pick the top three you'd genuinely start this month", 15),
       ("Open the first one properly and do the first real step", 30)]),
]

# ---------------------------------------------------------------------------
# Teaching yourself by teaching someone else — a kid, a colleague, a group
# ---------------------------------------------------------------------------
TEACH_TO_LEARN = [
    G("Promised my niece I'd explain how black holes actually work and now I realise I only sort of know",
      "Learn how black holes actually work before explaining them", "Get from a rough idea to an explanation that'll survive a curious kid's follow-up questions",
      "MEDIUM", "LEARNING",
      "You can explain it in plain words a kid would follow, including answering one obvious follow-up question",
      [("Write down what you'd say right now and where it gets shaky", 10),
       ("Read a solid explainer aimed at a general audience, not a physics paper", 30),
       ("Work out how you'd explain the one part that's still confusing", 25),
       ("Practise explaining the whole thing out loud as if she's actually there", 20)]),

    G("Volunteered to do the lunch-and-learn on the new tax rules at work next month and barely understand them myself",
      "Learn the new tax rules before the lunch-and-learn", "Get from barely understanding the rules to being able to explain them simply",
      "HIGH", "LEARNING",
      "You can explain the changes in plain terms and answer the two most obvious questions people will ask",
      [("Read the official summary of what's actually changed", 15),
       ("Work through one worked example so it's not just theory", 30),
       ("Write down the two questions people are most likely to ask", 15),
       ("Practise the explanation out loud, including answering those two questions", 25)],
      due="next month"),

    G("Said I'd help run the study group on evolutionary biology next week and haven't actually read past chapter one myself",
      "Get ahead of the study group on evolutionary biology", "Get properly past chapter one before you're meant to be helping others through it",
      "HIGH", "LEARNING",
      "You've read enough further than the group to actually field questions, not just recognise the chapter titles",
      [("Check which chapters the group will actually cover next week", 10),
       ("Reread chapter one properly, since it's been a while", 25),
       ("Read the next two chapters the group is covering", 50),
       ("Note the two points you'd guess people will get stuck on", 20)],
      due="next week"),

    G("Want to explain how the internet actually works to my son before he asks me something I can't answer again",
      "Learn how the internet actually works before he asks again", "Get ahead of the next question instead of bluffing through it",
      "LOW", "LEARNING",
      "You can explain, in plain terms, how a page actually gets from a server to his screen",
      [("Write down the last question that stumped you", 10),
       ("Read a plain-language explainer on how the internet actually works", 30),
       ("Work out a simple analogy a kid would actually follow", 20),
       ("Practise the explanation out loud before he asks again", 15)]),

    G("Offered to explain cryptocurrency to my parents at Christmas and realised I don't actually understand it beyond the buzzwords",
      "Actually understand cryptocurrency before Christmas", "Get past the buzzwords so the explanation to your parents actually makes sense",
      "MEDIUM", "LEARNING",
      "You can explain what a blockchain actually does in plain terms, without leaning on jargon",
      [("Write down the buzzwords you currently repeat without really understanding", 10),
       ("Read a plain explainer of how a blockchain actually works", 35),
       ("Work out a simple, non-jargon example to use with your parents", 25),
       ("Practise the explanation on someone else first", 20)],
      due="at Christmas"),

    G("Promised to teach my flatmate chess and I'm not sure I could explain half the rules properly myself",
      "Get the chess rules straight before teaching your flatmate", "Make sure you actually know the rules before you're the one explaining them",
      "LOW", "PERSONAL",
      "You can explain how the pieces move and the two odd rules, castling and en passant, without checking",
      [("Look up the rules you're genuinely unsure about", 15),
       ("Set up a board and walk through each piece's moves out loud", 25),
       ("Look up castling and en passant properly since those trip everyone up", 20),
       ("Run through a mock explanation as if your flatmate were already sitting there", 20)]),
]

# ---------------------------------------------------------------------------
# Open-ended hobby learning projects — no deadline, no employer behind them
# ---------------------------------------------------------------------------
HOBBY_LEARNING = [
    G("Got a telescope for Christmas and haven't got further than pointing it at the moon, want to actually learn the sky",
      "Actually learn the night sky", "Get past pointing at the moon and into recognising what's actually up there",
      "LOW", "LEARNING",
      "You can find two or three constellations on your own without an app pointing them out",
      [("Check what's actually visible from your garden this month", 10),
       ("Learn one easy constellation and find it in the sky", 20),
       ("Go out again and find that same one before trying a new one", 20),
       ("Learn a second constellation and find both in one session", 25)]),

    G("Getting into birdwatching and can currently identify approximately one bird, want to actually learn to tell them apart",
      "Learn to actually identify garden birds", "Build up from the one bird you already know",
      "LOW", "LEARNING",
      "You can identify four or five common birds on sight without needing to check the app",
      [("Note which birds actually show up in your garden or local park", 10),
       ("Learn two more common ones properly, not just skimming the app", 25),
       ("Go out and try to spot those two in real life", 30),
       ("Add one more once the first two feel automatic", 20)]),

    G("Want to actually learn about wine instead of just picking whatever's on offer",
      "Actually learn about wine", "Build some real understanding instead of guessing off the offer sticker",
      "LOW", "PERSONAL",
      "You can describe what you're tasting in your own words and explain why you picked a bottle",
      [("Pick two very different wines to compare side by side", 15),
       ("Read a short beginner guide on what to actually taste for", 20),
       ("Taste both properly, writing down what you actually notice", 30),
       ("Try two more the following week, using the same method", 30)]),

    G("DNA test came back months ago and I still haven't learned enough to make sense of the ancestry results",
      "Actually make sense of the DNA ancestry results", "Turn the sitting results into something you actually understand",
      "LOW", "PERSONAL",
      "You can explain what the regions and percentages in your results actually mean",
      [("Reopen the results and note what's actually confusing about them", 10),
       ("Read how the company estimates the regions and percentages", 25),
       ("Look up the one region that surprised you the most", 25),
       ("Explain your own results to someone else in plain terms", 20)]),

    G("Started tracing the family tree and got stuck after three generations, want to actually learn how genealogy research works",
      "Learn how genealogy research actually works", "Get unstuck by learning the method, not just the software",
      "MEDIUM", "LEARNING",
      "You've found one new confirmed relative using a source beyond what you started with",
      [("Note exactly where the trail went cold", 10),
       ("Read a beginner guide on the records genealogists actually use", 30),
       ("Search one new source type for the generation you got stuck on", 40),
       ("Confirm or rule out whatever you found against what you already had", 25)]),

    G("Want to learn to identify the mushrooms in the woods behind the house instead of just walking past them",
      "Learn to identify local mushrooms", "Go from walking past them to actually recognising a few safely",
      "LOW", "LEARNING",
      "You can confidently identify two or three common species using a proper guide, not a guess",
      [("Get a proper regional field guide instead of relying on an app alone", 15),
       ("Learn the two or three most common, easily identified species in the guide", 25),
       ("Walk the woods and try to spot those specific ones", 40),
       ("Check what you found against the guide properly before deciding what it was", 20)]),

    G("Want to learn to read a topographic map properly before we get properly lost on the next hike",
      "Learn to read a topographic map", "Get comfortable with contour lines before it matters on the trail",
      "MEDIUM", "LEARNING",
      "You can read the contour lines and symbols on a real map and roughly picture the terrain",
      [("Get a map of an area you actually know well to practise on", 10),
       ("Learn what the contour lines and basic symbols mean", 25),
       ("Trace a route you've actually walked and check it against the map", 30),
       ("Try the same on a map of an area you don't know", 30)]),
]

GOLD: list[Gold] = (
    CURIOSITY_RESEARCH + ACADEMIC_WRITING + NEW_SOFTWARE + KNOWLEDGE_SYSTEM
    + TEACH_TO_LEARN + HOBBY_LEARNING
)
