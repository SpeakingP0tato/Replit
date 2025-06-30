import random, os, time

listOfWords = ["british", "suave", "integrity", "accent", "evil", "genius", "Downton"]
letterpicked = []
lives = 5

wordChosen = random.choice(listOfWords)

while True:
  time.sleep(1)
  os.system("clear")  
  letter = input("Choose a letter: ").lower()
  
  if letter in letterpicked:
    print("You already picked that letter.")
    continue

  letterpicked.append(letter)

  if letter in wordChosen:    
    print("Correct!")
  else:
    print("Wrong!")
    lives -= 1

  allltters = True
  print()
  for i in wordChosen:
    if i in letterpicked:
      print(i, end=" ")
    else:
      print("_", end=" ")
      allltters = False
  print()

  if allltters:
    print("You won!")
    break

  if lives <= 0:
    print(f"You lost!\nThe word was {wordChosen}")
    break
  else:
    print(f"You have {lives} left.")
