#-----------------------------------------------------------------------------
# Name:       Skipping Even Numbers
# Purpose:    For the program to print odd numbers from 1 to 10
#
# Author:      ZI
# Created:     8-Mar-2025
# Updated:     17-Mar-2025
#-----------------------------------------------------------------------------

for num in range(1, 11):
    if num % 2 == 0:  # Check if the number is even
        continue  # Skip the even number and move on
    print(num)  # Print only odd numbers