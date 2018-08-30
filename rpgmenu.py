print("Welcome to the RPG menu: Choose your preferred option by typing the shortcode or number")
print("q: Return to main menu")
from ConfigWriter import rpgcodes
exec(open("./rpgnames.py").read())
menu_choice = input("Please enter your choice:")
    if menu_choice == "q":
        import DiceRoller
    else:
            if menu_choice in rpgcodes[:]:
                open("./rpg"+menu_choice+".py").read()
            break
                print("Sorry I don't have that RPG")



