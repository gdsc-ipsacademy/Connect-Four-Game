import numpy as np

# Connect four board has dimentions 6*7
def createBoard():
    return np.zeros((6,7))

board = createBoard()
gameOver = False
turn = 0

while not gameOver:
    # Ask for player 1 input
    if turn == 0:
        selection = int(input("Player 1 make your selection (0-6): "))

    # Ask for player 2 input
    else:
        selection = int(input("Player 2 make your selection (0-6): "))

    turn += 1
    turn %= 2











