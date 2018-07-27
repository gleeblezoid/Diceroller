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

rpgfile = str("rpg"+"".join(rpgsystem.split()) + ".py")
config = open(rpgfile,'w')
config.write("rpgsystem = " + rpgsystem + "\n")
config.write("sides = " + str(sides) + "\n")
config.write("explode = " + explode + "\n")

rpglist = open(("rpglist.py"),'a')
rpglist.write("\n"+"print(\"" + rpgshortcode +": " + rpgsystem + "\")" + "\n")

rpgmenu = open(("rpgmenu.py"),'a')

rpgmenu.write("\n"+"if menu_choice == \'" + rpgshortcode + "\':\n" + "      exec(open(\"./" + rpgfile + "\").read())")

# Need a way to save configs for specific roleplay systems
