#!/usr/bin/python3
"""10 commits from the newest of the repository rails by given user"""
import requests
import sys

if __name__ == "__main__":

    user = sys.argv[2]
    repo = sys.argv[1]
    url = "https://api.github.com/repos/" + user + "/" + repo + "/commits"
    try:
        req = requests.get(url)
        d = req.json()
        for i in range(10):
            print("{}: {}".format(d[i]['sha'], d[i]['commit']['author']['name']))
    except:
        print("None")
