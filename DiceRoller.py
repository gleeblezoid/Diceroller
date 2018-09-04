############################
# Future plans/patch notes #
############################

# Currently only allows a single type of polyhedral in a given pool
# Do not yet have a means of defining non-numeric dice
# No logging function yet
# Allow removal of RPG systems as well as addition

#################################
# Menu for choosing dice roller #
#################################

print("\nChoose your preferred option from the menu below by typing the shortcode or number for the option\n")
print("1: Standard polyhedral dice")
print("2: Exploding polyhedral dice")
print("3: RPG System Menu")
print("4: RPG Config Writer")
print("5: Roll single D20")
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


# The "option 3" section opens up into the customised RPG Menu section of the program
elif menu_choice == '3':
    exec(open("./rpgmenu.py").read())

# Option 4 allows you to add more RPG systems

elif menu_choice == '4':
    exec(open("./ConfigWriter.py").read())

elif menu_choice == '5':
    pool = 1
    sides = 20
    exec(open("./PolyhedralRoller.py").read())