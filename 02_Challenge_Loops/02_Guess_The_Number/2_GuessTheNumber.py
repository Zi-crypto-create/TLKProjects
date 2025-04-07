#-----------------------------------------------------------------------------
# Name:       Guess The Number
# Purpose:    For the user to guess a random number between 1 and 10
#
# Author:      ZI
# Created:     8-Mar-2025
# Updated:     17-Mar-2025
#-----------------------------------------------------------------------------
import random

def guess_the_number():
  """This game picks a secret number and you have to guess it!"""

  #Pick a secret number between 1 and 10.
  secret_number = random.randint(1, 10)

  #Start guessing!
  guess = 0  # We'll use this to store the player's guesses.

  #Keep asking until they guess right.
  while True != secret_number:
    #Ask the player for their guess.
    try:
      guess = int(input("Guess a number between 1 and 10: "))

      #Check if the guess is too high, too low, or correct.
      if guess < secret_number:
        print("Too low! Try again.")
      elif guess > secret_number:
        print("Too high! Try again.")
      else:
        print("You got it! The secret number was", secret_number)

    # 6. If they didn't enter a number, tell them to try again.
    except ValueError:
      print("That's not a number! Please try again.")

# 7. Start the game!
guess_the_number()