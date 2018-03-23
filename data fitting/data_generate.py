#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 10:15:32 2018

@author: Binderiya
"""
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd 
num_sample = 150
def sigmoid(x, c, a, d):
    return float(c)/(1 + np.exp((a-x)/float(d)))
noise = abs(np.random.normal(scale = 300, size = num_sample))
times = np.linspace(1, 199, num_sample)
num_tweets = sigmoid(times, 70000, 90, 12)
num_tweets += noise
num_tweets = num_tweets.reshape(num_sample, 1)
times =  times.reshape(num_sample, 1)
data = np.concatenate((times, num_tweets), axis = 1)
df = pd.DataFrame(data, columns = ['times', 'number of tweets'])
df.to_csv(path_or_buf = 'simulated_data.csv', header = False, index = False)

plt.scatter(times, num_tweets, marker = '.')
plt.ylabel('Number of tweets')
plt.xlabel('Time elapsed (hours)')
plt.title('Number of tweets vs Time (simulated)')
plt.show()