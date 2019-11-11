# https://www.practicepython.org/exercise/2014/12/27/24-draw-a-game-board.html
# Ask the user what size game board they want to draw, and draw it for them to
# the screen using Python’s print statement.


def print_board(x=3, y=3):
    top = " ---"
    side = "|   "

    for i in range(y):
        print(top * x + ' ')
        print(side * x + '|')

    print(top * x + ' ')  # Printing bottom of the board


print_board(3, 3)
