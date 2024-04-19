#!/usr/bin/python3
"""This script use a REST API, to retive data from it to a json file"""
import json
import requests
import sys


def get_username(id):
    """This method grabs the username of the given employeeId
        Args:
            id = targeted id to fetch data
        Returns:
            The username of the employee
        Exceptions:
            ValueError - if id is not existing or request fail
    """

    if id:
        route = f"https://jsonplaceholder.typicode.com/users?id={id}"
        signal = requests.get(route)
        if signal.status_code == 200:
            data = signal.json()
            return data[0].get('username', '')
    else:
        raise ValueError("Fail, requesting data for given ID")


def format_for_json(data=None):
    """This method takes data from REST API and creates a dictionary with it
        Args:
            data = data to create the dictionary
        Returns:
            A dict with the data
    """
    for info in data:
        userId = data[0].get('userId', '')
        username = get_username(userId)
        core_dict = {str(userId): []}
        while(info.get('userId', None) != userId):
            title = info.get('title', 'Not Found')
            status = info.get('completed', 'Not Found')
            temp = {"username": username, "task": title, "completed": status}
            core_dict[str(userId)].append(temp.copy())
    return core_dict


if __name__ == "__main__":
    if len(sys.argv) > 1:
        emplo_id = sys.argv[1]
    else:
        raise ValueError(f"request failed, no employee ID found")
    url = f"https://jsonplaceholder.typicode.com/todos/"
    connection = requests.get(url)
    if connection.status_code == 200:
        data = connection.json()
        info = format_for_json(data)
        filename = "todo_all_employees.json"
        with open(filename, 'w') as file:
            json.dump(info, file, indent=2)
    else:
        raise requests.exceptions.HTTPError(
            f"request failed, status code: {connection.status_code}")
