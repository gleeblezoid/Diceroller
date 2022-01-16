import sys

from ..rollers import BucketOfDice as bod
from ..rollers import ExplodingDice as ed
from ..rollers import FateRoller as fr
from ..rollers import PolyhedralRoller as pr
from ..rollers import StarWarsDice as swd
from ..RPG_systems import existing_system as es
from ..RPG_systems import new_system as ns


def show_menu():
    print(
        "\nChoose your preferred option from the menu below by typing the shortcode or number for the option\n"
    )

    print("1: Use a saved RPG System")
    print("2: Add/Remove a saved RPG System")
    print("3: Roll single D20")
    print("4: Standard polyhedral dice")
    print("5: Exploding polyhedral dice")
    print("6: Roll FATE dice")
    print("7: Roll Star Wars Narrative Dice")
    print("8: Roll a big bucket of dice!")
    print("q: Quit")


def main_menu():
    show_menu()
    menu_choice = input("Please enter your choice: ")
    selection(menu_choice)


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


def option1():
    es.saved_system()


def option2():
    ns.new_system()


def option3():
    pr.polyhedralroller(1, 20)


def option4():
    dice = input(
        "What do you want to roll? Enter in the format 1d6 (for one six-sided die) "
    )
    pool = int(dice[: dice.find("d")])
    sides = int(dice[dice.find("d") + 1 :])
    pr.polyhedralroller(pool, sides)


def option5():
    dice = input(
        "What do you want to roll? Enter in the format 1d6 (for one six-sided die) "
    )
    pool = int(dice[: dice.find("d")])
    sides = int(dice[dice.find("d") + 1 :])
    ed.explodingdice(pool, sides)


def option6():
    fr.fateroller()


def option7():
    swd.starwarsdice()


def option8():
    bod.bucketofdice()
