#!/usr/bin/python3
# takes URL, sends a POST with variable q, displays [<id>] <name> or print error
import requests
import sys
from requests.auth import HTTPBasicAuth

user = sys.argv[1]
passwd = sys.argv[2]
try:
    req = requests.get('https://api.github.com/user', auth=HTTPBasicAuth(user, passwd))
    dir_element = req.json()
    print(dir_element['id'])
except:
    print("None")
