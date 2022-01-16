from ..menus import base_menus as m


def new_system():
    #######################################################################
    # Provides framework to create and set up a config file               #
    # Config files provide custom defined variables for the dice rollers  #
    #######################################################################
    # What are your variables?

    print(
        "Welcome to the dice roller customizer. "
        "This works best for systems which use pools of dice."
        "\n Please choose whether you want to add or remove an RPG system"
        "\n1: Add RPG System"
        "\n2: Remove RPG System"
    )
    # Import dictionary for rpgsystems
    from ..data.RPGDictionary import rpgsystems

    try:
        mode = int(input("Enter the number for your choice: "))
    except (ValueError, NameError):
        print("Nope - try something else\n")
        m.main_menu()

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
        rpgsystems[rpgshortcode]["name"] = rpgshortcode + ":" + rpgsystem
        rpgsystems[rpgshortcode]["sides"] = sides
        rpgsystems[rpgshortcode]["explodes"] = str.upper(explode)
        dictionary = "rpgsystems =" + str(rpgsystems)
        rpglist = open(r"../RPGDictionary.py", "w+")
        rpglist.write(str(dictionary))
        rpglist.close()

        print("Thanks - back to the Main Menu")
        m.main_menu()
        # Remove an RPG system
    elif mode == 2:

        rpgnames = "\n ".join([rpgsystems[i]["name"] for i in rpgsystems])
        print(rpgnames)
        rpgmenu_choice = input("Which RPG system would you like to remove? ")
        if rpgmenu_choice in rpgsystems:
            del rpgsystems[rpgmenu_choice]
            dictionary = "rpgsystems =" + str(rpgsystems)
            rpglist = open(r"RPGDictionary.py", "w+")
            rpglist.write(str(dictionary))
            rpglist.close()
            print("Thanks - back to the Main Menu")
            m.main_menu()
        else:
            print("Sorry - please try something else!")
            m.main_menu()
