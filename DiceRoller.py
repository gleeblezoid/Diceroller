###############################################
# Main Dice Roller File - including main menu #
###############################################

from pathlib import Path

print("\nChoose your preferred option from the menu below by typing the shortcode or number for the option\n")

print("1: Use a saved RPG System")
print("2: Add/Remove a saved RPG System")
print("3: Roll single D20")
print("4: Standard polyhedral dice")
print("5: Exploding polyhedral dice")
print("6: Roll FATE dice")
print("7: Roll a big bucket of dice!")
print("q: Quit")
menu_choice = input("Please enter your choice:")

if menu_choice == "q":
    exit(0)

elif menu_choice == '1':
    print("Welcome to the RPG menu: Choose your preferred option by typing the shortcode or number")
    print("q: Return to main menu")
    rollagain = "Y"
    # Set up a while loop for rolling again within an RPG system
    try:
        exec(Path('./RPGDictionary.py').open('r').read())
        rpgnames = '\n '.join([rpgsystems[i]['name'] for i in rpgsystems])
        print(rpgnames)
        menu_choice = input("Please enter your choice:")
        if menu_choice == "q":
            exec(Path('./Diceroller.py').open('r').read())
        elif menu_choice in rpgsystems:
            sides = rpgsystems[menu_choice]['sides']
            explode = rpgsystems[menu_choice]['explodes']
            pool = int(input("How many dice would you like to roll?"))

            if explode == 'Y':
                exec(Path('./ExplodingDice.py').open('r').read())
            elif explode == 'N':
                exec(Path('./PolyhedralRoller.py').open('r').read())
        else:
            print("Sorry I don't have that RPG")

            exec(Path('./Diceroller.py').open('r').read())

    except (NameError, TypeError, ValueError):

        print("Sorry, try something else please!")
        exec(Path('./Diceroller.py').open('r').read())

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
    # Import dictionary for rpgsystems
    exec(Path('./RPGDictionary.py').open('r').read())
    try:
        mode = int(input("Enter the number for your choice:"))
    except(ValueError, NameError):
        print("Nope - try something else\n")
        exec(Path('./Diceroller.py').open('r').read())

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
                if str.upper(explode) == "Y":
                    break
                elif str.upper(explode) == "N":
                    break
                else:
                    raise ValueError
                    break
            except ValueError:
                print("Nope - try something else - like a Y or N \n")

        # This creates a dictionary entry containing the parameters for your chosen RPG System

        rpgsystems[rpgshortcode] = {}
        rpgsystems[rpgshortcode]['name'] = rpgshortcode + ":" + rpgsystem
        rpgsystems[rpgshortcode]['sides'] = sides
        rpgsystems[rpgshortcode]['explodes'] = str.upper(explode)
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

    exec(Path('./Diceroller.py').open('r').read())

# Set up while loops for rerolls

elif menu_choice == '3':
    rollagain = "Y"
    while rollagain == "Y":
        pool = 1
        sides = 20
        exec(Path('./PolyhedralRoller.py').open('r').read())

elif menu_choice == '4':
    dice = input("What do you want to roll? Enter in the format 1d6 (for one six-sided die)")
    pool = int(dice[:dice.find('d')])
    sides = int(dice[dice.find('d') + 1:])
    exec(Path('./PolyhedralRoller.py').open('r').read())

elif menu_choice == '5':
    dice = input("What do you want to roll? Enter in the format 1d6 (for one six-sided die)")
    pool = int(dice[:dice.find('d')])
    sides = int(dice[dice.find('d') + 1:])
    exec(Path('./ExplodingDice.py').open('r').read())

elif menu_choice == '6':
    pool = int(input("How many dice are you rolling?"))
    exec(Path('./FateRoller.py').open('r').read())

elif menu_choice == '7':
    exec(Path('./BucketOfDice.py').open('r').read())
