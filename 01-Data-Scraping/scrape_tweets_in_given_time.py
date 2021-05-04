## here is how you scrape what they were tweeting during 2020-12-31 and 2021-01-19, 

# To run this code, you need to have twitter premium API or academic API


for i in range(len(all_name)):
    screen_name = all_name[i]
    print(i,screen_name)
    cmd ="search_tweets.py "+\
      "--max-tweets 1000 "+\
      "--results-per-call 500 "\
      "--query 'from:%s' "%screen_name+\
      "--start-time '2020-12-31' "+\
      "--end-time '2021-01-19' "+\
      "--tweet-fields 'created_at,id,text,geo,author_id,in_reply_to_user_id,lang' "+\
      "--filename-prefix %s  "%screen_name+\
      "--print-stream"


    process = Popen([cmd], shell =True)
    process.wait()
