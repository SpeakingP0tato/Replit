import os, time

ToDoList = []

def printList():
  print()
  for item in ToDoList:
    print(item)
  print()

while True:
    menu = input("1.List\n2.Add\n3.edit\n4.Remove\n5.All remove\n> ")
    if menu == "list" or menu == "1":
      os.system('clear')
      print("Here is your to do list: ")
      printList()
    elif menu == "add" or menu == "2":
      time.sleep(0.3)
      os.system('clear')
      item = input("What do you want to add to your to do list?: ")
      if item in ToDoList:
        print("Item already in list.")
        time.sleep(1)
      else:
        ToDoList.append(item)
        print("Item added.")
      while True:
        extra = input("add more list? (y/n): ")
        if extra == "y":
          item = input("What do you want to add to your to do list?: ")
          if item in ToDoList:
            print("Item already in list.")
            time.sleep(1)
          else:
            ToDoList.append(item)
            print("Item added.")
        elif extra == "n":
          break
    elif menu == "edit" or menu == "3":
      time.sleep(1)
      os.system('clear')
      printList()
      old_value = input("What do you want to edit from your to do list?: ")
      if old_value in ToDoList:
        new_value = input("What do you want to change it to?: ")
        ToDoList[ToDoList.index(old_value)] = new_value
        print("Item updated.")
        time.sleep(1)
        os.system('clear')
      else:
        print("Item not found.")
        time.sleep(1)
        os.system('clear')
    elif menu == "remove" or menu == "4":
      time.sleep(0.3)
      os.system('clear')
      printList()
      item = input("What do you want to remove?\n ")
      if item in ToDoList:
        notice = input("Are you sure you want to remove this? (y/n): ")
        while True:
          if notice == "y":
            ToDoList.remove(item)
            break
          elif notice == "n":
            print("item not removed.")
            break
          else:
            print("Item not found.")
      else:
        print("Item not found.")
        time.sleep(1)
        os.system('clear')
    elif menu == "all remove" or menu == "5":
      time.sleep(0.3)
      os.system('clear')
      notice = input("Are you sure you want to remove all items? (y/n): ")
      if notice == "y":
        ToDoList.clear()
        print("All items removed.")
      elif notice == "n":
        print("Items not removed.")
    else:
      print("Invalid input.")
      time.sleep(1)
      os.system('clear')
