"""                 DICE GAME
The Objective of the game is to get closest to 21.
A player competes against the computer to roll 2 dices
enough times to get to 21.  They can choose to stop
rolling dice whenever they would like however if their
total goes above 21 by default they loose.
"""
from random import randint


def display_history(hist):
    print(BOLD + UNDERLINE + "\n\n                SUMMARY                " + END)
    print("HISTORY: ")
    for state in hist:
        print("\t" + state)
    wins = hist.count("PLAYER WINS")
    loses = hist.count("COMPUTER WINS")
    print(f"W/L: {wins}/{loses}")


def game_over(state):
    global run
    run = False
    print("\n")
    print(UNDERLINE + BOLD + state + END)
    history.append(state)


def check_winner(ps, cs):
    if run is False or ps >= 21 or cs >= 21:
        state = "CONTINUE"
        if ps > 21 and cs > 21:
            state = "NO WINNERS"
        elif cs > 21:
            state = "PLAYER WINS"
        elif ps > 21:
            state = "COMPUTER WINS"
        elif ps > cs:
            state = "PLAYER WINS"
        elif cs > ps:
            state = "COMPUTER WINS"
        else:
            state = "TIE"

        if state != "CONTINUE":
            game_over(state)


def roll_dice():
    dice1 = randint(1, 6)
    dice2 = randint(1, 6)
    total = dice1 + dice2
    return total


def plyr_turn():
    global run
    user_input = input(BOLD + "Roll Dice? y/n: " + END)
    if user_input == 'y' or user_input == 'Y':
        return roll_dice()
    else:
        run = False
        return 0


def comp_turn():
    if run is True:
        return roll_dice()
    elif plyr_score >= comp_score:
        return roll_dice()
    else:
        return 0


plyr_score = 0
comp_score = 0

history = []

RED = '\033[31m'
BLUE = '\033[34m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
END = '\033[0m'

play = "y"
while play == "y":
    run = True
    while run:
        plyr_score += plyr_turn()
        comp_score += comp_turn()
        check_winner(plyr_score, comp_score)
        print(BLUE + f"Player Score: {plyr_score}" + END)
        print(RED + f"Computer Score: {comp_score}" + END)
    play = input("\n\nPlay Again? y/n: ").lower()
    plyr_score = 0
    comp_score = 0

display_history(history)