# -*- coding: utf-8 -*-
# Usage: pip3 install requests
#        python3 GetReadme.py YourGitHubID GitHubPassword owner project
import sys
import os
import json
import requests

ARGS = sys.argv

user = ARGS[1]
password = ARGS[2]
owner = ARGS[3]
project = ARGS[4]

url = "https://api.github.com/repos/" + owner + "/" + project + "/commits?path=README.md&per_page=100"

page = 1
pages = []
while(True):
    resp = requests.get(url + '&page=' + str(page), auth=requests.auth.HTTPBasicAuth(user, password))
    data = json.loads(resp.content.decode('utf-8'))
    if len(data) <= 1:
        break
    print(url + '&page=' + str(page))
    page += 1
    pages.extend(data)
with open(owner +"-" + project + ".json", "w") as f:
    json.dump(pages, f, indent=4)
