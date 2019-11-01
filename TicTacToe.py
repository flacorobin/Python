#https://www.practicepython.org/exercise/2016/08/03/29-tic-tac-toe-game.html
#The next step is to put all these three components together to make a two-player Tic Tac Toe game!

def print_ttt_board(x, y, board):
#Function to draw TicTacToe Results
    top = " ---"
    side = "|   "

    for i in range(y):
        print(top * x + ' ')
        print("|", board[i][0], '|', board[i][1], '|', board[i][2], '|')

    print(top * x + ' ') #Printing bottom of the board

def tic_tac_toe_check(ttt_board):
#function  to check if there is a winner. Should run every turn
    winner =  ' '

    for i in range(0, len(ttt_board)):
        if (ttt_board[i][0] == ttt_board[i][1] == ttt_board[i][2]) and (ttt_board[i][0] != ' '): #Cross Checks
            winner = ttt_board[i][0]
            break

        if (ttt_board[0][i] == ttt_board[1][i] == ttt_board[2][i]) and (ttt_board[0][i] != ' '): #Vertical Checks
            winner = ttt_board[0][i]
            break


    if (ttt_board[0][0] == ttt_board[1][1] == ttt_board[2][2]) and (ttt_board[0][0] != ' '): #Diagonal Check
        winner = ttt_board[0][0]

    if (ttt_board[0][2] == ttt_board[1][1] == ttt_board[2][2]) and (ttt_board[2][2] != ' '): #Diagonal Check
        winner = ttt_board[0][2]

    return winner

def input_check(player, board):
#Function to check input, more check should be in place
    answer = ''
    while True:
        try:
            while ',' not in answer:
                answer = input(f"Player {player} enter coordinates (row, col): ")           

            coordinates = answer.split(',')

            x = int(coordinates[0]) -1
            y = int(coordinates[1]) -1

            if ( 3 < x < -1) and (3 < y < -1):
                print("Row and Col must be either 0,1,2")
                continue

            if player == 1:
                symbol = 'X'
            else:
                symbol = 'O'

            if board[x][y] == ' ':
                board[x][y] = symbol
                break
            else:
                print("Space used, input again")
        except ValueError:
            print("Not a number")
    return board


def big_letters(letter):
    letter_dict = {
    'X':'x   x\n'+' x x \n'+'  x  \n'+' x x \n'+'x   x\n',
    'O':' 000 \n'+'0   0\n'+'0   0\n'+'0   0\n'+' 000 \n'
    }
    print(letter_dict[letter])
    pass



board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
winner = ' '
player = 1
print("TicTacToe Game")
print_ttt_board(3,3,board)

while winner == ' ':
    board = input_check(player, board)
    print_ttt_board(3,3,board)
    winner = tic_tac_toe_check(board)
    if player == 1:
        player = 2
    else:
        player = 1

print("The winner is: \n")
big_letters(winner)
