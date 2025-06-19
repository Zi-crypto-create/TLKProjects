#-----------------------------------------------------------------------------
# Name:        To Do List
# Purpose:     To-Do List App where users can add, complete, and delete tasks. A simple way to stay organized.
# Author:      ZI
# Created:     13-May-2025
# Updated:     16-June-2025
#-----------------------------------------------------------------------------

# Create a list to store tasks
tasks = []

def addTask(task_list):
    task = input("Please enter a task: ")
    task_list.append(task)
    print(f"\n'{task}' has been added to the list.")

def listTasks(task_list):
    if not task_list:
        print("\nThere are no tasks currently.")
    else:
        print("Current Tasks:")
        for index, task in enumerate(task_list, start=1):
            print(f"Task #{index}: {task}")

def deleteTask(task_list):
    listTasks(task_list)
    try:
        taskToDelete = int(input("Please enter the task # to delete: ")) - 1
        if taskToDelete >= 0 and taskToDelete < len(task_list):
            removed = task_list.pop(taskToDelete)
            print(f"\n'{removed}' has been removed.")
        else:
            print(f"\nThat task number was not found.")
    except:
        print("Invalid input.")

# Loop
print("Welcome to the To-Do List App!")

while True:
    print("\nPlease select one of the following options:")
    print("-----------------------------------")
    print("1. Add a new task")
    print("2. Delete a task")
    print("3. List tasks")
    print("4. Quit")

    choice = input("Please enter your choice: ")
    if choice == "1":
        addTask(tasks)
    elif choice == "2":
        deleteTask(tasks)
    elif choice == "3":
        listTasks(tasks)
    elif choice == "4":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid input. Please try again.")