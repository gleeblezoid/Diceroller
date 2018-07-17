import random

# Define why you're rolling, how many dice, and how many sides on the dice
type = input("What are you rolling for?")
pool = int(input("How many dice are you rolling?"))
sides = int(input("How many sides are on each die?"))

if sides <= 1:
    print("Nice try")
    exit(0)

if pool < 1:
    print("Silly human")
    exit(0)

print(type)
i = 0
while i < (pool):
    roll = random.randint(1, sides)
    if roll < sides : i = i + 1
    elif roll == sides:
            random.randint(1, sides)
            i = i
    print(roll, end=",")
print("\n")

