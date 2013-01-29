World of Warcraft Screenshot Organizer
--------------------------------------

WOWSSO is a python script that searches a folder tree for images that match the filename format of WoW Screenshots.
WOWSSO will copy these screenshots to the specified directory. This script was created to make screenshot migrations
super easy and also to find screenshots on my computer that I didn't even know existed.

Currently this script only sorts by the expansion number. I plan to make it have optional patch sorting in the future.


Screenshot Filename Format
--------------------------

Super simple:

    WoWScrnShot_MMDDYY_TTTTTT.EXT

    MM = Month
    DD = Day
    YY = Year
    EXT = File extension


Intended Behaviour
------------------

Currently this script dumps pre-expansion screenshots in the directory of the previous expansion. This will be changed
when patch sorting is added in the future.