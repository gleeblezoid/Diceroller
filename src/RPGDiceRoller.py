# Copyright 2018 Ursula Searle
# !/usr/bin/env python3

import sys
import gc
import random

#########################
# Star Wars Dice Roller #
#########################





# Define the dice
class dice:
    def __init__(self, colour, name, sides, results, swpoolcount):
        self.colour = colour
        self.name = name
        self.sides = sides
        self.results = results
        self.swpoolcount = swpoolcount

global dice_name_list
global dice_colour_list
global dice_sides_list
global dice_results_list
global dice_swpoolcount_list
dice_name_list = []
dice_colour_list = []
dice_sides_list = []
dice_results_list = []
dice_swpoolcount_list = []

# Green (Ability) - d8 [s,a,sa,ss,a,s,aa,' ']
ability = dice('green', 'ability', 8, ['s', 'a', 'sa', 'ss', 'a', 's', 'aa', ' '], 0)
# Yellow (Proficiency) - d12 [aa,a,aa,ts,s,sa,s,sa,ss,sa,ss,' ']
proficiency = dice('yellow', 'proficiency', 12,
                   ['aa', 'a', 'aa', 'Ts', 's', 'sa', 's', 'sa', 'ss', 'sa', 'ss', ' '], 1)
# Purple (Difficulty) - d8 [t,f,ft,t,' ',tt,ff,t]
difficulty = dice('purple', 'difficulty', 8, ['t', 'f', 'ft', 't', ' ', 'tt', 'ff', 't'], 2)
# Red (Challenge) - d12 [tt,t,tt,t,ft,f,ft,f,ff,df,ff,' ']
challenge = dice('red', 'challenge', 12, ['tt', 't', 'tt', 't', 'ft', 'f', 'ft', 'f', 'ff', 'Df', 'ff', ' '], 3)
# Blue (Boost) - d6 [sa,aa,,s,a,' ',' ']
boost = dice('blue', 'boost', 6, ['sa', 'aa', 's', 'a', ' ', ' '], 4)
# Black (Setback) - d6 [' ',' ',t,t,f,f]
setback = dice('black', 'setback', 6, [' ', ' ', 't', 't', 'f', 'f'], 5)
# White (Force) - d12 [d,d,d,d,d,d,ll,ll,ll,l,l,dd]
force = dice('white', 'force', 12, ['d', 'd', 'd', 'd', 'd', 'd', 'll', 'll', 'll', 'l', 'l', 'dd'], 6)

dice_name_set = set(dice_name_list)
dice_name_list = list(dice_name_set)
dice_colour_set = set(dice_colour_list)
dice_colour_list = list(dice_colour_set)
dice_sides_set = set(dice_sides_list)
dice_sides_list = list(dice_sides_set)
dice_results_set = set(dice_results_list)
dice_results_list = list(dice_results_set)
dice_swpoolcount_set = set(dice_swpoolcount_list)
dice_swpoolcount_list = list(dice_swpoolcount_set)


def printchoices():
    for obj in gc.get_objects():
        if isinstance(obj, dice):
            print(obj.name + " (" + obj.colour + "): " + str(swpool[obj.swpoolcount]))
            dice_name_list.append(obj.name)
            dice_colour_list.append(obj.colour)
            dice_sides_list.append(obj.sides)
            dice_results_list.append(obj.results)
            dice_swpoolcount_list.append(obj.swpoolcount)


# Create swPool: Ask about which dice are being rolled by colour


def createswpool():
    global swpool
    swpool = []
    pc = 0
    for i in range(0, 7):
        try:
            die = abs(int(input("How many " + str(dice_name_list[pc]) + " (" + str(dice_colour_list[pc]) + ") dice? ")))
            swpool.append(die)
        except (NameError, TypeError, ValueError):
            swpool.append(0)
        pc = pc + 1


# Roll dice

