import os
import re

# WoWScrnShot_MMDDYY_TTTTTT.EXT
wow_expansion_dates = {
    '0x': {            # January 1, 2000 (safety)
        'folder-name': 'wow-beta',
              'start': '010100',
                'end': '112204'
    },         
    '1x': {            # November 23, 2004
        'folder-name': 'classic',
              'start': '112304',
                'end': '011507'
    },
    '2x': {            # January 16, 2007
        'folder-name': 'the-burning-crusade',
              'start': '011607',
                'end': '111208'
    },
    '3x': {            # November 13, 2008
        'folder-name': 'wrath-of-the-lich-king',
              'start': '111308',
                'end': '120610'
    },
    '4x': {            # December 7, 2010
        'folder-name': 'cataclysm',
              'start': '120710',
                'end': '082412'
    },
    '5x': {            # September 25, 2012
        'folder-name': 'mists-of-pandaria',
              'start': '082512',
                'end': '010115'
    }
}

screenshots_folder = 'input'
screenshots_organized_folder = 'output/wow-screenshots'

def get_screenshot_datestamp(filename):
    
    expression = re.compile('((?:[a-z][a-z]+))'+'(_)'+'(\\d+)')
    matches = expression.search(filename)

    if matches:
        datestamp = matches.group(3)
    else:
        datestamp = None

    return datestamp


# testing shit
filenum = 1
for _, _, files in os.walk(screenshots_folder):
    
    for fname in files:
        print filenum
        filenum+=1
        yar = get_screenshot_datestamp(fname)
        print yar