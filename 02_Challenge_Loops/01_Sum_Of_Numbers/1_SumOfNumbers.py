#-----------------------------------------------------------------------------
# Name:        Sum of Numbers
# Purpose:     To calculate the sum of all numbers from 1 to n
#
# Author:      Zahra Imran
# Created:     8-Mar-2025
# Updated:     17-Mar-2025
#-----------------------------------------------------------------------------
print("start")
n = int(input("Enter a number: "))
total = sum(range(1, n + 1))
print("Sum =", total)