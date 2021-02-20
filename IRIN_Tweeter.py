import tweepy
import datetime

consumer_key = '______'
consumer_secret = '_____'
access_token = '________'
access_token_secret = '_________'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

print(datetime.date.today().weekday())