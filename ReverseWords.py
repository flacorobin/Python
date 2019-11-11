# https://www.practicepython.org/exercise/2014/05/21/15-reverse-word-order.html
# Asks the user for a long string containing multiple words. Print back to the
# user the same string, except with the words in backwards order


def inputRW():
    while True:
        text = input("Enter a phrase with 2 words or more: ")
        if ' ' in text:
            break
        else:
            print("The phrase needs at least 2 words. Try again")

    return text


print("This script will reverse the orders of the words you input.")
text = inputRW()

print("Reverse phrase:")
textlist = text.split(' ')

# Remeving the code to reverse, using the list function instead
# tracker = len(textlist) - 1
# list_to_show = []
#
# while tracker >= 0:
#     list_to_show.append(textlist[tracker])
#     tracker = tracker - 1

# print(' '.join(list_to_show))
textlist.reverse()
print(' '.join(textlist))
