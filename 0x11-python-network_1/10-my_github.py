#!/usr/bin/python3

"""
script that takes your Github credentials (username and password)
and uses the Github API to display your id
"""


import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/user"
    r = requests.get(url, auth=(sys.argv[1], sys.argv[2])).json()
    try:
        print(r['id'])
    except:
        print("None")
