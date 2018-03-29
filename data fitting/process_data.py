import pandas as pd
import matplotlib.pyplot as plt
df  = pd.read_csv('/Users/Binderiya/personalwork/GitHub/twitter-ideas-spread/Trebes_processed.csv', lineterminator='\n')

df = df.drop(['Unnamed: 0','screen_name', 'text'], axis = 1)
df.time = pd.to_datetime(df['time'], format = '%Y-%m-%d %H:%M:%S', errors = 'coerce')
df = df.dropna()
index = pd.DatetimeIndex(df.time)
ts = pd.Series(df.cumulative_tweets.values, index=index)
ts = ts[~ts.index.duplicated(keep='first')]
plt.figure()
ts.plot()
plt.show()
converted = ts.asfreq('30min', method='pad')
converted.to_csv(path= 'Trebes.csv', header = False, index = False)

