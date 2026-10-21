import random
roll = True

def roll_dice():
    spin1 = random.randint(1, 6)
    spin2 = random.randint(1, 6)
    return spin1, spin2

while roll:
    pick = input ("roll the dice? (y/n): ").lower()
    if pick == "y":
        print(roll_dice())
    elif pick == "n":
        print("Thanks for playing!")
        break
    else:
        print("Invalid choice!")

    

