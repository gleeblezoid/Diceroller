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

print("\nChoose your preferred option from the menu below by typing the shortcode or number for the option\n")
print("1: Standard polyhedral dice")
print("2: Exploding polyhedral dice")
print("3: RPG System Menu")
print("4: RPG Config Writer")
print("q: Quit")
menu_choice = input("Please enter your choice:")

if menu_choice == "q":
    exit(0)
elif menu_choice == '1':
    exec(open("./oneoffinput.py").read())
    exec(open("./PolyhedralRoller.py").read())
elif menu_choice == '2':
    exec(open("./oneoffinput.py").read())
    exec(open("./ExplodingDice.py").read())

# Option 3 section starts here
# The "option 3" section opens up into the customised RPG Menu section of the program
elif menu_choice == '3':
    import rpgmenu

# Option 3 ends here

elif menu_choice == '4':
    import ConfigWriter
