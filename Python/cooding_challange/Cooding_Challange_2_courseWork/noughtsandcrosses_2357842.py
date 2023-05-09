#
#
#
import random
import os.path
import json
random.seed()


def draw_board(board):
    # It will print the current state of the board.
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def welcome(board):
    # It will display a welcome message and the initial board.
    print("!!! Welcome to Noughts and Crosses !!!")
    draw_board(board)


def initialise_board(board):
    # It initializes the game board by setting all cells to empty.
    for i in range(3):
        for j in range(3):
            board[i][j] = ' '
    return board


def get_player_move(board):
    # It prompts the player to enter a number (or move) and returns the corresponding row and column.
    while True:
        try:
            cell = int(input("Enter the cell number (1-9): "))
            if 1 <= cell <= 9:
                row = (cell - 1) // 3
                col = (cell - 1) % 3
                if board[row][col] == ' ':
                    return row, col
                else:
                    print("That cell is already occupied. Please choose another.")
            else:
                print("Invalid cell number. Please choose a number from 1 to 9.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def choose_computer_move(board):
    # It randomly selects an empty cell for the computer's move.
    empty_cells = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                empty_cells.append((i, j))
    return random.choice(empty_cells)


def check_for_win(board, mark):
    # It checks if a player (player=X or computer=O) has won the game.
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == mark:
            return True
        if board[0][i] == board[1][i] == board[2][i] == mark:
            return True
    if board[0][0] == board[1][1] == board[2][2] == mark:
        return True
    if board[0][2] == board[1][1] == board[2][0] == mark:
        return True
    return False


def check_for_draw(board):
    # It checks if the game has ended in a draw.
    for row in board:
        if ' ' in row:
            return False
    return True


def play_game(board):
    board = initialise_board(board)
    draw_board(board)
    while True:
        player_row, player_col = get_player_move(board)
        board[player_row][player_col] = 'X'
        draw_board(board)
        if check_for_win(board, 'X'):
            print("Wow!! You have won this round.")
            return 1
        if check_for_draw(board):
            return 0
        computer_row, computer_col = choose_computer_move(board)
        board[computer_row][computer_col] = 'O'
        draw_board(board)
        if check_for_win(board, 'O'):
            print("Sorry, Computer have won this game.")
            return -1
        if check_for_draw(board):
            return 0


def menu():
    # It displays the game menu and returns the user's choice.
    while True:
        print("Enter one of the following options:")
        print("1 - Play the game")
        print("2 - Save your score in the leaderboard")
        print("3 - Load and display the leaderboard")
        print("q - End the program")
        choice = input("Your choice: ")
        if choice in ('1', '2', '3', 'q'):
            return choice
        else:
            print("Invalid input. Please enter a valid option.")


def load_scores():
    # It loads the leaderboard from a file if it exists or returns an empty leaderboard.
    if os.path.exists("leaderboard.txt"):
        with open("leaderboard.txt", "r") as file:
            try:
                leaderboard = json.load(file)
            except json.JSONDecodeError:
                leaderboard = {}
    else:
        leaderboard = {}
    return leaderboard


def save_score(score):
    # It saves the player's score in the leaderboard.txt file.
    name = input
    if os.path.exists("leaderboard.txt"):
        with open("leaderboard.txt", "r") as file:
            try:
                leaderboard = json.load(file)
            except json.JSONDecodeError:
                leaderboard = {}
    else:
        leaderboard = {}
    name = input("Enter your name: ")
    leaderboard[name] = score
    with open("leaderboard.txt", "w") as file:
        json.dump(leaderboard, file)


def display_leaderboard(leaderboard):
    # It displays the leaderboard.
    print("Leaderboard:")
    for name, score in leaderboard.items():
        print(f"{name}: {score}")
