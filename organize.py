import os
import re
import sys
import shutil

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
screenshots_organized_folder = 'output/wow-screenshots/'

def get_screenshot_datestamp(filename):
    
    expression = re.compile('((?:[a-z][a-z]+))'+'(_)'+'(\\d+)')
    matches = expression.search(filename)

    if matches:
        datestamp = matches.group(3)
    else:
        datestamp = None

    return datestamp


# main stoofs

# 
if not os.path.exists(screenshots_organized_folder):
    try: 
        os.makedirs(screenshots_organized_folder)
    except OSError as e:
        print e
        sys.exit()

for _, expansion in wow_expansion_dates.items():
    expansion_folder_path = screenshots_organized_folder + expansion['folder-name']

    if not os.path.exists(expansion_folder_path):
        try:
            os.makedirs(expansion_folder_path)
        except OSError as e:
            print e
            sys.exit()

for path, _, files in os.walk(screenshots_folder):

    for file_name in files:
        file_datestamp = get_screenshot_datestamp(file_name)

        if file_datestamp is not None:

            for _, expansion in wow_expansion_dates.items():
                expansion_folder_path = screenshots_organized_folder + expansion['folder-name']

                if file_datestamp >= expansion['start'] and file_datestamp <= expansion['end']:

                    try:
                        shutil.copy(path+'/'+file_name, screenshots_organized_folder + expansion['folder-name']+file_name)
                    except IOError as e:
                        print e

