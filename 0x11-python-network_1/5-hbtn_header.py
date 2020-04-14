#!/usr/bin/python3
# script that fetches https://intranet.hbtn.io/statu,  variable X-Request-Id

import requests
import sys

url = sys.argv[1]
req = requests.get(url)
print(req.headers['X-Request-Id'])
