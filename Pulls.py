import json
import datetime
from pprint import pprint
import sys
import calendar
import csv

args = sys.argv
directory = args[1]
project = args[2]
file_header = args[1] + "/" + args[2]

def getDate(date_str):
    return datetime.datetime.strptime(date_str, "%Y-%m-%dTH:%M:%SZ")

with open(file_header + "pulls.json", "r", encoding = "utf-8") as data:
    data = [x for x in json.load(data) if x["closed_at"] is not None]

with open(file_header + "issues_comment.json", "r", encoding = "utf-8") as comments:
    comments = [x for x in json.load(comments)]

for d in data:
    d["solve_time"] = getDate(d["closed_at"]) - getDate(d["created_at"])
    d["state"] = "merged" if "merged_at" in d else "closed"
    comment_date = [x for x in comments if x["issue_url"] == d["url"]]
    if len(comment_date) > 0:
        d["comments_time"] = getDate(comment_date[0]["created_at"] - getDate(d["created_at"]))
    else:
        d["comments_time"] = d["solve_time"]

data = sorted(data, key=lambda x:x["comments_time"])

threshold_time = datetime.timedelta(1, 0)

writer = csv.writer(sys.stdout, lineterminator = "\n")

for d in data:
    writer.writerow([d["solve_time"],
                     d["comments_time"],
                     d["title"],
                     d["user"]["login"],
                     d["state"],
                     calendar.day_name[getDate(d["created_at"]).weekday()]])