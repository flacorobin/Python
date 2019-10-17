#Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)
def RPSinput (Player):
    answer = ''
    while (not answer == 'rock' and not answer == 'paper' and not answer == 'scissors'):
        answer = input(Player + " enter [Rock or Paper or Scissors]: ")
        answer = answer.lower()
    return answer

def RPSlogic (player1, player2):
    result = ''
    if player1 == player2:
        result = 'Tie'

    if player1 == 'rock':
        if player2 == 'paper':
            result = 'Player 2'
        else:
            result = 'Player 1'

    if player1 == 'scissors':
        if player2 == 'rock':
            result = 'Player 2'
        else:
            result = 'Player 1'

    if player1 == 'paper':
        if player2 == 'rock':
            result = 'Player 1'
        else:
            result = 'Player 2'

    return result

def RPSPlayagain ():
    answer = input("Do you want to play again? [Type No to exit]")
    answer = answer.lower()
    if answer == 'no':
        return False
    else:
        return True


print("Rock Paper Scissors")
keep_playing = True
while keep_playing == True:
    input_player1 = RPSinput('Player 1')
    input_player2 = RPSinput('Player 2')
    result = RPSlogic(input_player1, input_player2)
    print(result)
    keep_playing = RPSPlayagain()

print("Thanks for playing")
