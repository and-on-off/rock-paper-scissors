import random

score_win = 0
score_lose = 0
score_draw = 0

ROCK = "Rock"
PAPER = "Paper"
SCISSORS = "Scissors"

def valid_input_checker():
    while True:
        try:
            player_input = input("Choose [r]ock, [p]aper or [s]cissors: ")
            if player_input == "r":
                return player_input
            elif player_input == "p":
                return player_input
            elif player_input == "s":
                return player_input
        except ValueError:
            pass
        print("Invalid input. Try again...")

def print_in_red(result):
    print(f"\033[91m {result}\033[00m")

def print_in_green(result):
    print(f"\033[92m {result}\033[00m")

def print_in_blue(result):
    print(f"\033[34m {result}\033[00m")

def print_in_grey(result):
    print(f"\033[90m {result}\033[00m")


print_in_blue("Welcome to Rock-Paper-Scissors game! \n")
while True:

    player_move = valid_input_checker()

    if player_move == "r":
        player_move = ROCK
    elif player_move == "p":
        player_move = PAPER
    elif player_move == "s":
        player_move = SCISSORS
    else:
        raise SystemExit("Invalid Input. Try again...")

    computer_random_number = random.randint(1, 3)
    computer_move = ""

    if computer_random_number == 1:
        computer_move = ROCK
    elif computer_random_number == 2:
        computer_move = PAPER
    elif computer_random_number == 3:
        computer_move = SCISSORS

    print_in_blue(f"The computer chose {computer_move}.")

    if (player_move == ROCK and computer_move == SCISSORS) or \
            (player_move == PAPER and computer_move == ROCK) or \
            (player_move == SCISSORS and computer_move == PAPER):
        score_win += 1
        print_in_green("You win!")
    elif player_move == computer_move:
        score_draw += 1
        print_in_grey("Draw!")
    else:
        print_in_red("You lose!")
        score_lose += 1

    print()
    print("Type [yes] to play again or [no] to quit: ")
    play_again_response = input()

    if not play_again_response == "yes":
        print(f"Thank you for playing, you scored: \n"
              f"Wins: {score_win} | Loses: {score_lose} | Draws: {score_draw}")
        break