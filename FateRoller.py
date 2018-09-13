########################
# Roller for FATE dice #
########################

import random
from pathlib import Path

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

    exec(Path('./Diceroller.py').open('r').read())

except (NameError, TypeError, ValueError):

    print("Sorry, try something else!")
    exec(Path('./Diceroller.py').open('r').read())