import numpy as np

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
    return board[5][col] == 0

# Getting the lowest empty slot of the selected column
def getNextOpenRow(board, col):
    for slot in range(ROW_COUNT):
        if board[slot][col] == 0:
            return slot

# Dropping the piece in the board
def dropPiece(board, row, col, piece):
    board[row][col] = piece

def printBoard(board):
    print(np.flip(board, 0))

printBoard(board)
#  Game loop
while not gameOver:
    # Ask for player 1 input
    if turn == 0:
        col = int(input("Player 1 make your selection (0-6): "))

        if isValidLocation(board, col):
            row = getNextOpenRow(board, col)
            dropPiece(board, row, col, 1)

    # Ask for player 2 input
    else:
        col= int(input("Player 2 make your selection (0-6): "))

        if isValidLocation(board, col):
            row = getNextOpenRow(board, col)
            dropPiece(board, row, col, 2)

    printBoard(board)

    #  Switching turns between players
    turn += 1
    turn %= 2











