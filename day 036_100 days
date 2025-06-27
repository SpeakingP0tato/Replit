name = []

def namelist():
  print()
  for Full_name in name:
    print(Full_name)
  print()

while True:
  first_name = input("What is your fist name?").capitalize().strip()
  last_name = input("What is your last name?").capitalize().strip()
  full_name = f"{first_name} {last_name}"
  if full_name not in name:
    name.append(full_name)
    namelist()
  elif full_name in name:
    print("That name is already in the list")
