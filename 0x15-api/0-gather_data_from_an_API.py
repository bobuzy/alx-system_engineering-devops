#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    emp_id = str(int(sys.argv[1]))
    user = requests.get(url + "users/" + emp_id).json()
    user_name = user.get("name")
    task_dict = requests.get(url + "todos", params={"userId":emp_id}).json()
    tasks = len(task_dict)
    
    done_tasks = 0
    for task in task_dict:
        if task.get("completed") == True:
            done_tasks += 1

    print("Employee {} is done with tasks({}/{}):".format(
            user_name, done_tasks, tasks))
    for task in task_dict:
        if task.get("completed") == True:
            print("\t ", task.get("title"))
