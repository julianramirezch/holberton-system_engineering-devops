#!/usr/bin/python3
''' Python script that, using a REST API, for a given employee ID, returns
information about his/her todo list progress '''
import requests
import sys


def make_request(todo, empl, user_id):
    ''' Make request to url '''
    titles = []
    completed = 0
    tasks = 0
    response_todo = requests.get(todo)
    if response_todo.status_code == 200:
        for task, i in enumerate(response_todo.json()):
            if i.get('userId') == user_id:
                tasks += 1
                if i.get('completed') is True:
                    completed += 1
                    titles.append(i.get('title'))

    response_empl = requests.get(empl)
    if response_empl.status_code == 200:
        name = response_empl.json().get('name')

    print('Employee {} is done with tasks({}/{}):'.format(name, completed,
          tasks))
    [print('\t {}'.format(title)) for title in titles]


if __name__ == "__main__":
    user_id = sys.argv[1]
    todo_url = 'https://jsonplaceholder.typicode.com/todos'
    empl_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    make_request(todo_url, empl_url, int(user_id))
