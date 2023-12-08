# tests/test_app.py
import pytest
import requests

def test_test_route():
    response = requests.get('http://localhost:4000/test')
    assert response.status_code == 200
    assert response.json()['message'] == 'Hello World!'

def test_create_task():
    # create user to avoid foreign key error
    requests.post('http://localhost:4000/users', json={
        'pseudo': 'task_test',
        'email': 'tasks@example.com',
        'password': 'tasks'
    })
    response = requests.post('http://localhost:4000/tasks', json={
        'title': 'test task',
        'done': 0,
        'user_id': 1
    })
    assert response.status_code == 200
    assert response.json()['message'] == 'task created'

def test_get_tasks():
    response = requests.get('http://localhost:4000/tasks')
    assert response.status_code == 200
    assert isinstance(response.json()['tasks'], list)

def test_get_task():
    response = requests.get('http://localhost:4000/tasks/1')
    assert response.status_code == 200
    assert isinstance(response.json()['task'], dict)

def test_update_task():
    response = requests.put('http://localhost:4000/tasks/1', json={
        'title': 'update task',
        'done': 1,
        'user_id': 1
    })
    assert response.status_code == 200
    assert response.json()['message'] == 'task updated'
    response = requests.get('http://localhost:4000/tasks/1')
    assert response.json()['task']['title'] == 'update task'
    

def test_delete_task():
    response = requests.delete('http://localhost:4000/tasks/1')
    assert response.status_code == 200
    assert response.json()['message'] == 'task deleted'
    response = requests.get('http://localhost:4000/tasks')
    assert len([task for task in response.json()['tasks'] if task['id'] == 1]) == 0