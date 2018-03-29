import pandas as pd
import matplotlib.pyplot as plt
df  = pd.read_csv('DeleteFacebook_processed.csv')
df = df.drop(['Unnamed: 0','screen_name', 'text'], axis = 1)
df.time = pd.to_datetime(df['time'], format = '%Y-%m-%d %H:%M:%S', errors = 'coerce')
df = df.dropna()
index = pd.DatetimeIndex(df.time)
ts = pd.Series(df.cumulative_tweets.values, index=index)
ts = ts[~ts.index.duplicated(keep='first')]
converted = ts.asfreq('15min', method='pad')
converted.to_csv(path= 'DeleteFacebook.csv', header = False, index = False)
