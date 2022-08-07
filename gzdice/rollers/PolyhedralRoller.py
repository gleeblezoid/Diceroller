# Rolls a set of custom defined polyhedral dice

import random


def polyhedral_dice(pool, sides):
    result = ""
    try:
        # Error handling
        if sides < 1:
            print("Wow, just wow...")
            pass
        if pool < 1:
            print("Silly human")
            pass
        # Dice roll resolution
        i = 0
        while i < (pool):
            roll = random.randint(1, sides)
            i = i + 1
            result += f"{roll},"
    except (NameError, TypeError, ValueError):
        print("Sorry, try something else!")
        pass
    return result


def roll_again(pool, sides):
    rollagain = input("Roll the same again? Enter Y or N: ")
    if rollagain == "Y":
        polyhedral_dice(pool, sides)
    else:
        pass


def polyhedral_dice_roller():
    dice = input(
        "What do you want to roll? Enter in the format 1d6 \
            (for one six-sided die) "
    )
    pool = int(dice[: dice.find("d")])
    sides = int(dice[dice.find("d") + 1 :])
    polyhedral_dice(pool, sides)
    roll_again(pool, sides)
