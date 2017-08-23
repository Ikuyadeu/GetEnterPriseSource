# Usage: python3 GetData.py apiurl user owner project
import sys
import os

args = sys.argv
print(args)

url = args[1]
user = args[2]
owner = args[3]
project = args[4]

url = url + "/repos/" + owner + "/" + project + "/"

metricses = ["issues", "pulls", "issues/comments", "branches", "assignees", "contributors", "languages"]

for metrics in metricses:
  os.system("curl -u " + user + " "+ url + metrics + "\\?state=all\&sort=created\&per_page=100 > " + project + "-" + metrics.replace('/', '_') + ".json")
