import random

# Define why you're rolling, how many dice, and how many sides on the dice
type = input("What are you rolling for?")
pool = int(input("How many dice are you rolling?"))
sides = int(input("How many sides are on each die?"))

#Explode once
print(type)
i = 0
while i < (pool):
    roll = random.randint(1, sides)
    if roll < sides : i = i + 1
    elif roll == random.randint(1, sides) : i = i + 1
    print(roll, end=",")
print("\n")

