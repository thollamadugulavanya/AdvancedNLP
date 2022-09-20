import tweepy
from tweepy import *
import pandas as pd
import csv
import re 
import string
import preprocessor as p
 
consumer_key = "cRR6iEZH6RXZY13rSaeCL5clJ"
consumer_secret = "le7pmHaXmGrIymEYQ6JOZf1938xHzL4JPgR6wF8YkhPkt1FXnS"
access_key= "1565416428257169410-gDKdun1YBJjMFBqwqYqNkAuFQNy8XM"
access_secret = "hiHUlsBlj9AlfeMvTjaaZiGRizg00xTgezjcfbUhkWWAA"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
 
api = tweepy.API(auth,wait_on_rate_limit=True)
 
csvFile = open('C:\\Users\\tholl\\Desktop\\AV.NLP\\fridayfeeling.csv', 'w')
csvWriter = csv.writer(csvFile)
print("Here") 
search_words = "#fridayfeeling"      # enter your words
#new_search = search_words + "retweets"
 
for tweet in tweepy.Cursor(api.search_tweets,q=search_words,count=100,
                           lang="en",
                           since_id=0).items(1000):
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8'),tweet.user.screen_name.encode('utf-8'), tweet.user.location.encode('utf-8')])
