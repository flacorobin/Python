# https://www.practicepython.org/exercise/2016/09/24/30-pick-word.html
# In this exercise, the task is to write a function that picks a random word
# from a list of words from the SOWPODS dictionary.

import random

print("Python scrip that will pick a random word from SOWPODS dicitonary.")

with open('PickAWord.txt', 'r') as f:
    list_of_words = f.readlines()

number = random.randint(0, len(list_of_words)-1)
word = list_of_words[number].strip()
print("Random word is: ", word)
