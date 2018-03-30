import pandas as pd
import matplotlib.pyplot as plt
file_path = '/Users/Binderiya/personalwork/GitHub/twitter-ideas-spread/GreatMillsHighSchool_processed.csv'
df  = pd.read_csv(file_path, lineterminator='\n')

df = df.drop(['Unnamed: 0','screen_name', 'text'], axis = 1)
df.time = pd.to_datetime(df['time'], format = '%Y-%m-%d %H:%M:%S', errors = 'coerce')
df = df.dropna()
index = pd.DatetimeIndex(df.time)
ts = pd.Series(df.cumulative_tweets.values, index=index)
ts = ts[~ts.index.duplicated(keep='first')]
start_time = '2018-03-20'
end_time = '2018-03-25'
ts = ts[start_time:end_time]
plt.figure()
ts.plot()
plt.show()
converted = ts.asfreq('10min', method='pad')
converted.to_csv(path= 'GreatMills.csv', header = False, index = False)

