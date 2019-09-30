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

def user_choice():
    game = \
    """
    Let's play Rock, Paper, Scissors!
    You pick first.
    1 - Rock
    2 - Paper
    3 - Scissors
    4 - Exit game
    Your choice: """
    return int(input(game))


if __name__ == "__main__":
    COMPUTER_CHOICE = computer_choice()
    MENU_CHOICE = user_choice()
    PLAYER_CHOICE = 'rock'
    while MENU_CHOICE != 4:
        if MENU_CHOICE == 1:
            PLAYER_CHOICE = 'rock'
        if MENU_CHOICE == 2:
            PLAYER_CHOICE = 'paper'
        if MENU_CHOICE == 3:
            PLAYER_CHOICE = 'scissors'

        print(f'\n\n{PLAYER} played {PLAYER_CHOICE}.')
        print(f'Computer played {COMPUTER_CHOICE}')
        print('The winner is...', score(COMPUTER_CHOICE, PLAYER_CHOICE))

        MENU_CHOICE = user_choice()
        COMPUTER_CHOICE = computer_choice()
