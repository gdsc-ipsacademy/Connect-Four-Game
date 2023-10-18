import itertools
import random

from variables import ROW_COUNT, COLUMN_COUNT, PLAYER_PIECE, AI_PIECE, WINDOW_LENGTH, EMPTY
from functions import get_valid_locations, get_next_open_row, drop_piece

# Evaluating scores of connections
def evaluate_window(window, piece):

    score = 0
    opponent_piece = PLAYER_PIECE
    if piece == PLAYER_PIECE:
        opponent_piece = AI_PIECE

    if window.count(piece) == 4:
        score += 100
    elif window.count(piece) == 3 and window.count(EMPTY) == 1:
        score += 50
    elif window.count(piece) == 2 and window.count(EMPTY) == 2:
        score += 10

    if window.count(opponent_piece) == 3 and window.count(EMPTY) == 1:
        score -= 75
    elif window.count(opponent_piece) == 2 and window.count(EMPTY) == 2:
        score -= 25

    return score

# Getting scores for connections
def score_position(board, piece, directions=(1, 1, 1, 1)):

    score = 0

    # Prefer center column for increased probablity of win
    centerArray = [int(i) for i in list(board[ : , COLUMN_COUNT//2])]
    centerCount = centerArray.count(piece)
    score += centerCount*10

    if directions[0]:
        # Horizontal score
        for r in range(ROW_COUNT):
            rowArray = [int(i) for i in list(board[r , : ])]
            for c in range(COLUMN_COUNT - 3):
                window = rowArray[c : c + WINDOW_LENGTH]
                score += evaluate_window(window, piece)

    if directions[1]:
        # Vertical score
        for c in range(COLUMN_COUNT):
            colArray = [int(i) for i in list(board[ : , c])]
            for r in range(ROW_COUNT):
                window = colArray[r : r + WINDOW_LENGTH]
                score += evaluate_window(window, piece)

    if directions[2]:
        # Positive slope diagonal score
        for r, c in itertools.product(range(ROW_COUNT - 3), range(COLUMN_COUNT - 3)):
            window = [board[r + i][c + i] for i in range(WINDOW_LENGTH)]
            score += evaluate_window(window, piece)

    if directions[3]:
        # Negative slope diagonal score
        for r, c in itertools.product(range(ROW_COUNT - 3), range(COLUMN_COUNT - 3)):
            window = [board[r + 3 - i][c + i] for i in range(WINDOW_LENGTH)]
            score += evaluate_window(window, piece)

    return score

# Picking best moves based on scores
def pick_best_move(board, piece, directions=(1, 1, 1, 1)):
    valid_locations = get_valid_locations(board)

    best_score = -10000
    best_col = random.choice(valid_locations)

    for c in valid_locations:
        r = get_next_open_row(board, c)
        temp_board = board.copy()
        drop_piece(temp_board, r, c, piece)
        score = score_position(temp_board, piece, directions)

        if score > best_score:
            best_score = score
            best_col = c

    return best_col
