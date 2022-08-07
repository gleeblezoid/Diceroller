# Roller for multiple polyhedral types in one pool

import random


def bucket_of_dice():
    # Define multiple dice pools (make a list)
    bucket = []
    moredice = "Y"

    try:
        while str.upper(moredice) == "Y":
            dice = input(
                "What do you want to roll? e.g 1d6 \
                (for one six-sided die) "
            )
            bucket.append(dice)
            moredice = input(
                "Do you want to add more dice to the bucket? \
                    Type Y or N: "
            )

        else:
            explode = input(
                "Do you want your dice to explode? \
                Type Y or N: "
            )
            result = ""
            if str.upper(explode) == "N":
                for dice in bucket:
                    print("\n" + dice)
                    pool = int(dice[: dice.find("d")])
                    sides = int(dice[dice.find("d") + 1 :])
                    i = 0
                    while i < (pool):
                        roll = random.randint(1, sides)
                        i = i + 1
                        result += f"{roll},"
                    result = result.rstrip(str[-1])

            elif str.upper(explode) == "Y":
                for dice in bucket:
                    print("\n" + dice)
                    pool = int(dice[: dice.find("d")])
                    sides = int(dice[dice.find("d") + 1 :])
                    if sides <= 1:
                        raise ValueError
                    else:
                        i = 0
                        while i < (pool):
                            roll = random.randint(1, sides)
                            if roll < sides:
                                i = i + 1
                            elif roll == sides:
                                random.randint(1, sides)
                                i = i
                        result += f"{roll},"
                    result = result.rstrip(str[-1])

    except (NameError, TypeError, ValueError):
        print("Sorry, try something else!")
        pass

    return result


def roll_again():
    rollagain = input(
        "Do you want to roll another bucket of dice?\
        Enter Y or N: "
    )
    if str.upper(rollagain) == "Y":
        bucket_of_dice()
    else:
        pass


def bucket_of_dice_roller():
    bucket_of_dice()
    roll_again()
