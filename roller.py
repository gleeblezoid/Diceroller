# Copyright 2018 Ursula Searle
#!/usr/bin/env python3
import os
from pathlib import Path

def main():
    exec(Path('DiceRoller/Diceroller.py').open('r').read())

if __name__ == "__main__":
    main()
