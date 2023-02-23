import random

def create_ship():
    return random.randint(1, 8), random.randint(A, G)

def play_again():
    try_again = input("Want to try again? <Y> <N>")
    if jls_extract_def(try_again):
       play_game()
    else:
        print("See you next time, Goodbye!")
        return

print("Welcome to Battleship"
    "\nThis is the game where you go against the computer.\n"
    "\nTry to sink all of the computers ships in the number of turns you have. Best of Luck\n")

def print_board(board):
    print(' A B C D E F G ')
    