from ..menus import base_menus as m
from ..rollers import PolyhedralRoller as pr
from ..rollers import ExplodingDice as ed


def saved_system():
    print(
        "Welcome to the RPG menu: Choose your preferred option by typing the shortcode or number"
    )
    print("q: Return to main menu")
    rollagain = "Y"
    # Set up a while loop for rolling again within an RPG system
    try:
        from ..data.RPGDictionary import rpgsystems

        rpgnames = "\n ".join([rpgsystems[i]["name"] for i in rpgsystems])
        print(rpgnames)
        submenu_choice = input("Please enter your choice:")
        if submenu_choice == "q":
            m.main_menu()
        elif submenu_choice in rpgsystems:
            sides = rpgsystems[submenu_choice]["sides"]
            explode = rpgsystems[submenu_choice]["explodes"]
            pool = int(input("How many dice would you like to roll?"))

            if explode == "Y":
                ed.explodingdice(pool, sides)
            elif explode == "N":
                pr.polyhedralroller(pool, sides)
        else:
            print("Sorry I don't have that RPG")

            m.main_menu()

    except (NameError, TypeError, ValueError):

        print("Sorry, try something else please!")
        m.main_menu()
