# To-Do List App

A simple command-line To-Do List application that helps users manage their tasks. Users can add, delete, and view tasks interactively from the terminal.

## Features

- Add new tasks
- Delete existing tasks by task number
- View current tasks
- Looping menu interface for continuous task management

## How It Works

- The app maintains a list of tasks using a Python list.
- Users interact through a menu that runs in a loop until they choose to quit.
- Task actions are handled by dedicated functions:
  - `addTask()` – Adds a new task to the list.
  - `listTasks()` – Displays all current tasks with their task numbers.
  - `deleteTask()` – Deletes a task based on the number provided by the user.

## Getting Started

1. Ensure you have Python installed (Python 3.x).
2. Save the code in a file named `todo_list.py`.
3. Run the script from the terminal:
