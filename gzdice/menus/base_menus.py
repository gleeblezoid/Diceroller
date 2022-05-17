import sys

from ..rollers import BucketOfDice as bod
from ..rollers import ExplodingDice as ed
from ..rollers import FateRoller as fr
from ..rollers import PolyhedralRoller as pr
from ..rollers import GenesysDice as gs
from ..RPG_systems import existing_system as es
from ..RPG_systems import new_system as ns


def main_menu():
    show_menu()
    menu_choice = input("Please enter your choice: ")
    selection(menu_choice)


def show_menu():
    print(
        "\nChoose your preferred option from the menu below by typing \
            the shortcode or number for the option\n"
    )


def selection(menu_choice):
    if menu_choice == "q":
        sys.exit("Roll on")

    elif menu_choice == "1":
        option1()

    elif menu_choice == "2":
        option2()

    elif menu_choice == "3":
        option3()

    elif menu_choice == "4":
        option4()

    elif menu_choice == "5":
        option5()

    elif menu_choice == "6":
        option6()

    elif menu_choice == "7":
        option7()

    elif menu_choice == "8":
        option8()
    else:
        print("Sorry - please try something else")
        main_menu()


class menu_choice:
    def __init__(self, option_id: str, menu_description: str, option_function):
        self.option_id = option_id
        self.menu_description = f"{self.option_id}: {menu_description}"


quit = menu_choice("q", "Quit")
saved_rpg = menu_choice("1", "Use a saved RPG System")
add_remove_rpg = menu_choice("2", "Add/Remove a saved RPG System")
roll_d20 = menu_choice("3", "Roll single D20")
standard_polyhedral = menu_choice("4", "Standard polyhedral dice")
exploding_polyhedral = menu_choice("5", "Exploding polyhedral dice")
fate_roller = menu_choice("6", "Roll FATE dice")
genesys_roller = menu_choice("7", "Roll Genesys Narrative Dice")
bucket_roller = menu_choice("8", "Roll a big bucket of dice!")


def quit():
    sys.exit("Roll on")


def option1():
    es.saved_system()


def option2():
    ns.new_system()


def option3():
    pr.polyhedralroller(1, 20)


def option4():
    dice = input(
        "What do you want to roll? Enter in the format 1d6 \
            (for one six-sided die) "
    )
    pool = int(dice[: dice.find("d")])
    sides = int(dice[dice.find("d") + 1 :])
    pr.polyhedralroller(pool, sides)


def option5():
    dice = input(
        "What do you want to roll? Enter in the format 1d6 \
            (for one six-sided die) "
    )
    pool = int(dice[: dice.find("d")])
    sides = int(dice[dice.find("d") + 1 :])
    ed.explodingdice(pool, sides)


def option6():
    fr.fateroller()


def option7():
    gs.genesysdice()


def option8():
    bod.bucketofdice()
