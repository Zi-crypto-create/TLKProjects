#-----------------------------------------------------------------------------
# Name:       Countdown Timer
# Purpose:    To countdown numbers from 10
# Author:      ZI
# Created:     8-Mar-2025
# Updated:     17-Mar-2025
#-----------------------------------------------------------------------------
count = 10  # Start countdown from 10

while count > 0:
    print(count)  # Print the count
    user_input = input('Enter "stop" to cancel or press Enter: ')  # Ask user for input
    if user_input.lower() == "stop":  # Check if user entered 'stop'
        print("Countdown stopped!")
        break  # Exit loop if 'stop' is entered
    count -= 1  # Decrease count by 1