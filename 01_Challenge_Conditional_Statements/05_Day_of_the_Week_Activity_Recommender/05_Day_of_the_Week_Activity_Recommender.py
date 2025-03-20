#-----------------------------------------------------------------------------
# Name:       Day of the Week Activity Recommender
# Purpose:    To suggest an activity to the user based on the day of the week.
#
# Author:     Zahra Imran
# Created:     01-Mar-2025
# Updated:     -
#-----------------------------------------------------------------------------

print("Hello there!")
print("Welcome to the Day of the Week Activity Recommender!")
print("Please enter the day of the week you would like to recommend an activity for:")
day = input("Enter the day of the week (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday):").strip().capitalize()
if day == "Monday":
    print("Start your week with a workout!")
    print("You can also try a yoga session!")
    print("Have fun!")
elif day == "Tuesday":
    print("It's a great day to read a book!")
    print("Have a nice day!")
elif day == "Wednesday":
    print("Mid-week movie night!")
    print("Grab some popcorn and enjoy the night!")
elif day == "Thursday":
    print("Try a new recipe")
    print("Have fun!")
elif day == "Friday":
    print("Relax and enjoy the weekend")
    print("Enjoy your free time while you can!")
elif day == "Saturday":
    print("Go for a hike")
elif day == "Sunday":
    print("Prepare for the week ahead with some self-care")
else:
    print("Invalid input. Please enter a valid day of the week.")