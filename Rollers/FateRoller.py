# Copyright 2018 Ursula Searle
#!/usr/bin/env python3

########################
# Roller for FATE dice #
########################

import random
from Rollers.DiceRoller import show_menu, selection
def fateroller():
    pool = int(input("How many dice are you rolling? "))
    rollagain = "Y"
    while str.upper(rollagain) == "Y":
        try:
            sides = 6

            if pool < 1:
                print("Silly human")

            # Dice roll resolution
            i = 0
            while i < (pool):
                roll = random.randint(1, sides)
                i = i + 1
                if roll == (1 or 2):
                    print("[+]", end=",")
                elif roll == (3 or 4):
                    print("[-]", end=",")
                else:
                    print("[ ]", end=",")

            rollagain = input("Do you want to roll the same again? Enter Y or N: ")

        except (NameError, TypeError, ValueError):

            print("Sorry, try something else!")
            show_menu()
            menu_choice = input("Please enter your choice: ")
            selection(menu_choice)
    else:
        show_menu()
        menu_choice = input("Please enter your choice: ")
        selection(menu_choice)
