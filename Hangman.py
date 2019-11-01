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

def print_guesses(guess_num):
    if guess_num > 1:
        print("You have", guess_num, "guesses left.")
    else:
        print("You have", guess_num, "guess left.")

def play_again_check():
    answer = ''
    while not len(answer) == 1 or not answer.isalpha():
        answer = input("Do you want to play again? (Y, N)")
        if answer.upper() == 'Y' or answer.upper() == 'N':
            answer = answer.upper()
        else:
            answer = ''
    print("\n\n")
    if answer == 'Y':
        answer = True
    else:
        answer = False

    return answer

def draw_hangman():
    hangman_dict = {
    0:'  -----\n'+' |     0 \n'+' |    \|/\n'+' |     |\n'+' |    / \ \n'+' |\n'+' |\n'+"/ \ \n"
    }
    print(hangman_dict[0]+"\n\n")

print("Python Hangman!")
draw_hangman()

play_again = True

while play_again:
    word = pick_word()
    print(word)
    print("Word Length:", len(word))

    guesses = 6
    set_letters = set()
    winner = False

    while guesses > 0:
        winner = print_hangman_board(word, set_letters)
        if winner == True:
            break
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

    play_again = play_again_check()
