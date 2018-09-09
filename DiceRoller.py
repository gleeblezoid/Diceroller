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

print("1: Use a saved RPG System")
print("2: Add a saved RPG System")
print("3: Roll single D20")
print("4: Standard polyhedral dice")
print("5: Exploding polyhedral dice")
print("q: Quit")
menu_choice = input("Please enter your choice:")

if menu_choice == "q":
    exit(0)

elif menu_choice == '1':
    print("Welcome to the RPG menu: Choose your preferred option by typing the shortcode or number")
    print("q: Return to main menu")
    try:
        exec(open("./RPGDictionary.py").read())
        rpgnames = '\n '.join([rpgsystems[i]['name'] for i in rpgsystems])
        print(rpgnames)
        menu_choice = input("Please enter your choice:")
        if menu_choice == "q":
            exec(open("./Diceroller.py").read())
        elif menu_choice in rpgsystems:
            sides = rpgsystems[menu_choice]['sides']
            explode = rpgsystems[menu_choice]['explodes']
            pool = int(input("How many dice would you like to roll?"))

            if explode == 'Y':
                exec(open('./ExplodingDice.py').read())
            elif explode == 'N':
                exec(open('./PolyhedralRoller.py').read())
        else:
            print("Sorry I don't have that RPG")

        exec(open("./Diceroller.py").read())

    except (NameError, TypeError, ValueError):

        print("Sorry, try something else please!")
        exec(open("./DiceRoller.py").read())

elif menu_choice == '2':

    #######################################################################
    # Provides framework to create and set up a config file               #
    # Config files provide custom defined variables for the dice rollers  #
    #######################################################################
    # What are your variables?

    print("Welcome to the dice roller customizer. "
          "This works best for systems which use pools of dice."
          "\n Please choose whether you want to add or remove an RPG system"
          "\n1: Add RPG System"
          "\n2: Remove RPG System")
    try:
        mode = int(input("Enter the number for your choice:"))
    except(ValueError, NameError):
        print("Nope - try something else\n")
        exec(open("./DiceRoller.py").read())

    # Import dictionary for rpgsystems
    exec(open("./RPGDictionary.py").read())

    # Add an RPG System
    if mode == 1:
        rpgsystem = input("What RPG system are you using?")
        rpgshortcode = input("What shortcode do you want to use for this RPG system?")

        while True:
            try:
                sides = int(input("How many sides do your dice have?"))
                if sides <= 1:
                    raise ValueError
                break
            except ValueError:
                print("Nope - try something else \n")
        while True:
            try:
                explode = input("Do your dice explode? Type either Y or N:")
                if explode == "Y":
                    break
                elif explode == "N":
                    break
                else:
                    raise ValueError
                    break
            except ValueError:
                print("Nope - try something else - like an uppercase Y or N \n")

        # This creates a dictionary entry containing the parameters for your chosen RPG System

        rpgsystems[rpgshortcode] = {}
        rpgsystems[rpgshortcode]['name'] = rpgshortcode + ":" + rpgsystem
        rpgsystems[rpgshortcode]['sides'] = sides
        rpgsystems[rpgshortcode]['explodes'] = explode
        dictionary = "rpgsystems =" + str(rpgsystems)
        rpglist = open(r'RPGDictionary.py', 'w+')
        rpglist.write(str(dictionary))
        rpglist.close()

        print("Thanks - back to the Main Menu")

        # Remove an RPG system
    elif mode == 2:

        rpgnames = '\n '.join([rpgsystems[i]['name'] for i in rpgsystems])
        print(rpgnames)
        menu_choice = input("Which RPG system would you like to remove?")
        if menu_choice in rpgsystems:
            del rpgsystems[menu_choice]
            dictionary = "rpgsystems =" + str(rpgsystems)
            rpglist = open(r'RPGDictionary.py', 'w+')
            rpglist.write(str(dictionary))
            rpglist.close()
        else:
            print("Sorry - please try something else!")

    # Need a way to save configs for specific roleplay systems

    exec(open("./DiceRoller.py").read())

elif menu_choice == '3':
    pool = 1
    sides = 20
    exec(open("./PolyhedralRoller.py").read())

elif menu_choice == '4':
    pool = int(input("How many dice are you rolling?"))
    sides = int(input("How many sides are on each die?"))
    exec(open("./PolyhedralRoller.py").read())

elif menu_choice == '5':
    pool = int(input("How many dice are you rolling?"))
    sides = int(input("How many sides are on each die?"))
    exec(open("./ExplodingDice.py").read())
