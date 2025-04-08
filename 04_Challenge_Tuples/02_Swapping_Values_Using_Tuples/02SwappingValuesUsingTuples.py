#-----------------------------------------------------------------------------
# Name:        Swapping Values Using Tuples
# Purpose:     To swap values using tuples
# Author:      ZI
# Created:     26-Mar-2025
# Updated:     -
#-----------------------------------------------------------------------------

print("Hello there!")
NumberOne = int(input("Please input a number: ")) #Prompt user to input a number
NumberTwo = int(input("Please input another number: ")) #Prompt user to enter another number
Numbers = (NumberOne, NumberTwo)  #Put the numbers in a tuple
print(Numbers) #print the numbers
NumberOne, NumberTwo = NumberTwo, NumberOne  #Swap the values of the tuple
print(NumberOne, NumberTwo) #Print the swapped numbers
print("End")