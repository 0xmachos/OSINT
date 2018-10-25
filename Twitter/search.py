#!/usr/bin/env python3
# OSINT/Twitter/search.py

# search.py
#   Search Twitter users name and username for a string 
#   Use dump.py to get the data

# Imports
import sys
import argparse
import re
import signal


def ctrl_c(sig, frame):
    print("\n{} chose to quit via CTRL+C!".format(os.environ['USER']))
    sys.exit(0)


def search_following(username, search_string):

    filepath = "{}/following".format(username)
    with open(filepath) as fp:  
        for line in fp:
            fields = line.strip().split('|')
            names = "{}:{}".format(fields[1], fields[2])
            if re.search(search_string, names, re.IGNORECASE):
                print("Following match: {}".format(names))


def search_followers(username, search_string):

    filepath = "{}/followers".format(username)
    with open(filepath) as fp:  
        for line in fp:
            fields = line.strip().split('|')
            names = "{}:{}".format(fields[1], fields[2])
            if re.search(search_string, names, re.IGNORECASE):
                print("Followers match: {}".format(names))


def main():

    parser = argparse.ArgumentParser(description="Get a list of Twitter users Followers and Following")
    parser.add_argument("-u", "--username", action='store', dest='username', required=True,  
                        help="Targets Twitter username")
    parser.add_argument("-s", "--search", action='store', dest='search_string', required=True,  
                        help="String to search")
    args = parser.parse_args()

    signal.signal(signal.SIGINT, ctrl_c)

    username = args.username
    search_string = args.search_string
    
    search_following(username, search_string)
    search_followers(username,search_string)

    exit(0)

if __name__== "__main__":
    main()
