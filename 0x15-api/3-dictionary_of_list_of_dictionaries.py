#!/usr/bin/python3
''' Python script to export all employees data in the JSON format.'''
import json
import requests
from sys import argv


def make_request(ids):
    ''' Make request to url '''
    titles = []
    data_json = {}
    for user_id in ids:
        data = {user_id: []}
        todo = 'https://jsonplaceholder.typicode.com/users/{}/todos/'.\
            format(user_id)
        empl = 'https://jsonplaceholder.typicode.com/users/{}'.\
            format(user_id)
        r_todo = requests.get(todo)
        if r_todo.status_code == 200:
            titles = [i.get('title') for task, i in enumerate(r_todo.json())]
            comp = [i.get('completed') for task, i in enumerate(r_todo.json())]

        r_empl = requests.get(empl)
        if r_empl.status_code == 200:
            username = r_empl.json().get('username')

        data_json[user_id] = []
        for title, status in zip(titles, comp):
            row = {
                "username": username,
                "task": title,
                "completed": status, }
            data_json[user_id].append(row)

    with open('todo_all_employees.json'.format(user_id), 'w') as f:
        json.dump(data_json, f)


def get_ids(url):
    ''' Get ids from REST API '''
    response = requests.get(url)
    ids = [i.get('userId') for i in response.json()]

    return list(set(ids))


if __name__ == "__main__":
    ids = get_ids('http://jsonplaceholder.typicode.com/todos')
    make_request(ids)
