#########################
# Genesys Dice Roller #
#########################

import gc
import random

# Define the dice


class dice:
    def __init__(self, colour, name, sides, results, pool):
        self.colour = colour
        self.name = name
        self.sides = sides
        self.results = results
        self.pool = pool


global dice_name_list
global dice_colour_list
global dice_sides_list
global dice_results_list
global dice_pool_list
dice_name_list = []
dice_colour_list = []
dice_sides_list = []
dice_results_list = []
dice_pool_list = []

# Green (Ability) - d8 [s,a,sa,ss,a,s,aa,' ']
ability = dice("green", "ability", 8, ["s", "a", "sa", "ss", "a", "s", "aa", " "], 0)
# Yellow (Proficiency) - d12 [aa,a,aa,ts,s,sa,s,sa,ss,sa,ss,' ']
proficiency = dice(
    "yellow",
    "proficiency",
    12,
    ["aa", "a", "aa", "Ts", "s", "sa", "s", "sa", "ss", "sa", "ss", " "],
    1,
)
# Purple (Difficulty) - d8 [t,f,ft,t,' ',tt,ff,t]
difficulty = dice(
    "purple", "difficulty", 8, ["t", "f", "ft", "t", " ", "tt", "ff", "t"], 2
)
# Red (Challenge) - d12 [tt,t,tt,t,ft,f,ft,f,ff,df,ff,' ']
challenge = dice(
    "red",
    "challenge",
    12,
    ["tt", "t", "tt", "t", "ft", "f", "ft", "f", "ff", "Df", "ff", " "],
    3,
)
# Blue (Boost) - d6 [sa,aa,,s,a,' ',' ']
boost = dice("blue", "boost", 6, ["sa", "aa", "s", "a", " ", " "], 4)
# Black (Setback) - d6 [' ',' ',t,t,f,f]
setback = dice("black", "setback", 6, [" ", " ", "t", "t", "f", "f"], 5)
# White (Force) - d12 [d,d,d,d,d,d,ll,ll,ll,l,l,dd]
force = dice(
    "white",
    "force",
    12,
    ["d", "d", "d", "d", "d", "d", "ll", "ll", "ll", "l", "l", "dd"],
    6,
)

dice_name_set = set(dice_name_list)
dice_name_list = list(dice_name_set)
dice_colour_set = set(dice_colour_list)
dice_colour_list = list(dice_colour_set)
dice_sides_set = set(dice_sides_list)
dice_sides_list = list(dice_sides_set)
dice_results_set = set(dice_results_list)
dice_results_list = list(dice_results_set)
dice_pool_set = set(dice_pool_list)
dice_pool_list = list(dice_pool_set)


def print_choices():
    for obj in gc.get_objects():
        if isinstance(obj, dice):
            print(obj.name + " (" + obj.colour + "): " + str(gspool[obj.pool]))
            dice_name_list.append(obj.name)
            dice_colour_list.append(obj.colour)
            dice_sides_list.append(obj.sides)
            dice_results_list.append(obj.results)
            dice_pool_list.append(obj.pool)


# Create gsPool: Ask about which dice are being rolled by colour


def create_gs_pool():
    global gspool
    gspool = []
    pc = 0
    for i in range(0, 7):
        try:
            die = abs(
                int(
                    input(
                        "How many "
                        + str(dice_name_list[pc])
                        + " ("
                        + str(dice_colour_list[pc])
                        + ") dice? "
                    )
                )
            )
            gspool.append(die)
        except (NameError, TypeError, ValueError):
            gspool.append(0)
        pc = pc + 1


# Roll dice


def roll_dice():
    global rolled_results
    rolled_results = []
    result_output = "\n"
    rpc = 0
    for i in range(0, 7):
        if gspool[rpc] > 0:
            for p in range(0, gspool[rpc]):
                roll = random.randint(0, int(dice_sides_list[rpc]) - 1)
                die_face = dice_results_list[rpc][roll]
                rolled_results.append(die_face)
        else:
            rolled_results.append(" ")
        rpc = rpc + 1

    # Consolidate the success/failure, advantage/disadvantage, \
    # triumph/despair

    final_result = str(rolled_results)
    successes = final_result.count("s")
    failures = final_result.count("f")
    advantages = final_result.count("a")
    threats = final_result.count("t")
    triumphs = final_result.count("T")
    despairs = final_result.count("D")
    light = final_result.count("l")
    dark = final_result.count("d")

    success_vs_failure = int(successes - failures)
    advantages_vs_threats = int(advantages - threats)


    if success_vs_failure >= 0:
        result_output += f"\nSuccess {str(success_vs_failure)}"
    else:
        result_output += f"\nFailure {str(abs(success_vs_failure))}"

    if advantages_vs_threats >= 0:
        result_output += f"\nAdvantage {str(advantages_vs_threats)}"
    else:
        result_output += f"\nThreat {str(abs(advantages_vs_threats))}"

    result_output += f"\nTriumphs {str(triumphs)}\nDespair {str(despairs)}\nLightside {str(light)}\nDarkside {str(dark)}\n"
    
    return result_output, gs_dice_menu()

# Offer reroll same, new gspool, or quit to menu
def gs_dice_menu():
    print("Choose an option from the menu:")
    print("1: Reroll the same dice pool")
    print("2: Roll a new pool of dice")
    print("q: Quit to main menu")
    gsubmenu_choice = input("Please enter your choice: ")

    if gsubmenu_choice == "1":
        print("\n")
        print_choices()
        print("\n")
        roll_dice()
        print("\n")
        gs_dice_menu()
        print("\n")
    elif gsubmenu_choice == "2":
        create_gs_pool()
        print("\n")
        print_choices()
        print("\n")
        roll_dice()
        gs_dice_menu()
        print("\n")
    elif gsubmenu_choice == "q":
        pass
    else:
        print("Sorry - please try something else.")
        print("\n")
        gs_dice_menu()


def genesysdice():
    try:
        global gspool
        gspool = [0, 0, 0, 0, 0, 0, 0]
        print("What dice do you want to roll?")
        print_choices()
        print("\n")
        print("Enter how many of each die you want:")
        create_gs_pool()
        print("\n")
        print_choices()
        print("\n")
        roll_dice()
    except (NameError, TypeError, ValueError):
        print("Sorry, try something else")
        gs_dice_menu()
