#!/usr/bin/python3
"""This script use a REST API, to retive data into a cvs file"""
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


def CVS_format(data=None):
    """This method takes data from REST API and creates a informative text
        Args:
            data = data to create the text
        Returns:
            A text with the data in a more detail format
        Exceptions:
            ValueError - data arg is None/Null
    """

    txt = ''
    if data:
        userId = data[1].get('userId', '')
        name = get_name(userId)
        for info in data:
            current = info.get('completed', 'Not Found')
            title = info.get('title', 'Not Found')
            txt += '"{}","{}","{}","{}"'.format(userId, name, current, title)
            txt += '\n'
        return txt
    else:
        raise ValueError("Fail To Create Text, Data Missing")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        emplo_id = sys.argv[1]
    else:
        raise ValueError(f"request failed, no employee ID found")
    url = f"https://jsonplaceholder.typicode.com/todos?userId={emplo_id}"
    connection = requests.get(url)
    if connection.status_code == 200:
        data = connection.json()
        info = CVS_format(data)
        filename = f"{emplo_id}.csv"
        with open(filename, 'w') as file:
            file.write(info)
    else:
        raise requests.exceptions.HTTPError(
            f"request failed, status code: {connection.status_code}")
