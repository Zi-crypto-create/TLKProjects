#-----------------------------------------------------------------------------
# Name:        Grocery List and Add Items
# Purpose:     To create a list of groceries and then add new items to the list
#
# Author:      ZI
# Created:     20-Mar-2025
# Updated:     -
#-----------------------------------------------------------------------------

grocery = ['apples', 'bread', 'milk', 'eggs']
print(grocery)
grocery_2 = ['cheese', 'tomatoes'] #add items 'cheese' and 'tomatoes' in the list
grocery.extend(grocery_2) #add the two items to the initial list
print(grocery) #print modified grocery list