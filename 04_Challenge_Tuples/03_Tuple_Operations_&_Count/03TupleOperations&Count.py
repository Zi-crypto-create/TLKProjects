#-----------------------------------------------------------------------------
# Name:        Swapping Values Using Tuples
# Purpose:     To swap values using tuples
# Author:      ZI
# Created:     31-Mar-2025
# Updated:     05-April-2025
#-----------------------------------------------------------------------------

print("Start")
fruits = ("apple", "banana", "apple", "cherry", "banana", "apple") #tuple containing fruits
print(fruits) #Print tuple
value = input("Please enter a fruit name from the list: ") #Prompt user to enter fruit name from the list, store in a variable
count = fruits.count(value) #Count amount of the fruit in the list
print(f"'{value}' appears {count} times in the tuple.") #Print the result