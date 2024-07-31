#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import csv
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    emp_id = str(int(sys.argv[1]))
    user = requests.get(url + "users/" + emp_id).json()
    user_name = user.get("name")
    task_dict = requests.get(url + "todos", params={"userId": emp_id}).json()

    csv_file = "{}.csv".format(emp_id)
    fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS",
                  "TASK_TITLE"]

    with open(csv_file, mode='w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames,
                                quoting=csv.QUOTE_ALL)

        for task in task_dict:
            writer.writerow({
                "USER_ID": emp_id,
                "USERNAME": user_name,
                "TASK_COMPLETED_STATUS": task['completed'],
                "TASK_TITLE": task['title']
            })
