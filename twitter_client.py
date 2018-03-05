# Chap02-03/twitter_client.py

import os
import sys
from tweepy import API
from tweepy import OAuthHandler


def get_twitter_auth():
    try:
        consumer_key = 'LkK6GlKXxDuqmeThRhca4PbN0'
        consumer_secret = '5XFYpsQ5fuTwAwJ0xIwDjXHRrFjWwehZwMciwZfyZrEBlSIUHA'
        access_token = '3253298310-DECk7ejxDhudH5Pp6RJ4gfu1xrktfee4uyrbOt5'
        access_secret = 'YTS6QOVykC7z4DCDONfGXWXiRTFTghFh9XsSzv5QKpR23'
    except KeyError:
        print('ey')
        sys.stderr.write("TWITTER_*environment variables not set\n")
        sys.ext(1)
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    return auth


def get_twitter_client():
    auth = get_twitter_auth()
    client = API(auth)
    return client

print(get_twitter_client)
