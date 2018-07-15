############################
# Future plans/patch notes #
############################

# Currently only allows a single type of polyhedral in a given pool
# Does not yet allow you to save your settings (for specific systems)
# Do not yet have a means of defining non-numeric dice
# No initial config options to be saved for using in a campaign
# No logging function yet

#################################
# Menu for choosing dice roller #
#################################

import os
from pathlib import Path

cwd = Path("").resolve().parent

print("\nChoose your preferred option from the menu below by typing a number\n")
print("1: Standard polyhedral dice")
print("2: Exploding polyhedral dice")
print("q: Quit")
menu_choice = input("What roller would you like to use?")

if menu_choice == "q":
    exit(0)
elif menu_choice == '1':
    exec(open("/Users/usearle/PycharmProjects/bish-bash-bosh/DiceRoller/PolyhedralRoller.py").read())
elif menu_choice == '2':
#    exec(open("Exploding Dice.py").read())
     exec(open(os.path.join(Path.cwd(),"Exploding Dice.py")))

