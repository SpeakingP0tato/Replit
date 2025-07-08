import os, time, random

f = open("my.idea", "a+")

def add():
  add = input("Add :").strip().capitalize()
  f.write(f"{add}\n")
  print("Added to list")
  time.sleep(1)
  os.system("clear")

def view():
  f.seek(0)
  print(f.read())
  time.sleep(3)
  os.system("clear")

def delete():
  Del = input("Please enter the idea you want to delete : ").capitalize()
  with open("my.idea", "r") as f:
    lines = f.readlines()
  time.sleep(1)
  os.system("clear")

  found = False
  with open("my.idea", "w") as f:
    for line in lines:
      if line.strip() != Del:
        f.write(line)
      else:
        found = True
        
  if found:
    print(f"{Del} has been deleted.")
  else:
    print("Item not found.")

def Loadrandom():
  with open("my.idea", "r") as f:
    ideas = [line. strip() for line in f if line.strip()]
  if ideas:
    print(random.choice(ideas))
  else:
    print("No ideas available.")
  time.sleep(1)
  os.system("clear")

while True:

  menu = input("1. Add Idea\n2. View Ideas\n3. Delete Idea\n4. Load random\n5. Exit\n").lower()
  time.sleep(1)
  os.system("clear")
  
  if menu == "1" or menu == "add":
    add()
  elif menu == "2" or menu == "view":
    view()
  elif menu == "3" or menu == "delete":
    delete()
  elif menu == "4" or menu == "load":
    Loadrandom()
  elif menu == "5" or menu == "exit":
    break
  else:
    print("Invalid input")

f.close()
