import numpy as np
import itertools
import pygame
import random
import math

from variables import ROW_COUNT, COLUMN_COUNT, size, colors, SQUARESIZE, RADIUS, height, width, PLAYER_PIECE, AI_PIECE

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
    
    
def getValidLocations(board):
    return [c for c in range(COLUMN_COUNT) if isValidLocation(board, c)]
