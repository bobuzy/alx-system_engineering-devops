#!/usr/bin/python3
"""Exports to-do list information of all employees in JSON format"""
import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            us.get("id"): [{
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": us.get("username")
            } for task in requests.get(url + "todos",
                                       params={"userId": us.get("id")}).json()]
            for us in users}, jsonfile)
