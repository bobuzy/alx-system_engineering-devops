#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys
import csv


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    emp_id = str(int(sys.argv[1]))
    user = requests.get(url + "users/" + emp_id).json()
    user_name = user.get("name")
    task_dict = requests.get(url + "todos", params={"userId": emp_id}).json()

    csv_file = "{}.csv".format(emp_id)

    with open(csv_file, mode='w', newline='') as csvfile:
        for task in task_dict:
            csvfile.write('"{}","{}","{}","{}"\n'.format(
                emp_id, user_name, task.get("completed"), task.get("title")))
