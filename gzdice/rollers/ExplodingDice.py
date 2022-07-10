# Rolls repeatedly exploding dice #

import random

def exploding_dice(pool, sides):
    result = ""
    try:
        # Error handling
        if sides <= 1:
            print("Nice try")
        if pool < 1:
            print("Silly human")
        # Dice roll resolution
        i = 0
        while i < (pool):
            roll = random.randint(1, sides)
            if roll < sides:
                i = i + 1
            elif roll == sides:
                random.randint(1, sides)
                i = i
                result += f"{roll},"
    except (NameError, TypeError, ValueError):
        print("Sorry, try something else!")
        pass
    result = result.rstrip(str[-1])
    return result


def roll_again(pool, sides):
    rollagain = input("Roll the same again? Enter Y or N: ")
    if rollagain == "Y":
        return exploding_dice(pool,sides)
    else:
        pass

def exploding_dice_roller():
    dice = input(
        "What do you want to roll? Enter in the format 1d6 \
            (for one six-sided die) "
    )
    pool = int(dice[: dice.find("d")])
    sides = int(dice[dice.find("d") + 1 :])
    exploding_dice(pool,sides)
    roll_again(pool,sides)
