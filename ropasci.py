#!/usr/bin/env python3
'''Rock paper scissors game built with python'''

import random


CHOICES = {'rock': 1, 'scissors': 2, 'paper': 3}
PLAYER = "Player 1"

def score(computer: str, player: str) -> str:
    '''scores the results and returns the winner'''
    tally = CHOICES[computer] - CHOICES[player]
    if tally in [-1, 2]:
        return "Computer"
    if tally == 0:
        return "TIE"
    return PLAYER

def computer_choice() -> str:
    '''uses a random generator to play for computer'''
    return random.choice(list(CHOICES.keys()))


if __name__ == "__main__":
    import sys
    COMPUTER_CHOICE = computer_choice()
    PLAYER_CHOICE = sys.argv[1].lower()
    if PLAYER_CHOICE not in ['rock', 'paper', 'scissors']:
        print("Please choose either: rock, paper, or scissors.")
        sys.exit()
    print(f'{PLAYER} played {PLAYER_CHOICE}.')
    print(f'Computer played {COMPUTER_CHOICE}.')
    print('The winner is...', score(COMPUTER_CHOICE, PLAYER_CHOICE))
