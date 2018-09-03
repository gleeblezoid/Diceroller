#######################################################################
# Provides framework to create and set up a config file               #
# Config files provide custom defined variables for the dice rollers  #
#######################################################################
# What are your variables?

print("Welcome to the dice roller customizer. "
      "This works best for systems which use pools of dice.")
rpgsystem = input("What RPG system are you using?")
rpgshortcode = input("What shortcode do you want to use for this RPG system?")


while True:
      try:
            sides = int(input("How many sides do your dice have?"))
            if sides <= 1:
                raise ValueError
            break
      except ValueError:
          print("Nope - try something else \n")
while True:
    try:
        explode = input("Do your dice explode? Type either Y or N:")
        if explode == "Y":
            break
        elif explode == "N":
            break
        else:
            raise ValueError
            break
    except ValueError:
        print("Nope - try something else - like an uppercase Y or N \n")

# This creates a file containing the parameters for your chosen RPG System
rpgfile = str("rpgsys"+"".join(rpgshortcode.split()) + ".py")
config = open(rpgfile,'w')
config.write("rpgsystem = \"" + rpgsystem + "\"\n")
config.write("sides = " + str(sides) + "\n")
config.write("explode = \"" + explode + "\"\n")
config.write("pool = int(input(\"How many dice are you rolling?\"))")


# This generates a menu entry for RPG selection via DiceRoller
rpglist = open(("rpgnames.py"),'a')
rpglist.write("\n"+"print(\"" + rpgshortcode +": " + rpgsystem + "\")" + "\n")

# This generates a usable entry from the RPG menu which pulls in the correct RPG parameters file

codeslist = open("rpgcodes.py",'a')
codeslist.write("\n" + rpgshortcode + "\n")

# Need a way to save configs for specific roleplay systems
print("Thanks - back to the Main Menu")

exec(open("./DiceRoller.py").read())