import os
import pprint
import csv
import pandas as pd
import numpy as np
import re

def clean_hashtag(hashtag, tweet, tag_index):
    if 'http://' in tweet or 'https://' in tweet:

        if 'http://' in tweet:
            link_beg = tweet.find('http://')

        if 'https://' in tweet:
            link_beg = tweet.find('https://')

        link_end = tweet.find(' ', link_beg)
        if link_end == -1:
            link_end = len(tweet)

        if tag_index >= link_beg and tag_index <= link_end:
            hashtag = ''

    if 'pic.' in hashtag:
        index = hashtag.find('pic.')
        hashtag = hashtag[:index]

    if 'http:' in hashtag:
        index = hashtag.find('http:')
        hashtag = hashtag[:index]

    if 'https:' in hashtag:
        index = hashtag.find('https:')
        hashtag = hashtag[:index]
    hashtag = re.sub('[^A-Za-z0-9]+', '', hashtag)
    if hashtag.isdigit():
        hashtag = ''
    return hashtag


def find_hashtags(line):
    line = line.split(" ", 5)
    try:
        if '#' in line[5]:
            indices = [i for i in range(len(line[5])) if line[5].startswith('#', i)]
            hashtag_list = list()
            if len(indices) > 1:
                for index in indices:
                    hashtag_end = line[5].find(' ', index)
                    hashtag = line[5][index:hashtag_end]
                    if hashtag.count('#') > 1:
                        tmp = hashtag[1:].split('#')
                        for i in tmp:
                            hashtag_list.append(clean_hashtag(i, line[5], index))
                    else:
                        hashtag_list.append(clean_hashtag(line[5][index:hashtag_end], line[5], index))
                return hashtag_list

            else:
                beginning = indices[0]
                end = line[5].find(' ', indices[0])
                hashtag = line[5][beginning: end]
                hashtag = clean_hashtag(hashtag, line[5], indices[0])
                return hashtag
    except(IndexError):
        print(line)

    else:
        return None


def write_data(write_to, read_from):
    print('Writing DATA')
    f = open(read_from, 'r')
    text_file = f.readlines()
    f.close()

    with open(write_to + '.csv', 'w') as csvfile:
        fieldnames = ['ID', 'Date', 'Time', 'Time_Zone', 'Username', 'Tweet', 'Hashtags']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'ID': 'ID', 'Date': 'Date', 'Time': 'Time', 'Time_Zone': "Time_Zone", 'Username': "Username", 'Tweet': 'Tweet', 'Hashtags': 'Hashtags'})

        for line in text_file:
            hashtags = str(find_hashtags(line))
            line = line.split(" ", 5)
            writer.writerow({'ID': line[0], 'Date': line[1], 'Time': line[2], 'Time_Zone': line[3], 'Username': line[4].replace('<', '').replace('>', ''), 'Tweet': line[5], 'Hashtags': hashtags})


def raw_data(twitter_username, parent):
    if not os.path.exists('raw_data_of_person/' + parent):
        print ('Making Directory raw_data_of_person/' + parent)
        os.makedirs('raw_data_of_person/' + parent)
    if not os.path.exists('tweets_of_person/' + parent):
        print ('Making Directory tweets_of_person/' + parent)
        os.makedirs('tweets_of_person/' + parent)

    os.system("python3 tweep.py -u " + twitter_username + " -o " + 'raw_data_of_person/' + parent + '/' + twitter_username + "_raw_data.txt --since 2016-01-20")
    try:
        write_data('tweets_of_person/' + parent + '/' + twitter_username + '_processed', 'raw_data_of_person/' + parent + '/' + twitter_username + "_raw_data.txt")
    except:
        IOError
