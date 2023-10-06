import numpy as np
import itertools
import pygame
import random

from variables import ROW_COUNT, COLUMN_COUNT, size, colors, SQUARESIZE, RADIUS, height, width, PLAYER_PIECE, AI_PIECE, WINDOW_LENGTH, EMPTY


# Creating board
def createBoard():
    return np.zeros((ROW_COUNT,COLUMN_COUNT))

# Creating the board
board = createBoard()

# Checking if the top row of a selected column is empty or not
def isValidLocation(board, col):
    return board[ROW_COUNT-1][col] == 0

# Getting the lowest empty slot of the selected column
def getNextOpenRow(board, col):
    for slot in range(ROW_COUNT):
        if board[slot][col] == 0:
            return slot

# Dropping the piece in the board
def dropPiece(board, row, col, piece):
    board[row][col] = piece

# Checking if the game is over
def gameOverCheck(board, piece):
    
    # Checking horizontal win
    for c, r in itertools.product(range(COLUMN_COUNT - 3), range(ROW_COUNT)):
        if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
            return True

    # Checking vertical win
    for c, r in itertools.product(range(COLUMN_COUNT), range(ROW_COUNT - 3)):
        if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
            return True

    # Checking positive slop diagonal win
    for c, r in itertools.product(range(COLUMN_COUNT - 3), range(ROW_COUNT - 3)):
        if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
            return True
        
    # Checking negative slop diagonal win
    for c, r in itertools.product(range(COLUMN_COUNT - 3), range(3, ROW_COUNT)):
        if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
            return True

# Setting screen size
screen = pygame.display.set_mode(size)

# Drawing board graphics
def drawBoard(board):

    for c, r in itertools.product(range(COLUMN_COUNT), range(ROW_COUNT)):
        pygame.draw.rect(screen, colors["VERDIGRIS"], (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
        pygame.draw.circle(screen, colors["CHARCOAL"], (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
        
    for c, r in itertools.product(range(COLUMN_COUNT), range(ROW_COUNT)):
        if board[r][c] == PLAYER_PIECE:
            pygame.draw.circle(screen, colors["CERISE"], (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
        elif board[r][c] == AI_PIECE: 
            pygame.draw.circle(screen, colors["ICTERINE"], (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)

    pygame.display.update()

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

# Getting valid locations for AI
def getValidLocations(board):
    return [c for c in range(COLUMN_COUNT) if isValidLocation(board, c)]

# Checking for terminal nodes
def isTerminalNode(board):
    return gameOverCheck(board, PLAYER_PIECE) or gameOverCheck(board, AI_PIECE) or len(getValidLocations) == 0

# Implimenting minimax algorithm
def minimax(board, depth, maximizingPlayer):
    validLocations = getValidLocations(board)

    if isTerminal := isTerminalNode(board):
        if gameOverCheck(board, AI_PIECE):
            return math.inf
        elif gameOverCheck(board, PLAYER_PIECE):
            return -math.inf
        else: 
            return 0
    elif depth == 0:
        return scorePosition(board, AI)

    if maximizingPlayer:
        value = -math.inf
        column = random.choice(validLocations)

        for c in validLocations:
            r = getNextOpenRow(board, c)
            tempBoard = board.copy()
            dropPiece(tempBoard, r, c, AI_PIECE)
            newScore = minimax(tempBoard, depth - 1, False)

            if newScore > value:
                value = newScore
                column = c

            return column, value

    # Minimizing player
    else:
        value = math.inf
        for c in validLocations:
            r = getNextOpenRow(board, c)
            tempBoard = board.copy()
            dropPiece(tempBoard, r, c, PLAYER_PIECE)
            newScore = minimax(tempBoard, depth - 1, True)

            if newScore < value:
                value = newScore
                column = c
                
            return column, value
    
    
