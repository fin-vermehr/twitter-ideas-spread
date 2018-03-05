import tweepy
import time

# NRA_prototype = '@DLoesch'
# Surviver_prototype = '@Emma4Change'
# Donald_prototype = '@realDonaldTrump'
def get_followers(username):

    key1 = "k"
    key2 = "k"
    key3 = "k"
    key4 = "k"

    accountvar = username

    auth = tweepy.OAuthHandler(key1, key2)
    auth.set_access_token(key3, key4)

    api = tweepy.API(auth)

    users = tweepy.Cursor(api.followers, screen_name=accountvar, count=200).items()
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

get_followers('@realDonaldTrump')
