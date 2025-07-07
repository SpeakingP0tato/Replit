print("Guess the Nintendo Switch 2 price in American dollars!")
print()

NintendoSwitch2 = float(449.99)
counter = 1

while True:

  price = float(input("Enter a price between 1$ and 1,000,000$: "))
  
  
  if price > 1000000 or price < 1:
    print("Please enter a valid price")

  elif price < NintendoSwitch2:
    print("The Price is higher than that")
    counter += 1
    
  elif price > NintendoSwitch2:
    print("The Price is lower than that")
    counter += 1
    continue
    
  elif price == NintendoSwitch2:
    print("You guessed it right!")
    break
    
  else:
    print("input error")  

print("It took you", counter, "guesses to get the price!")
    
