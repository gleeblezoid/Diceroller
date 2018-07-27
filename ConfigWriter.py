#######################################################################
# Provides framework to create and set up a config file               #
# Config files provide custom defined variables for the dice rollers  #
#######################################################################

# What are your variables?

print("Welcome to the dice roller customizer. "
      "This works best for systems which use pools of dice.")
rpgsystem = input("What RPG system are you using?")
rpgshortcode = input("What shortcode do you want to use for this RPG system?")
sides = int(input("How many sides do your dice have?"))
explode = input("Do your dice explode? Type either Y or N")


config = open(str("".join(rpgsystem.split()) + ".py"),'w')
config.write("rpgsystem = " + rpgsystem + "\n")
config.write("sides = " + str(sides) + "\n")
config.write("explode = " + explode + "\n")

rpglist = open(("rpglist.py"),'w')
rpglist.write("print(\"" + rpgshortcode +": " + rpgsystem + "\")" + "\n")

rpgmenu = open(("rpgmenu.py"), 'w')

rpgmenu.write("if menu_choice == \'" + rpgshortcode + "\':\n" + "      import " + "".join(rpgsystem.split()))

# Need a way to save configs for specific roleplay systems
