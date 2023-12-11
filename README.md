# TaskManager

<p align="center">
  <img width="300" height="225" src="https://github.com/Pernam75/TaskManager/assets/58521821/6b7ef78b-ccc0-4b28-8974-93fb454de82b">
</p>

## Description

This is a simple task manager app that allows you to create, edit, and delete tasks. You can create users and assign tasks to them. You can also mark tasks as complete, and view all tasks assigned to a user.

## Installation

1. Clone the repository
2. Run `docker-compose up --build`
3. Navigate to `localhost:3000` in your browser

## Usage

1. Create a user, fill in the username, password, and email fields and click `Create User`
2. Create a task, fill in the title, done, and user fields and click `Create Task`
3. Edit a task, click the `Edit` button next to the task you want to edit, fill in the fields you want to change and click `Update Task`
4. Delete a task, click the `Delete` button next to the task you want to delete
5. Mark a task as complete, click the `Done` button next to the task you want to mark as complete
6. View all tasks assigned to a user, click the `View Tasks` button next to the user you want to view tasks for

## Github Actions

The release and main branches are protected by Github Actions, the tests will run on every push and pull request to these branches.
You can view the tests in the [tests folder](https://github.com/Pernam75/TaskManager/tree/release/tests).

## License

MIT License
