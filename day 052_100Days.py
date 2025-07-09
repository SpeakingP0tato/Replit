import os, time
pizza = []

try:
  f = open("pizza.txt", "r")
  pizza = eval(f.read())
  f.close()
except:
  print("ERROR: No existing pizza list, using a blank list")

def viewpizza():
  h1 = "Name"
  h2 = "Topping"
  h3 = "Size"
  h4 = "Quantity"
  h5 = "Total"
  print(f"{h1:10} {h2:10} {h3:10} {h4:10} {h5:10}")
  for row in pizza:
    print(f"{row[0]:10} {row[1]:10} {row[2]:10} {row[3]:10} {row[4]:10}")
    time.sleep(1.5)

def addpizza():
  time.sleep(1)
  os.system("clear")
  name = input("Name: ")
  topping = input("Topping: ")
  size = input("Size(s/m/l): ")
  while True:
    try:
      qty = int(input("Quantity: "))
      break
    except:
      print("ERROR: Invalid input, please enter a number")
  cost = 0
  if size == "s":
    cost = 5.99
  elif size == "m":
    cost = 9.99
  elif size == "l":
    cost = 14.99
  else:
    print("ERROR: Invalid size, please enter s, m, or l")
  total = cost * qty
  total = round(total, 2)
  row = [name, topping, size, qty, total]
  pizza.append(row)

while True:
  time.sleep(1)
  os.system("clear")
  print("Rominos Pizza")
  print()
  menu = input("1: Add Pizza\n2: View Pizzas\n> ")
  if menu == "1":
    addpizza()
  elif menu == "2":
    viewpizza()
  else:
    print("ERROR: Invalid input, please enter 1 or 2")

  f.open("pizza.txt", "w")
  f.write(str(pizza))
  f.close()
