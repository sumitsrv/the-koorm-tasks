"""Gold examples: studying and learning a skill (hand-authored).

LEARNING was the thinnest category in the corpus before this file — six
examples total, spread across gold_core.py and the other slices. It is also
the category where the shipped v1 model failed most visibly: asked to restart
running after two months off, it prescribed 5-6 sessions a week and a
"30-minute warm-up" whose own description lasted fifteen minutes. Progression
that contradicts itself inside one step, and habits pitched at someone who
just told you they'd stopped, is the specific defect this file exists to not
repeat.

So every multi-session plan here starts from wherever the person actually is
(not zero, not "textbook diligent"), repeats the same easy rep before adding
difficulty, and assumes a job that eats evenings and swallows some days
outright — two realistic sessions beats an ambitious five that collapse by
Wednesday.

See `goldlib.Gold` for the format and `quality.py` for the rules every example
must pass.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from goldlib import Gold

G = Gold

# ---------------------------------------------------------------------------
# Exams and tests with a real sitting attached — revision, resits, citizenship
# ---------------------------------------------------------------------------
EXAMS = [
    G("GCSE maths resit is in six weeks and I haven't opened a book yet",
      "Start revising for the maths resit", "Build revision going again from a standing start",
      "HIGH", "LEARNING",
      "You've worked through past-paper questions on the topics you're weakest on and know roughly where you stand",
      [("Find the exam specification and mark which topics feel shaky", 15),
       ("Do one past paper under no time pressure to see where you actually stand", 30),
       ("Pick the two weakest topics and work through practice questions on just those", 45),
       ("Repeat with a second past paper and compare the weak spots", 45),
       ("Do one final practice paper under exam time conditions", 45)],
      due="in six weeks"),

    G("Driving theory test is booked for three weeks on Thursday and I haven't touched the book",
      "Start revising for the driving theory test", "Get through the question bank before test day",
      "HIGH", "LEARNING",
      "You're consistently passing the practice tests, not just scraping through",
      [("Download the official question bank and skim the topic list", 15),
       ("Do one practice test cold to see where you stand", 30),
       ("Go through the hazard perception clips and learn the scoring pattern", 40),
       ("Work through the practice questions on the topics you got wrong", 45),
       ("Do a second full practice test under time conditions", 30)],
      due="three weeks on Thursday"),

    G("Failed the theory test once already, the resit is in a fortnight",
      "Prepare for the theory test resit", "Fix the gaps from the first attempt before trying again",
      "URGENT", "LEARNING",
      "You know why you failed last time and are passing practice tests on those sections now",
      [("Look at the breakdown of which sections you got wrong last time", 15),
       ("Redo the question bank filtered to just those sections", 30),
       ("Work through the hazard perception clips again, focusing on the ones you missed", 35),
       ("Do a full practice test under time conditions", 30),
       ("Review only the questions you got wrong on that last practice test", 20)],
      due="in a fortnight"),

    G("Citizenship test is booked for next month and the study guide's still shrink-wrapped",
      "Start revising for the citizenship test", "Get through the official study guide before test day",
      "HIGH", "LEARNING",
      "You're consistently passing the practice tests, not just recognising the answers",
      [("Unwrap the study guide and skim the contents to see the scope", 10),
       ("Read the first section and do the practice questions for it", 30),
       ("Read the second section and do its practice questions", 30),
       ("Do a full practice test and note what you got wrong", 30),
       ("Go back over just the sections behind the wrong answers", 30)],
      due="next month"),

    G("Want to actually learn the history in the citizenship guide properly, not just memorise the answers",
      "Actually learn the citizenship history", "Understand the material instead of pattern-matching answers",
      "LOW", "PERSONAL",
      "You can explain the events behind a few of the practice answers, not just recite them",
      [("Pick one period from the guide to start with", 10),
       ("Read that section properly instead of skimming for answers", 25),
       ("Look up the one or two events that didn't make sense from the summary", 20),
       ("Explain what you read out loud in your own words", 25),
       ("Move on to the next period the same way", 25)]),

    G("Failed the bar exam by a handful of marks and the next sitting is in four months",
      "Prepare for the bar exam resit", "Fix the specific weak sections before the next sitting",
      "HIGH", "LEARNING",
      "You know exactly which sections cost you the marks and are scoring better on those in practice",
      [("Get the examiner's report or your own notes on where the marks were lost", 15),
       ("Redo practice questions on the weakest one or two sections", 40),
       ("Work through a full practice paper under timed conditions", 45),
       ("Mark it and compare the weak areas to last time", 30),
       ("Focus the next block of study on whatever is still weak", 45)],
      due="in four months"),

    G("Failed my driving test on the manoeuvres again, third time now",
      "Fix the driving test manoeuvres", "Get the manoeuvres consistent before trying again",
      "MEDIUM", "LEARNING",
      "You can do the manoeuvre correctly a few times in a row, not just once",
      [("Look at exactly what the examiner marked you down for", 15),
       ("Go over that manoeuvre slowly, talking through each step", 30),
       ("Repeat it a few more times at the same slow pace before speeding up", 30),
       ("Try it at normal speed once it's consistent at the slow pace", 30)]),
]

# ---------------------------------------------------------------------------
# Language learning and reading hard books
# ---------------------------------------------------------------------------
LANGUAGE_AND_READING = [
    G("Learn enough Spanish to get by before the trip to Mexico in April",
      "Learn survival Spanish for the trip", "Get to functional Spanish before you fly",
      "MEDIUM", "LEARNING",
      "You can order food, ask directions and handle basic small talk without switching to English",
      [("Pick one app or course and stick with just that one", 15),
       ("Learn the survival phrases: greetings, please, thank you, asking for the bill", 20),
       ("Practise ordering food and asking directions out loud, not just reading them", 45),
       ("Record yourself running through a short conversation both sides", 45),
       ("Review the phrases that still don't come automatically", 30)],
      due="before the trip to Mexico in April"),

    G("Learn a bit of Punjabi so I'm not silent at every family dinner",
      "Learn some conversational Punjabi", "Pick up enough to join the family conversation",
      "LOW", "PERSONAL",
      "You can follow simple family conversation and say a few things back, even with mistakes",
      [("Write down the ten phrases you hear most often at dinner", 10),
       ("Learn what they mean and how to say them back", 20),
       ("Practise saying them out loud until they don't feel awkward", 30),
       ("Try using two or three of them at the next family dinner", 30),
       ("Add the phrases that came up but you didn't know", 20)]),

    G("Keep starting Being and Nothingness and giving up by chapter two",
      "Actually get through Being and Nothingness", "Build a reading habit that survives past chapter two",
      "LOW", "LEARNING",
      "You're getting further into the book than last time and can explain the last chapter you read",
      [("Find a reading guide or summary for the introduction so you're not lost from page one", 10),
       ("Reread the introduction properly, taking rough notes as you go", 15),
       ("Read one chapter in a single sitting rather than in fragments", 30),
       ("Write a few sentences summarising it before moving on", 20),
       ("Read the next chapter, referring back to your notes when it gets dense", 30)]),

    G("Want to finally get through Ulysses instead of it just sitting on the shelf",
      "Actually finish Ulysses", "Get properly past where the bookmark's been stuck",
      "LOW", "PERSONAL",
      "You're a good way further into the book than the bookmark that's been stuck at page forty for a year",
      [("Find a chapter-by-chapter guide so the structure makes sense", 10),
       ("Reread the opening chapter with the guide alongside it", 20),
       ("Read one more chapter in a single sitting", 40),
       ("Jot down what actually happened before you forget", 20),
       ("Read the next chapter, using the guide only when you're properly lost", 40)]),
]

# ---------------------------------------------------------------------------
# Courses paid for and stalled, and self-taught subjects
# ---------------------------------------------------------------------------
COURSES = [
    G("IELTS writing keeps scoring the same band no matter how many essays I write",
      "Improve the IELTS writing score", "Fix whatever's actually capping the writing band",
      "MEDIUM", "LEARNING",
      "You can write a band-appropriate essay in the time limit without stalling halfway through",
      [("Find your last practice essay and read the band descriptors against it", 15),
       ("Write one essay untimed, focusing only on structure", 30),
       ("Write a second essay timed, using the structure from the first", 40),
       ("Compare both against the band descriptors and note the recurring problem", 30),
       ("Write one more timed essay fixing only that one problem", 40)]),

    G("Paid two hundred pounds for that data science course in January and haven't opened it since week two",
      "Get back into the data science course", "Pick the paid course back up from where it stalled",
      "MEDIUM", "LEARNING",
      "You're back into the course material and have finished one more module than before",
      [("Log in and see exactly which module you stopped at", 10),
       ("Rewatch the last ten minutes of that module as a refresher", 20),
       ("Finish that module properly, including the exercises", 45),
       ("Do the next module in one sitting rather than in fragments", 45),
       ("Note a realistic day each week to come back to it", 15)]),

    G("Signed up for the UX design course, did module one, then just stopped",
      "Get back into the UX course", "Pick the course back up past module one",
      "LOW", "LEARNING",
      "You've picked the course back up and are past where you left off",
      [("Reopen the course and skim module one to remind yourself where you got to", 10),
       ("Do module two in one sitting", 30),
       ("Do the exercise for module two instead of skipping it", 30),
       ("Pick a fixed day each week to keep going instead of relying on motivation", 15)]),

    G("Need to actually understand statistics instead of just copying the formulas for my research methods module",
      "Actually understand statistics", "Build real understanding, not formula copying",
      "MEDIUM", "LEARNING",
      "You can explain what a p-value and a confidence interval actually mean, in your own words",
      [("Find one beginner resource and stick to it instead of ten different ones", 15),
       ("Work through the section on descriptive statistics and try the examples by hand", 30),
       ("Move on to probability once descriptive statistics actually makes sense", 40),
       ("Work through hypothesis testing, redoing any example that doesn't click first time", 40),
       ("Apply it to your own dataset instead of the textbook's", 30)]),

    G("Teaching myself statistics from scratch for the career change, don't know where to start",
      "Start teaching myself statistics", "Get a real beginning going instead of an open tab of options",
      "LOW", "LEARNING",
      "You've got a beginner resource picked and are through the first section without being lost",
      [("Look up two or three beginner statistics courses and pick one", 15),
       ("Do the first lesson and try the practice questions rather than just watching", 30),
       ("Redo any practice question you got wrong before moving on", 30),
       ("Do the second lesson in the same sitting style", 30)]),
]

# ---------------------------------------------------------------------------
# Deliberate practice — typing, music theory, chess
# ---------------------------------------------------------------------------
SKILLS_PRACTICE = [
    G("Still hunt-and-peck typing at thirty, want to actually learn to touch-type properly",
      "Learn to touch-type", "Get off hunt-and-peck and onto proper finger placement",
      "LOW", "LEARNING",
      "You're typing common words without looking at the keyboard, even if your speed is still slow",
      [("Find a typing course or site that teaches proper finger placement", 10),
       ("Learn the home row and do the first lesson without looking down", 15),
       ("Repeat the home row lesson a couple more times until it stops feeling foreign", 20),
       ("Move on to the next row only once the home row feels automatic", 20),
       ("Type something real, like an email, resisting the urge to look down", 20)]),

    G("Need faster, accurate typing for the transcription work but haven't practised beyond the basics",
      "Build typing speed for transcription work", "Get speed and accuracy both up before it matters day to day",
      "HIGH", "LEARNING",
      "Your speed and accuracy are both trending up on the practice tests you're taking",
      [("Take a typing speed test to see where you're actually starting from", 10),
       ("Do a short accuracy-focused drill rather than typing fast and sloppy", 20),
       ("Repeat the same drill until the error rate drops, not just the time", 20),
       ("Move to a harder drill only once accuracy is solid", 25),
       ("Take the speed test again and compare it to the first one", 15)]),

    G("Been playing piano by ear for years and want to finally understand the theory behind it",
      "Learn the theory behind piano playing", "Connect what you already play by ear to the theory underneath",
      "LOW", "LEARNING",
      "You can name the intervals and chords in something you already play, even slowly",
      [("Find one beginner theory resource instead of ten different articles", 10),
       ("Learn the major scale and how intervals are counted", 20),
       ("Work out the intervals in a piece you already know by ear", 25),
       ("Learn how basic triads are built from those intervals", 30),
       ("Find the triads in the same piece and label them", 30)]),

    G("Grade 5 theory exam prep keeps stalling, only three chapters in",
      "Get grade 5 theory prep moving again", "Pick the syllabus back up from chapter three",
      "MEDIUM", "LEARNING",
      "You're getting most of a past paper right, even if a couple of question types still trip you up",
      [("Check which chapters the exam actually draws questions from", 15),
       ("Work through the next chapter and its exercises", 35),
       ("Work through the chapter after that", 35),
       ("Do a past paper and mark it properly", 30),
       ("Go back over whichever question type you got wrong most", 30)]),

    G("Want to get actually good at chess instead of just losing to the computer on easy",
      "Get properly better at chess", "Learn the patterns instead of just playing on instinct",
      "LOW", "LEARNING",
      "You can spot basic tactics like forks and pins in your own games, even if you still lose",
      [("Learn the names and shapes of the basic tactics: forks, pins, skewers", 10),
       ("Go through ten quick puzzles on just forks and pins", 30),
       ("Play one game against a weak opponent, trying to spot those patterns", 30),
       ("Review the game afterwards and find where you missed one", 20),
       ("Do another puzzle set on whatever you missed", 30)]),

    G("Club championship is coming and my opening repertoire is basically nothing",
      "Build an opening repertoire before the club championship", "Get one real opening ready instead of improvising every game",
      "MEDIUM", "LEARNING",
      "You've got one opening as white and one response as black that you actually understand, not just memorised moves",
      [("Pick one opening for white and one reply for black to focus on", 15),
       ("Learn the first few moves and the idea behind them, not just the sequence", 30),
       ("Play through a few example games in that opening to see the ideas in practice", 40),
       ("Play a few games using it and note where you went off book", 45),
       ("Look up what you should have played at the point you went off book", 30)]),
]

# ---------------------------------------------------------------------------
# Career-adjacent learning — certifications, codebases, talks, study routines
# ---------------------------------------------------------------------------
CAREER = [
    G("Work wants the AWS certification done and I keep starting the course material and stalling",
      "Get moving on the AWS certification", "Actually get through the course material this time",
      "MEDIUM", "LEARNING",
      "You're passing timed practice exams comfortably above the pass mark",
      [("Check the exam guide and note which domains carry the most weight", 15),
       ("Work through the official course material for the heaviest domain", 45),
       ("Do a practice exam and see where the wrong answers cluster", 45),
       ("Study just the domains behind those wrong answers", 45),
       ("Do a second timed practice exam and repeat on whatever is still weak", 60)]),

    G("Been meaning to get the PRINCE2 certification done for two years, keep not starting",
      "Actually start the PRINCE2 certification", "Get the study material open and moving after years of putting it off",
      "LOW", "LEARNING",
      "You've started the course material and know the structure of the exam, even if you're not through it yet",
      [("Book onto the course or buy the study material, whichever you keep putting off", 15),
       ("Read the first module and note what the exam actually tests", 30),
       ("Work through the practice questions for that module", 45),
       ("Set a realistic date for the exam now you know the scope", 30)]),

    G("Literature review for the dissertation is due in a month and I've got forty tabs open and nothing written",
      "Get the literature review drafted", "Turn the open tabs into an actual structured draft",
      "HIGH", "LEARNING",
      "There's a structured draft covering the main themes, even if some papers still need chasing down",
      [("Close the browser tabs and list the papers you've actually already read", 15),
       ("Sort them into the two or three themes they actually fall under", 30),
       ("Write a rough paragraph summarising the first theme from your notes", 45),
       ("Write the paragraph for the second theme", 45),
       ("Write the paragraph for the third theme and note the gaps still to fill", 45),
       ("Read back through and add the transitions between themes", 30)],
      due="in a month"),

    G("Supervisor wants a lit review draft by our next meeting and I've barely started reading",
      "Draft the literature review before the meeting", "Get a rough draft together from what's been read so far",
      "HIGH", "LEARNING",
      "There's a written draft covering what's been read, with clear gaps flagged rather than papers still open in tabs",
      [("List the papers already read and skim-sort them into themes", 15),
       ("Read the two or three papers that are clearly central but still unread", 40),
       ("Write a rough section per theme from your notes", 45),
       ("Note which themes are thin and need more reading", 30),
       ("Send the draft ahead of the meeting so there's something to react to", 20)],
      due="by our next meeting"),

    G("Giving the conference talk in three weeks and haven't rehearsed it once",
      "Rehearse the conference talk", "Get the talk out loud before it's out loud for the first time on stage",
      "HIGH", "LEARNING",
      "You can get through the talk without reading from notes for most of it, even if timing is a bit off",
      [("Read through the slides once and note where you'll need to explain more", 15),
       ("Say the talk out loud alone, working out the rough timing", 30),
       ("Practise just the two sections that felt shakiest", 35),
       ("Run through the whole talk again, timing it properly", 35),
       ("Record yourself once and watch back for anything distracting", 30)],
      due="in three weeks"),

    G("Best man speech is at the wedding in five weeks and I keep avoiding writing it",
      "Write and practise the best man speech", "Get a draft written and rehearsed before the wedding",
      "MEDIUM", "PERSONAL",
      "You can read through the speech without wanting to change most of the lines, and it fits the time you've got",
      [("Jot down three stories or moments you actually want to include", 15),
       ("Write a rough draft straight through without editing", 30),
       ("Read it aloud once and time it", 20),
       ("Cut it down if it runs long, or practise the transitions if it doesn't", 25),
       ("Read it aloud again from memory as much as you can manage", 20)],
      due="in five weeks"),

    G("Joining a new team and want a head start on their codebase before I'm useless in standup",
      "Get a head start on the new codebase", "Learn enough of the codebase before you're expected to know it",
      "MEDIUM", "LEARNING",
      "You can find your way around the main modules and roughly explain what talks to what",
      [("Get repo access sorted and clone it locally", 15),
       ("Read the README and get it running locally", 20),
       ("Trace one real user action through the code, module by module", 40),
       ("Skim the test suite to see how the team expects things to be checked", 40),
       ("Write yourself a short map of the main modules and what each does", 30)]),

    G("Inherited the reporting service at work and it's a black box to me so far",
      "Learn the inherited reporting service", "Turn the black box into something you could actually debug",
      "HIGH", "LEARNING",
      "You can trace a request through the main path and know where you'd start for a bug",
      [("Get it running locally and confirm you can hit it", 15),
       ("Read through the entry point and trace one endpoint end to end", 30),
       ("Look at the last ten commits to see what actually gets touched often", 30),
       ("Pick one small known issue and use it as an excuse to dig into that part properly", 40),
       ("Write yourself notes on what confused you, to reread later", 20)]),

    G("Want to actually study for the qualification instead of it always losing to work",
      "Build a study routine around the job", "Find study time that survives a bad week at work",
      "MEDIUM", "LEARNING",
      "You've got a slot in the week that survived a bad week at work, even if it moved",
      [("Look honestly at which evenings or mornings are actually free most weeks", 10),
       ("Pick two slots rather than an ambitious five", 15),
       ("Protect the first slot this week, even if the session is short", 30),
       ("Protect the second slot, moving it rather than skipping it if work eats it", 30),
       ("Review at the end of the week what actually happened and adjust the slots", 15)]),

    G("Every time I try to build a study habit it survives about a week before work swallows it again",
      "Make the study habit survive past week one", "Work out what actually kills it and study around that",
      "LOW", "LEARNING",
      "The routine has made it through one bad week without falling apart",
      [("Write down what actually killed the habit last time", 10),
       ("Pick one slot a realistic bad week couldn't easily take", 15),
       ("Do a short session in that slot this week, on purpose keeping it small", 30),
       ("Do it again next week even if the first week was patchy", 30),
       ("Notice which week it survived and repeat exactly that setup", 20)]),
]

# ---------------------------------------------------------------------------
# Hands-on life skills — swimming, first aid, cooking a cuisine, memorising a script
# ---------------------------------------------------------------------------
LIFE_SKILLS = [
    G("Never learned to swim properly and thirty-four feels like a stupid age to start",
      "Learn to swim as an adult", "Get comfortable in the water from a standing start",
      "LOW", "LEARNING",
      "You can get from one end of the shallow end to the other without stopping or panicking",
      [("Find a beginner adult class or a quiet pool session to start in", 15),
       ("Go once and just get comfortable putting your face in the water", 15),
       ("Go again and practise floating and basic kicking in the shallow end", 30),
       ("Repeat the same drills a couple more times before trying anything new", 30),
       ("Try a few strokes across the shallow end once floating feels easy", 30)]),

    G("Family beach holiday is in ten weeks and I still can't swim a length",
      "Learn to swim a length before the holiday", "Get from not swimming to one steady length",
      "MEDIUM", "PERSONAL",
      "You can swim a length slowly without needing to stop halfway",
      [("Book a couple of pool sessions for this week and next", 15),
       ("Practise the stroke you're most comfortable with in the shallow end", 30),
       ("Try a length, stopping to rest partway if you need to", 30),
       ("Repeat a few more lengths the same way before trying to go faster", 30),
       ("Try one length without stopping", 30)],
      due="in ten weeks"),

    G("Workplace first aid course is in two weeks and I haven't looked at the pre-reading",
      "Get through the first aid pre-reading", "Go into the course already knowing the basics",
      "HIGH", "LEARNING",
      "You've been through the pre-reading once and could describe the basics without the book in front of you",
      [("Find the pre-reading material the course sent over", 10),
       ("Read the section on primary survey and checking a casualty", 30),
       ("Read the section on CPR and choking", 30),
       ("Try explaining both sections out loud without looking at the page", 25),
       ("Skim back over whichever one you fumbled", 20)],
      due="in two weeks"),

    G("Had the baby three months ago and still haven't done the infant first aid course I meant to book before she arrived",
      "Get the infant first aid course sorted", "Get booked on and get the basics learned",
      "MEDIUM", "PERSONAL",
      "The course is booked, or you've been through the basics some other way, whichever comes first",
      [("Look up infant first aid courses running nearby or online", 15),
       ("Book onto the one that fits your week", 15),
       ("Read through the choking and CPR basics before the session so it's not all new", 30),
       ("Practise the choking technique on the course's model if it provides one", 20)]),

    G("Want to actually learn Thai cooking instead of just getting a takeaway every time I fancy it",
      "Learn to cook Thai food properly", "Build a small repertoire instead of relying on takeaway",
      "LOW", "PERSONAL",
      "You can cook two or three Thai dishes without the recipe open the whole time",
      [("Pick two or three dishes you actually want to eat regularly", 15),
       ("Track down the ingredients that aren't in a normal supermarket", 20),
       ("Cook the first dish closely following the recipe", 60),
       ("Cook it again a few days later, checking the recipe less", 60),
       ("Cook the second dish the same way", 60)]),

    G("Grandmother's Sicilian recipes only exist in her head and I want to actually learn them before it's too late",
      "Learn grandmother's Sicilian recipes", "Get the recipes out of her head and onto paper while you still can",
      "MEDIUM", "PERSONAL",
      "You've cooked one recipe alongside her and written down what she actually does, not just what she says",
      [("Pick the one dish to start with and arrange a time to cook it together", 15),
       ("Watch and note quantities as she cooks, since the recipe is all by eye", 20),
       ("Cook it alongside her, asking questions as you go", 90),
       ("Write the recipe up properly while it's fresh in your memory", 30),
       ("Cook it alone from your notes and compare", 90)]),

    G("Play opens in three weeks and I still don't know act two",
      "Memorise act two of the play", "Get off-book for act two before opening night",
      "URGENT", "LEARNING",
      "You can get through act two with only the odd prompt needed",
      [("Read through act two once with the script in hand", 15),
       ("Learn the first half of the act line by line", 30),
       ("Run the first half without the script, checking only when stuck", 30),
       ("Learn the second half the same way", 30),
       ("Run the whole act without the script, checking only when stuck", 30)],
      due="in three weeks"),

    G("Writing and memorising the vows for the wedding in seven weeks, haven't started either",
      "Write and memorise the wedding vows", "Get from nothing to vows you can say from memory",
      "MEDIUM", "PERSONAL",
      "You can say the vows out loud from memory without needing the paper as a safety net most of the way through",
      [("Jot down the moments and feelings you actually want to include", 15),
       ("Write a full draft straight through without editing", 30),
       ("Read it aloud a few times and trim anything that doesn't sound like you", 20),
       ("Learn the first half by repeating it aloud until it sticks", 30),
       ("Learn the second half the same way", 30),
       ("Run the whole thing from memory, glancing at the paper only when stuck", 20)],
      due="in seven weeks"),
]

GOLD: list[Gold] = EXAMS + LANGUAGE_AND_READING + COURSES + SKILLS_PRACTICE + CAREER + LIFE_SKILLS
