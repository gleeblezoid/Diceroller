import sys

from ..data import MenuObjects as m


def show_menu(menu_list):
    menu = "\nChoose your preferred option from the menu below by typing \
the shortcode or number for the option\n"
    for i in menu_list:
        menu += i.menu_description
    return menu


def selection(menu_choice, menu_list):
    for item in menu_list:
        if menu_choice == item.option_id:
            item.option_function
        else:
            print("Sorry - please try something else")
            main_menu()


def main_menu():
    print(show_menu(m.menu_list))
    menu_choice = input("Please enter your choice: ")
    selection(menu_choice, m.menu_list)
