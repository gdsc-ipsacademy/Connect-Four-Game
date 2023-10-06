import pygame
import sys
import math
import random
from variables import ROW_COUNT, COLUMN_COUNT, SQUARESIZE, size, RADIUS, colors, height, width, PLAYER, AI, \
    PLAYER_PIECE, AI_PIECE
from functions import createBoard, isValidLocation, getNextOpenRow, dropPiece, gameOverCheck, drawBoard, pickBestMove, \
    board, screen

gameOver = False
turn = random.randint(PLAYER, AI)

# Initialising the game
pygame.init()

# Drawing board
drawBoard(board)
pygame.display.update()

myfont = pygame.font.SysFont("monospace", 80)

# Game loop
while not gameOver:

    # Getting the events
    for event in pygame.event.get():

        # Checking if the game has been quit
        if event.type == pygame.QUIT:
            sys.exit()

        # Checking mouse hover event
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, colors["CHARCOAL"], (0, 0, width, SQUARESIZE))
            posx = event.pos[0]
            if turn == PLAYER:
                pygame.draw.circle(screen, colors["CERISE"], (posx, int(SQUARESIZE / 2)), RADIUS)

        pygame.display.update()

        # Checking mouse click event
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, colors["CHARCOAL"], (0, 0, width, SQUARESIZE))
            posx = event.pos[0]

            # Ask for player 1 input
            if turn == PLAYER:
                col = int(math.floor(posx / SQUARESIZE))

                if isValidLocation(board, col):
                    row = getNextOpenRow(board, col)
                    dropPiece(board, row, col, PLAYER_PIECE)

                    if gameOverCheck(board, PLAYER_PIECE):
                        label = myfont.render("You win!! ^_^", 1, colors["MISTYROSE"])
                        screen.blit(label, (40, 10))
                        gameOver = True

                    turn ^= 1

                    drawBoard(board)

    # Ask for player 2 input
    if turn == AI and not gameOver:

        # Random move selection
        # col = random.randint(0, COLUMN_COUNT - 1)
        col = pickBestMove(board, AI_PIECE)

        if isValidLocation(board, col):

            # Adding delay to AI move
            pygame.time.wait(500)

            row = getNextOpenRow(board, col)
            dropPiece(board, row, col, AI_PIECE)

            if gameOverCheck(board, AI_PIECE):
                label = myfont.render("AI wins!! :[", 1, colors["MISTYROSE"])
                screen.blit(label, (40, 10))
                gameOver = True

            drawBoard(board)

            # Switching turns between players
            turn ^= 1

    # Wait after game is over 
    if gameOver:
        pygame.time.wait(3000)
