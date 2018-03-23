import pandas as pd
import os
import datetime
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates

# 'GreatMillsHighSchool', 'Maryland', 'GreatMills', 'marylandschoolshooting'
hashtag_list = ['Ontario']
user_set = set([])
df_list = []


for hashtag in hashtag_list:
    df = pd.read_csv(hashtag + '.csv')
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
        print type(row['time'])
    time_list.append(time)
    cummulative_tweets += 1
    y_axis.append(cummulative_tweets)
    # y_axis.append(1)

# time_list = [datetime.datetime.strptime(d, '%m/%d/%Y').date() for d in time_list]
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d %H:%M:%S'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())
plt.plot(time_list, y_axis)
plt.gcf().autofmt_xdate()
plt.show()
