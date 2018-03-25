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
            user = filename.split('_processed')[0]
            df = pd.read_csv('tweets_of_person/' + parent + '/' + filename)
            hashtags = df['Hashtags']

            for hashtag in hashtags:
                if type(hashtag) == str and hashtag is not None and hashtag.strip() != '' and hashtag.lower() != 'none':
                    hashtag = hashtag.lower()
                    if '[' in hashtag:
                        hashtag = hashtag.replace('[', '').replace(']', '').replace("'", "").split(',')
                        for i in hashtag:
                            i = i.strip()
                            if i .strip() == '':
                                pass
                            elif i not in hashtag_dict:
                                hashtag_dict[i] = set([user])
                            else:
                                hashtag_dict[i].add(user)
                    else:
                        hashtag = hashtag.strip()
                        if hashtag not in hashtag_dict:
                            hashtag_dict[hashtag] = set([user])
                        else:
                            hashtag_dict[hashtag].add(user)
    return hashtag_dict


def assign_number(hashtag_dict):
    users = set([])
    size_dict = dict()
    for key in hashtag_dict:
        user_list = hashtag_dict[key]
        for user in user_list:
            users.add(user)
    for key in hashtag_dict:
        size = float(len(hashtag_dict[key])) / float(len(users))
        size_dict[key] = size
        biggest = float(len(hashtag_dict[key])) / float(len(users))

    return size_dict




# hashtag_dict = shared_tweeters('test_folder')

# assign_number(hashtag_dict)
