#-----------------------------------------------------------------------------
# Name:        Temperature Advice
# Purpose:     Gives advice for appropriate dressing according to the temperature
#
# Author:     Zahra Imran
# Created:     28-Feb-2025
# Updated:     01-Mar-2025
#-----------------------------------------------------------------------------

print("Hello there!")
temperature = int(input("Please enter the current temperature in celsius:)?:"))
if temperature < 10: # If temperature is below 10
    print("It's a cold day today!")
    print("Please wear a jacket and stay warm!")

elif temperature >= 10 and temperature <= 25: # If temperature is between 10 and 25
    print("It's a nice day today! Wear short-sleeves and spend time outdoors!")

else:  # If temperature is above 25
    print("It's a hot day! Stay cool!")
    print("Make sure to drink plenty of water!")

print("Goodbye! Have a nice day!")