import random

player_wins = 0
cpu_wins = 0


print('welcome to the game!')

player_choice = input('Enter your choice (rock, paper, scissors): ')
game = True

choices = ['rock', 'paper', 'scissors']
cpu_choice = random.choice(choices)

while player_choice not in choices:
    player_choice = input('Enter your choice (rock, paper, scissors): ')
    if player_choice not in choices:
        print('Choose again!')

print(f"Player choose {player_choice}")
print('--------')
print(f"CPU choose {cpu_choice}")

if player_choice == 'rock' and cpu_choice == 'scissors':
    print('Player wins!')
    player_wins += 1
    print(f"PlayerWins: {player_wins}, CpuWins: {cpu_wins}")
elif player_choice == 'scissors' and cpu_choice == 'paper':
    print('Player wins!')
    player_wins += 1
    print(f"PlayerWins: {player_wins}, CpuWins: {cpu_wins}")
elif player_choice == 'paper' and cpu_choice == 'rock':
    print('Player wins!')
    player_wins += 1
    print(f"PlayerWins: {player_wins}, CpuWins: {cpu_wins}")
elif player_choice == cpu_choice:
    print('Its a tie!')
else:
    print('CPU wins!')
    cpu_wins += 1
    print(f"CpuWins: {cpu_wins}, PlayerWins: {player_wins}")

result = input('If you wanna continue press y, if you wanna quite press q')
if result.lower() == 'y':
    print('ok, continue')
game = True
if result.lower() == 'q':
    print('game over!')
game = False


