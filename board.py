# board.py
from constants import letters

def initialize_board(column_size):
    game_board = []
    for a in range(7):
        row = [' ' for _ in range(column_size + 1)]
        game_board.append(row)
    for a in range(column_size):
        game_board[0][a] = letters[a]
    return game_board

def display_board(game_board, column_size):
    print("C O N N E C T  4")
    print("'X O V H M'")
    print()
    for a in range(len(letters) - column_size):
        letters.pop()
    for letter in letters:
        print(' ', letter, end=' ')
    print()
    for a in range(1, 7):
        for _ in range(len(letters)):
            print('+---', end='')
        print('+')
        for i in range(column_size):
            print('|', game_board[a][i], '', end='')
        print('|')
    for _ in range(len(letters)):
        print('+---', end='')
    print('+')
