from getpass import getpass as input

print("Select rock, paper, or scissors.")

p1count = 0
p2count = 0

while True:
  player1 = input("Player 1 > ")
  player2 = input("Player 2 > ")

  if (player1 == "r"):
    if (player2 == "r"):
      print("Player 1's rock beats Player 2's rock. draw!")
    elif (player2 == "p"):
      print("Player 2's paper beats Player 1's rock. Player 2 wins!")
      p2count += 1
    elif (player2 == "s"):
      print("Player 1's rock beats Player 2's scissors. Player 1 wins!")
      p1count += 1
    else:
      print("Invalid input. Try again.")

  if (player1 == "p"):
    if (player2 == "p"):
      print("Player 1's paper beats Player 2's paper. draw!")
    elif (player2 == "r"):
      print("Player 1's paper beats Player 2's rock. Player 1 wins!")
      p1count += 1
    elif (player2 == "s"):
      print("Player 2's scissors beats Player 1's paper. Player 2 wins!")
      p2count += 1
    else:
      print("Invalid input. Try again.")

  if (player1 == "s"):
    if (player2 == "s"):
      print("Player 1's scissors beats Player 2's scissors. draw!")
    elif (player2 == "p"):
      print("Player 1's scissors beats Player 2's paper. Player 1 wins!")
      p1count += 1
    elif (player2 == "r"):
      print("Player 2's rock beats Player 1's scissors. Player 2 wins!")
      p2count += 1
    else:
      print("Invalid input. Try again.")

  print("Player 1 has", p1count, "wins!")
  print("Player 2 has", p2count, "wins!")

  if p1count == 5 or p2count == 5:
    print("Game over!")
    exit()
  else:
    continue
