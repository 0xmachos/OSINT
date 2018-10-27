#!/usr/bin/env python3
# OSINT/Infrastructure/ct-abuse.py

# ct-abuse.py
#   Enumerate HTTPS enabled subdomains via Certificate Transparency 
#   Also checks which domains are live (http)

# Imports
import sys
import requests
import json
import argparse


def get_subdomains(target_domain):

    url = "https://crt.sh/?q=%25.{}&output=json".format(target_domain)
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1'
    
    req = requests.get(url, headers={'User-Agent': user_agent})
    
    if req.ok:
        data = req.content.decode('utf-8')
        real_json = json.loads("[{}]".format(data.replace('}{', '},{')))
        # Thanks to PaulSec (https://github.com/PaulSec) for the above two lines
        # https://github.com/PaulSec/crt.sh/blob/5354baac7ba711f1730f64aab56915e230892316/crtsh.py#L41-L42 

        domains = []

        for cert in real_json:
            domains.append(cert['name_value'])

        unique_domains = sorted(set(domains))

        print("  All domains: ")
        for domain in unique_domains:
            print("     {}".format(domain))

        return unique_domains


def check_live(domains):

    print("\n  Live domains (HTTP 200): ")
    for domain in domains:
        try:
            if "*" in domain:
                continue
            if requests.get("https://{}".format(domain)).status_code == 200:
                print("       {}".format(domain))
        except requests.exceptions.ConnectionError:
            continue
    print()


def main():

    parser = argparse.ArgumentParser(description="Enumerate HTTPS enabled subdomains via Certificate Transparency")
    parser.add_argument("-t", "--target", action='store', dest='target_domain', required=True,  
                        help="Domain to enumerate")

    args = parser.parse_args()
    check_live(get_subdomains(args.target_domain))

    exit(0)

if __name__== "__main__":
    main()
