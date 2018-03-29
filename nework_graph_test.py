import tweepy
import csv
import pandas as pd
####input your credentials here
consumer_key = 'LkK6GlKXxDuqmeThRhca4PbN0'
consumer_secret = '5XFYpsQ5fuTwAwJ0xIwDjXHRrFjWwehZwMciwZfyZrEBlSIUHA'
access_token = '3253298310-DECk7ejxDhudH5Pp6RJ4gfu1xrktfee4uyrbOt5'
access_token_secret = 'YTS6QOVykC7z4DCDONfGXWXiRTFTghFh9XsSzv5QKpR23'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

def scrape_twitter(hashtag):
    #####United Airlines
    # Open/Create a file to append data
    csvFile = open(hashtag + '.csv', 'a')
    #Use csv Writer
    csvWriter = csv.writer(csvFile)
    for tweet in tweepy.Cursor(api.search,q="#" + hashtag, count=100,
                               lang="en",
                               since="2018-02-13", show_user=True).items():
        print (tweet.created_at, tweet.text, tweet.user.screen_name)
        csvWriter.writerow([tweet.created_at, tweet.user.screen_name.encode('utf-8'), tweet.text.encode('utf-8')])

hashtag_list = ['DeleteFacebook']
# GreatMillsHighSchool', 'GreatMills', 'marylandschoolshooting
for hashtag in hashtag_list:
    print hashtag
    scrape_twitter(hashtag)
