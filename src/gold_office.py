"""Gold examples: office and knowledge work (hand-authored).

The deadline-dense professional slice: board papers, workshops, difficult
conversations, handovers, pitches, hiring, incident postmortems, quarterly
planning. Deliberately carries most of the corpus's WORK and HIGH/URGENT
weight, since that combination is otherwise underrepresented — and carries a
deliberate pocket of LOW-priority WORK too (a tidied wiki page, an idea
someone means to write up "eventually"), which the wider corpus otherwise has
almost none of.

See `goldlib.Gold` for the format and `quality.py` for the rules every example
must pass.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from goldlib import Gold

G = Gold

# ---------------------------------------------------------------------------
# Board papers, memos, decisions
# ---------------------------------------------------------------------------
BOARD = [
    G("Pull together the board paper for Tuesday's meeting",
      "Prepare the board paper", "Write and format the paper for the board meeting",
      "HIGH", "WORK",
      "The paper covers the decision the board needs to make and the numbers behind it, in a form they can skim",
      [("Reread last quarter's board paper for the format they expect", 15),
       ("List the two or three points this paper needs to make", 15),
       ("Draft the narrative section around those points", 60),
       ("Pull the supporting figures into a chart or table", 40),
       ("Read it through once and circulate it ahead of the meeting", 20)],
      due="Tuesday's meeting"),

    G("Write the memo arguing we should reverse the office-days policy before it does more damage to retention",
      "Write the policy reversal memo", "Make the case for reversing the office-days policy",
      "HIGH", "WORK",
      "The memo lays out the evidence and the specific change you want, in something a reader will actually finish",
      [("Note the two or three data points that actually move this argument", 15),
       ("Draft the opening paragraph stating the change you want plainly", 20),
       ("Build the case underneath it with the evidence in order of strength", 45),
       ("Cut anything that isn't load-bearing to the argument", 25),
       ("Have someone outside the debate read it and flag where they got bored", 20)]),

    G("Chase the sign-off on the vendor contract that's been sitting with legal for three weeks",
      "Chase the stuck contract sign-off", "Get the vendor contract moving again",
      "MEDIUM", "WORK",
      "A direct question has gone to whoever is holding it and you have a date for a response",
      [("Check the contract portal for where it's actually stuck", 10),
       ("Write a short note asking what's blocking it and by when they can look", 15),
       ("Send it to the specific person holding it, not the general inbox", 5),
       ("Diary a follow-up for the date they gave you", 5)]),

    G("The decision on the pricing change has been sitting unmade for a month and everyone's just working around it",
      "Chase the stalled pricing decision", "Get someone to actually decide",
      "LOW", "WORK",
      "The decision has a named owner and a date attached, even if the answer itself is still pending",
      [("Write down what the decision actually needs to settle", 15),
       ("Note who has the authority to make the call", 10),
       ("Ask them directly for a decision or a date by which they'll give one", 15)]),
]

# ---------------------------------------------------------------------------
# Workshops, pitches, demos
# ---------------------------------------------------------------------------
PRESENT = [
    G("Run a workshop for the new starters on how the planning process actually works",
      "Run the new-starter planning workshop", "Design and deliver the workshop",
      "MEDIUM", "WORK",
      "The room understands the process well enough to follow it next sprint, questions answered",
      [("Write down the two things people need to be able to do afterwards", 15),
       ("Sketch an agenda with a short exercise, not just slides", 25),
       ("Build the slides and the exercise handout", 60),
       ("Do a dry run out loud and time it", 20),
       ("Deliver the session and leave time for questions", 60)]),

    G("Prepare the workshop for the client visit next Wednesday, I haven't started",
      "Prepare the client workshop", "Design and prepare materials for the client workshop",
      "HIGH", "WORK",
      "The agenda and materials exist and cover what the client asked to work through",
      [("Reread the client's brief for what they actually want out of the session", 15),
       ("Draft an agenda with rough timings for each segment", 20),
       ("Build the slides and any worksheets the exercises need", 75),
       ("Print or share the materials and confirm the room and equipment", 20)],
      due="next Wednesday"),

    G("Put the pitch together for the client renewal meeting",
      "Prepare the client renewal pitch", "Build the case for the client to renew",
      "MEDIUM", "WORK",
      "The pitch covers what they got this year and what's next, and answers the renewal question directly",
      [("Pull the results and usage numbers from this year", 15),
       ("Note the two things they've complained about and how you'll address them", 20),
       ("Draft the slides telling that story in order", 60),
       ("Rehearse it once against the clock", 25)]),

    G("Build the pitch deck for the new client, we present Thursday and I keep putting the first slide off",
      "Build the client pitch deck", "Get the pitch deck ready to present",
      "URGENT", "WORK",
      "The deck exists end to end and tells a clear story, even if a slide or two is rougher than you'd like",
      [("Write the one sentence the pitch has to land", 15),
       ("Outline the slide sequence on paper before opening the deck tool", 20),
       ("Build the opening and closing slides first, since they matter most", 40),
       ("Fill in the slides between them", 60),
       ("Run through it once against the clock", 20)],
      due="Thursday"),

    G("Get the demo ready for leadership tomorrow, the feature's barely working",
      "Prepare tomorrow's leadership demo", "Get a working demo path ready to show",
      "URGENT", "WORK",
      "One path through the feature works reliably end to end, even if the edges are rough",
      [("Decide the exact path you'll click through, nothing more", 10),
       ("Test that path start to finish and note where it breaks", 20),
       ("Fix or work around whatever breaks on that specific path", 60),
       ("Run through it three times until it's boring", 30),
       ("Write one line of fallback if something fails live", 10)],
      due="tomorrow"),

    G("Prepare the internal show-and-tell demo for Friday, it's low-key but I still haven't looked at it",
      "Prepare the internal demo", "Put together a short demo for the team show-and-tell",
      "LOW", "WORK",
      "You can show the thing working and say what it does, without needing a polished script",
      [("Pick the two features actually worth showing", 10),
       ("Get the environment into a state that won't break mid-demo", 20),
       ("Run through it once so you know what to click", 15)],
      due="Friday"),
]

# ---------------------------------------------------------------------------
# Managing people: reviews, 1:1s, onboarding, job descriptions, applications
# ---------------------------------------------------------------------------
PEOPLE_OFFICE = [
    G("Write the performance review for my direct report before calibration next week",
      "Write the performance review", "Write a fair, specific review of the year",
      "HIGH", "WORK",
      "The review names specific pieces of work and outcomes and reads as something they'd recognise themselves in",
      [("Look back through notes and delivery records for the year", 15),
       ("List four or five concrete examples with the outcome next to each", 40),
       ("Draft the strengths section around those examples", 30),
       ("Draft the growth areas as specific and actionable, not vague", 30),
       ("Read it back as if you were the one receiving it", 20)],
      due="before calibration next week"),

    G("I've been avoiding writing Sam's review since Monday, it's overdue now",
      "Write Sam's overdue review", "Get the review written and out of the drafts folder",
      "HIGH", "WORK",
      "The review is written, specific and sent, even a week later than planned",
      [("Reread the goals that were set at the start of the period", 15),
       ("Note what was actually delivered against each one", 25),
       ("Draft the review straight through without polishing each line", 45),
       ("Read it once for tone and send it", 20)]),

    G("Have the difficult conversation with someone on the team about missed deadlines that I keep pushing to next week",
      "Have the difficult deadline conversation", "Raise the missed-deadline pattern directly",
      "MEDIUM", "WORK",
      "The pattern has been named clearly and you've agreed what changes from here",
      [("Write down the specific dates that were missed, not a general impression", 15),
       ("Decide the one change you actually want to see", 10),
       ("Book time that isn't squeezed between other things", 5),
       ("Have the conversation and listen to their side before deciding anything", 40)]),

    G("Prepare for the awkward 1:1 about the attitude in meetings that everyone's noticed but no one's said",
      "Prepare for the awkward 1:1", "Get ready to raise the meeting behaviour directly",
      "HIGH", "WORK",
      "You have two or three specific examples ready and know how you want to open the conversation",
      [("Write down two or three specific moments, not a general vibe", 15),
       ("Decide the outcome you actually want from the conversation", 10),
       ("Draft the opening line so you don't waffle into it", 10),
       ("Book the 1:1 for somewhere private", 5)]),

    G("Hand the project over properly before I go on leave, I always leave this to the last afternoon",
      "Hand over the project before leave", "Get someone else able to run this while you're away",
      "HIGH", "WORK",
      "Whoever covers it can find what they need without messaging you on leave",
      [("List everything with a deadline that falls while you're away", 15),
       ("Write a short status note for each: where it stands, what's next", 40),
       ("Note the passwords, access and contacts they'll actually need", 20),
       ("Walk whoever's covering through it out loud, not just by document", 30),
       ("Set an out-of-office that points to them by name", 10)]),

    G("Write the handover notes for maternity cover, I keep starting the document and closing it again",
      "Write the maternity cover handover", "Document the role so cover can pick it up",
      "MEDIUM", "WORK",
      "The document covers what someone needs to function in the role from day one, refined later as gaps show up",
      [("List the recurring things you do weekly and monthly", 15),
       ("Write up each one as a short how-to, not a full manual", 65),
       ("Note who to go to for what you can't write down", 20),
       ("Have your cover read it and ask what's missing", 25)]),

    G("Write the job description for the role we're finally allowed to hire",
      "Write the job description", "Draft the role description for the open position",
      "MEDIUM", "WORK",
      "The description is clear enough that a reasonable applicant knows what the job actually involves",
      [("List what the role will actually spend its time on", 15),
       ("Separate that into must-have and nice-to-have requirements", 15),
       ("Draft the description around the real day-to-day, not a wishlist", 40),
       ("Get a second pair of eyes on it before it's posted", 20)]),

    G("Get through the pile of applications, we said we'd shortlist by Friday",
      "Sift the job applications", "Get to a shortlist from the applicant pile",
      "HIGH", "WORK",
      "There's a shortlist with a reason jotted against the name, even if some calls were close",
      [("Set the two or three must-haves you'll screen against", 15),
       ("Do a fast first pass, sorting into yes, no and maybe", 60),
       ("Read the maybes properly and move them into yes or no", 45),
       ("Write one line of reasoning against each shortlisted name", 20)],
      due="by Friday"),

    G("Read through the applications for the graduate role, there are way more than I expected",
      "Read the graduate applications", "Work through the applicant pile to a first cut",
      "MEDIUM", "WORK",
      "A first cut exists that removes the clear no's, even if the strong ones need a second look later",
      [("Reread the role's must-haves before starting", 10),
       ("Skim each application against those must-haves", 90),
       ("Set aside the clear no's with one reason each", 20),
       ("Flag the strongest few for a closer read", 20)]),

    G("New starter begins Monday and I haven't touched the onboarding plan",
      "Prepare the new starter's onboarding", "Get their first week actually planned",
      "HIGH", "WORK",
      "Their first day has a plan, access works, and someone is assigned to answer questions",
      [("Request their accounts and equipment today so access is ready", 15),
       ("Draft a rough plan for the first week, not just the first day", 25),
       ("Line up someone to be their point of contact for questions", 15),
       ("Book the introductions they'll need in the first few days", 20),
       ("Send them a short welcome note with what to expect Monday", 15)],
      due="Monday"),

    G("Sort out the desk, laptop and system access for the new starter before she arrives",
      "Set up the new starter's access", "Get the practical basics ready before day one",
      "MEDIUM", "WORK",
      "The desk, laptop and logins work on arrival, even if a minor permission needs sorting later",
      [("Confirm the start date and which systems she'll need", 10),
       ("Request the laptop and desk setup", 15),
       ("Submit the access requests for the systems she'll need", 20),
       ("Test the logins yourself before she starts if you can", 15)]),
]

# ---------------------------------------------------------------------------
# Planning, budgets, forecasting
# ---------------------------------------------------------------------------
PLANNING = [
    G("Build the budget forecast for next fiscal year, finance wants a first draft by the end of the month",
      "Build next year's budget forecast", "Draft the coming year's budget",
      "HIGH", "WORK",
      "The forecast has numbers against the main lines with a stated assumption behind anything non-obvious, ready to be challenged",
      [("Pull this year's actuals as the starting baseline", 15),
       ("List what's changing next year that would move any line", 20),
       ("Draft the numbers line by line against those assumptions", 60),
       ("Write one line of assumption next to anything that isn't obvious", 25),
       ("Sanity check the total against last year's before sending it on", 15)],
      due="by the end of the month"),

    G("Revise the department budget now the headcount's changed",
      "Revise the department budget", "Update the budget for the new headcount",
      "MEDIUM", "WORK",
      "The revised numbers reflect the actual headcount and the total is defensible if someone asks",
      [("Get the confirmed new headcount numbers", 10),
       ("Update the salary and related lines against them", 30),
       ("Check knock-on lines like equipment and travel", 20),
       ("Note what changed and why, for whoever asks", 15)]),

    G("Do the quarterly planning for next quarter, the team's expecting priorities by the planning meeting",
      "Do quarterly planning", "Set next quarter's priorities",
      "HIGH", "WORK",
      "There's a short, ordered list of priorities that people can actually plan their work against",
      [("Review what did and didn't get done this quarter", 15),
       ("List the candidate priorities from requests and the backlog", 30),
       ("Cut the list down to what can realistically get done", 30),
       ("Order what's left and write one line of why for each", 25),
       ("Share it and take the obvious pushback before it's final", 30)],
      due="the planning meeting"),

    G("Review the roadmap for next quarter, half of it is already out of date",
      "Review next quarter's roadmap", "Update the roadmap to reflect reality",
      "MEDIUM", "WORK",
      "The roadmap matches what's actually likely to happen, even if some dates are now ranges",
      [("Go through the roadmap and mark each item done, live or dead", 15),
       ("Update the dates on what's still live", 40),
       ("Remove or archive what's dead rather than leaving it looking active", 15),
       ("Circulate the updated version", 15)]),

    G("Negotiate a deadline extension for the report, there's no way it's ready by tomorrow",
      "Negotiate the report deadline", "Get a realistic new date agreed",
      "URGENT", "WORK",
      "A new date is agreed and confirmed in writing, even if it's not the date you'd have liked",
      [("Work out honestly how much more time you actually need", 10),
       ("Note what's realistically done versus what's left", 10),
       ("Ask for the extension with a specific new date, not just more time", 15)],
      due="tomorrow"),
]

# ---------------------------------------------------------------------------
# Incidents, endings, meeting hygiene
# ---------------------------------------------------------------------------
OPS = [
    G("Write the postmortem for yesterday's outage before it gets forgotten",
      "Write the outage postmortem", "Document what happened and what changes",
      "URGENT", "WORK",
      "The timeline and root cause are written down and at least one concrete follow-up is named",
      [("Pull the timeline together from logs and alerts", 15),
       ("Write what happened in plain order, no blame language", 40),
       ("Identify the root cause, not just the trigger", 30),
       ("List the follow-up actions that would actually prevent a repeat", 25),
       ("Share it with whoever needs to know before it goes cold", 15)],
      due="before it gets forgotten"),

    G("Write up the near-miss from last week, nothing broke but it easily could have",
      "Write up the near-miss", "Document what almost went wrong",
      "MEDIUM", "WORK",
      "The near-miss is written down with what stopped it becoming worse, and one thing to fix",
      [("Reconstruct what actually happened, from whoever was involved", 15),
       ("Note what stopped it turning into a real incident", 25),
       ("Write one concrete thing to change so it's less likely again", 20)]),

    G("Kill the internal tool project properly instead of letting it quietly die",
      "Wind down the internal tool project", "Close the project down and say so clearly",
      "HIGH", "WORK",
      "Everyone using or watching the project knows it's stopped, why, and what to do instead",
      [("Write down the actual reason it's stopping", 15),
       ("List who's using it and what they'll need instead", 20),
       ("Draft a short note explaining the decision plainly", 25),
       ("Send the note and update wherever the project is tracked as active", 20),
       ("Archive the repository or documents so it doesn't look live", 15)]),

    G("Write up notes from today's planning meeting that people will actually read this time",
      "Write readable meeting notes", "Turn today's meeting into notes worth reading",
      "MEDIUM", "WORK",
      "The notes are short enough to read in a minute and say clearly who's doing what by when they said",
      [("Reread your scrawled notes while the meeting is still fresh", 10),
       ("Pull out only the decisions and actions, dropping the discussion", 15),
       ("Write each action against a named owner", 15),
       ("Send it the same day, before anyone forgets what they agreed", 10)]),

    G("Cut the standing meeting series down, we've got four recurring calls that could be one",
      "Cut the bloated meeting series", "Consolidate the recurring meetings",
      "LOW", "WORK",
      "The recurring calendar is shorter and covers the same ground, even if one person grumbles",
      [("List what each recurring meeting actually decides or unblocks", 15),
       ("Mark which ones genuinely overlap in purpose", 20),
       ("Propose merging or cancelling the overlapping ones", 20),
       ("Update the calendar invites once people have agreed", 15)]),

    G("Prepare for the audit next month, I don't even know where half the evidence lives",
      "Prepare for the audit", "Get the evidence together before the auditors arrive",
      "HIGH", "WORK",
      "The requested evidence is gathered in one place and you know where the gaps are before they ask",
      [("Get the list of what the audit will actually ask for", 15),
       ("Work out which items you already have and where they live", 25),
       ("Chase down the items that are missing or scattered", 60),
       ("Put everything in one folder organised against the request list", 30),
       ("Do a dry run through the list as if you were the auditor", 25)],
      due="next month"),
]

# ---------------------------------------------------------------------------
# Expenses, admin, and the low-stakes office tasks nobody prioritises
# ---------------------------------------------------------------------------
OFFICE_ADMIN = [
    G("Submit the expenses from the conference trip before finance closes the month",
      "Submit the conference expenses", "Claim back what was spent on the trip",
      "MEDIUM", "WORK",
      "The claim is submitted with receipts attached against the categories finance uses",
      [("Gather the receipts from the trip into one place", 15),
       ("Sort them against the expense categories", 15),
       ("Fill in the claim form line by line", 25),
       ("Attach the receipts and submit it", 10)],
      due="before finance closes the month"),

    G("Do the expenses claim from that trip in March, I still haven't got round to it",
      "Do the overdue expenses claim", "Finally claim back the March trip costs",
      "LOW", "WORK",
      "The claim goes in with whatever receipts you can still find, even a partial one is better than none",
      [("Dig out whatever receipts and card statements survived", 15),
       ("Match what you can to the trip and note anything missing", 20),
       ("Fill in the claim form with what you've got", 20),
       ("Submit it and flag the gaps rather than waiting to fill them", 10)]),

    G("Tidy up the team wiki, half the pages are years out of date and it winds me up every time I open it",
      "Tidy the team wiki", "Clean up the stale wiki pages",
      "LOW", "WORK",
      "The obviously wrong pages are fixed or archived, even if some tidying is left for another pass",
      [("Skim the page list and flag anything obviously out of date", 15),
       ("Archive or delete the pages nobody needs any more", 25),
       ("Update the handful that are wrong in a way that actually misleads people", 40)]),

    G("Write up the process improvement idea I keep meaning to properly document",
      "Write up the process improvement idea", "Get the idea out of your head and onto a page",
      "LOW", "WORK",
      "The idea exists as a written page someone else could read and understand, ready to pitch later",
      [("Write the problem it solves in two or three sentences", 10),
       ("Sketch the proposed change in rough bullet points", 20),
       ("Note the obvious objections and your answer to each", 20),
       ("Save it somewhere findable rather than in a random notes app", 5)]),

    G("Reply to the escalation email before it goes further up, it's been sitting since this morning",
      "Reply to the escalation email", "Get a response out before it escalates further",
      "URGENT", "WORK",
      "A clear reply has gone out addressing the specific complaint, even if the full fix comes later",
      [("Reread the email and note exactly what's being asked", 10),
       ("Check the facts before promising anything", 15),
       ("Draft a short, direct reply addressing the actual complaint", 15),
       ("Send it and note anywhere else it needs flagging", 10)]),

    G("Archive the old project folders that are cluttering the shared drive",
      "Archive the old project folders", "Clear finished projects out of the active drive",
      "LOW", "WORK",
      "The finished projects are moved out of the active space and still findable if anyone needs them",
      [("List the projects that have actually finished or stalled for good", 15),
       ("Check nothing in them is still being referenced", 15),
       ("Move them into an archive folder with a clear naming pattern", 30),
       ("Update any links that pointed to the old location", 15)]),

    G("Write the runbook for on-call handover before the rota changes over next week",
      "Write the on-call runbook", "Document what the on-call handover actually needs",
      "MEDIUM", "WORK",
      "The runbook covers the steps someone unfamiliar would need to get through a normal shift",
      [("List the recurring alerts and what each one actually means", 15),
       ("Write the response steps for the two or three most common ones", 50),
       ("Note who to escalate to and when", 15),
       ("Have someone on the current rota check it for gaps", 20)],
      due="before the rota changes over next week"),

    G("Consolidate the two overlapping trackers the team's been double-entering into for months",
      "Consolidate the overlapping trackers", "Merge the two trackers into one",
      "MEDIUM", "WORK",
      "One tracker holds the live items and everyone knows the other is retired",
      [("Compare the two trackers and note what's duplicated", 15),
       ("Decide which one becomes the single source", 20),
       ("Migrate the items that only exist in the other one", 40),
       ("Archive the retired tracker and point people to the survivor", 15)]),
]

GOLD: list[Gold] = BOARD + PRESENT + PEOPLE_OFFICE + PLANNING + OPS + OFFICE_ADMIN
