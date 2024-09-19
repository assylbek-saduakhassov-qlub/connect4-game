# game.py
import os
import random
from board import initialize_board, display_board
from players import get_player_label, get_player_name, validate_number_of_players
from constants import column_size, letters, range_reverse

# Game logic to handle player turns, board updates, and checking winning conditions.
def play_game():
    os.system("clear")
    game_board = initialize_board(column_size)
    players = setup_players()
    display_board(game_board, column_size)
    cells = column_size * 6  # Maximum number of cells on the board
    draw_moves = int(cells / len(players))  # Maximum number of moves per player

    # Main game loop
    for i in range(draw_moves + 2):  # Allow some extra turns for potential moves
        for f in range(len(players)):
            os.system('clear')
            display_board(game_board, column_size)
            player_name = get_player_name(players, f)
            player_label = get_player_label(f)
            print('Player', player_name + '(' + player_label + ')', end=' ')
            insert_column = input("choose the column(A, B, ...): ")

            # Validate input and update board
            while insert_column not in letters:
                print('Player', player_name + '(' + player_label + ')', end=' ')
                insert_column = input("enter a valid column letter: ")

            column_index = letters.index(insert_column)
            while game_board[1][column_index] != ' ':
                insert_column = input("The column is full, Please choose another column: ")
                while insert_column not in letters:
                    print('Player', player_name + '(' + player_label + ')', end=' ')
                    insert_column = input("enter a valid column letter: ")
                column_index = letters.index(insert_column)

            for row in range_reverse:
                if game_board[row][column_index] == ' ':
                    game_board[row][column_index] = player_label
                    if check_winner(player_label, game_board, row, column_index):
                        os.system("clear")
                        print('THE MISSION IS COMPLETED!!! Player', player_name, 'won!!!')
                        display_board(game_board, column_size)
                        exit()
                    break

            # Check for draw
            if all(game_board[1][col] != ' ' for col in range(column_size)):
                os.system("clear")
                print('DRAW...')
                display_board(game_board, column_size)
                exit()

# Function to set up players and determine their order
def setup_players():
    number_players = validate_number_of_players()
    players_temp = []

    # Getting player names
    for a in range(number_players):
        print(a + 1, "Player: ", end='')
        player_name = input("Please enter your name: ")
        while player_name.strip() == '':
            print(a + 1, "Player: ", end='')
            player_name = input("The name must consist of elements(at least 1): ")
        players_temp.append(player_name)

    # Randomizing player sequence
    players = []
    all_players = 0
    while all_players != number_players:
        random_num = random.randint(0, number_players - 1)
        if random_num not in players:
            players.append(players_temp[random_num])
            all_players += 1

    return players

# Function to check if a player has won after each move
def check_winner(player_label, game_board, row, column):
    # Check all possible directions for a connect-4 win
    directions = [(1, 0), (0, 1), (1, 1), (1, -1)]  # vertical, horizontal, diagonal right-down, diagonal left-down
    for dr, dc in directions:
        count = 1  # Starting with the current cell
        for step in range(1, 4):
            r, c = row + dr * step, column + dc * step
            if 0 <= r < 6 and 0 <= c < column_size and game_board[r][c] == player_label:
                count += 1
            else:
                break
        for step in range(1, 4):
            r, c = row - dr * step, column - dc * step
            if 0 <= r < 6 and 0 <= c < column_size and game_board[r][c] == player_label:
                count += 1
            else:
                break
        if count >= 4:
            return True
    return False
