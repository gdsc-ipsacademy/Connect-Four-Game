import numpy as np
import itertools
import pygame
import sys

# Connect four board has dimentions 6*7
ROW_COUNT = 6
COLUMN_COUNT = 7

def createBoard():
    return np.zeros((ROW_COUNT,COLUMN_COUNT))

board = createBoard()
gameOver = False
turn = 0

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

#  Flipping the board before printing it because numpy starts 0,0 index from top left instaed of bottom left
def printBoard(board):
    print(np.flip(board, 0))

# Checking if the game is over
def gameOverCheck(board, piece):
    
    #  Checking horizontal win
    for c, r in itertools.product(range(COLUMN_COUNT - 3), range(ROW_COUNT)):
        if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
            return True

    #  Checking vertical win
    for c, r in itertools.product(range(COLUMN_COUNT), range(ROW_COUNT - 3)):
        if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
            return True

    #  Checking positive slop diagonal win
    for c, r in itertools.product(range(COLUMN_COUNT - 3), range(ROW_COUNT - 3)):
        if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
            return True
        
    #  Checking negative slop diagonal win
    for c, r in itertools.product(range(COLUMN_COUNT - 3), range(3, ROW_COUNT)):
        if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
            return True

def drawBoard(board):
    pass

printBoard(board)

#  Initialising the game
pygame.init()

SQUARESIZE = 100

width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT + 1) * SQUARESIZE

size = (width, height)

screen = pygame.display.set_mode(size)

#  Game loop
while not gameOver:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:

            # Ask for player 1 input
            # if turn == 0:
            #     col = int(input("Player 1 make your selection (0-6): "))

            #     if isValidLocation(board, col):
            #         row = getNextOpenRow(board, col)
            #         dropPiece(board, row, col, 1)

            #         if gameOverCheck(board, 1):
            #             print("Player 1 Wins!!")
            #             gameOver = True

            # # Ask for player 2 input
            # else:
            #     col= int(input("Player 2 make your selection (0-6): "))

            #     if isValidLocation(board, col):
            #         row = getNextOpenRow(board, col)
            #         dropPiece(board, row, col, 2)

            #         if gameOverCheck(board, 2):
            #             print("Player 2 Wins!!")
            #             gameOver = True

            printBoard(board)

            # #  Switching turns between players
            # turn += 1
            # turn %= 2











