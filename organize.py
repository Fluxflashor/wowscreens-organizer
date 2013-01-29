import os
import re

# WoWScrnShot_MMDDYY_TTTTTT.EXT
wow_expansion_dates = {
    '0x-warcraft.beta': '010100',          # January 1, 2000 (safety)
    '1x-classic': '112304',                # November 23, 2004
    '2x-the.burning.crusade': '011607',    # January 16, 2007
    '3x-wrath.of.the.lich.king': '111308', # November 13, 2008
    '4x-cataclysm': '120710',              # December 7, 2010
    '5x-mists.of.pandaria': '082512'       # September 25, 2012
}

screenshots_folder = 'input'
screenshots_organized_folder = 'output/wow-screenshots'
