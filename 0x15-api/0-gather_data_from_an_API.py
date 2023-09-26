#!/usr/bin/python3
"""module to get employee information from REST API"""
from requests import get
from sys import argv


if __name__ == "__main__":
    detail_task = get(f"https://jsonplaceholder.typicode.com/users/{argv[1]}")
    task = get(f"https://jsonplaceholder.typicode.com/users/{argv[1]}/todos")
    data_1 = task.json()
    info_data = detail_task.json()
    total_task = len(data_1)
    completed_task = 0
    complete_task = []
    for i in data_1:
        if i.get('completed') is True:
            completed_task += 1
            complete_task.append(i)
    print(f"Employee {info.get('name')} is done with"
          f" tasks({completed}/{total}):")
    for i in complete_task:
        print(f"\t {i.get('title')}")
