#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3

import pandas as pd
import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib

def clean_data(hashtag_list, event_name):
    # AustinBombings'GreatMillsHighSchool', 'Maryland', 'GreatMills', 'marylandschoolshooting'
    df_list = []

    # Clean all the hashtags dataframes, concatenate them into one dataframe,
    # remove all the duplicate accounts tweeting about an event, and sort them by
    # the date created.
    for hashtag in hashtag_list:
        df = pd.read_csv(hashtag + '.csv', skiprows=2, error_bad_lines=False)
        df.columns = ['time', 'screen_name', 'text']
        df = df.drop_duplicates('screen_name', keep='first')
        df_list.append(df)

    df = pd.concat(df_list, axis=0, join='outer', join_axes=None, ignore_index=False,
                   keys=None, levels=None, names=None, verify_integrity=False,
                   copy=True)

    df = df.sort_values(by=['time'])
    df = df.drop_duplicates('screen_name', keep='first')

    time_list = []
    y_axis = []
    cummulative_tweets = 0

    # Convert time of type string to a usable type, datetime.datetime.

    for i, row in df.iterrows():
        if type(row['time']) is str:
            month = int(row['time'][-14:-12])
            day = int(row['time'][-11:-9])
            hour = int(row['time'][-8:-6])
            minute = int(row['time'][-5:-3])
            second = int(row['time'][-2:])
            time = datetime.datetime(2018, month, day, hour=hour, minute=minute, second=second)
            df.set_value(i, 'time', time)
        elif type(row['time']) is datetime.datetime:
            pass
        else:
            print(type(row['time']))
        time_list.append(time)
        cummulative_tweets += 1
        y_axis.append(cummulative_tweets)
        df.loc[i, 'cumulative_tweets'] = cummulative_tweets
    # y_axis.append(1)
    # Create a csv file with all the cleaned_data from this event.
    df.to_csv(event_name + '_processed.csv', sep=',', encoding='utf-8')
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d %H:%M:%S'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator())
    plt.plot(time_list, y_axis)
    plt.gcf().autofmt_xdate()
    plt.show()

hashtag_list = ['AppleEvent']
clean_data(hashtag_list, 'AppleEvent')
