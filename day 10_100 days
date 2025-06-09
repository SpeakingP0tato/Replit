myBill = float(input("What was the bill?: "))
People = int(input("How many people?: "))
tips = input("Do you want to leave a tip? ")

if tips == "yes":
  tippercent = float(input("What percentage tip would you like to give?: "))
else:
  tippercent = 0
  print("No tip is given")

totaltip = myBill * (tippercent / 100)

bill_with_tip = myBill + totaltip

answer = bill_with_tip / People

print("Your total bill with tip is: ", bill_with_tip)
print("and we payed tip: ", totaltip)
print("You all owe: ", answer)
