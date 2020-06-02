# Copyright 2018 Ursula Searle
#!/usr/bin/env python3

###################################
# Rolls repeatedly exploding dice #
###################################

import random
from Rollers.DiceRoller import show_menu, selection

def explodingdice(pool,sides):


    rollagain = "Y"
    while str.upper(rollagain)=="Y":
        try:
        # Error handling

            if sides <= 1:
                print("Nice try")

        if pool < 1:
                print("Silly human")

        # Dice roll resolution
            i = 0
            while i < (pool):
                roll = random.randint(1, sides)
                if roll < sides:
                    i = i + 1
                elif roll == sides:
                    random.randint(1, sides)
                    i = i
                print(roll, end=",")
            print("\n")
            rollagain=input("Do you want to roll the same again? Enter Y or N: ")

        except (NameError, TypeError, ValueError):

            print("Sorry, try something else!")
            show_menu()
            menu_choice = input("Please enter your choice: ")
            selection(menu_choice)
    else:
            # Go back to main menu

            show_menu()
            menu_choice = input("Please enter your choice: ")
            selection(menu_choice)