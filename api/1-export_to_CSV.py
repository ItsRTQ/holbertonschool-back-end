#!/usr/bin/python3
"""This script use a REST API, to retive data from it"""
import csv
import requests
import sys


if __name__ == "__main__":
    userId = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(userId)).json()
    name = user.get("username")
    for_file = requests.get(url + "todos", params={"userId": userId}).json()
    with open("{}.csv".format(userId), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [userId, name, ele.get("completed"), ele.get("title")]
         ) for ele in for_file]
