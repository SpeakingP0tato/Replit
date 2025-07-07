import os, time

print("Score table")

s = open("Score table.txt", "a+")

while True:
  init = input("Input your inituals > ").upper()
  score = input("Input your score > ")
  
  s.write(f"{init} {score}\n")
  
  print("Added to score table")

  add = input("Add another y/n? ").strip().lower()
  if add == "y":
    time.sleep(1)
    os.system("clear")
    continue
  else:
    break

s.close()
