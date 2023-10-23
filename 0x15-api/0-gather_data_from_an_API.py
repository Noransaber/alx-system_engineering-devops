#!/usr/bin/python3
"""Return information about TODO list progress"""
import requests
from sys import argv
import json
import requests

if __name__ == "__main__":
    user_id = argv[1]

    # URL of the api
    url = "https://jsonplaceholder.typicode.com/"

    # USER ID
    url_user_id = "user/{}".format(user_id)

    # To Do
    todo_url = "todos"

    # To get the user
    user = requests.get(url + url_user_id).json()

    # To get the tasks
    tasks = requests.get(url + todo_url, params={"userId" : user_id}).json()

    # Compeleted tasks
    cmp_tasks = [task for task in tasks if task.get("completed") is True]

    print("Employee {} is done with tasks({}/{}):".format(user.get("name"),
                                                          len(cmp_tasks),
                                                       len(tasks)))

    [print("\t {}".format(task.get("title"))) for task in cmp_tasks]
