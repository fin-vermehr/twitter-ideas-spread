import pandas as pd
import matplotlib.pyplot as plt
<<<<<<< HEAD
df  = pd.read_csv('DeleteFacebook_processed.csv')
=======
df  = pd.read_csv('DeleteFacebook_processed.csv', lineterminator='\n')
>>>>>>> f023e21c473fecc513c0d95e267912e9367e1503
df = df.drop(['Unnamed: 0','screen_name', 'text'], axis = 1)
df.time = pd.to_datetime(df['time'], format = '%Y-%m-%d %H:%M:%S', errors = 'coerce')
df = df.dropna()
index = pd.DatetimeIndex(df.time)
ts = pd.Series(df.cumulative_tweets.values, index=index)
ts = ts[~ts.index.duplicated(keep='first')]
<<<<<<< HEAD
converted = ts.asfreq('15min', method='pad')
converted.to_csv(path= 'DeleteFacebook.csv', header = False, index = False)
=======
plt.figure()
ts.plot()
plt.show()
converted = ts.asfreq('30min', method='pad')
converted.to_csv(path= 'DeleteFacebook.csv', header = False, index = False)
>>>>>>> f023e21c473fecc513c0d95e267912e9367e1503
