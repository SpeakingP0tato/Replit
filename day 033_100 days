import os, time

ToDoList = []

def printList():
  print()
  for item in ToDoList:
    print(item)
  print()

while True:
    todo = input("Do you want to view, add, or remove your to do list? ")
    if todo == "add":
      time.sleep(0.3)
      os.system('clear')
      item = input("What do you want to add to your to do list?: ")
      ToDoList.append(item)
    elif todo == "remove":
      time.sleep(0.3)
      os.system('clear')
      item = input("What do you want to remove from your to do list?: ")
      ToDoList.remove(item)
    elif todo == "view":
      time.sleep(0.3)
      os.system('clear')
      print("Here is your to do list: ")
      printList()
