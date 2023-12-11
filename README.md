# TaskManager

<p align="center">
  <img width="300" height="225" src="https://github.com/Pernam75/TaskManager/assets/58521821/6b7ef78b-ccc0-4b28-8974-93fb454de82b">
</p>

## Description

This is a simple task manager app that allows you to create, edit, and delete tasks. You can create users and assign tasks to them. You can also mark tasks as complete, and view all tasks assigned to a user.

## Preview

<p align="center">
  <img src="https://github.com/Pernam75/TaskManager/assets/58521821/6bb4975a-71d3-43c4-9535-ead98e38d769">
</p>

## Installation

1. Clone the repository
2. Run `docker-compose up --build`
3. Navigate to `localhost:3000` in your browser

## Usage

1. Create a user, fill in the username, password, and email fields and click `Add Account`
2. Create a task, fill in the title, done, and user fields and click `Add Task`
3. Edit a task, click the `Modify` button next to the task you want to edit, fill in the fields you want to change and click `Edit Task`
4. Delete a task, click the `Delete` button next to the task you want to delete
5. Mark a task as complete, click the `Done` button next to the task you want to mark as complete
6. View all tasks assigned to a user. Select a user from the dropdown menu will display all tasks assigned to that user.
7. Dark mode, click the `Dark Mode` button on the top left of the screen to toggle dark or light mode

## Github Actions

The release and main branches are protected by Github Actions, the tests will run on every push and pull request to these branches.
You can view the tests in the [tests folder](https://github.com/Pernam75/TaskManager/tree/release/tests).

## Upcoming Features

- [ ] Host the app using a cloud service
- [ ] Add a login page to the app
- [ ] Add tags to tasks
- [ ] Add a search bar to the app
- [ ] Add a calendar to the app through API integration
- [ ] Add a pomodoro timer to the app

## License

MIT License
