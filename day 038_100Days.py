def colorchange(color):
  if color == "r":
    print("\033[31m")
  elif color == "g":
    print("\033[32m")
  elif color == "y":
    print("\033[33m")
  elif color == "b":
    print("\033[34m")
  elif color == "p":
    print("\033[35m")
  elif color == "w":
    print("\033[0m")


sentence = input("What sentence do you want rainbow-izing: ")
for letter in sentence:
  colorchange(letter.lower())
  print(letter, end="")
  print()
