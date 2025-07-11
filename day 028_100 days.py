import random
import time
import os 

print("Welcome to the game!")

while True:
    start = input("Press 's' to start or 'x' to exit: ")
    if start == "s":
        print("Game started")
        print("loading...")

    os.system("clear")
    time.sleep(1)
    
    def roll_dice(sides):
        result = random.randint(1,sides)
        return result

    def human_health():
        healthstat = int((roll_dice(6) * roll_dice(12)) / 2) + 5
        return healthstat

    def human_Strength():
        Strengthstat = int((roll_dice(6) * roll_dice(12)) / 2) + 15
        return Strengthstat

    def human_Magic():
        Magicstat = max(0, int((roll_dice(6) * roll_dice(12)) / 2) - 3)
        return Magicstat

    def elf_health():
        healthstat = int((roll_dice(6) * roll_dice(12)) / 2) + 5
        return healthstat

    def elf_Strength():
        Strengthstat = int((roll_dice(6) * roll_dice(12)) / 2) + 15
        return Strengthstat

    def elf_Magic():
        Magicstat = int((roll_dice(6) * roll_dice(12)) / 2) + 10
        return Magicstat

    def wizard_health():
        healthstat = max(8,int((roll_dice(6) * roll_dice(12)) / 2) - 3)
        return healthstat

    def wizard_Strength():
        Strengthstat = int((roll_dice(6) * roll_dice(12)) / 2) + 5
        return Strengthstat

    def wizard_Magic():
        Magicstat = int((roll_dice(6) * roll_dice(12)) / 2) + 15
        return Magicstat

    def orc_health():
        healthstat = int((roll_dice(6) * roll_dice(12)) / 2) + 15
        return healthstat

    def orc_Strength():
        Strengthstat = int((roll_dice(6) * roll_dice(12)) / 2) + 20
        return Strengthstat

    def orc_Magic():
        Magicstat = max(0, int((roll_dice(6) * roll_dice(12)) / 2) - 8)
        return Magicstat

    while True:
        print("Character Builder")
        P1 = input("Name Your Legend: ")
        if P1 == "":
            print("Please enter a valid name")
            break
        else:
            while True:
                type = input("Character Type (Human, Elf, Wizard, Orc): ")
                print("")
                if type == "human" or type == "Human":
                    print(P1)
                    print(type)
                    P1_Health = human_health()
                    P1_Strength = human_Strength()
                    P1_Magic = human_Magic()
                    print("Health: ", P1_Health)
                    print("Strength: ", P1_Strength)
                    print("Magic: ", P1_Magic)
                    print("May your name go down in legend...")
                    break
                elif type == "elf" or type == "Elf":
                    print(P1)
                    print(type)
                    P1_Health = elf_health()
                    P1_Strength = elf_Strength()
                    P1_Magic = elf_Magic()
                    print("Health: ", P1_Health)
                    print("Strength: ", P1_Strength)
                    print("Magic: ", P1_Magic)
                    print("May your name go down in legend...")
                    break
                elif type == "wizard" or type == "Wizard":
                    print(P1)
                    print(type)
                    P1_Health = wizard_health()
                    P1_Strength = wizard_Strength()
                    P1_Magic = wizard_Magic()
                    print("Health: ", P1_Health)
                    print("Strength: ", P1_Strength)
                    print("Magic: ", P1_Magic)
                    print("May your name go down in legend...")
                    break
                elif type == "orc" or type == "Orc":
                    print(P1)
                    print(type)
                    P1_Health = orc_health()
                    P1_Strength = orc_Strength()
                    P1_Magic = orc_Magic()
                    print("Health: ", P1_Health)
                    print("Strength: ", P1_Strength)
                    print("Magic: ", P1_Magic)
                    print("May your name go down in legend...")
                    break
                else:
                    print("Please choose a valid Character Type")
                
            time.sleep(1)
        break
    break


os.system("clear")
time.sleep(0.5)

