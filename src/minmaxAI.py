import math
import random

from variables import ROW_COUNT, COLUMN_COUNT, PLAYER_PIECE, AI_PIECE
from functions import isValidLocation, gameOverCheck, get_next_open_row, drop_piece, get_valid_locations
from scoreAI import score_position


# Checking for terminal nodes
def isTerminalNode(board):
    return gameOverCheck(board, PLAYER_PIECE) or gameOverCheck(board, AI_PIECE) or len(get_valid_locations(board)) == 0

# Implimenting minimax algorithm
def minimax(board, depth, alpha, beta, maximizingPlayer):
    validLocations = get_valid_locations(board)

    if isTerminal := isTerminalNode(board):
        if gameOverCheck(board, AI_PIECE):
            return (None, math.inf)
        elif gameOverCheck(board, PLAYER_PIECE):
            return (None, -math.inf)
        else:
            return (None, 0)
    elif depth == 0:
        return (None, score_position(board, AI_PIECE))

    if maximizingPlayer:
        value = -math.inf
        column = random.choice(validLocations)

        for c in validLocations:
            r = get_next_open_row(board, c)
            tempBoard = board.copy()
            drop_piece(tempBoard, r, c, AI_PIECE)
            newScore = minimax(tempBoard, depth - 1, alpha, beta, False)[1]

            if newScore > value:
                value = newScore
                column = c

            alpha = max(alpha, value)

            if alpha >= beta:
                break

    # Minimizing player
    else:
        value = math.inf
        column = random.choice(validLocations)

        for c in validLocations:
            r = get_next_open_row(board, c)
            tempBoard = board.copy()
            drop_piece(tempBoard, r, c, PLAYER_PIECE)
            newScore = minimax(tempBoard, depth - 1, alpha, beta, True)[1]

            if newScore < value:
                value = newScore
                column = c

            beta = min(beta, value)

            if alpha >= beta:
                break
    return column, value
