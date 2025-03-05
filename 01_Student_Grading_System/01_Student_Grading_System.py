#-----------------------------------------------------------------------------
# Name:        Student Grading System
# Purpose:    To let student's know if they passed or failed their exam depending on their score.
#
# Author:     Zahra Imran
# Created:     24-Feb-2025
# Updated:     27-Feb-2025
#-----------------------------------------------------------------------------
print("Hello")
myScore = int(input("What is your score (out of a 100)?:"))
if myScore >= 90:
    print("Grade A.")
    print("Congrats! You have passed your exam.")
elif myScore == 80-89:
    print("Grade B.")
    print("Congrats! You have passed your exam.")
elif myScore == 70-79:
    print("Grade C.")
    print("Congrats! You have passed your exam.")
elif myScore == 60-69:
    print("Grade D")
    print("Hmm, you could have get better marks...")
    print("However, you have passed the exam! Make sure to work harder next time.")
else:
    print("Grade F.")
    print("Sorry, you have failed the exam. Better luck next time!")