#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3
import os
import numpy as np
import subprocess
from hashtag_collection import find_hashtags
from hashtag_collection import write_data

def scraper(start_date, end_date, keyword, month):

    for date in range(start_date, end_date):
        if not os.path.exists('raw_data_date/' + str(month)):
            print ('Making Directory raw_data_date/' + str(month))
            os.makedirs('raw_data_date/' + str(month))
        if not os.path.exists('processed_data_date/' + str(month)):
            print ('Making Directory processed_data_date/' + str(month))
            os.makedirs('processed_data_date/' + str(month))

        start = '2018-' + str(month) + '-' + str(date)
        end = '2018-' + str(month) + '-' + str(date + 1)
        filename = str(month * 100 + date)
        try:
            subprocess.call("python3 tweep.py -s " + keyword + " -o raw_data_date/"
                            + str(month) + '/' + filename + ".txt --since " + start +
                            ' --till ' + end, shell=True, timeout=270)
        except(subprocess.TimeoutExpired):
            pass

        try:
            write_data('processed_data_date/' + str(month) + '/' + filename, "raw_data_date/" + str(month) + '/' + filename + ".txt")
        except(IOError):
            print('IOError Notice Help')


scraper(12, 28, 'GunReform', 2)
scraper(1, 20, 'GunReform', 3)



# endTime = datetime.datetime.now() + datetime.timedelta(seconds=5)
# while True:
#     if datetime.datetime.now() >= endTime:
#         break
#     while True:
#         print('hello')
#     subprocess.
#     os.system("python3 tweep.py -u " + twitter_username + " -o " + 'raw_data_of_person/' + parent + '/' + twitter_username + "_raw_data.txt --since 2016-01-20")
