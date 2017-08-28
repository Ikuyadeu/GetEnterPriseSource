# -*- coding: utf-8 -*-
# Usage: python3 GetData.py apiurl user owner project
import sys
import os
import requests
import json

args = sys.argv

url = args[1]
user = args[2]
owner = args[3]
project = args[4]

url = api + "/repos/" + owner + "/" + project + "/"

# metricses = ["issues", "pulls", "issues/comments","pulls/comments", "branches", "assignees", "contributors", "languages", "commits", "stats/contributors"]

metricses = ["issues","commits"]

for metrics in metricses:
  page=1
  pages = []
  header = api + "/repos/" + owner + "/" + project + "/"
  while(True):
    url = header + metrics + "?state=all&sort=created&per_page=100"
    resp = requests.get(url + '\&page=' + str(page), auth=requests.auth.HTTPBasicAuth(user, password))
    data = json.loads(resp.content.decode('utf-8'))
    if len(data) <= 1:
      break
    page += 1
    pages.extend(data)
    print(url + '\&page=' + str(page))
      
  print(str(pages).encode('utf-8'))
