import random

print("Infinity Dice Roller")

sides = int(input("How many sides?: "))
play = "y"

def Dice(sides):
  if sides > 0:
    print("You rolled ", random.randint(1, sides))
  elif sides == 0:
    print("Please enter a number greater than 0")
  else:
    print("Invalid input")

while True:
  if play =="y" or play == "Y":
    Dice (sides)
    play = input("Roll again? (y/n): ")
  else:
    if play == "n" or play == "N":
      regame = input("Would you like to roll a different dice? (y/n): ")
      if regame == "y" or regame == "Y":
        sides = int(input("How many sides?: "))
        play = "y"
      else:
        break    
  
print("Thanks for playing")
  
