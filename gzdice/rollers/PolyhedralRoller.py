#################################################
# Rolls a set of custom defined polyhedral dice #
#################################################

import random
from ..menus import base_menus as m


def polyhedralroller(pool, sides):
    rollagain = "Y"
    while str.upper(rollagain) == "Y":
        try:
            # Error handling
            if sides < 1:
                print("Wow, just wow...")

            if pool < 1:
                print("Silly human")

            # Dice roll resolution
            i = 0
            while i < (pool):
                roll = random.randint(1, sides)
                i = i + 1
                print(roll, end=",")
            print("\n")
            rollagain = input("Do you want to roll the same again? Enter Y or N: ")
        except (NameError, TypeError, ValueError):
            print("Sorry, try something else!")
            m.main_menu()

    else:
        # Go back to main menu
        m.main_menu()
