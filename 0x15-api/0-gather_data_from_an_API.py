#!/usr/bin/python3

""" Python script that, using this REST API, for a given employee ID
"""

import requests
import sys



def fetch_todo_list_progress(employee_id):
    # Fetch employee info
    employee_info_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    if employee_info_response.status_code != 200:
        print(f"Error fetching employee information: {employee_info_response.status_code}")
        return
    
    employee_info = employee_info_response.json()
    employee_name = employee_info['name']

    # Fetch todo list for the employee
    todos_response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")
    if todos_response.status_code != 200:
        print(f"Error fetching TODO list: {todos_response.status_code}")
        return

    todos = todos_response.json()

    # Calculate progress
    total_tasks = len(todos)
    completed_tasks = sum(1 for todo in todos if todo['completed'])

    # Display progress
    print(f"Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):")
    for todo in todos:
        if todo['completed']:
            print(f"\t{todo['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)
    
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)
    
    fetch_todo_list_progress(employee_id)
