# Usage: python3 GetData.py apiurl owner project
import sys
import os

args = sys.argv
print(args)

url = args[1]
owner = args[2]
project = args[3]

url = url + "/repos/" + owner + "/" + project + "/"

os.system("curl -i " + url + "issues\\?state=all\&sort=created > " + project + "-issues.json")
os.system("curl -i " + url + "pulls\\?state=all\&sort=created > " + project + "-pulls.json")
os.system("curl -i " + url + "issues/comments\\?state=all\&sort=created > " + project + "-comments.json")
os.system("curl -i " + url + "branches\\?state=all\&sort=created > " + project + "-branchs.json")
os.system("curl -i " + url + "commits\\?state=all\&sort=created > " + project + "-commits.json")
os.system("curl -i " + url + "assignees\\?state=all\&sort=created > " + project + "-assignees.json")
