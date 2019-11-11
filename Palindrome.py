# This script will check if a word is a Palindrome and will return TRUE
# if it does


def palindrome(word):
    word = word.lower()
    middle = int(len(word)/2)
    first_half = word[:middle]
    second_half = word[-1:middle:-1]
    if first_half == second_half:
        return True


word = input('Enter a word, if it is a palindrome it will return TRUE: ')
print(palindrome(word))
