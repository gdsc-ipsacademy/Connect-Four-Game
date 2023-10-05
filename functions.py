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
        pygame.draw.rect(screen, colors["BLUE"], (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
        pygame.draw.circle(screen, colors["BLACK"], (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
        
    for c, r in itertools.product(range(COLUMN_COUNT), range(ROW_COUNT)):
        if board[r][c] == PLAYER_PIECE:
            pygame.draw.circle(screen, colors["RED"], (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
        elif board[r][c] == AI_PIECE: 
            pygame.draw.circle(screen, colors["YELLOW"], (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)

    pygame.display.update()

# Getting scores for connect 4s and connect 3s
def scorePosition(board, piece):

    # Horizontal score
    score = 0
    for r in range(ROW_COUNT):
        rowArray = [int(i) for i in list(board[r , : ])]
        for c in range(COLUMN_COUNT - 3):
            window = rowArray[c : c + WINDOW_LENGTH]

            if window.count(piece) == 4:
                score += 100

            elif window.count(piece) == 3 and window.count(EMPTY) == 1:
                score += 10
    
    # Vertical score
    for c in range(COLUMN_COUNT):
        colArray = [int(i) for i in list(board[ : , c])]
        for r in range(ROW_COUNT):
            window = colArray[r : r + WINDOW_LENGTH]

            if window.count(piece) == 4:
                score += 100

            elif window.count(piece) == 3 and window.count(EMPTY) == 1:
                score += 10
            
    return score

# Picking best moves based on scores
def pickBestMove(board, piece):

    validLocations = getValidLocations(board)

    bestScore = 0
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
