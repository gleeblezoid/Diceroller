# Copyright 2018 Ursula Searle
#!/usr/bin/env python3

def main():
    from DiceRoller import show_menu, selection
    show_menu()
    menu_choice = input("Please enter your choice: ")
    selection(menu_choice)

if __name__ == "__main__":
    main()
