
# Online Python - IDE, Editor, Compiler, Interpreter

# Automatic Dice Roller

# Written by [Watts]
import random
from random import randint

print ("Automatic Dice Roller")

input("Press Enter to roll")
random_number = random.randint(1,6)
print(random_number)
x = input("Press x to quit Press enter to roll again")
while x == (""):
    random_number = random.randint(1,6)
    print(random_number)
    x = input("Press x to quit Press enter to roll again")
    
print("Goodbye")
