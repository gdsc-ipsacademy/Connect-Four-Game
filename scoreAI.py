import itertools

from variables import ROW_COUNT, COLUMN_COUNT, PLAYER_PIECE, AI_PIECE, WINDOW_LENGTH, EMPTY

# Evaluating scores of connections
def evaluateWindow(window, piece):

    score = 0
    opponentPiece = PLAYER_PIECE
    if piece == PLAYER_PIECE:
        opponentPiece = AI_PIECE
    
    if window.count(piece) == 4:
        score += 100
    elif window.count(piece) == 3 and window.count(EMPTY) == 1:
        score += 50
    elif window.count(piece) == 2 and window.count(EMPTY) == 2:
        score += 10

    if window.count(opponentPiece) == 3 and window.count(EMPTY) == 1:
        score -= 75    
    elif window.count(opponentPiece) == 2 and window.count(EMPTY) == 2:
        score -= 25

    return score

# Getting scores for connections
def scorePosition(board, piece):

    score = 0

    # Prefer center column for increased probablity of win
    centerArray = [int(i) for i in list(board[ : , COLUMN_COUNT//2])]
    centerCount = centerArray.count(piece)
    score += centerCount*10

    # Horizontal score
    for r in range(ROW_COUNT):
        rowArray = [int(i) for i in list(board[r , : ])]
        for c in range(COLUMN_COUNT - 3):
            window = rowArray[c : c + WINDOW_LENGTH]
            score += evaluateWindow(window, piece)

    # Vertical score
    for c in range(COLUMN_COUNT):
        colArray = [int(i) for i in list(board[ : , c])]
        for r in range(ROW_COUNT):
            window = colArray[r : r + WINDOW_LENGTH]
            score += evaluateWindow(window, piece)

    # Positive slope diagonal score
    for r, c in itertools.product(range(ROW_COUNT - 3), range(COLUMN_COUNT - 3)):
        window = [board[r + i][c + i] for i in range(WINDOW_LENGTH)]
        score += evaluateWindow(window, piece)

    # Negative slope diagonal score
    for r, c in itertools.product(range(ROW_COUNT - 3), range(COLUMN_COUNT - 3)):
        window = [board[r + 3 - i][c + i] for i in range(WINDOW_LENGTH)]
        score += evaluateWindow(window, piece)

    return score

# Picking best moves based on scores
def pickBestMove(board, piece):

    validLocations = getValidLocations(board)

    bestScore = -10000
    bestCol = random.choice(validLocations)

    for c in validLocations:
        r = getNextOpenRow(board, c)
        tempBoard = board.copy()
        dropPiece(tempBoard, r, c, piece)
        score = scorePosition(tempBoard, piece)

        if score > bestScore:
            bestScore = score
            bestCol = c

    return bestCol