# -*- coding: utf-8 -*-
"""
Summary: Get single file history and real file
Usage: mkdir out
       pip3 install requests
       python3 GetReadme.py YourGitHubID GitHubPassword owner project filePath
       (e.g.) python3 python3 GetReadme.py GitTaro Gitpass Ikuyadeu vscode-r Readme.md
"""
import json
import sys

import requests

ARGS = sys.argv

USER = ARGS[1]
PASSWORD = ARGS[2]
OWNER = ARGS[3]
PROJECT = ARGS[4]
PATH = ARGS[5]
OUT_DIR = "out/"

URL = "https://api.github.com/repos/" \
      + OWNER \
      + "/" \
      + PROJECT \
      + "/commits"

RAW_URL = "https://raw.githubusercontent.com/" \
          + OWNER \
          + "/" \
          + PROJECT

PAGE = 1
PAGES = []

while True:
    PARAMS = (
        ("path", PATH),
        ("per_page", 100),
        ("page", PAGE),
    )
    RESP = requests.get(URL,
                        params=PARAMS,
                        auth=requests.auth.HTTPBasicAuth(USER, PASSWORD))
    DATA = json.loads(RESP.content.decode("utf-8"))
    if len(DATA) <= 1:
        break
    print(URL + '&page=' + str(PAGE))
    PAGE += 1
    PAGES.extend(DATA)

with open(OUT_DIR + OWNER +"-" + PROJECT + ".json", "w") as f:
    json.dump(PAGES, f, indent=4)
    print("Output commit log to" + OUT_DIR + OWNER +"-" + PROJECT + ".json")

for data in PAGES:
    FILE_URL = RAW_URL + "/" + data["sha"] + "/" + PATH
    RESP = requests.get(FILE_URL, auth=requests.auth.HTTPBasicAuth(USER, PASSWORD))
    with open(OUT_DIR + data["sha"] + "-" + PATH, "w") as f:
        f.write(RESP.content.decode("utf-8"))
