# Roller for FATE dice

import random


def fate_roller():
    result = ""
    pool = int(input("How many dice are you rolling? "))
    try:
        sides = 6
        if pool < 1:
            print("Silly human")
            pass
        # Dice roll resolution
        i = 0
        while i < (pool):
            roll = random.randint(1, sides)
            i = i + 1
            if roll == (1 or 2):
                result += "[+],"
            elif roll == (3 or 4):
                result += "[-],"
            else:
                result += "[ ],"
    except (NameError, TypeError, ValueError):
        pass
    return result


def roll_again():
    rollagain = input("Roll again? Enter Y or N: ")
    if rollagain == "Y":
        fate_roller()
    else:
        pass


def fate_dice_roller():
    fate_roller()
    roll_again()
