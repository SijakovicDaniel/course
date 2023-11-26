print('rock')
print('paper')
print('scissors')

player1 = input('player 1, make your move')
player2 = input('player 2, make your move')


if player1 == 'rock' and player2 == 'scissors':
    print('player1 wins!')
elif player1 == 'rock' and player2 == 'paper':
    print('player 2 wins!')
elif player1 == 'paper' and player2 == 'rock':
    print('player 1 wins!')
elif player1 == 'paper' and player2 == 'scissors':
    print('player 2 wins!')
elif player1 == 'scissors' and player2 == 'rock':
    print('player 2 wins!')
elif player1 == 'scissors' and player2 == 'paper':
    print('player 1 wins!')
elif player1 == player2:
    print('play again')
else:
    print('something went wrong')


