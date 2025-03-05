#-----------------------------------------------------------------------------
# Name:       Voting Eligibility Checker
# Purpose:    To check if a user is eligible to vote based on their age
#
# Author:     Zahra Imran
# Created:     01-Mar-2025
# Updated:     -
#-----------------------------------------------------------------------------

print("Hello there!")
print("Voting time is near")
print("You will know if you are eligible to vote in the next few minutes")
age = int(input("Please enter your age:"))
if age >= 18:
    print("You are eligible to vote!")
    print("Have fun voting!")
else:
    print("Sorry, you are not eligible to vote yet.")
    print("Please come back in", 18 - age, "years.")