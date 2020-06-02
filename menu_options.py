# Copyright 2018 Ursula Searle
# !/usr/bin/env python3

###############################################
# Menu options for DiceRoller                 #
###############################################

from DiceRoller import show_menu, selection


def option1():
    print("Welcome to the RPG menu: Choose your preferred option by typing the shortcode or number")
    print("q: Return to main menu")
    rollagain = "Y"
    # Set up a while loop for rolling again within an RPG system
    try:
        from RPGDictionary import rpgsystems

        rpgnames = '\n '.join([rpgsystems[i]['name'] for i in rpgsystems])
        print(rpgnames)
        menu_choice = input("Please enter your choice:")
        if menu_choice == "q":
            from roller import main
        elif menu_choice in rpgsystems:
            sides = rpgsystems[menu_choice]['sides']
            explode = rpgsystems[menu_choice]['explodes']
            pool = int(input("How many dice would you like to roll?"))

            if explode == 'Y':
                import ExplodingDice
            elif explode == 'N':
                import PolyhedralRoller
        else:
            print("Sorry I don't have that RPG")

            show_menu()
            menu_choice = input("Please enter your choice: ")
            selection(menu_choice)

    except (NameError, TypeError, ValueError):

        print("Sorry, try something else please!")
        show_menu()
        menu_choice = input("Please enter your choice: ")
        selection(menu_choice)

def option2():

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
    from RPGDictionary import rpgsystems
    try:
        mode = int(input("Enter the number for your choice: "))
    except(ValueError, NameError):
        print("Nope - try something else\n")
        show_menu()
        menu_choice = input("Please enter your choice: ")
        selection(menu_choice)

    # Add an RPG System
    if mode == 1:
        rpgsystem = input("What RPG system are you using? ")
        rpgshortcode = input("What shortcode do you want to use for this RPG system? ")

        while True:
            try:
                sides = int(input("How many sides do your dice have? "))
                if sides <= 1:
                    raise ValueError
                break
            except ValueError:
                print("Nope - try something else \n")
        while True:
            try:
                explode = input("Do your dice explode? Type either Y or N: ")
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
        menu_choice = input("Which RPG system would you like to remove? ")
        if menu_choice in rpgsystems:
            del rpgsystems[menu_choice]
            dictionary = "rpgsystems =" + str(rpgsystems)
            rpglist = open(r'RPGDictionary.py', 'w+')
            rpglist.write(str(dictionary))
            rpglist.close()
        else:
            print("Sorry - please try something else!")
            show_menu()
            menu_choice = input("Please enter your choice: ")
            selection(menu_choice)

# Set up while loops for rerolls

def option3():
        from PolyhedralRoller import polyhedralroller
        polyhedralroller(1,20)

def option4():
    dice = input("What do you want to roll? Enter in the format 1d6 (for one six-sided die) ")
    from PolyhedralRoller import polyhedralroller
    pool = int(dice[:dice.find('d')])
    sides = int(dice[dice.find('d') + 1:])
    polyhedralroller(pool,sides)

def option5():
    from ExplodingDice import explodingdice
    explodingdice()

def option6():

    from FateRoller import fateroller
    fateroller()

def option7():
    import StarWarsDice

def option8():
    from BucketOfDice import bucketofdice
    bucketofdice()


