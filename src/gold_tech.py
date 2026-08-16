"""Gold examples: technology and digital life (hand-authored).

Covers the domain gold_core.py barely touches: setting up and migrating
devices, hands-on hardware repairs with real physical prerequisites (power
down and unplug before opening a case; back up before wiping a drive),
account security and recovery, photo and file storage that has gotten out of
hand, home network and media gear, and the digital admin nobody enjoys —
subscriptions, filters, spreadsheets nobody automated.

See `goldlib.Gold` for the format and `quality.py` for the rules every
example must pass.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from goldlib import Gold

G = Gold

# ---------------------------------------------------------------------------
# New and retiring devices
# ---------------------------------------------------------------------------
DEVICES = [
    G("Set up the new phone before the old one gets recycled",
      "Set up the new phone", "Get the new phone ready for daily use",
      "MEDIUM", "PERSONAL",
      "The new phone has your contacts, photos and the apps you use daily, and you have sent a test message from it",
      [("Charge the new phone and turn it on", 10),
       ("Sign in with the account and start the transfer from the old phone", 15),
       ("Wait for apps and photos to finish copying across", 30),
       ("Check messaging apps, banking apps and two-factor codes still work", 20),
       ("Reset the old phone once everything is confirmed on the new one", 15)],
      due="before the old one gets recycled"),

    G("Set up the new laptop, mine's finally dead",
      "Set up the new laptop", "Get the replacement laptop ready for daily use",
      "MEDIUM", "PERSONAL",
      "You can do your normal daily tasks on the new laptop without hunting for a missing file or password",
      [("Charge it fully and run the initial setup", 15),
       ("Sign into the browser and email to sync bookmarks and settings", 15),
       ("Install the handful of programs you actually use", 30),
       ("Copy files across from the backup or the old machine", 40),
       ("Sign into your saved passwords and check the important logins still work", 20)]),

    G("I've been putting off moving the photos off the old phone for a year",
      "Move the photos off the old phone", "Get years of photos safely off the old phone before it dies or gets wiped",
      "LOW", "PERSONAL",
      "The photos are off the old phone and you have opened a handful to check they came across properly",
      [("Find a charging cable and turn the old phone on", 10),
       ("Plug it into the laptop or open the cloud backup app", 10),
       ("Copy or upload the photos to the laptop or cloud storage", 45),
       ("Spot check a folder of photos to make sure they actually opened", 10)]),

    G("Wipe the old laptop so I can finally get rid of it",
      "Wipe and pass on the old laptop", "Back up what matters, then securely wipe the old laptop before selling or donating it",
      "LOW", "ADMIN",
      "The old laptop is wiped and signed out, with your files safely copied across first",
      [("Find the charger and plug the old laptop in", 5),
       ("Copy any files still only on that laptop to the new one or a drive", 25),
       ("Check the copied files actually opened before wiping anything", 10),
       ("Sign out of iCloud, Google, and any other accounts on it", 10),
       ("Reset it to factory settings, wiping the drive", 30)]),

    G("Set up the work laptop, I start the new job tomorrow and it's still in the box",
      "Set up the new work laptop", "Get the company laptop ready before the first day",
      "HIGH", "WORK",
      "You can log in, get online and open your email on the new laptop without fumbling on the first morning",
      [("Unbox it, charge it and turn it on", 10),
       ("Log in with the credentials sent over", 10),
       ("Install the VPN, email and whatever else the onboarding note listed", 30),
       ("Connect it to the home wifi and confirm email and calendar sync", 15),
       ("Charge it fully overnight so it's ready in the morning", 5)],
      due="tomorrow"),
]

# ---------------------------------------------------------------------------
# Hands-on hardware — physical procedures with real prerequisites
# ---------------------------------------------------------------------------
HARDWARE = [
    G("The phone screen's properly cracked now, glass came off in my pocket",
      "Replace the cracked phone screen", "Fit a replacement screen so the phone is safe to use again",
      "HIGH", "PERSONAL",
      "The new screen is in, the touch and cameras work, and the case is closed back up",
      [("Order the correct replacement screen and a set of opening tools", 15),
       ("Back up the phone before opening it up", 15),
       ("Power the phone off completely before starting", 5),
       ("Heat and pry the case open, then disconnect the battery first", 25),
       ("Unclip the old screen, fit the new one and reconnect the battery", 40),
       ("Power it on and test the touch screen and cameras before closing the case", 20)]),

    G("The laptop battery's swollen and the trackpad's started bulging, need to sort this before it's actually dangerous",
      "Replace the swollen laptop battery", "Safely remove the swollen battery and fit a replacement",
      "HIGH", "PERSONAL",
      "The old battery is out without incident, the new one is fitted, and the laptop charges normally",
      [("Back up anything not already saved elsewhere, just in case", 15),
       ("Order the correct replacement battery for the model", 15),
       ("Power the laptop off and unplug the charger completely", 5),
       ("Undo the case screws and lift the bottom panel off carefully", 20),
       ("Disconnect and remove the swollen battery without puncturing it", 20),
       ("Fit the new battery, close the case and check it charges and holds charge", 25)]),

    G("The old laptop's grinding to a halt, I think the hard drive's dying and I need this thing for work",
      "Swap the laptop's hard drive for an SSD", "Replace the failing hard drive with an SSD before it dies completely",
      "HIGH", "PERSONAL",
      "The laptop boots from the SSD noticeably faster and you have checked your files and programs are present",
      [("Buy an SSD that fits and a USB enclosure or cloning cable", 15),
       ("Back up everything on the current drive while it still boots", 30),
       ("Clone the old drive onto the new SSD", 45),
       ("Power down, unplug and open the case to swap the drives", 20),
       ("Boot from the new SSD and check your files and programs are there", 20)]),

    G("Finally set up the NAS that's been sitting in its box since Christmas",
      "Set up the NAS", "Get the network drive installed, configured and backing up the important folders",
      "MEDIUM", "ADMIN",
      "The NAS is online, the important folders are backing up to it, and you have pulled one file back to confirm it works",
      [("Unbox it and fit the hard drives into the bays", 15),
       ("Connect it to the router with an ethernet cable and power it on", 10),
       ("Run the setup wizard and create the drive volume", 25),
       ("Set up folders and user accounts for who needs access", 20),
       ("Point the important folders at it and run a first backup", 30),
       ("Restore one file from the NAS to check the backup actually works", 10)]),

    G("The wifi barely reaches the back bedroom, it's been annoying us for months",
      "Fix the wifi dead zone", "Extend coverage so the back bedroom gets a usable signal",
      "MEDIUM", "PERSONAL",
      "The back bedroom gets a usable, stable signal, checked with the same test as before",
      [("Run a quick speed test in the dead spot to see how bad it actually is", 10),
       ("Check where the router is and whether repositioning it would help", 15),
       ("Buy a mesh extender or access point if repositioning isn't enough", 30),
       ("Set it up and connect it to the main network", 20),
       ("Retest the signal in the same spot as before", 10)]),

    G("The wifi keeps dropping mid video call and I've got back to back meetings tomorrow",
      "Fix the wifi before tomorrow's calls", "Get the connection stable enough to trust it for video calls",
      "HIGH", "WORK",
      "A test call ran for several minutes without dropping",
      [("Restart the router and modem and see if that alone fixes it", 10),
       ("Check for a firmware update on the router", 15),
       ("Move the work laptop closer to the router, or run an ethernet cable", 20),
       ("Check which other devices are hogging the bandwidth and pause them", 10),
       ("Do a test video call to confirm it holds", 15)],
      due="tomorrow"),
]

# ---------------------------------------------------------------------------
# Accounts and security
# ---------------------------------------------------------------------------
SECURITY = [
    G("Set up a password manager, I'm sick of reusing the same three passwords",
      "Set up a password manager", "Get a password manager installed and start moving logins into it",
      "LOW", "ADMIN",
      "Your most-used logins are in the password manager and it unlocks quickly enough that you'll actually use it",
      [("Pick a password manager and create the account", 15),
       ("Install the browser extension and the phone app", 10),
       ("Import or add the logins you use most often", 30),
       ("Turn on unlock by fingerprint or face so it's actually convenient", 10)]),

    G("Turn two-factor on for the accounts that actually matter",
      "Turn on two-factor authentication", "Add a second layer of login security to the accounts that matter most",
      "LOW", "ADMIN",
      "Email, banking and your main social accounts have two-factor turned on, and the backup codes are saved somewhere safe",
      [("List the accounts where a breach would actually hurt: email, bank, main social", 10),
       ("Turn on two-factor for email first, since it can reset everything else", 15),
       ("Do the same for banking and the main social accounts", 30),
       ("Save the backup codes somewhere other than your phone", 10)]),

    G("Set up a VPN before the trip, I don't trust hotel wifi",
      "Set up a VPN for the trip", "Get a VPN installed and working on your phone and laptop before you travel",
      "LOW", "ADMIN",
      "The VPN connects on both devices and the IP address changes when it's on",
      [("Pick a VPN provider and sign up", 15),
       ("Install the app on your phone and laptop", 15),
       ("Turn it on and check your IP address actually changes", 10),
       ("Test it on a public wifi network like a cafe before you go", 20)],
      due="before the trip"),

    G("Locked out of the old email account and I need it for the job applications",
      "Recover the locked email account", "Get back into the email account you're locked out of",
      "HIGH", "ADMIN",
      "You're back into the account and can send and receive email from it",
      [("Try the normal password reset with the recovery email or phone", 10),
       ("If that fails, go through the provider's identity verification process", 30),
       ("Gather proof of ownership it asks for, like old emails or the account creation date", 20),
       ("Once back in, update the recovery details so this doesn't happen again", 15)]),

    G("Someone's got into my email, there's a password reset I didn't ask for sitting in the inbox",
      "Secure the hacked email account", "Lock the attacker out and secure everything connected to the account",
      "URGENT", "PERSONAL",
      "Only your sessions are active, two-factor is on, and no forwarding rules were left behind",
      [("Change the password immediately from a device you trust", 5),
       ("Sign out of other active sessions from the account settings", 10),
       ("Turn on two-factor authentication if it wasn't already on", 15),
       ("Check the recovery email and phone number haven't been changed", 10),
       ("Check for forwarding rules or filters the attacker may have added", 15),
       ("Change the password on any account that reused the same one", 30)]),

    G("Need to sort out parental controls on the kids' tablet, found some stuff on there I didn't like",
      "Set up parental controls on the tablet", "Restrict content and screen time on the kids' tablet properly",
      "HIGH", "PERSONAL",
      "The filters and screen time limits are on, and you've confirmed a blocked app or site is actually blocked",
      [("Check what's already been seen and talk to them about it first", 15),
       ("Turn on the built-in parental control or family account feature", 15),
       ("Set age-appropriate content filters and app restrictions", 25),
       ("Set screen time limits and a bedtime cutoff", 15),
       ("Test the restrictions yourself by trying to access something blocked", 10)]),
]

# ---------------------------------------------------------------------------
# Photos, files and storage that got out of hand
# ---------------------------------------------------------------------------
STORAGE = [
    G("Ten years of photos scattered across three drives, two phones and a laptop I don't even use, need to get this under control",
      "Consolidate and organise the scattered photos", "Pull years of scattered photos into one organised, backed-up place",
      "MEDIUM", "PERSONAL",
      "The photos are in one place, duplicates are mostly cleared out, and they're sorted by year",
      [("Plug in the old drives and phones and check what's actually on each one", 15),
       ("Pick one destination, whether a drive or a cloud account, with enough space", 15),
       ("Copy everything across, keeping the folder structure for now", 90),
       ("Run a duplicate finder over the result", 30),
       ("Sort what's left into folders by year", 45)]),

    G("The cloud storage is full and now my phone won't back up, and I'm meant to be trading it in",
      "Clear out the full cloud storage", "Free up cloud storage so backups start working again",
      "HIGH", "ADMIN",
      "There's enough free space that the phone backup runs and finishes without stalling",
      [("Check the storage breakdown to see what's actually taking the space", 10),
       ("Delete old device backups you no longer need", 15),
       ("Go through photos and delete the obvious duplicates and screenshots", 40),
       ("Empty the trash or recently-deleted folder, since it still counts", 10),
       ("Run the phone backup again and check it completes", 20)]),

    G("Set up automatic backups for the laptop before I lose something the way I lost the wedding photos",
      "Set up automatic backups for the laptop", "Get a proper automatic backup running with an external drive",
      "MEDIUM", "ADMIN",
      "The backup has finished once and you've restored a file from it to prove it works",
      [("Buy an external drive with enough capacity for the laptop", 15),
       ("Plug it in and turn on the built-in backup tool", 10),
       ("Pick which folders to include and set it to run automatically", 15),
       ("Let the first full backup finish", 60),
       ("Restore one file from the backup to check it actually works", 15)]),

    G("Scan in the box of old family photo prints before they fade any further",
      "Digitise the old photo prints", "Scan the box of family prints and save them somewhere safe",
      "MEDIUM", "CREATIVE",
      "The prints are scanned, roughly dated, and saved somewhere other than just the scanner app",
      [("Find or borrow a scanner and clear a space to work", 15),
       ("Sort the prints into rough date order first", 30),
       ("Scan them in batches, wiping the glass between dusty ones", 90),
       ("Rename or tag the files with rough dates while it's fresh in memory", 40),
       ("Copy the scans to cloud storage or a drive, not just the scanner's app", 20)]),
]

# ---------------------------------------------------------------------------
# Home network and media gear, and the small admin chores nobody enjoys
# ---------------------------------------------------------------------------
HOME_TECH = [
    G("Set up the new printer, it's still in the box",
      "Set up the new printer", "Get the printer unboxed, connected and printing over wifi",
      "LOW", "ADMIN",
      "A test page has printed successfully from both the laptop and the phone",
      [("Unbox it and fit the ink or toner cartridges", 10),
       ("Connect it to the wifi network", 15),
       ("Install the drivers or app on your laptop and phone", 15),
       ("Print a test page from each device", 10)]),

    G("Set up a proper media system so we stop juggling five different apps and cables",
      "Set up the home media system", "Get the streaming box and TV set up as one simple system",
      "MEDIUM", "PERSONAL",
      "Turning the TV on gets you straight to a streaming app without juggling separate remotes or inputs",
      [("Unbox the streaming box and plug it into the TV", 10),
       ("Connect it to the wifi and sign into the main accounts", 15),
       ("Set it as the default input and hide the ones you don't use", 10),
       ("Install the streaming apps you actually pay for", 20),
       ("Set up one remote to control the TV, sound and streaming box", 15),
       ("Test that turning on the TV brings up the streaming box automatically", 15)]),

    G("I'm paying for about six streaming services now, half of which I never use",
      "Cut down the streaming subscriptions", "Work out what you actually use and cancel the rest",
      "LOW", "ADMIN",
      "The subscriptions you don't use are cancelled and the next statement is shorter",
      [("List every subscription and what you actually pay each month", 15),
       ("Note which ones you've genuinely used in the last month", 10),
       ("Cancel the ones that didn't make the cut", 20),
       ("Check the bank statement next month to confirm they stopped", 10)]),

    G("My personal inbox is basically just newsletters now, can't find real emails in there",
      "Unsubscribe from the newsletter pile", "Cut the personal inbox down to emails that matter",
      "LOW", "ADMIN",
      "The regular newsletter flood has stopped and the inbox shows real emails first",
      [("Search the inbox for 'unsubscribe' to surface the worst offenders", 10),
       ("Unsubscribe from the ones you never open", 30),
       ("Set up a filter to auto-archive the few you want to keep but not see daily", 15),
       ("Archive the backlog so the inbox starts fresh", 15)]),
]

# ---------------------------------------------------------------------------
# Digital work, creative and learning
# ---------------------------------------------------------------------------
DIGITAL = [
    G("Set up proper filters on the work inbox before it buries something important again",
      "Set up filters on the work inbox", "Route routine email automatically so the inbox is easier to triage",
      "MEDIUM", "WORK",
      "New routine email is being sorted automatically and a real message hasn't been misfiled",
      [("List the senders and subjects that clutter the inbox most", 15),
       ("Create filters to label or archive the automated ones", 30),
       ("Set up a separate folder for anything CC'd rather than sent to you directly", 20),
       ("Run the filters over the existing backlog to test them", 15),
       ("Adjust any filter that caught something it shouldn't have", 20)]),

    G("I keep restarting the personal website because it's never good enough to publish",
      "Get the personal website live", "Get a first version of the website actually published, however imperfect",
      "MEDIUM", "CREATIVE",
      "The site is live at the domain and someone other than you has opened the link successfully",
      [("Pick a template or starting point instead of building from scratch again", 15),
       ("Write the home page copy in one sitting without polishing it", 30),
       ("Add the two or three pages you actually need, nothing extra", 60),
       ("Buy a domain and connect it if you don't have one already", 20),
       ("Publish it, even with a placeholder photo you'll swap later", 15)]),

    G("The monthly budget spreadsheet takes an hour of copy-pasting every single time, there has to be a better way",
      "Automate the budget spreadsheet", "Cut the manual copy-pasting out of the monthly budget update",
      "MEDIUM", "ADMIN",
      "Next month's update takes minutes instead of an hour, and the numbers matched a manual check",
      [("Write down exactly what you currently copy and paste by hand", 15),
       ("Look up the formula or import function that would replace the worst step", 20),
       ("Rebuild that one section so it pulls or calculates automatically", 40),
       ("Run it against last month's numbers to check it matches what you did by hand", 25),
       ("Fix whatever the automated version got wrong", 20)]),

    G("Actually learn Excel properly instead of just googling the same three formulas forever",
      "Learn Excel properly", "Build real working knowledge of spreadsheets instead of ad hoc googling",
      "LOW", "LEARNING",
      "You can build a pivot table and use a lookup formula without searching for the syntax",
      [("Find a solid beginner-to-intermediate course or structured guide", 15),
       ("Work through the basics: formulas, formatting, and sorting", 60),
       ("Learn pivot tables and lookup functions properly", 60),
       ("Rebuild one spreadsheet you actually use with what you've learned", 45)]),

    G("Get a proper 'goodnight' routine set up on the smart speaker instead of turning eight things off by hand",
      "Set up a smart home routine", "Automate the lights, plugs and heating into one voice command",
      "LOW", "PERSONAL",
      "Saying the phrase turns off or dims the devices you meant it to, tested at least once",
      [("Check which devices are already connected to the smart home app", 10),
       ("Create a new routine and name it something you'll actually say", 10),
       ("Add each device and the state you want it left in", 25),
       ("Test the routine and adjust anything that didn't trigger", 15)]),
]

GOLD: list[Gold] = DEVICES + HARDWARE + SECURITY + STORAGE + HOME_TECH + DIGITAL
