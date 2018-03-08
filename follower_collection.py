import tweepy
import time


# NRA_prototype = '@DLoesch'
# Surviver_prototype = '@Emma4Change'
# Donald_prototype = '@realDonaldTrump'
def get_followers(username):

    key1 = "LkK6GlKXxDuqmeThRhca4PbN0"
    key2 = "5XFYpsQ5fuTwAwJ0xIwDjXHRrFjWwehZwMciwZfyZrEBlSIUHA"
    key3 = "3253298310-DECk7ejxDhudH5Pp6RJ4gfu1xrktfee4uyrbOt5"
    key4 = "YTS6QOVykC7z4DCDONfGXWXiRTFTghFh9XsSzv5QKpR23"

    auth = tweepy.OAuthHandler(key1, key2)
    auth.set_access_token(key3, key4)

    api = tweepy.API(auth)

    users = tweepy.Cursor(api.followers, screen_name=username, count=200).items()
    with open('followers_of_person/' + username + "_followers.txt", "w") as text_file:

        while True:
            try:
                user = next(users)
            except tweepy.TweepError:
                time.sleep(60 * 15)
                user = next(users)
            except StopIteration:
                break
            print "@" + user.screen_name
            text_file.write("@" + user.screen_name + "\n")

get_followers('@cameron_kasky')
