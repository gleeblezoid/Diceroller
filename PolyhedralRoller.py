#################################################
# Rolls a set of custom defined polyhedral dice #
#################################################

import random
import subprocess
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

# Go back to main menu

    exec(open("./DiceRoller.py").read())

except (NameError, TypeError, ValueError):

    print("Sorry, try something else!")
    exec(open("./DiceRoller.py").read())
