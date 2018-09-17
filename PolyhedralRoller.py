#################################################
# Rolls a set of custom defined polyhedral dice #
#################################################

import random
from pathlib import Path

rollagain = "Y"
while str.upper(rollagain)=="Y":
    try:
# Error handling
        if sides < 1:
            print("Wow, just wow...")
            import PolyhedralRoller

        if pool < 1:
            print("Silly human")
            import PolyhedralRoller

# Dice roll resolution
        i = 0
        while i < (pool):
            roll = random.randint(1, sides)
            i = i + 1
            print(roll, end=",")
        print("\n")
        rollagain=input("Do you want to roll the same again? Enter Y or N:")
    except (NameError, TypeError, ValueError):
        print("Sorry, try something else!")
        exec(Path('./Diceroller.py').open('r').read())

else:
# Go back to main menu
    exec(Path('./Diceroller.py').open('r').read())


