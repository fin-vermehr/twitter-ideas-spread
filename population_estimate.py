import datetime
import os
import pandas as pd

df_list = list()

DeleteFacebook_dict = {'Facebook': 6.8, 'WeThePeople': 0.9, 'MAGA': 1.5,
                       'DrainTheSwamp': 1, 'IBOR': 1.2, 'Defend2A': 0.9,
                       'GreatAwakening': 1.2, 'QAnon': 1.5,
                       'FuckZuckerbeg': 0.9, 'DeleteFacebookNow': 1.2}

Trebes_dict = {'Carcassonne': 14.2, 'Aude': 5.7, 'ArnaudBeltrame': 5.1,
               'RedouaneLakdim': 3.1, 'France': 2.8, 'Collomb': 1.8, 'Beltrame': 1.6,
               'Lakdim': 1.5, 'attentat': 1.5, 'Macron': 1.2}

AppleEvent_dict = {'iPhoneX': 7.2, 'Apple': 4.9, 'iPhone': 1.7,
                   'AppleLive': 2.5, 'iPhoneSE': 2.1, 'AppleTH': 1.9,
                   'iPhone8': 3.6, 'AppleWatch': 1.5, 'iPhone6': 1.2,
                   'AppleEvents': 1.1}

hashtag_tweet_dict = dict()


def get_daily_tweets(file):
    df = pd.read_csv(file)
    df = df.drop(['ID', 'Time_Zone', 'Tweet', 'Hashtags'], axis=1)

    for i, row in df.iterrows():
        if type(row['Time']) is str:
            year = int(row['Date'][0:4])
            month = int(row['Date'][5:7])
            day = int(row['Date'][8:10])

            hour = int(row['Time'][0:2])
            minute = int(row['Time'][3:5])
            second = int(row['Time'][6:8])
            time = datetime.datetime(year=year, month=month, day=day, hour=hour, minute=minute, second=second)
            df.set_value(i, 'Time', time)
    df = df.drop(['Date'], axis=1).drop_duplicates('Username', keep='first')
    time_delta = (df['Time'].iloc[0] - df['Time'].iloc[len(df) - 1]).total_seconds()
    cumulative_tweets = len(df)
    if time_delta != 0:
        tweets_p_second = cumulative_tweets / time_delta
    else:
        tweets_p_second = 0
    tweets_p_hour = tweets_p_second * 60 * 60
    daily_tweets = tweets_p_hour / 0.047
    return daily_tweets
# get_daily_tweets('processed_data_date/iPhone/3/301.csv')


def get_population(ratio, event):
    for dict in os.listdir('processed_data_date'):
        if dict in event:
            for month in os.listdir('processed_data_date/' + dict):
                print(dict, month)
                if month != '.DS_Store':
                    for filename in os.listdir('processed_data_date/' + dict + '/' + month):
                        if filename != '.DS_Store':
                            tweets_p_day = get_daily_tweets('processed_data_date/' + dict + '/' + month + '/' + filename)

                            if dict not in hashtag_tweet_dict:
                                hashtag_tweet_dict[dict] = [tweets_p_day]
                            else:
                                hashtag_tweet_dict[dict].append(tweets_p_day)
    for key in hashtag_tweet_dict:
        hashtag_tweet_dict[key] = (sum(hashtag_tweet_dict[key]) / len(hashtag_tweet_dict[key])) * event[key] * 0.1 * (3 / 2) * 12
    return hashtag_tweet_dict

s = get_population(1, Trebes_dict)
sum = 0

for key in s:
    sum += s[key]
print sum
