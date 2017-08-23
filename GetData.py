# Usage: python3 GetData.py apiurl user owner project
import sys
import os

args = sys.argv
print(args)

url = args[1]
user = args[2]
owner = args[3]
project = args[4]
# curl -i https://api.github.com/repos/Ikuyadeu/vscode-r/issues\?state=all\&sort=created > issues.json

url = "https://api.github.com"
owner = "Ikuyadeu"
project = "vscode-r"

url = url + "/repos/" + owner + "/" + project + "/"

metricses = ["issues", "pulls", "issues/comments", "branches", "assignees"]

for metrics in metricses:
  os.system("curl -i "+ url + metrics + "\\?state=all\&sort=created\&per_page=100 > " + project + "-" + metrics.replace('/', '_') + ".json")
