# -*- coding: utf-8 -*-
# Usage: python3 GetData.py apiurl user password owner project
import sys
import os
import requests
import json

args = sys.argv

api = args[1]
user = args[2]
password = args[3]
owner = args[4]
project = args[5]
# curl -i https://api.github.com/repos/Ikuyadeu/vscode-r/issues\?state=all\&sort=created > issues.json

url = api + "/repos/" + owner + "/" + project + "/"

metricses = ["issues", "pulls", "issues/comments","pulls/comments", "branches", "assignees", "contributors", "languages", "commits", "stats/contributors"]

for metrics in metricses:
  page=1
  pages = []
  header = api + "/repos/" + owner + "/" + project + "/"
  while(True):
    print(metrics + ":" + page)
    url = header + metrics + "?state=all&sort=created&per_page=6"
    resp = requests.get(url + '&page=' + str(page), auth=requests.auth.HTTPBasicAuth(user, password))
    data = json.loads(resp.content.decode('utf-8'))
    if len(data) <= 1:
      break
    page += 1
    pages.extend(data)
  with open(project + "-" + metrics.replace('/', '_') + "2.json", "w") as f:
    json.dump(pages, f, indent=4)
