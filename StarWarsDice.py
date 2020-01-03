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

pool = []
dice_name_list = []
dice_colour_list = []
dice_sides_list = []
dice_results_list = []
dice_poolcount_list = []

# Green (Ability) - d8 [s,a,sa,ss,a,s,aa,' ']
ability = dice('green','ability',8,['s','a','sa','ss','a','s','aa',' '],0)
# Yellow (Proficiency) - d12 [aa,a,aa,ts,s,sa,s,sa,ss,sa,ss,' ']
proficiency = dice('yellow','proficiency',12,['aa','a','aa','Ts','s','sa','s','sa','ss','sa','ss',' '],1)
# Purple (Difficulty) - d8 [t,f,ft,t,' ',tt,ff,t]
difficulty = dice('purple','difficulty',8,['t','f','ft','t',' ','tt','ff','t'],2)
# Red (Challenge) - d12 [tt,t,tt,t,ft,f,ft,f,ff,df,ff,' ']
challenge =  dice('red','challenge',12,['tt','t','tt','t','ft','f','ft','f','ff','Df','ff',' '],3)
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
            dice_sides_list.append(obj.sides)
            dice_results_list.append(obj.results)
            dice_poolcount_list.append(obj.poolcount)

dice_name_set = set(dice_name_list)
dice_name_list = list(dice_name_set)
dice_colour_set = set(dice_colour_list)
dice_colour_list = list(dice_colour_set)
dice_sides_set = set(dice_sides_list)
dice_sides_list = list(dice_sides_set)
dice_results_set = set(dice_results_list)
dice_results_list = list(dice_results_set)
dice_poolcount_set = set(dice_poolcount_list)
dice_poolcount_list = list(dice_poolcount_set)



# Create Pool: Ask about which dice are being rolled by colour


def createpool():
    pc = 0
    for i in range (0,7):
        die = int(input("How many "+str(dice_name_list[pc])+" ("+str(dice_colour_list[pc])+") dice? "))
        pc = pc + 1
        pool.append(die)


# Roll dice
rolled_results = []
def rolldice():
    rpc = 0
    for i in range (0,7):
        if pool[rpc] > 0:
            for p in range (0,pool[rpc]):
                roll = random.randint(0,int(dice_sides_list[rpc])-1)
                die_face = dice_results_list[rpc][roll]
                rolled_results.append(die_face)
        else:
            rolled_results.append(" ")
        rpc = rpc + 1

# Consolidate the success/failure, advantage/disadvantage, triumph/despair

    final_result = str(rolled_results)
    successes = final_result.count('s')
    failures = final_result.count('f')
    advantages = final_result.count('a')
    threats = final_result.count('t')
    triumphs = final_result.count('T')
    despairs = final_result.count('D')
    light = final_result.count('l')
    dark = final_result.count('d')

    success_vs_failure = int(successes - failures)
    advantages_vs_threats = int(advantages - threats)

    if success_vs_failure >= 0:
        print("Success " + str(success_vs_failure))
    else:
        print("Failure "+str(abs(success_vs_failure)))

    if advantages_vs_threats >= 0:
        print("Advantage " + str(advantages_vs_threats))
    else:
        print("Threat "+str(abs(advantages_vs_threats)))

    print("Triumphs "+ str(triumphs))
    print("Despair " + str(despairs))
    print("Lightside " + str(light))
    print("Darkside " + str(dark))
    print('\n')


# Offer reroll same, new pool, or quit to menu
def swdicemenu():
    print("Choose an option from the menu:")
    print("1: Reroll the same dice pool")
    print("2: Roll a new pool of dice")
    print("q: Quit to main menu")
    menu_choice = input("Please enter your choice: ")

    if menu_choice == '1':
        printchoices()
        rolldice()
        swdicemenu()
    elif menu_choice == '2':
        pool = []
        createpool()
        printchoices()
        rolldice()
        swdicemenu()
    elif menu_choice == 'q':
        exec(Path('./Diceroller.py').open('r').read())



pool = [0,0,0,0,0,0,0]
print("What dice do you want to roll?")
printchoices()
print("Enter how many of each die you want:")
pool = []
createpool()
printchoices()
print('\n')
rolldice()
swdicemenu()
