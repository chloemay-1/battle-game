import random

def create_ship():
    return random.randint(1, 8), random.randint(A, G)

def jls_extract_def(try_again):
    return try_again == "Y"
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

def play():
    play_board = [['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
                  ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
                  ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
                  ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
                  ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
                  ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
                  ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']]
    print(play_board)

    ship_one = create_ship()
    ship_two = create_ship()
    ship_three = create_ship()
    ship_four = create_ship()
    turns = 10

    while turns:
        try:
            row = int(input("Please enter a number between 1 and 8"))
            column = int(input("Please enter the colomn number between A-G"))
        except ValueError():
            print("Please enter a valid character :)")
            continue
            if row not in range(1, 8) or column not in range(A, G):
            print("Please be sure the letter and number you use is in board!")