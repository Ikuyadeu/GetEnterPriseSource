# -*- coding: utf-8 -*-
"""
Summary: Get single file history and real file
Usage: mkdir out
       pip3 install requests
       python3 GetSyngleFile.py YourGitHubID GitHubPassword owner project filePath
       (e.g.) python3 GetSyngleFile.py GitTaro Gitpass Ikuyadeu vscode-r README.md
Warning: This script can't get identify Readme.md README.md
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

PROJECT_PATH = OWNER + "/" + PROJECT

URL = "https://api.github.com/repos/" \
      + PROJECT_PATH \
      + "/commits"

RAW_URL = "https://raw.githubusercontent.com/" + PROJECT_PATH

PAGE = 1
COMMITS = []

AUTH = requests.auth.HTTPBasicAuth(USER, PASSWORD)
PARAMS = {"path": PATH,
          "per_page": 100,
          "page": 1,}

# Get All commit log
while True:
    PARAMS["page"] = PAGE
    RESP = requests.get(URL,
                        params=PARAMS,
                        auth=AUTH)
    print(RESP.url)
    DATA = json.loads(RESP.content.decode("utf-8"))
    if len(DATA) <= 1:
        break
    PAGE += 1
    COMMITS.extend(DATA)

# Output Commit log
with open(OUT_DIR + OWNER +"-" + PROJECT + ".json", "w") as f:
    json.dump(COMMITS, f, indent=4)
    print("Output commit log to" + OUT_DIR + OWNER +"-" + PROJECT + ".json")

# Curl real files
for commit in COMMITS:
    FILE_URL = RAW_URL + "/" + commit["sha"] + "/" + PATH
    RESP = requests.get(FILE_URL, auth=AUTH)
    CONTENT = RESP.content.decode("utf-8")
    with open(OUT_DIR + commit["sha"] + "-" + PATH, "w") as f:
        f.write(CONTENT)
