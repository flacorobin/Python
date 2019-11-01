#https://www.practicepython.org/exercise/2017/01/10/32-hangman.html
#In this exercise, we will finish building Hangman. In the game of Hangman, the player only has 6 incorrect guesses (head, body, 2 legs, and 2 arms) before they lose the game.

import random

def pick_word():
    with open('PickAWord.txt', 'r') as f:
        list_of_words = f.readlines()

    number = random.randint(0, len(list_of_words)-1)
    word = list_of_words[number].strip()
    return word

def hangman_input():
    letter = ''
    while not len(letter) == 1 or not letter.isalpha():
        letter = input("Enter a letter: ")

    return letter.upper()

def print_hangman_board(word, set_letters):
    winner = True
    for i in range(len(word)):
        if word[i] in set_letters:
            print(word[i] + ' ', end = '')
        else:
            print('_ ', end = '')
            winner = False

    print('\n')
    return winner

def print_guesses(guesses):
    if guesses > 1:
        print("You have ", guesses, "guesses left.")
    else:
        print("You have ", guesses, "guess left.")


print("Python Hangman!")
word = pick_word()
print(word)
print("Word Length:", len(word))
guesses = 6
set_letters = set()
winner = False

while guesses > 0:
    if winner == True:
        break
    winner = print_hangman_board(word, set_letters)
    print_guesses(guesses)

    print('\n')
    letter = hangman_input()
    while letter in set_letters:
        print("You already guesses that letter.")
        letter = hangman_input()
    if letter in word:
        print("Letter guessed!")
    else:
        print("Letter not in word :(")
        guesses -= 1

    set_letters.add(letter)

if winner == True:
    print('You Won!')
else:
    print('You Lost...')
