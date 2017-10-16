#!/usr/bin/python

"""
Purpose - Tic-Tac-Toe Game Simulation
"""

"""
Data Structures to be used - 
board - set of slots - For example: (A, B, C, D, E, F, G, H, I)
                                    To visualize it on the Tic Tac Toe Grid
                                    *************
                                    * A * B * C *
                                    *************
                                    * D * E * F *
                                    *************
                                    * G * H * I *
                                    *************
winning_patterns - set of winning patterns - ('ABC', 'ADG', 'GHI', 'CFI', 'BEH', 'DEF', 'AEI', 'CEG')
symbols - set of symbols - ('x', 'o')
players - list of players - For example [('player1', 'x'), ('player2', 'o')]
player_moves - set of moves - For example ('A, 'B', 'C')

APIs - 
register_player:
    - Ask players name
    - Ask players symbol of choice - present list of symbol choices
      check if entered symbol is in set of symbols <Player has to select only one the given choices i.e. set symbols)
      Once symbol is selected by one player, delete symbol from symbols set
      In this way, second player would have only one choice to choose from

choose_first_player:
    - Randomly pick one player from the set of players

ask_player_to_move:
    - Ask to choose one of the avaiable slots - set board
      check if user entered move is in set board
      if valid, delete slot from set board
    - check for winning pattern
      if winner - and announce winner

check for winning pattern:
    - after each move by any player, check for winning pattern
    - scan players move against each winning pattern in set winning_patterns
    - if winning pattern found in player's moves then announce winner and exit

announce winner:
    - print out player name, symbol and winning pattern
"""

import logging
import sys
import random

logging.basicConfig(level=logging.CRITICAL)

