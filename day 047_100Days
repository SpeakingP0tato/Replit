import os, time, random

trumps = {}
trumps["David"] = {"Intelligence": 180, "Strength": 5, "Speed": 10, "Health": 5}
trumps["Goliath"] = {"Intelligence": 30, "Strength": 15, "Speed": 5, "Health": 15}
trumps["Saul"] = {"Intelligence": 15, "Strength": 10, "Speed": 10, "Health": 10}
trumps["Professor"] = {"Intelligence": 99, "Strength": 5, "Speed": 5, "Health": 10}

while True:
  print("Trump Game")
  print()
  print("characters")
  print()
  for key in trumps:
    print(key)
  user = random.choice(list(trumps.keys()))
  print("your character", user )
  comp = random.choice(list(trumps.keys()))
  print("Computer chooses: ", comp)

  print("Choose your stat: Intelligence, Strength, Speed, Health")

  anwer = input("> ").capitalize()

  print(f"{user}: {trumps[user][anwer]}")
  print(f"{comp}: {trumps[comp][anwer]}")

  if trumps[user] == trumps["David"] or trumps[comp] == trumps["David"]:
    print("David Win! Some power used game(BECAUSE HE IS BALD)")
  elif trumps[user][anwer] > trumps[comp][anwer]:
    print(user, "wins!")
  elif trumps[user][anwer] < trumps[comp][anwer]:
    print(comp, "wins!")
  else:
    print("Draw")
