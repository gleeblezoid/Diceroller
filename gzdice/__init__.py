"""A Python diceroller designed for tabletop roleplayers and running in terminal to make you feel like a wizard."""

__version__ = "0.1.1"


from .menus import base_menus as m


def main():
    m.main_menu()
