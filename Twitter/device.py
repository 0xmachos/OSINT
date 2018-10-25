#!/usr/bin/env python2
# OSINT/Twitter/device.py

# device.py
# 	Get the last x tweets from a user
#	Get the device they tweeted from and count number of times

## Imports
import sys
import tweepy
import json
import re
from collections import Counter


def main():
    args = sys.argv[1:]

    if len(args) == 0:
    	print("./tweet-device.py @handle")
    	exit(1)

    username = sys.argv[1]
    num_tweets_retrieved = 100
    device_regex = "(?<=>).*?(?=<)"
    results = []

    auth = tweepy.OAuthHandler(
        'consumer_key', 'consumer_secret')
    auth.set_access_token('access_key',
                          'access_secret_key')

    tweet_list = tweepy.API(auth).user_timeline(
            screen_name=username, count=num_tweets_retrieved)


    for tweet in tweet_list:
    	device = re.findall(device_regex, tweet._json['source'])
    	for x in device:
    		results.append(x)

    count=Counter(results)

    for device, count in count.most_common():
   		print('{} : {}'.format(device, count))

    exit(0)

if __name__== "__main__":
    main()
