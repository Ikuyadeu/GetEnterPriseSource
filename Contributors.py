import json
import datetime
import sys
import calendar
import csv
import collections

args = sys.argv
directory = args[1]
project = args[2]
file_header = args[1] + "/" + args[2]

with open(file_header + "issues.json", "r", encoding = "utf-8") as data:
    data = [x for x in json.load(data) if x["closed_at"] is not None]

developer_list = []

metricses1 = [("contributors", "contributions")]
statuses = {}
for metrics in metricses1:
    with open(file_header + metrics[0] + ".json", "r", encoding = "utf-8") as data:
        statuses[metrics[0]] = {x["login"]:x[metrics[1]] for x in json.load(data)}
        developer_list.extend(statuses[metrics[0]].keys())

metricses2 = ["issues", "pulls", "issues_comments", "pulls_comment"]
for metrics in metricses2:
    with open(file_header + metrics + ".json", "r", encoding = "utf-8") as data:
        statuses[metrics] = collections.Counter([x["user"]["login"] for x in json.load(data)])
        developer_list.extend(statuses[metrics].keys())

developer_list = set(developer_list)

developers = {}

metricses = ["contributors"] + metricses2

for login in developer_list:
    developers[login] = {}
    developer = developers[login]
    developer["login"] = login
    for metrics in metricses:
        developer[metrics] = statuses[metrics][login] if login in statuses[metrics] else 0

writer = csv.DictWriter(sys.stdout, lineterminator="\n", fieldnames = ["login"] + metricses)
writer.writeheader()
for login, developer in developers.items():
    writer.writerow(developer)
