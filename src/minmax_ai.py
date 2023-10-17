import math
import random

from variables import ROW_COUNT, COLUMN_COUNT, PLAYER_PIECE, AI_PIECE
from functions import is_valid_location, game_over_check, get_next_open_row, drop_piece
from score_ai import score_position

# Getting valid locations for AI
def get_valid_locations(board):
    return [c for c in range(COLUMN_COUNT) if is_valid_location(board, c)]

# Checking for terminal nodes
def is_terminal_node(board):
    return game_over_check(board, PLAYER_PIECE) or game_over_check(board, AI_PIECE) or len(get_valid_locations(board)) == 0

# Implimenting minimax algorithm
def minimax(board, depth, alpha, beta, maximizing_player):
    valid_locations = get_valid_locations(board)

    if isTerminal := is_terminal_node(board):
        if game_over_check(board, AI_PIECE):
            return (None, math.inf)
        elif game_over_check(board, PLAYER_PIECE):
            return (None, -math.inf)
        else: 
            return (None, 0)
    elif depth == 0:
        return (None, score_position(board, AI_PIECE))

    if maximizing_player:
        value = -math.inf
        column = random.choice(valid_locations)

        for c in valid_locations:
            r = get_next_open_row(board, c)
            temp_board = board.copy()
            drop_piece(temp_board, r, c, AI_PIECE)
            new_score = minimax(temp_board, depth - 1, alpha, beta, False)[1]

            if new_score > value:
                value = new_score
                column = c
            
            alpha = max(alpha, value)

            if alpha >= beta:
                break

    # Minimizing player
    else:
        value = math.inf
        column = random.choice(valid_locations)

        for c in valid_locations:
            r = get_next_open_row(board, c)
            temp_board = board.copy()
            drop_piece(temp_board, r, c, PLAYER_PIECE)
            new_score = minimax(temp_board, depth - 1, alpha, beta, True)[1]

            if new_score < value:
                value = new_score
                column = c

            beta = min(beta, value)

            if alpha >= beta:
                break
            
    return column, value