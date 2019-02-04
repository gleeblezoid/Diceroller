########################
# Roller for FATE dice #
########################

import random
from pathlib import Path

rollagain = "Y"
while str.upper(rollagain)=="Y":
    try:
        sides = 6

        if pool < 1:
            print("Silly human")
            import FateRoller

    # Dice roll resolution
        i = 0
        while i < (pool):
            roll = random.randint(1, sides)
            i = i + 1
            if roll == (1 or 2):
                print("[+]", end=",")
            elif roll == (3 or 4):
                print("[-]",end=",")
            else:
                print("[ ]",end=",")
        rollagain=input("Do you want to roll the same again? Enter Y or N: ")
            if str.upper(rollagain)=="Y"
                pool=input("How many dice do you want to roll")
    except (NameError, TypeError, ValueError):

        print("Sorry, try something else!")
        exec(Path('./Diceroller.py').open('r').read())
else:
    exec(Path('./Diceroller.py').open('r').read())
