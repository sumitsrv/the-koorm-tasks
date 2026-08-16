"""Gold examples: software engineering & technical work (hand-authored).

Distinct from gold_tech.py, which is consumer/personal tech (new phones,
home wifi, password managers). This module is the job itself: the flaky
test, the memory leak, the dependency upgrade, the migration nobody wants
to write, the production incident, the PR review, the release.

The point of this domain is prerequisite ordering done right by an engineer
who has been burned before: reproduce before you fix, write the failing
test before the patch, back up before the migration, check the rollback
path before deploying, measure before optimising. See `quality.py` for the
rules every example must pass.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from goldlib import Gold

G = Gold

# ---------------------------------------------------------------------------
# Bugs, incidents, flaky tests — reproduce before you fix
# ---------------------------------------------------------------------------
DEBUG = [
    G("Track down why the checkout test fails about one run in twenty, need it stable before the release freeze on Friday",
      "Fix the flaky checkout test", "Find and remove the source of the intermittent failure",
      "MEDIUM", "WORK",
      "The test has passed twenty runs in a row locally and the fix explains why it was flaky",
      [("Run the test in a loop locally to catch it failing", 15),
       ("Read the failure output and note what differs on the bad runs", 20),
       ("Add logging or a debugger around the suspect step", 25),
       ("Reproduce it reliably by forcing the timing that triggers it", 40),
       ("Fix the race or wait condition and rerun the loop to confirm", 45)],
      due="before the release freeze on Friday"),

    G("Users are reporting the app slowly eating memory until it crashes after a few hours, needs fixing before next week's store submission",
      "Track down the memory leak", "Find what is retaining memory and stop it",
      "HIGH", "WORK",
      "The suspect object stops growing in a profiler session and you have a named cause",
      [("Reproduce the growth locally by leaving the app running", 15),
       ("Take a heap snapshot early and another after it has grown", 30),
       ("Diff the snapshots for the object type that keeps climbing", 30),
       ("Trace what is holding a reference to it", 45),
       ("Remove the reference or close the resource and confirm the graph flattens", 40)],
      due="before next week's store submission"),

    G("The payment service is throwing 500s in production right now",
      "Respond to the payment service outage", "Restore the payment service and understand why it broke",
      "URGENT", "WORK",
      "Requests are succeeding again and you have a rough idea of the trigger, even before the writeup",
      [("Check the dashboards to confirm scope and impact", 10),
       ("Look at recent deploys and changes for anything that lines up", 10),
       ("Roll back the most likely change or fail over", 15),
       ("Confirm requests are succeeding again", 10),
       ("Note the timeline and suspected cause while it is fresh", 15)]),

    G("The nightly import job has been silently dropping rows for a week and nobody noticed until finance flagged it",
      "Fix the silent data drop in the nightly import", "Stop the import from losing rows and recover what it dropped",
      "HIGH", "WORK",
      "New runs import the expected row count and the missing week has been backfilled",
      [("Pull a recent run's logs and skim the row counts", 15),
       ("Compare rows in versus rows written stage by stage", 25),
       ("Narrow down which stage of the pipeline drops the rows", 30),
       ("Reproduce the drop against a copy of last week's input", 30),
       ("Fix the stage and rerun against the same copy to confirm the count matches", 40),
       ("Backfill the missing week from the source", 45)]),

    G("Customers on the older app version are getting logged out randomly and support is fielding the complaints",
      "Fix the random logout bug on the old app version", "Stop sessions from dropping unexpectedly",
      "HIGH", "WORK",
      "You can reproduce the logout on demand and the fix stops it happening in that same reproduction",
      [("Get one concrete report with device, version and rough timing", 15),
       ("Install that app version and try to trigger it the same way", 30),
       ("Check the token refresh logic around the point it drops", 30),
       ("Patch the refresh path once you can reproduce the drop reliably", 45),
       ("Retest the same steps and confirm the session survives", 25)]),

    G("Something in last night's deploy pushed our page load times up and I need to find what before the peak traffic window this weekend",
      "Find the regression from last night's deploy", "Identify what in the deploy slowed page loads",
      "HIGH", "WORK",
      "You can point to the specific change responsible, whether or not the fix ships today",
      [("Confirm the timing lines up with the deploy, not something else", 10),
       ("Pull the list of changes that shipped in that deploy", 10),
       ("Profile a slow page load and see where the time actually goes", 30),
       ("Bisect the suspect changes against a staging build", 40),
       ("Confirm which change is responsible by reverting it alone", 20)],
      due="before the peak traffic window this weekend"),
]

# ---------------------------------------------------------------------------
# Dependency and platform upgrades — measure the blast radius first
# ---------------------------------------------------------------------------
UPGRADE = [
    G("Upgrade the app off the major version of the UI framework that loses support next month",
      "Upgrade the UI framework major version", "Move the app onto the supported major version",
      "MEDIUM", "WORK",
      "The app builds and runs on the new version and the main screens work as before",
      [("Skim the framework's migration guide for the headline breaking changes", 15),
       ("Create a branch and bump the version", 10),
       ("Fix the build errors one file at a time", 90),
       ("Run the app and click through the main screens", 30),
       ("Run the test suite and fix what the upgrade broke", 45)],
      due="next month"),

    G("Move the API off the deprecated authentication library before the callers stop working next quarter",
      "Replace the deprecated auth library", "Swap in the supported replacement before the old one is pulled",
      "MEDIUM", "WORK",
      "Logins work end to end against the new library and the deprecated one is out of the dependency list",
      [("Skim what the replacement library expects and how it differs", 15),
       ("Add the new library alongside the old one behind a flag", 30),
       ("Port the login and token refresh paths to the new library", 60),
       ("Test the main login flows against the new path", 30),
       ("Remove the deprecated library once the new path is confirmed working", 20)],
      due="next quarter"),

    G("The database version we're on stops getting security patches in a month",
      "Upgrade the database major version", "Move the database onto a supported version",
      "HIGH", "WORK",
      "The database is on the supported version and the application connects and runs its usual queries",
      [("Skim the release notes for breaking changes affecting the schema", 15),
       ("Take a verified backup and confirm you can restore it", 20),
       ("Upgrade a staging copy first and run the application against it", 60),
       ("Fix any queries or extensions the new version rejects", 45),
       ("Schedule the production upgrade during a quiet window", 40),
       ("Watch the logs after cutover and confirm queries are succeeding", 30)],
      due="stops getting security patches in a month"),

    G("Replace the deprecated image-resizing call before it's removed in the next release",
      "Replace the deprecated image-resizing API", "Swap the deprecated call for its supported replacement",
      "LOW", "WORK",
      "Images resize correctly using the replacement call and the deprecated one is gone from the codebase",
      [("Find every call site using the deprecated function", 15),
       ("Read the replacement's signature and confirm it covers the same cases", 15),
       ("Swap one call site and check the output looks right", 20),
       ("Swap the remaining call sites", 30),
       ("Run the image tests and check a few outputs by eye", 20)],
      due="in the next release"),

    G("Bump the logging library, the version we're pinned to has a known vulnerability and it needs patching before the security audit next week",
      "Upgrade the vulnerable logging library", "Move off the version with the known vulnerability",
      "HIGH", "WORK",
      "The dependency scan no longer flags the library and logs are still being written correctly",
      [("Check the advisory for the exact fixed version", 10),
       ("Bump the version in the dependency file", 10),
       ("Build and run the test suite", 30),
       ("Check logs are still being written in a local run", 15),
       ("Deploy and confirm the scanner no longer flags it", 20)],
      due="before the security audit next week"),
]

# ---------------------------------------------------------------------------
# Migrations nobody wants to write — back up before you touch anything
# ---------------------------------------------------------------------------
MIGRATION = [
    G("Write the migration to split the single address field into structured columns, been avoiding this one",
      "Write the address field migration", "Split the single address field into structured columns",
      "MEDIUM", "WORK",
      "The migration runs cleanly against a copy of production data and the parsed columns look right for a spot check",
      [("Kick off a copy of production data to migrate against", 15),
       ("Sample fifty real addresses and note the formats you'll need to parse", 30),
       ("Write the parsing logic and the new columns", 60),
       ("Run it against the copy and spot-check the results", 30),
       ("Write the rollback that restores the single field", 30),
       ("Run the migration against production during a quiet window", 25)]),

    G("The old orders table needs to move to the new schema before the old service can be switched off",
      "Migrate the orders table to the new schema", "Move order data onto the new schema",
      "HIGH", "WORK",
      "Orders read and write correctly against the new schema and the row counts match",
      [("Kick off a backup of the orders table and confirm it restores", 15),
       ("Write the transform from old schema to new", 45),
       ("Run it against a staging copy and compare row counts", 30),
       ("Point a read path at the new schema behind a flag and check it", 40),
       ("Run the migration against production", 30),
       ("Switch writes over and watch the logs for errors", 30)]),

    G("We need to rename the primary identifier column everywhere without breaking the callers mid-flight",
      "Rename the primary identifier column", "Roll the column rename out without breaking live callers",
      "HIGH", "WORK",
      "Reads and writes work under both the old and new column names and nothing downstream has broken",
      [("Search the codebase for every place that reads or writes the column", 15),
       ("Add the new column alongside the old one", 20),
       ("Backfill the new column from the old one", 40),
       ("Update the code to write both columns", 30),
       ("Switch reads over to the new column once writes are confirmed consistent", 30),
       ("Drop the old column once nothing references it anymore", 20)]),

    G("Consolidate the two half-finished user tables into one before they drift any further apart",
      "Consolidate the duplicate user tables", "Merge the two user tables into a single source of truth",
      "MEDIUM", "WORK",
      "One table holds the merged data with no lost accounts, and the application reads from it",
      [("Back up both tables", 15),
       ("Diff the tables to find accounts that only exist in one", 40),
       ("Write the merge rules for rows that conflict", 45),
       ("Run the merge into a new table and spot-check a sample", 40),
       ("Point the application at the merged table behind a flag", 30)]),
]

# ---------------------------------------------------------------------------
# Features, flags, dead code, monitoring
# ---------------------------------------------------------------------------
BUILD = [
    G("Add the new pricing screen behind a flag so we can test it with a slice of users first",
      "Add the pricing screen behind a flag", "Ship the new pricing screen gated by a feature flag",
      "MEDIUM", "WORK",
      "The flag is wired up and flipping it on shows the new screen without touching anyone left on the old one",
      [("Create the flag and default it off", 10),
       ("Build the new screen against the flag check", 90),
       ("Wire the old screen to keep showing when the flag is off", 20),
       ("Enable it for yourself and click through it", 20),
       ("Enable it for a small percentage and watch for errors", 25)]),

    G("Delete the old reporting module, nothing's called it since the dashboard rewrite",
      "Delete the dead reporting module", "Remove the unused module safely",
      "LOW", "WORK",
      "The module is gone, the build passes and nothing that used to depend on it broke",
      [("Search the codebase for any remaining references to it", 15),
       ("Check the logs for any calls into it over the last month", 15),
       ("Remove the module and its tests", 20),
       ("Run the build and full test suite", 25),
       ("Deploy and watch the error rate for a day", 15)]),

    G("Set up monitoring for the new payments endpoint before it goes live to real traffic next Tuesday",
      "Set up monitoring for the payments endpoint", "Get alerting in place before the endpoint takes real traffic",
      "HIGH", "WORK",
      "A dashboard shows request rate, latency and error rate, and an alert would page someone on a spike",
      [("Decide the metrics that actually matter here: rate, latency, errors", 15),
       ("Add the instrumentation to emit them", 40),
       ("Build the dashboard from the emitted metrics", 30),
       ("Set alert thresholds based on a sane baseline", 25),
       ("Send a test alert to confirm it actually pages", 15)],
      due="next Tuesday"),

    G("Add retries to the shipping carrier integration, it drops requests whenever their API hiccups",
      "Add retries to the shipping carrier integration", "Make the integration tolerate the carrier's flaky API",
      "MEDIUM", "WORK",
      "A simulated timeout gets retried and eventually succeeds or fails cleanly instead of silently dropping",
      [("Simulate a timeout to reproduce a dropped request", 15),
       ("Check which failures are actually safe to retry", 15),
       ("Add retry with backoff around the call", 30),
       ("Cap the retries and add a clear failure path beyond that", 25),
       ("Rerun the simulated timeout and confirm it now recovers", 20)]),

    G("Add caching in front of the product lookup, it's hammering the database on every page view",
      "Add caching to the product lookup", "Cut the repeated database hits for product data",
      "MEDIUM", "WORK",
      "Repeated lookups for the same product hit the cache instead of the database and results still stay fresh enough",
      [("Check the query logs for how often the same lookup repeats", 15),
       ("Pick a cache and a sensible expiry for how stale is tolerable", 15),
       ("Wire the lookup to check the cache before the database", 40),
       ("Invalidate the cache entry when the product is updated", 30),
       ("Watch the query count drop after deploying", 20)]),

    G("Split the billing monolith module, it's become impossible to change one part without breaking another",
      "Split the billing module", "Break the monolith module into separate pieces along its real seams",
      "HIGH", "WORK",
      "The pieces build and pass tests independently, even if a couple of edges still feel rough",
      [("Skim the module's file list to see the rough shape of it", 15),
       ("Map what actually calls what inside the module", 45),
       ("Pick the seam with the fewest cross-dependencies to cut first", 20),
       ("Extract that piece into its own module", 60),
       ("Fix the imports and run the tests", 40),
       ("Repeat for the next clean seam", 60)]),

    G("Reduce the build time, a full build now takes over twenty minutes and it's killing the feedback loop",
      "Reduce the build time", "Cut the full build down to something tolerable",
      "MEDIUM", "WORK",
      "A full build is noticeably faster and you can point to which change did it",
      [("Kick off a profiled build to see where the time goes", 15),
       ("Pick the single biggest offender to attack first", 15),
       ("Enable caching or parallelism for that stage", 45),
       ("Rerun the full build and compare the time", 15),
       ("Repeat once more on the next biggest offender if time allows", 45)]),

    G("Clean up the feature flags, half of them have been at one hundred percent for months and nobody's removed the code",
      "Clean up the stale feature flags", "Remove the flags that finished rolling out long ago",
      "LOW", "WORK",
      "The stale flags and their old-path code are gone and the app still behaves the same",
      [("List the flags and how long each has sat fully on or off", 15),
       ("Pick the ones clearly finished rolling out", 10),
       ("Remove the flag check and delete the losing branch of code", 45),
       ("Run the tests and check the flag is gone from the config", 25)]),
]

# ---------------------------------------------------------------------------
# Reviews, documentation, mentoring, releases, credentials, load testing
# ---------------------------------------------------------------------------
PROCESS = [
    G("Review the large pull request that rewrites the checkout flow before it sits any longer",
      "Review the checkout flow pull request", "Give the rewrite a proper review",
      "MEDIUM", "WORK",
      "You've left comments on the parts that matter and either approved it or said clearly what needs changing",
      [("Read the description to understand what the rewrite is meant to do", 15),
       ("Pull the branch and run it locally", 20),
       ("Read through the diff in logical order rather than file order", 45),
       ("Try the actual checkout flow against the new code", 25),
       ("Leave comments on what needs changing and summarise the review", 20)]),

    G("Write up documentation for the internal search library I built, nobody else can figure out how to use it",
      "Document the internal search library", "Write documentation someone else could actually follow",
      "MEDIUM", "WORK",
      "Someone unfamiliar with the library could get a basic search working from the docs alone",
      [("List the handful of things someone actually needs to do with it", 15),
       ("Write a short getting-started example that runs as-is", 30),
       ("Document the main functions with a real example each", 45),
       ("Have someone unfamiliar with it try to follow the docs", 30),
       ("Fix whatever tripped them up", 25)]),

    G("Write the runbook for the overnight batch job before I go on leave and someone else has to page through it blind",
      "Write the batch job runbook", "Get the on-call steps written down clearly",
      "HIGH", "WORK",
      "Someone unfamiliar with the job could follow the runbook to restart it and check it succeeded",
      [("List the ways the job has actually failed before", 15),
       ("Write the steps to check whether it's currently healthy", 15),
       ("Write the restart steps for the common failure cases", 30),
       ("Note who or what to escalate to if the restart doesn't fix it", 15),
       ("Walk someone else through it once to check it makes sense", 25)],
      due="before I go on leave"),

    G("Pair with the new starter on their first real change so they don't get stuck on the environment before they even start",
      "Pair on the new starter's first change", "Get them through a real change start to finish",
      "MEDIUM", "WORK",
      "Their change is merged and they could describe roughly how to repeat the process on the next one",
      [("Pick a small, well-scoped ticket for the first change", 15),
       ("Sit with them while they set up the local environment", 30),
       ("Have them write the change while you explain rather than take over", 60),
       ("Review it together before it goes up for wider review", 20),
       ("Watch them respond to review comments themselves", 25)]),

    G("Cut the release for this sprint, we're already a day behind on tagging it",
      "Cut this sprint's release", "Get the release tagged and shipped",
      "MEDIUM", "WORK",
      "The release is tagged, deployed and the changelog reflects what actually shipped",
      [("Check the test suite is green on the release branch", 15),
       ("Write the changelog from the merged pull requests", 25),
       ("Tag the release", 10),
       ("Deploy it to production", 30),
       ("Watch the error rate for a while after deploy", 20)]),

    G("Rotate the database credentials, they've been unchanged since before half the current people had access",
      "Rotate the database credentials", "Issue new credentials and retire the old ones",
      "HIGH", "WORK",
      "Services are running on the new credentials and the old ones no longer work",
      [("List every service and script that uses the current credentials", 15),
       ("Generate the new credentials", 10),
       ("Update the services to use the new credentials one at a time", 45),
       ("Confirm each service is healthy after switching", 20),
       ("Revoke the old credentials once nothing is using them", 15)]),

    G("Load test the new signup flow before the launch, we've never seen it under real traffic",
      "Load test the signup flow before launch", "Find out where it breaks under load before real users do",
      "HIGH", "WORK",
      "You know roughly the traffic level it holds up to and have a named bottleneck if it fell short",
      [("Decide the traffic level you actually expect at launch", 15),
       ("Set up a load test script against a staging copy", 45),
       ("Run it at expected load and watch the metrics", 30),
       ("Push past expected load until something clearly gives", 40),
       ("Note the bottleneck and whether it needs fixing before launch", 20)],
      due="before the launch"),

    G("The staging deploy for tomorrow's release needs a rollback plan checked before anyone signs off on it",
      "Check the rollback plan before tomorrow's deploy", "Confirm the release can actually be rolled back cleanly",
      "HIGH", "WORK",
      "You've actually triggered the rollback path once on staging and it left the system in a working state",
      [("Read what the rollback procedure is supposed to do", 15),
       ("Deploy the release to staging as a rehearsal", 20),
       ("Trigger the rollback and confirm staging returns to a working state", 30),
       ("Note any manual step the rollback doesn't cover", 15),
       ("Write the go/no-go decision with what you found", 10)],
      due="tomorrow's release"),

    G("Add accessibility to the settings screen, it's one of the ones that failed the audit",
      "Add accessibility to the settings screen", "Get the settings screen usable with a screen reader and keyboard",
      "MEDIUM", "WORK",
      "You can navigate the whole screen with a screen reader and keyboard alone and nothing is unreachable",
      [("Turn on the screen reader and try the screen for five minutes", 15),
       ("Add labels to the controls that are currently silent", 30),
       ("Fix the tab order so keyboard navigation makes sense", 30),
       ("Check colour contrast against the guideline", 15),
       ("Retest with the screen reader and keyboard only", 20)]),
]

# ---------------------------------------------------------------------------
# Learning, side projects — some LEARNING to balance the WORK weight
# ---------------------------------------------------------------------------
LEARNING = [
    G("Actually learn how the garbage collector works instead of just cargo-culting the tuning flags",
      "Learn how the garbage collector actually works", "Get past guessing at GC tuning flags",
      "LOW", "LEARNING",
      "You can explain the collection cycle in your own words and why one flag you use actually helps",
      [("Skim an overview of the collector your runtime actually uses", 15),
       ("Watch or read a deeper explanation of one collection cycle", 40),
       ("Reproduce a tuning change locally and watch the effect in a profiler", 45),
       ("Write a short note in your own words on what you now understand", 20)]),

    G("Get comfortable with the profiler properly, I only ever use the two features I already know",
      "Learn the profiler properly", "Get comfortable with more than the two features you already use",
      "LOW", "LEARNING",
      "You've used at least two new features of the profiler on a real problem, not just the tutorial",
      [("Skim the profiler's documentation for what it can actually do", 15),
       ("Pick one feature you've never used and try it on a real slow path", 40),
       ("Try a second feature on a different problem", 40),
       ("Note which ones you'd actually reach for again", 15)]),

    G("Set up a personal project to learn the new language properly instead of just reading about it",
      "Learn the new language with a small project", "Get hands-on instead of just reading",
      "LOW", "LEARNING",
      "A small working program exists and you wrote it without copying a tutorial line by line",
      [("Pick a small project scoped to a weekend, not a career", 15),
       ("Read enough of the basics to write a first line", 30),
       ("Build the smallest version that does one real thing", 90),
       ("Add one more feature without looking anything up you already learned", 60)]),

    G("Understand why our tests take so long to run before I propose speeding them up",
      "Understand why the test suite is slow", "Find out where the test time actually goes before proposing a fix",
      "MEDIUM", "LEARNING",
      "You can point to the slowest few tests and a plausible reason, even without fixing it yet",
      [("Run the suite with timing enabled", 15),
       ("Sort the results and note the slowest handful", 15),
       ("Read what those slow tests are actually doing", 30),
       ("Note the pattern, if there is one, across the slow ones", 20)]),
]

# ---------------------------------------------------------------------------
# Live incidents — act, then explain, in that order
# ---------------------------------------------------------------------------
INCIDENT = [
    G("The production database is throwing connection pool exhausted errors and requests are timing out right now",
      "Fix the exhausted connection pool incident", "Restore database connections and stop request timeouts",
      "URGENT", "WORK",
      "Requests are succeeding again and connections are stable, even before the writeup is finished",
      [("Check the pool metrics to confirm what's actually maxed out", 10),
       ("Look for a recent change or traffic spike that could explain it", 10),
       ("Restart the pool or fail over to a standby", 15),
       ("Confirm requests are succeeding and connections are draining normally", 15),
       ("Note the timeline and suspected cause for the writeup", 15)]),

    G("Just found out a debug endpoint has been returning customer email addresses without any authentication",
      "Lock down the exposed debug endpoint", "Take the endpoint out of reach before more data leaks",
      "URGENT", "WORK",
      "The endpoint is no longer reachable without credentials and you know roughly how long it was exposed",
      [("Confirm exactly which endpoint and what data it returns", 10),
       ("Disable it or add authentication in front of it", 15),
       ("Deploy the fix", 15),
       ("Check the endpoint is no longer reachable without credentials", 10),
       ("Pull the access logs to see how long it was exposed and by whom", 30)]),

    G("The overnight deploy put the app into a crash loop and it's been down since early morning",
      "Recover the app from the crash loop", "Get the app back up and stop the crash loop",
      "URGENT", "WORK",
      "The app is serving requests normally and staying up without restarting",
      [("Check the crash logs for the immediate error", 10),
       ("Roll back to the last known-good deploy", 15),
       ("Confirm the app starts and stays up", 15),
       ("Watch traffic and error rates for a stretch", 20),
       ("Note what in the deploy caused it for the follow-up", 15)]),
]

# ---------------------------------------------------------------------------
# Housekeeping — small, low-stakes, easy to keep putting off
# ---------------------------------------------------------------------------
HOUSEKEEPING = [
    G("Clean up the commented-out code and stale TODOs scattered through the auth module, it's impossible to tell what's still relevant",
      "Clean up the auth module's dead code and TODOs", "Remove commented-out code and resolve the stale TODOs",
      "LOW", "WORK",
      "The module has no commented-out blocks left and the remaining TODOs are ones still worth keeping",
      [("Search the module for commented-out code blocks", 15),
       ("Delete them, checking the git history covers anything worth keeping", 25),
       ("Search for TODO comments and read through them for relevance", 20),
       ("Remove the ones that no longer apply and note the keepers properly", 30),
       ("Run the tests to confirm nothing broke", 20)]),
]

GOLD: list[Gold] = DEBUG + UPGRADE + MIGRATION + BUILD + PROCESS + LEARNING + INCIDENT + HOUSEKEEPING
