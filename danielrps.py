import random

game = True
player_wins = 0
cpu_wins = 0
choices = ['rock', 'paper', 'scissors']

print('Welcome to the game')
while game:
    player_choice = ""
    while player_choice not in choices:
        player_choice = input('Choose one item: (rock, paper, scissors)')
    cpu_choices = random.choice(choices)

    print(f"Player choose: {player_choice}")
    print('--------')
    print(f"Cpu choose: {cpu_choices}")

    if (
        (player_choice == 'rock' and cpu_choices == 'paper') 
        or (player_choice == 'paper' and cpu_choices == 'scissors')
        or (player_choice == 'scissors' and cpu_choices == 'rock')
    ):
        print('Cpu wins!')
        cpu_wins += 1
        print(f"Cpu Wins: {cpu_wins}, Player wins: {player_wins} ")
    elif player_choice == cpu_choices:
        print('Its a tie!')
    else:
        print('Player wins!')
        player_wins += 1
        print(f"Player wins: {player_wins}, Cpu Wins: {cpu_wins} ")
    
    result = input('If you wanna continue pres y, if you wanna quite press q')
    if result.lower() == 'y':
        print('Ok, lets continue')
    if result.lower() == 'q':
        print('Ok, good bye')
        game = False