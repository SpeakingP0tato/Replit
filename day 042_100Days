print("👾 MokéBeast - The Non-Copyright Generic Beast Battle Game 👾")

mokeBeast = {"name" : None, "type" : None, "HP" : None, "MP" : None}

for name, value in mokeBeast.items():
  mokeBeast[name] = input(f"{name} : \t").strip().title()  
  
if mokeBeast["type"] == "Earth":
  print("\033[32m", end="")
elif mokeBeast["type"] == "Water":
  print("\033[34m", end="")
elif mokeBeast["type"] == "Fire":
  print("\033[31m", end="")
elif mokeBeast["type"] == "Air":
  print("\033[37m", end="")
else: 
  print("\033[33m", end="")

for name, value in mokeBeast.items():
  print(f"{name:<15} : \t {value}")
