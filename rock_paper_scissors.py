import random

score_win = 0
score_lose = 0
score_draw = 0

def print_in_red(result):
    print(f"\033[91m {result}\033[00m")

def print_in_green(result):
    print(f"\033[92m {result}\033[00m")

def print_in_blue(result):
    print(f"\033[34m {result}\033[00m")

def print_in_grey(result):
    print(f"\033[90m {result}\033[00m")

while True:
    rock = "Rock"
    paper = "Paper"
    scissors = "Scissors"

    player_move = input("Choose [r]ock, [p]aper or [s]cissors: ")

    if player_move == "r":
        player_move = rock
    elif player_move == "p":
        player_move = paper
    elif player_move == "s":
        player_move = scissors
    else:
        raise SystemExit("Invalid Input. Try again...")

    computer_random_number = random.randint(1, 3)
    computer_move = ""

    if computer_random_number == 1:
        computer_move = rock
    elif computer_random_number == 2:
        computer_move = paper
    elif computer_random_number == 3:
        computer_move = scissors

    print_in_blue(f"The computer chose {computer_move}.")

    if (player_move == rock and computer_move == scissors) or \
            (player_move == paper and computer_move == rock) or \
            (player_move == scissors and computer_move == paper):
        score_win += 1
        print_in_blue("You win!")
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
        print(f"Thank you for playing, you scored:"
              f"Wins: {score_win} | Loses: {score_lose} | Draws: {score_draw}")
        break