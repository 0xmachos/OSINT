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
import argparse
from collections import Counter


def get_device(auth, username, count):

    device_regex = "(?<=>).*?(?=<)"
    results = []
    
    tweet_list = tweepy.API(auth).user_timeline(
        screen_name=username, count=count)

    for tweet in tweet_list:
        device = re.findall(device_regex, tweet._json['source'])
        for x in device:
            results.append(x)

    count=Counter(results)

    for device, count in count.most_common():
        print('{} : {}'.format(device, count))


def main():

    auth = tweepy.OAuthHandler(
        'consumer_key', 'consumer_secret')
    auth.set_access_token('access_key',
                          'access_secret_key')

    parser = argparse.ArgumentParser(description="Print the devices the target used to tweet")
    parser.add_argument("-t", "--target", action='store', dest='username', required=True,  
                        help="Targets Twitter username")
    parser.add_argument("-c", "--count", action='store', dest='count', default=100,  
                        help="Number of tweets to retrieve")
    args = parser.parse_args()

    username = args.username
    count = args.count

    get_device(auth, username, count)

    exit(0)

if __name__== "__main__":
    main()