while True:
        print("Character Builder")
        P2 = input("Name Your Legend: ")
        if P2 == "":
            print("Please enter a valid name")
            break
        else:
            while True:
                type = input("Character Type (Human, Elf, Wizard, Orc): ")
                print("")
                if type == "human" or type == "Human":
                    print(P2)
                    print(type)
                    P2_Health = human_health()
                    P2_Strength = human_Strength()
                    P2_Magic = human_Magic()
                    print("Health: ", P2_Health)
                    print("Strength: ", P2_Strength)
                    print("Magic: ", P2_Magic)
                    print("May your name go down in legend...")
                    break
                elif type == "elf" or type == "Elf":
                    print(P2)
                    print(type)
                    P2_Health = elf_health()
                    P2_Strength = elf_Strength()
                    P2_Magic = elf_Magic()
                    print("Health: ", P2_Health)
                    print("Strength: ", P2_Strength)
                    print("Magic: ", P2_Magic)
                    print("May your name go down in legend...")
                    break
                elif type == "wizard" or type == "Wizard":
                    print(P2)
                    print(type)
                    P2_Health = wizard_health()
                    P2_Strength = wizard_Strength()
                    P2_Magic = wizard_Magic()
                    print("Health: ", P2_Health)
                    print("Strength: ", P2_Strength)
                    print("Magic: ", P2_Magic)
                    print("May your name go down in legend...")
                    break
                elif type == "orc" or type == "Orc":
                    print(P2)
                    print(type)
                    P2_Health = orc_health()
                    P2_Strength = orc_Strength()
                    P2_Magic = orc_Magic()
                    print("Health: ", P2_Health)
                    print("Strength: ", P2_Strength)
                    print("Magic: ", P2_Magic)
                    print("May your name go down in legend...")
                    break
                else:
                    print("Please choose a valid Character Type")
            time.sleep(1)
        break

os.system("clear")
time.sleep(0.5)

def p1attack():
    attack = int(P1_Strength * (P1_Health/2) * 0.08)
    return attack

def p1magic():
    magic = int(P1_Magic * (P1_Health/2) * 0.08)
    return magic

def p2attack():
    attack = int(P2_Strength * (P2_Health/2) * 0.08)
    return attack

def p2magic():
    magic = int(P2_Magic * (P2_Health/2) * 0.08)
    return magic
    
print("⚔️ BATTLE TIME ⚔️")
print()
print("The battle begins!")

while True:
    if P1_Health >= 0 and P2_Health >= 0:
        p1_dice = roll_dice(6)
        p2_dice = roll_dice(6)
        
        if p1_dice > p2_dice:
            print(P1, "rolls", p1_dice, "and", P2, "rolls", p2_dice)
            time.sleep(0.5)
            print(P1, "wins the first attack!")
            print()
            time.sleep(0.5)
            p1_se = input("Select your action a, d, m(attack, magic): ") 
            if p1_se == "a":
                p1dmg = p1attack()
                P2_Health -= p1dmg
                print (P2, "take a hit, whit", p1dmg, "damage")
            elif p1_se == "m":
                p1mdmg = p1magic()
                P2_Health -= p1mdmg
                print (P2, "take a hit, whit", p1mdmg, "damage")
            else:
               print("Please choose a valid action")
                
        elif p2_dice > p1_dice:
            print(P1, "rolls", p1_dice, "and", P2, "rolls", p2_dice)
            time.sleep(0.5)
            print(P2, "wins the first attack!")
            print()
            time.sleep(0.5)
            p2_se = input("Select your action a, d, m(attack, magic): ")
            
            if p2_se == "a":
                p2dmg = p2attack()
                P1_Health -= p2dmg
                print (P1, "take a hit, whit", p2dmg, "damage")
            elif p2_se == "m":
                p2mdmg = p2magic()
                P1_Health -= p2mdmg
                print (P1, "take a hit, whit", p2mdmg, "damage")
            else:
               print("Please choose a valid action")
                
        else:
            print("Both players have the same dice roll, it's a tie!")

            print({P1}, "'s Health:", {max(0, P1_Health)} , {P2},"'s Health:", {max(0, P2_Health)})
            time.sleep(0.5)
            
    elif P1_Health <= 0:
        print(P2, "wins!")
        break
    elif P2_Health <= 0:
        print(P1, "wins!")
        break
    else:
        continue
