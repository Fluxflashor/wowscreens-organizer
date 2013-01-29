import os
import re
import sys
import shutil

# Configure me!
screenshots_folder = 'input'
screenshots_organized_folder = 'output/wow-screenshots/'

# WoWScrnShot_MMDDYY_TTTTTT.EXT
wow_expansion_dates = {
    '0x': {            # January 1, 2000 (safety)
        'folder-name': 'wow-beta',
              'start': '000101',
                'end': '041122'
    },         
    '1x': {            # November 23, 2004
        'folder-name': 'classic',
              'start': '041123',
                'end': '070115'
    },
    '2x': {            # January 16, 2007
        'folder-name': 'the-burning-crusade',
              'start': '070116',
                'end': '081112'
    },
    '3x': {            # November 13, 2008
        'folder-name': 'wrath-of-the-lich-king',
              'start': '081113',
                'end': '101206'
    },
    '4x': {            # December 7, 2010
        'folder-name': 'cataclysm',
              'start': '101207',
                'end': '120824'
    },
    '5x': {            # September 25, 2012
        'folder-name': 'mists-of-pandaria',
              'start': '120825',
                'end': '150101'
    }
}

def get_screenshot_datestamp(filename):
    
    expression = re.compile('((?:[a-z][a-z]+))'+'(_)'+'(\\d+)')
    matches = expression.search(filename)

    if matches:
        datestamp_raw = matches.group(3)

        # the datestamp is always 6 digits so this will work.
        # if you ever change this blizzard, i'll hate you.

        datestamp = datestamp_raw[-2] + datestamp_raw[-1]+ datestamp_raw[:-2]

    else:
        datestamp = None

    return datestamp

def is_wow_screenshot(filename):
    # crude but it works for me

    if "WoWScrnShot" is in filename:
        return True
    else
        return False


# main stoofs

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

        if is_wow_screenshot(file_name):
            file_datestamp = get_screenshot_datestamp(file_name)
    
            if file_datestamp is not None:
    
                for _, expansion in wow_expansion_dates.items():
                    expansion_folder_path = screenshots_organized_folder + expansion['folder-name']
    
                    if file_datestamp >= expansion['start'] and file_datestamp <= expansion['end']:
    
                        try:
                            shutil.copy(path+'/'+file_name, screenshots_organized_folder + expansion['folder-name']+'/'+file_name)
                        except IOError as e:
                            print e

