import sys

from ..rollers import BucketOfDice as bod
from ..rollers import ExplodingDice as ed
from ..rollers import FateRoller as fr
from ..rollers import PolyhedralRoller as pr
from ..rollers import GenesysDice as gs
from ..RPG_systems import existing_system as es
from ..RPG_systems import new_system as ns


class menu_item:
    def __init__(self, option_id: str, menu_description: str, option_function):
        self.option_id = option_id
        self.option_function = option_function
        self.menu_description = f"{self.option_id}: {menu_description}\n"

    def print_option(self):
        print(self.menu_description)


def quit_menu():
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


quit = menu_item("q", "Quit", quit_menu)
saved_rpg = menu_item("1", "Use a saved RPG System", option1)
add_remove_rpg = menu_item("2", "Add/Remove a saved RPG System", option2)
roll_d20 = menu_item("3", "Roll single D20", option3)
standard_polyhedral = menu_item("4", "Standard polyhedral dice", option4)
exploding_polyhedral = menu_item("5", "Exploding polyhedral dice", option5)
fate_roller = menu_item("6", "Roll FATE dice", option6)
genesys_roller = menu_item("7", "Roll Genesys Narrative Dice", option7)
bucket_roller = menu_item("8", "Roll a big bucket of dice!", option8)
menu_list = [
    quit,
    saved_rpg,
    add_remove_rpg,
    roll_d20,
    standard_polyhedral,
    exploding_polyhedral,
    fate_roller,
    genesys_roller,
    bucket_roller,
]
