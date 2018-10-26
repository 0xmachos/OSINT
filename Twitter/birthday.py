#!/usr/bin/env python3
# OSINT/Twitter/birthday.py

# birthday.py
#  Search for tweets to a user which contain 'birthday' or 'bday'

# Imports
import sys
import requests
import collections
import argparse
from bs4 import BeautifulSoup


def make_soup(username):

    search_url = "https://twitter.com/search?f=tweets&vertical=default&q=birthday%20OR%20bday%20to%3A{}".format(username)
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1'
    r = requests.get(search_url, headers={'User-Agent': user_agent})
    
    soup = BeautifulSoup(r.text, 'html.parser')

    dates = soup.findAll("a", {"class": "tweet-timestamp js-permalink js-nav js-tooltip"})
    tweets = soup.findAll("div", {"class": "js-tweet-text-container"})

    return dates, tweets


def extract_data(dates, tweets):

    date_list = []
    tweet_list = []

    for title in dates:
        x = title.get("title")
        date_list.append(x.split('-')[1].strip())

    for tweet in tweets:
        x = tweet.find('p').getText()
        tweet_list.append(x)

    return date_list, tweet_list


def main():

    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-t", "--target", action='store', dest='username', required=True,  
                        help="Targets Twitter username")
    args = parser.parse_args()
    
    username = args.username
    
    dates, tweets = make_soup(username)
    date_list, tweet_list = extract_data(dates, tweets)

    print("\nTweets to @{} containing 'birthday' or 'bday':\n".format(username))
    for date, tweet_text in zip(date_list, tweet_list):
        print("  {} : {}".format(date, tweet_text))

    print("\nTop Three Dates: \n")
    for date in collections.Counter(date_list).most_common(3):
        day = date[0].split(' ')[0]
        month = date[0].split(' ')[1]
        print("  {} {} ({})".format(month, day, date[1]))

    print()
    exit(0)

if __name__== "__main__":
    main()
