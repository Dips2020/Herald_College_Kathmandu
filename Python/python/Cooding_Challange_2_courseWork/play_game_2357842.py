#
#
from noughtsandcrosses_2357842 import *


def main():
    board = [['1', '2', '3'],
             ['4', '5', '6'],
             ['7', '8', '9']]

    welcome(board)
    total_score = 0
    while True:
        # It is returning the menu function to return choice (of user)
        choice = menu()
        if choice == '1':
            # If the condition is true play_game function will be called
            score = play_game(board)
            # Every score is added to total_score
            total_score = total_score + score
            print('Your current score is:', total_score)
        if choice == '2':
            # If the condition is true save_funtion will be called
            save_score(total_score)
        if choice == '3':
            # If the condition is true load_scores function will be called
            leader_board = load_scores()
            # calling the display_leaderborad() funtion
            display_leaderboard(leader_board)
        if choice == 'q':
            # If the condition is true, prints the following print() messages and returns
            print('Thank you for playing the "Unbeatable Noughts and Crosses" game.')
            print('Good bye')
            return


main()
