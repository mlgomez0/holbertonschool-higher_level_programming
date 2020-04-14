#!/usr/bin/python3
# takes URL, displays body of response and print error for status code >= 400

import requests
import sys

url = sys.argv[1]
req = requests.get(url)
if req.status_code < 400:
    print(req.text)
else:
    print("Error code: {}".format(req.status_code))
