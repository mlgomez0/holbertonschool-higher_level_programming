#!/usr/bin/python3
# takes URL, sends a POST with variable q, displays [<id>] <name> or print error
import requests
import sys

url = sys.argv[1]
req = requests.get(url)
if req.status_code < 400:
    print(req.text)
else:
    print("Error code: {}".format(req.status_code))
