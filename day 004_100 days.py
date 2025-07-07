print(
    "Welcome to your adventure simulator. I am going to ask you a bunch of questions and then create an epic story with you as the star!"
)

print()
Name = input("What is your name? ")
Enemy = input("What is your worst enemy's name? ")
Power = input("What is your spuerpower? ")
Live = input("Where do you live? ")
Food = input("What is your favorite food? ")

print()
print("Hello　\033[33m" + Name + "\033[0m,your abillity to", Power,
      "will make sure you never have to look at", Enemy, "again. Go eat", Food,
      "as you walk down the streets of", Live, "and use", Power,
      "for good and not evil!")
