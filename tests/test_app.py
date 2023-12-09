import pytest
import requests
from os import environ

FLASK_URL = 'http://localhost:4000'
# FLASK_URL='http://172.27.0.3:4000'
# FLASK_URL='http://taskmanager:4000'
# FLASK_URL='http://flask_app:4000'

def test_test_route():
    response = requests.get(f'{FLASK_URL}/test')
    assert response.status_code == 200
    assert response.json()['message'] == 'Hello World!'

def test_create_task():
    # create user to avoid foreign key error
    requests.post(f'{FLASK_URL}/users', json={
        'pseudo': 'task_test',
        'email': 'tasks@example.com',
        'password': 'tasks'
    })
    response = requests.post(f'{FLASK_URL}/tasks', json={
        'title': 'test task',
        'done': 0,
        'user_id': 1
    })
    assert response.status_code == 200
    assert response.json()['message'] == 'task created'

def test_get_tasks():
    response = requests.get(f'{FLASK_URL}/tasks')
    assert response.status_code == 200
    assert isinstance(response.json()['tasks'], list)

def test_get_task():
    response = requests.get(f'{FLASK_URL}/tasks/1')
    assert response.status_code == 200
    assert isinstance(response.json()['task'], dict)

def test_update_task():
    response = requests.put(f'{FLASK_URL}/tasks/1', json={
        'title': 'update task',
        'done': 1,
        'user_id': 1
    })
    assert response.status_code == 200
    assert response.json()['message'] == 'task updated'
    response = requests.get(f'{FLASK_URL}/tasks/1')
    assert response.json()['task']['title'] == 'update task'
    

def test_delete_task():
    response = requests.delete(f'{FLASK_URL}/tasks/1')
    assert response.status_code == 200
    assert response.json()['message'] == 'task deleted'
    response = requests.get(f'{FLASK_URL}/tasks')
    assert len([task for task in response.json()['tasks'] if task['id'] == 1]) == 0

def test_get_user_tasks():
    response = requests.get(f'{FLASK_URL}/users/1/tasks')
    assert response.status_code == 200
    assert isinstance(response.json()['tasks'], list)

def test_create_user():
    response = requests.post(f'{FLASK_URL}/users', json={
        'pseudo': 'create',
        'email': 'create@example.com',
        'password': 'create'
    })
    assert response.status_code == 200
    assert response.json()['message'] == 'user created'
    all_users = requests.get(f'{FLASK_URL}/users').json()['users']
    # check if the user exists in the database
    assert any(user['email'] == 'create@example.com' for user in all_users)

def test_create_user_already_exists():
    requests.post(f'{FLASK_URL}/users', json={
        'pseudo': 'first',
        'email': 'first@example.com',
        'password': 'first'
    })
    response = requests.post(f'{FLASK_URL}/users', json={
        'pseudo': 'second',
        'email': 'first@example.com',
        'password': 'second'
    })
    assert response.status_code == 500
    assert response.json()['error'] == 'user already exists'
    all_users = requests.get(f'{FLASK_URL}/users').json()['users']
    assert len([user for user in all_users if user['email'] == 'first@example.com']) == 1

def test_create_user_invalid_email():
    response = requests.post(f'{FLASK_URL}/users', json={
        'pseudo': 'invalid',
        'email': 'invalid_email',
        'password': 'invalid'
    })
    assert response.status_code == 500
    assert response.json()['error'] == 'email is not valid'
    all_users = requests.get(f'{FLASK_URL}/users').json()['users']
    assert len([user for user in all_users if user['email'] == 'invalid_email']) == 0


def test_get_users():
    response = requests.get(f'{FLASK_URL}/users')
    assert response.status_code == 200
    assert isinstance(response.json()['users'], list)

def test_get_user():
    response = requests.get(f'{FLASK_URL}/users/1')
    assert response.status_code == 200
    assert isinstance(response.json()['user'], dict)

def test_update_user():
    response = requests.put(f'{FLASK_URL}/users/1', json={
        'pseudo': 'updated',
        'email': 'updated@example.com',
        'password': 'updated'
    })
    assert response.status_code == 200
    assert response.json()['message'] == 'user updated'
    user = requests.get(f'{FLASK_URL}/users/1').json()['user']
    assert user['pseudo'] == 'updated'

def test_delete_user():
    response = requests.delete(f'{FLASK_URL}/users/1')
    assert response.status_code == 200
    assert response.json()['message'] == 'user deleted'
    all_users = requests.get(f'{FLASK_URL}/users').json()['users']
    assert len([user for user in all_users if user['id'] == 1]) == 0
