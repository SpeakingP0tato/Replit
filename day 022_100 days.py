import random

print("Welcome to the Number Guessing Game!")
print("")
print("Let's start the game")
print("Please guess a number between 1 and 1000000")

myNumber = random.randint(1, 1000000)

count = 1

while True:

    answer = int(input("What is your guess?: "))
  
    if myNumber == answer:
      print("Correct!")
    elif  answer < 1 or answer > 1000000:
      print("Out of bounds\nplease enter a number between 1 and 1000000")
    elif myNumber < answer:
      print("Too high")
      count += 1
    elif myNumber > answer:
      print("Too low")
      count += 1
    else:
      print("Invalid input\nplease enter a number between 1 and 1000000")

    if myNumber == answer:
      print("It took you", count, "guesses to get the number corret.")
      break
