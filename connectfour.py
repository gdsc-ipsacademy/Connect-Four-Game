import pygame
import sys
import math
import random
from variables import ROW_COUNT, COLUMN_COUNT, SQUARESIZE, size, RADIUS, colors, height, width, PLAYER, AI
from functions import createBoard, isValidLocation, getNextOpenRow, dropPiece, gameOverCheck, drawBoard, board, screen

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
            pygame.draw.rect(screen, colors["BLACK"], (0, 0, width, SQUARESIZE))
            posx = event.pos[0]
            if turn == PLAYER:
                pygame.draw.circle(screen, colors["RED"], (posx, int(SQUARESIZE/2)), RADIUS)
        
        pygame.display.update()

        # Checking mouse click event
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, colors["BLACK"], (0, 0, width, SQUARESIZE))
            posx = event.pos[0]

            # Ask for player 1 input
            if turn == PLAYER:
                col = int(math.floor(posx/SQUARESIZE))

                if isValidLocation(board, col):
                    row = getNextOpenRow(board, col)
                    dropPiece(board, row, col, 1)

                    if gameOverCheck(board, 1):
                        label = myfont.render("Player 1 wins!!", 1, colors["RED"])
                        screen.blit(label, (40, 10))
                        gameOver = True

                    turn += 1
                    turn %= 2

                    drawBoard(board)


    # Ask for player 2 input
    if turn == AI and not gameOver:

        # Random move selection
        col = random.randint(0, COLUMN_COUNT - 1)

        if isValidLocation(board, col):

            # Adding delay to AI move
            pygame.time.wait(500)

            row = getNextOpenRow(board, col)
            dropPiece(board, row, col, 2)

            if gameOverCheck(board, 2):
                label = myfont.render("Player 1 wins!!", 1, colors["YELLOW"])
                screen.blit(label, (40, 10))
                gameOver = True

            drawBoard(board)

            # Switching turns between players
            turn += 1
            turn %= 2

    # Wait after game is over 
    if gameOver:
        pygame.time.wait(3000)











