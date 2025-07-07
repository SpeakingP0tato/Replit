mokebeast = {}

def prettyprint():
  print(f"name\ttype\tspecial move\tHP\tMP")
  for key, value in mokebeast.items():
    print(f"""{key:^10}|{value["type"]:^8}|{value["special move"]:^8}|{value["HP"]:^8}|{value["MP"]:^8}""")

print("MokeBeast Generator")

while True:
  name = input("Input the beast name > ").capitalize().title()
  type = input("Input the beast element > ").title()
  area = input("Input the beast special move > ")
  hp = input("Input the beast starting HP > ")
  mp = input("Input the beast starting MP > ")

  mokebeast[name] = {"type" : type, "special move" : area, "HP" : hp, "MP" : mp}
  
  retry = input("Would you like to add another beast? (y/n) > ")
  if retry == "n":
    prettyprint()
  else:
    continue

  
