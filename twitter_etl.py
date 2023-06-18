import tweepy
import pandas as pd
import s3fs
import json
from datetime import datetime


def run_twitter_etl():

    access_key = ""
    access_secret = ""
    consumer_key = ""
    consumer_secret = ""

    # Creating connection between this code and twitter api
    # Twitter authentication
    auth = tweepy.OAuthHandler(access_key,access_secret)
    auth.set_access_token(consumer_key,consumer_secret)

    # Creating an api object
    api = tweepy.API(auth)

    # Extracting data from twitter API
    tweets = api.user_timeline(
        screen_name = "@elonmusk", # twitter account
        count = 100,               # How many tweets to extract from particular timeline
        include_rts = False,       # Para for retweets
        tweet_mode = "extended" )

    tweet_list = []
    for tweet in tweets:
        text = tweet.json["full_text"]

        refined_tweet = {
            "user": tweet.user.screen_name,
            'text' : text,
            'favorite_count' : tweet.favorite_count,
            'retweet_count' : tweet.retweet_count,
            'created_at' : tweet.created_at
        }
        tweet_list.append(refined_tweet)

    df = pd.DataFrame(tweet_list)
    df.to_csv("s3://twitter-pipeline-project/elommusk_twitter_data.csv")