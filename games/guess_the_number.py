# Game: Guess the number
# Ask the user for a random number from 0, 10
# Check if they can guess the number on within range

from random import randint

#Refactor
def run_guess(guess, answer):
  if guess > 0 and guess < 11:
    if (guess == answer):
      print("You're brilliant")
      return True
  else:
    print ('I saide 1~10')
    return False


while True:
  try:
    answer = randint(1, 10)
    guess = int(input('guess a number: '))
    if run_guess(guess, answer):
        break
  except ValueError:
    print("please enter a number")
    continue
