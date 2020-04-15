#!/usr/bin/python3
# list 10 commits (from the most recent to oldest) of the repository rails by given user
import requests
import sys

user = sys.argv[2]
repo = sys.argv[1]
url = "https://api.github.com/repos/" + user + "/" + repo + "/commits"
req = requests.get(url)
dir_element = req.json()
print("{}: {}".format(dir_element['id'])
except:
    print("None")
