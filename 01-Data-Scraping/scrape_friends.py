import time
import tweepy
import csv
import os
import pandas as pd
import json
import numpy as np

# Here you need to put your own API tokens
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


def get_friends(user_id):
    """
    get a list of all followers of a twitter account
    :param user_name: twitter username without '@' symbol
    :return: list of usernames without '@' symbol
    """
#     print("inside")
    api = tweepy.API(auth)
#     print("here")
    friends = []
    i=0
    f = open("scraped_data/%s.json"%user_id,'a+')
    
    for page in tweepy.Cursor(api.friends, screen_name=user_id, wait_on_rate_limit=True,count=200).pages():
        # print(page)
       # if i>2:
        #    break
        try:
            
            for data in page:
#                 print(data)
                
                json.dump(data._json,f,ensure_ascii=False)
                f.write('\n')
#             print(page)
                
            print("k")
            friends.extend(page)
            i+=1
            print(i,len(friends))
            t = time.localtime()
            current_time = time.strftime("%H:%M:%S", t)
            print(current_time)
        except tweepy.TweepError as e:
            print("Going to sleep:", e)
            time.sleep(60)
    print("before close")
    f.close()
    return friends


def save_to_csv(user_name, data, type_='friends',output_dir='./'):
    """
    saves json data to csv
    :param data: data recieved from twitter
    :return: None
    """
    print("inside")
    HEADERS = ["name", "screen_name", "description", "followers_count", "followers_count",
               'friends_count', "listed_count", "favourites_count", "created_at"]
    print("here!!")
    with open(output_dir+user_name + "_%s.csv"%type_, 'w',encoding="utf-8") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(HEADERS)
        for profile_data in data:
            profile = []
            for header in HEADERS:
                profile.append(profile_data._json[header])
            csv_writer.writerow(profile)






df_hate = pd.read_csv("data/hate_groups - SPLC Hate Groups.tsv",sep='\t')
name_hate = list(set(df_hate[(df_hate.iloc[:,0]==1)].Twitter.apply(lambda x: x[1:]).tolist()))
for i in range(len(name_hate)):
    # print(i,name_hate[i])
    if not os.path.exists('scraped_data/%s_friends.csv'%name_hate[i]) :
        print(i,name_hate[i])

        try:
            # user = api.get_user(user_name)
            # friends_count = user.friends_count  
            
            friends = get_friends(name_hate[i])
            print("get friend")
            save_to_csv(name_hate[i], friends, type_ ='friends', output_dir ='scraped_data/')
            print("==============%d %s========"%(i,name_hate[i]))
            f_log=open('scrape_friends.log','a+')
            f_log.write("==============%d %s========"%(i,name_hate[i]))
            f_log.close()
        except:
#             break
            continue
#         break




