#########################
# Star Wars Dice Roller #
#########################
import gc
import random
from pathlib import Path

# Define the dice
class dice:
    def __init__(self,colour,name,sides,results,poolcount):
        self.colour = colour
        self.name = name
        self.sides = sides
        self.results = results
        self.poolcount = poolcount

pool = [0,0,0,0,0,0,0]
#dice_set = ["ability","proficiency","difficulty","challenge","boost","setback","force"]
dice_name_list = []
dice_colour_list = []

# Green (Ability) - d8 [s,a,sa,ss,a,s,aa,' ']
ability = dice('green','ability',8,['s','a','sa','ss','a','s','aa',' '],0)
# Yellow (Proficiency) - d12 [aa,a,aa,ts,s,sa,s,sa,ss,sa,ss,' ']
proficiency = dice('yellow','proficiency',12,['aa','a','aa','ts','s','sa','s','sa','ss','sa','ss',' '],1)
# Purple (Difficulty) - d8 [t,f,ft,t,' ',tt,ff,t]
difficulty = dice('purple','difficulty',8,['t','f','ft','t',' ','tt','ff','t'],2)
# Red (Challenge) - d12 [tt,t,tt,t,ft,f,ft,f,ff,df,ff,' ']
challenge =  dice('red','challenge',12,['tt','t','tt','t','ft','f','ft','f','ff','df','ff',' '],3)
# Blue (Boost) - d6 [sa,aa,,s,a,' ',' ']
boost = dice('blue','boost',6,['sa','aa','s','a',' ',' '],4)
# Black (Setback) - d6 [' ',' ',t,t,f,f]
setback = dice('black','setback',6,[' ',' ','t','t','f','f'],5)
# White (Force) - d12 [d,d,d,d,d,d,ll,ll,ll,l,l,dd]
force = dice('white','force',12,['d','d','d','d','d','d','ll','ll','ll','l','l','dd'],6)



# Print list of dice with number for each one being rolled

def printchoices():
    for obj in gc.get_objects():
        if isinstance(obj, dice):
            print(obj.name + " (" + obj.colour + "): " + str(pool[obj.poolcount]))
            dice_name_list.append(obj.name)
            dice_colour_list.append(obj.colour)

dice_name_set = set(dice_name_list)
dice_name_list = list(dice_name_set)
dice_colour_set = set(dice_colour_list)
dice_colour_list = list(dice_colour_set)

print("What dice do you want to roll?")
printchoices()

# Create Pool: Ask about which dice are being rolled by colour
print("Enter how many of each die you want:")
pool = []
pc = 0
for i in range (0,7):
    die = int(input("How many "+str(dice_name_list[pc])+" ("+str(dice_colour_list[pc])+") dice?"))
    pc = pc + 1
    pool.append(die)

# When input done print list of dice again with number against each
printchoices()

# Create function to roll dice
def rolldice:


    # Create function to clear dice pool back to zero
# Consolidate the success/failure, advantage/disadvantage, triumph/despair
    # Throw all the results into a list and then use a set of count functions to total up results
    # Subtract threat from advantage, and failure from success
    # Triumph, Despair, and Force Points just total up (normalise
# Offer reroll same, new pool, or quit to menu