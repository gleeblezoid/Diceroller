#######################################################################
# Provides framework to create and set up a config file               #
# Config files provide custom defined variables for the dice rollers  #
#######################################################################
# What are your variables?
import pickle
print("Welcome to the dice roller customizer. "
      "This works best for systems which use pools of dice.")
rpgsystem = input("What RPG system are you using?")
rpgshortcode = input("What shortcode do you want to use for this RPG system?")
sides = int(input("How many sides do your dice have?"))
explode = input("Do your dice explode? Type either Y or N")

# This creates a file containing the parameters for your chosen RPG System
rpgfile = str("rpg"+"".join(rpgshortcode.split()) + ".py")
config = open(rpgfile,'w')
config.write("rpgsystem = " + rpgsystem + "\n")
config.write("sides = " + str(sides) + "\n")
config.write("explode = " + explode + "\n")
config.write("pool = int(input(\"How many dice are you rolling?\"))")


# This generates a menu entry for RPG selection via DiceRoller
rpglist = open(("rpgnames.py"),'a')
rpglist.write("\n"+"print(\"" + rpgshortcode +": " + rpgsystem + "\")" + "\n")

# This generates a usable entry from the RPG menu which pulls in the correct RPG parameters file

codeslist = open("rpgcodes.py",'a')
codeslist.write(rpgshortcode + "\n")

# Need a way to save configs for specific roleplay systems
print("Thanks - back to the Main Menu")
exec(open("./Diceroller.py").read())