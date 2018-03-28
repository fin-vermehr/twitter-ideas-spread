#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3
import os
import numpy as np
import subprocess
from hashtag_collection import find_hashtags
from hashtag_collection import write_data

def scraper(start_date, end_date, keyword, month):

    for date in range(start_date, end_date):
        if not os.path.exists('raw_data_date/' + keyword + '/' + str(month)):
            print ('Making Directory raw_data_date/' + keyword + '/' + str(month))
            os.makedirs('raw_data_date/' + keyword + '/' + str(month))
        if not os.path.exists('processed_data_date/' + keyword + '/' + str(month)):
            print ('Making Directory processed_data_date/' + keyword + '/' + str(month))
            os.makedirs('processed_data_date/' + keyword + '/' + str(month))

        start = '2018-' + str(month) + '-' + str(date)
        end = '2018-' + str(month) + '-' + str(date + 1)
        filename = str(month * 100 + date)
        try:
            subprocess.call("python3 tweep.py -s " + keyword + " -o raw_data_date/" + keyword + '/'
                            + str(month) + '/' + filename + ".txt --since " + start +
                            ' --till ' + end, shell=True, timeout=15)
        except(subprocess.TimeoutExpired):
            pass

        try:
            write_data('processed_data_date/' + keyword + '/' + str(month) + '/' + filename, "raw_data_date/" + keyword + '/' + str(month) + '/' + filename + ".txt")
        except(IOError):
            print('IOError Notice Help')

DeleteFacebook_dict = {'Facebook': 6.8, 'WeThePeople': 0.9, 'MAGA': 1.5,
                       'DrainTheSwamp': 1, 'IBOR': 1.2, 'Defend2A': 0.9,
                       'GreatAwakening': 1.2, 'QAnon': 1.5,
                       'FuckZuckerbeg': 0.9, 'DeleteFacebookNow': 1.2}
# AppleEvent_dict = {'iPhoneX': 7.2, 'Apple': 4.9, 'iPhone': 1.7,
#                    'AppleLive': 2.5, 'iPhoneSE': 2.1, 'AppleTH': 1.9,
#                    'iPhone8': 3.6, 'AppleWatch': 1.5, 'iPhone6': 1.2,
#                    'AppleEvents': 1.1}
Trebes_dict = {'Carcassonne': 14.2, 'Aude': 5.7, 'ArnaudBeltrame': 5.1,
               'RedouaneLakdim': 3.1, 'France': 2.8, 'Collomb': 1.8, 'Beltrame': 1.6,
               'Lakdim': 1.5, 'attentat': 1.5, 'Macron': 1.2}

for key in Trebes_dict:
    scraper(0, 21, key, 3)
