import random

games_played = 0
score_win = 0
score_lose = 0
score_draw = 0
win_streak = 0
max_win_streak = 0

ROCK = "Rock"
PAPER = "Paper"
SCISSORS = "Scissors"

def valid_input_checker():
    while True:
        player_input = input("Choose [r]ock, [p]aper or [s]cissors: ")
        if player_input == "r":
            return player_input
        elif player_input == "p":
            return player_input
        elif player_input == "s":
            return player_input
        elif player_input == "q":
            return False
        print("Invalid input. Try again...")

def print_in_color(result, color):
    if color == "red":
        print(f"\033[91m{result}\033[00m")
    elif color == "green":
        print(f"\033[92m{result}\033[00m")
    elif color == "blue":
        print(f"\033[34m{result}\033[00m")
    elif color == "grey":
        print(f"\033[90m{result}\033[00m")
    elif color == "light green":
        print(f"\033[92m{result}\033[92m")

def calculate_and_display_results():
    if games_played > 0:
        win_rate = score_win / games_played * 100
        lose_rate = score_lose / games_played * 100
        draw_rate = score_draw / games_played * 100
    else:
        win_rate = 0
        lose_rate = 0
        draw_rate = 0

    print()
    print(f"Thank you for playing, you scored: \n"
          f"Wins: {score_win} - {win_rate:.0f}% | Loses: {score_lose} - {lose_rate:.0f}% | Draws: {score_draw} - {draw_rate:.0f}%")
    print_in_color(f"Your highest win streak was {max_win_streak}.", "light green")

def restart_the_game():
    while True:
        player_response = input("Type [yes] to play again or [no] to quit: ")

        if player_response == "yes":
            return True
        elif player_response == "no" or player_response == "q":
            print()
            calculate_and_display_results()
            return False
        else:
            print("Invalid input. Please enter [yes] or [no]")

def computer_choice():
    random_number = random.randint(1,3)
    choice = ""

    if random_number == 1:
        choice = ROCK
    elif random_number == 2:
        choice = PAPER
    elif random_number == 3:
        choice = SCISSORS

    return choice

print_in_color("Welcome to Rock-Paper-Scissors game! \n"
              "You can quit the game anytime by typing [q].", "blue")

while True:

    try:
        player_move = valid_input_checker()

        if not player_move:
            calculate_and_display_results()
            break

        computer_move = computer_choice()
        games_played += 1

        if player_move == "r":
            player_move = ROCK
        elif player_move == "p":
            player_move = PAPER
        elif player_move == "s":
            player_move = SCISSORS

        print_in_color(f"The computer chose {computer_move}.", "blue")

        if (player_move == ROCK and computer_move == SCISSORS) or \
                (player_move == PAPER and computer_move == ROCK) or \
                (player_move == SCISSORS and computer_move == PAPER):
            score_win += 1
            win_streak += 1
            if win_streak >= max_win_streak:
                max_win_streak = win_streak
            print_in_color("You win!", "green")
        elif player_move == computer_move:
            score_draw += 1
            win_streak = 0
            print_in_color("Draw!", "grey")
        else:
            print_in_color("You lose!", "red")
            score_lose += 1
            win_streak = 0

        print()
        if not restart_the_game():
            break
    except KeyboardInterrupt:
        calculate_and_display_results()
        break
