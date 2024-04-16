#!/usr/bin/python3
"""This script use a REST API, to retive data from it"""
import requests
import sys


def get_name(id):
    """This method grabs the name of the given employeeId
        Args:
            id = targeted id to fetch data
        Returns:
            The name of the employee
        Exceptions:
            ValueError - if id is not existing or request fail
    """

    if id:
        route = f"https://jsonplaceholder.typicode.com/users?id={id}"
        signal = requests.get(route)
        if signal.status_code == 200:
            data = signal.json()
            return data[0].get('name', '')
    else:
        raise ValueError("Fail, requesting data for given ID")


def To_do_list(data=None):
    """This method takes data from REST API and creates a informative text
        Args:
            data = data to create the text
        Returns:
            A text with the data in a more detail format
    """

    text = ""
    done = 0
    tasks = 0
    tasks_titles = []
    name = ""
    if data:
        name = get_name(data[1].get('userId', ''))
        for info in data:
            tasks += 1
            if info.get('completed', False):
                done += 1
                tasks_titles.append(info.get('title', ''))
        text += f"Employee {name} is done with tasks({done}/{tasks}):\n"
        for index, title in enumerate(tasks_titles):
            text += f"\t{title}"
            if index < len(tasks_titles) - 1:
                text += "\n"
    return text


if __name__ == "__main__":
    if len(sys.argv) > 1:
        emplo_id = sys.argv[1]
    else:
        raise ValueError(f"request failed, no employee ID found")
    url = f"https://jsonplaceholder.typicode.com/todos?userId={emplo_id}"
    connection = requests.get(url)
    if connection.status_code == 200:
        data = connection.json()
        info = To_do_list(data)
        print(info)
    else:
        raise requests.exceptions.HTTPError(
            f"request failed, status code: {connection.status_code}")