board = { 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I' } #Assumption
winning_patterns = { 'ABC', 'ADG', 'GHI', 'CFI', 'BEH', 'DEF', 'AEI', 'CEG' } #Pre-defined as per rule games
ALLOWED_NUMBER_OF_PLAYERS = 2 #Assumption
ALLOWED_SYMBOLS = { 'x', 'o' } #Assumption

players = [] #List to hold players and respective symbols
players_moves = []      # List of Lists to maintain player moves
                        # At index i, list of player (at index i in players list) are maintained
                        # For example - At index 0, moves of player at 0th index inplayers list are maintained

def register_player(players): #Register players - Expects a list of players to be updated in place
    player_name = input("Enter your name: ")
    logging.debug("player_name recorded: %s" % player_name)
    print("Available Symbols to choose from: ", ALLOWED_SYMBOLS)
    player_symbol = input('Choose symbol from given choices : ')
    if player_symbol in ALLOWED_SYMBOLS: #Validate entered symbol
        ALLOWED_SYMBOLS.remove(player_symbol) #Remove from set as it is already picked up for this game
    else:
        while player_symbol not in ALLOWED_SYMBOLS: #Keep asking until valid symbol is entered
            player_symbol = input('Choose symbol from given choices : ')
        ALLOWED_SYMBOLS.remove(player_symbol) #Remove from set as it is already picked up for this game
    logging.debug("player_symbol recorded: %s" %player_symbol)
    player = (player_name, player_symbol) #Represent player as one tuple
    players.append(player) #Add player to list of players
    logging.debug("current state of list players: %s" % players)
    return players #Return players


def choose_first_player(): #Randomly pick one player
    player_index = random.randint(0,len(players)-1) #Possible valules - either index 0 or 1
    logging.debug('Randomly chosen player_index: %s' %player_index)
    return player_index

def next_player(current_player_index, players): #Returns the index of next player in round robin fashion
    index_for_next_player = (current_player_index + 1) % len(players)
    logging.debug("index_for_next_player: %s" %index_for_next_player)
    return index_for_next_player

def ask_current_player_to_move(current_player_index, players_moves, players): #Ask current player to move
    #Check current state of board
    if len(board) > 0: #Slots available on board
        player_name = get_player_name(current_player_index, players)
        print("Turn for: ", player_name)
        logging.debug("following slots are available on board: %s" % board)
        print("Available lots on the board to choose from: ", board)
        slot = input("Choose one of the availble slots to mark: ")
        #validate slot value entered by user
        if slot in board: #valid value
            #update player move
            update_players_moves(current_player_index, slot, players_moves)
            #Remove slot from board set
            board.remove(slot)
        else:
            while slot not in board: #Keep asking until slot is not valid
                slot = input("Choose one of the availble slots to mark: ")
            #update player move
            update_players_moves(current_player_index, slot, players_moves)
            #Remove slot from board set
            board.remove(slot)

def update_players_moves(current_player_index, slot, players_moves): #In place update moves for players
                                         #Expects a list of lists as input
                                         #current player index to identify for which player moves should be updated
    logging.debug("update_players_moves request received for player: %s" %current_player_index)
    #Initialize for the first time
    if players_moves == []: #Empty for the first time
        players_moves.append([]) #Append empty list for first player
        players_moves.append([]) #Append empty list for second layer
        players_moves[current_player_index].append(slot) #Simply capture the move of player
        logging.debug("First time players_moves initialized: %s" %players_moves)
    else: #Not the very first chance for both players
        players_moves[current_player_index].append(slot) #Simply capture the move of player
        logging.debug("move captured for player having index: %s in players_moves: %s" % (current_player_index, players_moves))


def check_for_winning_pattern(current_player_index, players_moves, winning_patterns): #checks for current playing players winning pattern
    check_outcome = [] #To hold analysis of result
                       #To hold list like this [True, current_player_index, winning_pattern]
    won = False
    player_winning_pattern = None
   
    #Didn't win yet    
    check_outcome.append(won)
    check_outcome.append(current_player_index)
    check_outcome.append(player_winning_pattern)

    if len(players_moves[current_player_index]) < 3: #No point to check for winning pattern
        logging.debug("Returning check_outcome because players has not taken at least 3 moves yet: %s" %check_outcome)
        return check_outcome

    #Scan players moves for finding against winning pattern
    for winning_pattern in winning_patterns: #Linear scan through winning patterns
        counter = 0 #To count if all 3 slots of winning pattern are found in players move
        for slot in winning_pattern: #For each slot contained in winning pattern
            logging.debug("Scanning slot: %s in winning_pattern: %s" %(slot, winning_pattern))
            logging.debug("current_player_index: %s" %current_player_index)
            logging.debug("For current player: %s state of players moves: %s" %(current_player_index, players_moves[current_player_index]))

            if slot in players_moves[current_player_index]: #Scan player's moves
                counter += 1
                logging.debug("Counter: %s" %counter)

        if counter == 3: #Found a winning match
            won = True
            player_winning_pattern = winning_pattern
            check_outcome[0] = won
            check_outcome[1] = current_player_index
            check_outcome[2] = player_winning_pattern
            logging.debug("Winning pattern found, returning check_outcome: %s" %check_outcome)
            return check_outcome #No need to keep scanning further

    logging.debug("No winning pattern found, returning check_outcome: %s" %check_outcome)
    return check_outcome

def announce_winner(check_outcome, players, players_moves): # Input of format [True, current_player_index, winning_pattern]
    winning_player_index = check_outcome[1]
    winner_name = players[winning_player_index][0] #Refer players structure
    winning_pattern = check_outcome[2]
    total_moves = len(players_moves[winning_player_index])
    print("*"*25)
    print("Winner:", winner_name)
    print("Winning pattern:", winning_pattern)
    print("Won in total moves:", total_moves) 
    print("*"*25)

def get_player_name(current_player_index, players):
    return players[current_player_index][0] #Refer players structure

def start_game(): #Entry point of the game
    #Start Player Registration
    for n in range(ALLOWED_NUMBER_OF_PLAYERS):
        register_player(players)

    #Choose first player randomly
    current_player_index = choose_first_player() #hold current player index
    
    #Ask players to play until no available slot is remaining on the board or winning pattern is found
    while len(board) != 0 or check_for_winning_pattern(current_player_index, players_moves, winning_patterns)[0]:
        ask_current_player_to_move(current_player_index, players_moves, players) #Ask curent player to move
        check_outcome = check_for_winning_pattern(current_player_index, players_moves, winning_patterns)
        if check_outcome[0]: #Someone won
            announce_winner(check_outcome, players, players_moves) 
            sys.exit(0) #Exit Game
        current_player_index = next_player(current_player_index, players) #Ask next player
    print("No winner!!!")

if __name__ == "__main__":
   start_game() 
