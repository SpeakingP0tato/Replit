exit = "no"

while exit == "no":
  animal = input("What animal do you want to?")

  if animal == "cat":
    print("meow"a)
  elif animal == "dog":
    print("woof")
  elif animal == "cow":
    print("moo")
  elif animal == "duck":
    print("quack")
  elif animal == "pig":
    print("oink")
  else:
    print("How does the " +animal+ " say?")
    
    
  exit = input("Press anykeys to exit: ")
