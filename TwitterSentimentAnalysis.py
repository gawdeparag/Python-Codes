import tweepy
from textblob import TextBlob

consumer_key = 'lLma59kfdeyEAtCiSZfcMzpIc'
consumer_secret = 'Qx9RwxuHl7luVbuH7y9bS2EdEycJlroYgHCyO5izA95ciY0dSe'
access_token = '2685104628-TFLbgKF06V7QaNsJL010g8ocGe1rkpmHGCyBUvm'
access_token_secret = 'e9rokqrPqRuEtyEE43C4sMHzCdRj7XA0xgZm6MUbSIDJV'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

for tweets in public_tweets: 
    print(tweets.text)
    analysis = TextBlob(tweets.text)
    print(analysis.sentiment)