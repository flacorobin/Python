#https://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html
#Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.

def input_control():
    value = -1
    while (value < 0 or value > 10):
            value = input("Input a number between 1-9: ")
            if (not value.isdigit()):
                print("Value is not a number. Try again.")
                value = -1
            else:
                value = int(value)
                if (value < 0 or value > 10):
                    print("Value not in range!")
    return value

import random

number = random.randint(1, 9)
if str(number).isdigit():
    print("Random Number generated! Try to guess the number [between 1 - 9]")

guess = 0
count = 0

while number != guess:
    guess = input_control()
    if number > guess:
        print("Too low")
    elif number < guess:
        print("Too high")
    count = count + 1

print(f"You are right! It took you {count} times to guess")
