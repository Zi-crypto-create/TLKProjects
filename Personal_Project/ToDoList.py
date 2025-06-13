#-----------------------------------------------------------------------------
# Name:        To Do List
# Purpose:     To-Do List App where users can add, complete, and delete tasks. A simple way to stay organized.
# Author:      ZI
# Created:     13-May-2025
# Updated:     12-June-2025
#-----------------------------------------------------------------------------

# Create a list to store tasks
tasks = []

def addTask():
    task = input("Please enter a task: ")
    tasks.append(task)
    print(f"\n'{task}' has been added to the list.")

def listTasks():
    if not tasks:
        print("\nThere are no tasks currently.")
    else:
        print("Current Tasks:")
        for index, task in enumerate(tasks):
            print(f"Task #{index}: {task}")

def deleteTask():
    listTasks()
    try:
        taskToDelete = int(input("Please enter the task # to delete: "))
        if taskToDelete >= 0 and taskToDelete < len(tasks):
            removed = tasks.pop(taskToDelete)
            print(f"\n'{removed}' has been removed.")
        else:
            print(f"\nTask #{taskToDelete} was not found.")
    except:
        print("Invalid input.")

# ✅ Only ONE loop
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
        addTask()
    elif choice == "2":
        deleteTask()
    elif choice == "3":
        listTasks()
    elif choice == "4":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid input. Please try again.")