def rolldice():
    global rolled_results
    rolled_results = []
    rpc = 0
    for i in range(0, 7):
        if swpool[rpc] > 0:
            for p in range(0, swpool[rpc]):
                roll = random.randint(0, int(dice_sides_list[rpc]) - 1)
                die_face = dice_results_list[rpc][roll]
                rolled_results.append(die_face)
        else:
            rolled_results.append(" ")
        rpc = rpc + 1

    # Consolidate the success/failure, advantage/disadvantage, triumph/despair

    final_result = str(rolled_results)
    successes = final_result.count('s')
    failures = final_result.count('f')
    advantages = final_result.count('a')
    threats = final_result.count('t')
    triumphs = final_result.count('T')
    despairs = final_result.count('D')
    light = final_result.count('l')
    dark = final_result.count('d')

    success_vs_failure = int(successes - failures)
    advantages_vs_threats = int(advantages - threats)

    print("\n")

    if success_vs_failure >= 0:
        print("Success " + str(success_vs_failure))
    else:
        print("Failure " + str(abs(success_vs_failure)))

    if advantages_vs_threats >= 0:
        print("Advantage " + str(advantages_vs_threats))
    else:
        print("Threat " + str(abs(advantages_vs_threats)))

    print("Triumphs " + str(triumphs))
    print("Despair " + str(despairs))
    print("Lightside " + str(light))
    print("Darkside " + str(dark))
    print('\n')


# Offer reroll same, new swpool, or quit to menu
def swdicemenu():
    print("Choose an option from the menu:")
    print("1: Reroll the same dice pool")
    print("2: Roll a new pool of dice")
    print("q: Quit to main menu")
    swubmenu_choice = input("Please enter your choice: ")

    if swubmenu_choice == '1':
        print("\n")
        printchoices()
        print("\n")
        rolldice()
        print("\n")
        swdicemenu()
        print("\n")
    elif swubmenu_choice == '2':
        createswpool()
        print("\n")
        printchoices()
        print("\n")
        rolldice()
        swdicemenu()
        print("\n")
    elif swubmenu_choice == 'q':
        main_menu()
    else:
        print("Sorry - please try something else.")
        print("\n")
        swdicemenu()

def starwarsdice():
    try:
        global swpool
        swpool = [0, 0, 0, 0, 0, 0, 0]
        print("What dice do you want to roll?")
        printchoices()
        print('\n')
        print("Enter how many of each die you want:")
        createswpool()
        print('\n')
        printchoices()
        print('\n')
        rolldice()
        swdicemenu()
    except(NameError, TypeError, ValueError):
        print("Sorry, try something else")
        swdicemenu()



####################################################
# Roller for multiple polyhedral types in one pool #
####################################################

def bucketofdice():
    # Define multiple dice pools (make a list)
    bucket = []
    moredice = "Y"

    try:
        while str.upper(moredice) == "Y":
            dice = input("What do you want to roll? Enter in the format 1d6 (for one six-sided die) ")
            bucket.append(dice)
            moredice = input("Do you want to add more dice to the bucket? Type Y or N: ")

        else:
            explode = input("Do you want your dice to explode? Type Y or N: ")
            if str.upper(explode) == "N":
                for dice in bucket:
                    print("\n" + dice)
                    pool = int(dice[:dice.find('d')])
                    sides = int(dice[dice.find('d') + 1:])
                    i = 0
                    while i < (pool):
                        roll = random.randint(1, sides)
                        i = i + 1
                        print(roll, end=",")

            elif str.upper(explode) == "Y":
                for dice in bucket:
                    print("\n" + dice)
                    pool = int(dice[:dice.find('d')])
                    sides = int(dice[dice.find('d') + 1:])
                    if sides <= 1:
                        raise ValueError
                    else:
                        i = 0
                        while i < (pool):
                            roll = random.randint(1, sides)
                            if roll < sides:
                                i = i + 1
                            elif roll == sides:
                                random.randint(1, sides)
                                i = i
                            print(roll, end=",")

    except (NameError, TypeError, ValueError):
        print("Sorry, try something else!")
        main_menu()

    print("\n")

    rollagain = input("Do you want to roll another bucket of dice? Enter Y or N: ")
    if str.upper(rollagain) == "Y":
        pass
    else:
        main_menu()


###################################
# Rolls repeatedly exploding dice #
###################################

