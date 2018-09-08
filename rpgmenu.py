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
