import random

print("Character Stats Generator")

def rollDice(sides):
  result = random.randint(1, sides)
  return result

def health():
  hp1 = rollDice(6) 
  hp2 = rollDice(8)
  char = hp1 * hp2
  return char

havecharacter = "y"

havecharacter = input("Do you have a character? (y/n): ")

while True:
  if havecharacter == "y":
    character = input("Name your warrior: ")
    print("Their health is: " + str(health()))
    another = input("Do you have another character? (y/n): ")
    if another == "y":
      continue
    elif another == "n":
      New = input("Do you want to create a new character? (y/n): ")
      if New == "y" or New == "Y":
        havecharacter = "y"
      elif New == "n" or New == "N":
        print("Thank you for playing!")
        break
    
    else:
      print("Invalid input. Please enter 'y' or 'n'.")
      
  elif havecharacter == "n":
    New = input("Do you want to create a new character? (y/n): ")
    if New == "y" or New == "Y":
      havecharacter = "y"
    elif New == "n" or New == "N":
      print("Thank you for playing!")
      break
  else:
    print("Invalid input. Please enter 'y' or 'n'.")
