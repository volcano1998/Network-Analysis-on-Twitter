import tweepy
import pandas as pd
import numpy as np
import json
import time

# here you should add your own tokens
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

with open("retweet.txt",'r') as f:
    id_list = f.read().split('\n')[:-1]
    
for i in range(len(id_list)):
    tweet_id = id_list[i]
    try:
        retweets_list = api.retweets(tweet_id)
    except:
        time.sleep(61*15)
        retweets_list = api.retweets(tweet_id)
    f = open("retweet.txt","a+")  
    for retweet in retweets_list:
        user_id = retweet._json['user']['id_str']
        user_name = retweet._json['user']['screen_name']
        s = '%s,%s,%s\n'%(tweet_id,user_id,user_name)
        f.write(s)