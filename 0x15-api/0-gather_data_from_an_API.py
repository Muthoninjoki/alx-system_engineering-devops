#!/usr/bin/python3

import requests
import sys


def get_employee_todo_list(employee_id):
    """
    Retrieves the TODO list for the given employee ID from the API.
    Returns the employee name, number of done tasks and total number of tasks.
    """
    base_url = 'https://jsonplaceholder.typicode.com/'
    employee_url = base_url + 'users/{}'.format(employee_id)
    todo_url = base_url + 'todos?userId={}'.format(employee_id)

    employee_response = requests.get(employee_url)
    todo_response = requests.get(todo_url)

    if employee_response.status_code != 200:
        print('Error: Employee data not found.')
        sys.exit(1)

    if todo_response.status_code != 200:
        print('Error: TODO list not found for the employee.')
        sys.exit(1)


    employee_data = employee_response.json()
    todo_data = todo_response.json()


    employee_name = employee_data['name']
    total_tasks = len(todo_data)
    completed_tasks = sum(1 for task in todo_data if task['completed'])


    return employee_name, completed_tasks, total_tasks, todo_data


def display_todo_progress(employee_name, completed_tasks, total_tasks, todo_data):
    """
    Displays the TODO list progress
    """
    print('Employee {} is done with tasks({}/{}):'.format(employee_name, completed_tasks, total_tasks))

    for task in todo_data:
        if task['completed']:
            print('\t', task['title'])


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python3 gather_data_from_api.py <employee_id>')
        sys.exit(1)

    employee_id = int(sys.argv[1])
    employee_name, completed_tasks, total_tasks, todo_data = get_employee_todo_list(employee_id)
    display_todo_progress(employee_name, completed_tasks, total_tasks, todo_data)
