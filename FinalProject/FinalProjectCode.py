#-----------------------------------------------------------------------------
# Name:        To Do List
# Purpose:     To-Do List App where users can add, complete, and delete tasks. A simple way to stay organized.
# Author:      ZI
# Created:     13-May-2025
# Updated:     16-June-2025
#-----------------------------------------------------------------------------

# Create an empty list to store tasks
tasks = []

# Using function to add a task (using a parameter)
def addTask(task_list):
    task = input("Please enter a task: ") # Get user input
    task_list.append(task) # add the task to the list
    print(f"\n'{task}' has been added to the list.") # message of confirmation

#Using function to list all tasks, starting the count from 1
def listTasks(task_list):
    if not task_list: # if the list is empty
        print("\nThere are no tasks currently.")
    else:
        print("Current Tasks:")
        for index, task in enumerate(task_list, start=1): # numbering of tasks starts at 1
            print(f"Task #{index}: {task}") # show each task with a number

# Using function to delete a task
def deleteTask(task_list):
    listTasks(task_list) # show current tasks
    try:
        # User enters the task number (shown to them), so subtract 1 for index
        taskToDelete = int(input("Please enter the task # to delete: ")) - 1
        if taskToDelete >= 0 and taskToDelete < len(task_list): # Valid Index
            removed = task_list.pop(taskToDelete) # Remove the task
            print(f"\n'{removed}' has been removed.")
        else:
            print(f"\nThat task number was not found.") # If number is too high/low
    except:
        print("Invalid input.") # if user types something that is not a valid number

# Start of the app
print("Welcome to the To-Do List App!")

# Using a while loop to keep the program running
while True:
    # show menu
    print("\nPlease select one of the following options:")
    print("-----------------------------------")
    print("1. Add a new task")
    print("2. Delete a task")
    print("3. List tasks")
    print("4. Quit")

    choice = input("Please enter your choice: ")

    # Based on user input, call the right function
    if choice == "1":
        addTask(tasks)
    elif choice == "2":
        deleteTask(tasks)
    elif choice == "3":
        listTasks(tasks)
    elif choice == "4":
        print("Exiting... Goodbye!")
        break # Exit the loop and end the program
    else:
        print("Invalid input. Please try again.")