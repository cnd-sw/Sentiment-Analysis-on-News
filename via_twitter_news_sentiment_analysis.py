# -*- coding: utf-8 -*-
"""via_twitter_news_sentiment_analysis

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ClH8H29f_Ljen0jmGAjrqnDKWdSfLalx
"""

pip install vaderSentiment

pip install cartopy

pip install tweepy

pip install cartopy

# Dependencies
import tweepy
import cartopy
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json
import time
from datetime import datetime
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()



consumer_key = 'your_customer_key'
consumer_secret = 'your_customer_secret_key'

access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

target_users = ["@BBCWorld", "@CBSNews", "@CNN", "@FoxNews", "@nytimes"]

# Variables for holding sentiments
source_account = []
text = []
date = []
tweets_ago = []
compound_list = []
positive_list = []
negative_list = []
neutral_list = []

# Looping through all target users
for user in target_users:
     # Variable for holding the oldest tweet
    oldest_tweet = None

    tweet_count = 0
    # Get the last 100 tweets
    for x in range(5):
        # get all tweets from the home feed
        public_tweets = api.user_timeline(user, count=100, result_type="recent", max_id=oldest_tweet)
        #loop through all tweets
        for tweet in public_tweets:
            # keep adding the tweet_count
            tweet_count +=1
            #append values to empty lists
            source_account.append(user)
            text.append(tweet['text'])
            date.append(tweet['created_at'])
            tweets_ago.append(tweet_count)

            # Run the Vader Analysis on each tweet
            compound = analyzer.polarity_scores(tweet['text'])['compound']
            pos = analyzer.polarity_scores(tweet['text'])['pos']
            neg = analyzer.polarity_scores(tweet['text'])['neg']
            neu = analyzer.polarity_scores(tweet['text'])['neu']

            # append the values to the lists
            compound_list.append(compound)
            positive_list.append(pos)
            negative_list.append(neg)
            neutral_list.append(neu)