def explodingdice(pool, sides):
    rollagain = "Y"
    while str.upper(rollagain) == "Y":
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
            rollagain = input("Do you want to roll the same again? Enter Y or N: ")

        except (NameError, TypeError, ValueError):

            print("Sorry, try something else!")
            main_menu()
    else:
        # Go back to main menu

        main_menu()


########################
# Roller for FATE dice #
########################

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

            main_menu()
    else:
        main_menu()


#################################################
# Rolls a set of custom defined polyhedral dice #
#################################################


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
            main_menu()

    else:
        # Go back to main menu
        main_menu()



###############################################
# Main Dice Roller File - including main menu #
###############################################

def show_menu():
    print("\nChoose your preferred option from the menu below by typing the shortcode or number for the option\n")

    print("1: Use a saved RPG System")
    print("2: Add/Remove a saved RPG System")
    print("3: Roll single D20")
    print("4: Standard polyhedral dice")
    print("5: Exploding polyhedral dice")
    print("6: Roll FATE dice")
    print("7: Roll Star Wars Narrative Dice")
    print("8: Roll a big bucket of dice!")
    print("q: Quit")


def option1():
    print("Welcome to the RPG menu: Choose your preferred option by typing the shortcode or number")
    print("q: Return to main menu")
    rollagain = "Y"
    # Set up a while loop for rolling again within an RPG system
    try:
        from RPGDictionary import rpgsystems

        rpgnames = '\n '.join([rpgsystems[i]['name'] for i in rpgsystems])
        print(rpgnames)
        submenu_choice = input("Please enter your choice:")
        if submenu_choice == "q":
            main_menu()
        elif submenu_choice in rpgsystems:
            sides = rpgsystems[submenu_choice]['sides']
            explode = rpgsystems[submenu_choice]['explodes']
            pool = int(input("How many dice would you like to roll?"))

            if explode == 'Y':
                explodingdice(pool, sides)
            elif explode == 'N':
                polyhedralroller(pool, sides)
        else:
            print("Sorry I don't have that RPG")

            main_menu()

    except (NameError, TypeError, ValueError):

        print("Sorry, try something else please!")
        main_menu()


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
        main_menu()

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
        rpglist = open(r'../RPGDictionary.py', 'w+')
        rpglist.write(str(dictionary))
        rpglist.close()

        print("Thanks - back to the Main Menu")
        main_menu()
        # Remove an RPG system
    elif mode == 2:

        rpgnames = '\n '.join([rpgsystems[i]['name'] for i in rpgsystems])
        print(rpgnames)
        rpgmenu_choice = input("Which RPG system would you like to remove? ")
        if rpgmenu_choice in rpgsystems:
            del rpgsystems[rpgmenu_choice]
            dictionary = "rpgsystems =" + str(rpgsystems)
            rpglist = open(r'../RPGDictionary.py', 'w+')
            rpglist.write(str(dictionary))
            rpglist.close()
        else:
            print("Sorry - please try something else!")
            main_menu()


# Set up while loops for rerolls

def option3():
    polyhedralroller(1, 20)


def option4():
    dice = input("What do you want to roll? Enter in the format 1d6 (for one six-sided die) ")
    pool = int(dice[:dice.find('d')])
    sides = int(dice[dice.find('d') + 1:])
    polyhedralroller(pool, sides)


def option5():
    dice = input("What do you want to roll? Enter in the format 1d6 (for one six-sided die) ")
    pool = int(dice[:dice.find('d')])
    sides = int(dice[dice.find('d') + 1:])
    explodingdice(pool, sides)


def option6():
    fateroller()


def option7():
    starwarsdice()


def option8():
    bucketofdice()


def selection(menu_choice):
    if menu_choice == "q":
        sys.exit("Roll on")

    elif menu_choice == '1':
        option1()

    elif menu_choice == '2':
        option2()

    elif menu_choice == '3':
        option3()

    elif menu_choice == '4':
        option4()

    elif menu_choice == '5':
        option5()

    elif menu_choice == '6':
        option6()

    elif menu_choice == '7':
        option7()

    elif menu_choice == '8':
        option8()
    else:
        print("Sorry - please try something else")
        main_menu()

def main_menu():
    show_menu()
    menu_choice = input("Please enter your choice: ")
    selection(menu_choice)


main_menu()