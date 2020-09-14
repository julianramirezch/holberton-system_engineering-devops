#!/usr/bin/python3
''' Python script to export data in the CSV format'''
import csv
import requests
from sys import argv


def make_request(todo, empl, user_id):
    ''' Make request to url '''
    titles = []
    r_todo = requests.get(todo)
    if r_todo.status_code == 200:
        titles = [i.get('title') for task, i in enumerate(r_todo.json())]
        comp = [i.get('completed') for task, i in enumerate(r_todo.json())]

    r_empl = requests.get(empl)
    if r_empl.status_code == 200:
        username = r_empl.json().get('username')

    with open('{}.csv'.format(user_id), 'w') as f:
        w = csv.writer(f, quoting=csv.QUOTE_ALL)
        for title, status in zip(titles, comp):
            row = [
                '{}'.format(user_id),
                '{}'.format(username),
                '{}'.format(status),
                '{}'.format(title)]
            w.writerow(row)


if __name__ == "__main__":
    user_id = argv[1]
    todo_url = 'https://jsonplaceholder.typicode.com/users/{}/todos/'.format(
        user_id)
    empl_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    make_request(todo_url, empl_url, user_id)
