# players.py
from constants import player_symbol, column_size

def get_player_label(index):
    return player_symbol[index]

def get_player_name(players, index):
    return players[index]

def validate_number_of_players():
    number_players_checked = 0
    while number_players_checked != 1:
        try:
            number_players = int(input("Please enter the number of players(min - 2 players, max - 5 players): "))
            while 2 > number_players > 5:
                number_players = int(input("Please enter a valid number of players(2-5): "))
            if 2 <= number_players <= 5:
                number_players_checked = 1
        except ValueError:
            print("Please enter a valid number of players")    
    return number_players
