#######################################################################
# Provides framework to create and set up a config file               #
# Config files provide custom defined variables for the dice rollers  #
#######################################################################

# What are your variables?

print("Welcome to the dice roller customizer. "
      "This works best for systems which use pools of dice.")
rpgsystem = input("What RPG system are you using?")
sides = int(input("How many sides do your dice have?"))
explode = input("Do your dice explode? Type either Yes or No")


config = open((rpgsystem + ".py"),'w')
config.write("rpgsystem = " + rpgsystem + "\n")
config.write("sides = " + str(sides) + "\n")
config.write("explode = " + explode + "\n")

rpglist = open(("rpglist.py"),'w')
rpglist.write(rpgsystem + "\n")
# Need a way to save configs for specific roleplay systems