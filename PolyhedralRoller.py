#################################################
# Rolls a set of custom defined polyhedral dice #
#################################################

import random

# Error handling
if sides < 1:
    print("Wow, just wow...")
    import PolyhedralRoller

if pool < 1:
    print("Silly human")
    import PolyhedralRoller

# Dice roll resolution
print(type)
i = 0
while i < (pool):
    roll = random.randint(1, sides)
    i = i + 1
    print(roll, end=",")
print("\n")

# Go back to main menu

import DiceRoller