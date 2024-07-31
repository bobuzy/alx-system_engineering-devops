#!/usr/bin/python3
"""Create JSON file from information of a given employee"""
import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    emp_id = str(int(sys.argv[1]))
    user = requests.get(url + "users/" + emp_id).json()
    user_name = user.get("name")
    task_dict = requests.get(url + "todos", params={"userId": emp_id}).json()
    tasks = len(task_dict)

    json_file = "{}.json".format(emp_id)

    with open(json_file, "w") as jsonfile:
        json.dump({emp_id: [{
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": user_name
            } for task in task_dict]}, jsonfile)
