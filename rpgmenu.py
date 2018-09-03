print("Welcome to the RPG menu: Choose your preferred option by typing the shortcode or number")
print("q: Return to main menu")

try:
    exec(open("./rpgnames.py").read())
    menu_choice = input("Please enter your choice:")
    if menu_choice == "q":
        exec(open("./Diceroller.py").read())
    else:
        with open('rpgcodes.py', 'r') as codes:
            shortcodes = [line.strip() for line in codes]

    if menu_choice in shortcodes[:]:
        rpgfile = "./rpgsys" + menu_choice + ".py"
        exec(open(rpgfile).read())
        if explode == "Y":
            exec(open("./ExplodingDice.py").read())
        elif explode == "N":
            exec(open("./PolyhedralRoller.py").read())
    else:
        print("Sorry I don't have that RPG")

    exec(open("./Diceroller.py").read())

except (NameError, TypeError, ValueError):

    print("Sorry, try something else!")
    exec(open("./DiceRoller.py").read())
