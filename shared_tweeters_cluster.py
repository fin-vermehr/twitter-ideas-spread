import os
import pandas as pd
import numpy as np
from pprint import pprint


def shared_tweeters(parent):
    hashtag_dict = dict()
    data_length = 0
    for filename in os.listdir('tweets_of_person/' + parent):
        if filename == '.DS_Store':
            pass
        else:
            data_length += 1
            user = filename.split('_')[0]
            df = pd.read_csv('tweets_of_person/' + parent + '/' + filename)
            hashtags = df['Hashtags']

            for hashtag in hashtags:
                if type(hashtag) == str and hashtag is not None and hashtag.strip() != '':
                    if '[' in hashtag:
                        hashtag = hashtag.replace('[', '').replace(']', '').replace("'", "").split(',')
                        for i in hashtag:
                            i = i.strip()
                            if i .strip() == '':
                                pass
                            elif i not in hashtag_dict:
                                hashtag_dict[i] = [user]
                            else:
                                hashtag_dict[i].append(user)
                    else:
                        hashtag = hashtag.strip()
                        if hashtag not in hashtag_dict:
                            hashtag_dict[hashtag] = [user]
                        else:
                            hashtag_dict[hashtag].append(user)
    print hashtag_dict
    for key in hashtag_dict:
        if len(hashtag_dict[key]) > data_length * 0.15:
            print key

shared_tweeters('Emma4Change')
