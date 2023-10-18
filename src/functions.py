import numpy as np
import itertools
import pygame
import random
import math


from pygame import gfxdraw
from variables import ROW_COUNT, COLUMN_COUNT, size, colors, SQUARESIZE, RADIUS, height, width, PLAYER_PIECE, AI_PIECE

# Creating board
def create_board():
    return np.zeros((ROW_COUNT,COLUMN_COUNT))

# Creating the board
board = create_board()

# Checking if the top row of a selected column is empty or not
def is_valid_location(board, col):
    return board[ROW_COUNT-1][col] == 0

# Getting the lowest empty slot of the selected column
def get_next_open_row(board, col):
    for slot in range(ROW_COUNT):
        if board[slot][col] == 0:
            return slot

# Dropping the piece in the board
def drop_piece(board, row, col, piece):
    board[row][col] = piece

# Checking if the game is over
def game_over_check(board, piece):

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
def draw_board(board):
    for c, r in itertools.product(range(COLUMN_COUNT), range(ROW_COUNT)):
        rect_pos = (c * SQUARESIZE, r * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE)
        pygame.gfxdraw.box(screen, rect_pos, colors["BLUE"])
        x, y = (int(c * SQUARESIZE + SQUARESIZE / 2), int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2))

        # Gradient shading for holes
        for offset in range(RADIUS):
            pygame.gfxdraw.filled_circle(screen, x, y, RADIUS - offset, (40 + offset, 40 + offset, 40 + offset))

    for c, r in itertools.product(range(COLUMN_COUNT), range(ROW_COUNT)):
        x, y = (int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2))
        color = None
        if board[r][c] == PLAYER_PIECE:
            color = colors["GREEN"]
        elif board[r][c] == AI_PIECE:
            color = colors["RED"]

        if color:
            pygame.gfxdraw.filled_circle(screen, x, y, RADIUS, color)
            # Reflection highlight for discs
            pygame.gfxdraw.filled_circle(screen, x - RADIUS // 3, y - RADIUS // 3, RADIUS // 3, (255, 255, 255, 100))

        pygame.gfxdraw.aacircle(screen, x, y, RADIUS, colors["DARKGREY"])

    pygame.display.update()


def get_valid_locations(board):
    return [c for c in range(COLUMN_COUNT) if is_valid_location(board, c)]

def draw_dotted_circle(surface, x, y, radius, color, dot_length=4, gap_length=4, line_width=3):
    num_dots = int(2 * math.pi * radius / (dot_length + gap_length))
    angle_between_dots = 2 * math.pi / num_dots

    for i in range(num_dots):
        start_angle = i * angle_between_dots
        end_angle = start_angle + dot_length / radius

        start_x = x + radius * math.cos(start_angle)
        start_y = y + radius * math.sin(start_angle)

        end_x = x + radius * math.cos(end_angle)
        end_y = y + radius * math.sin(end_angle)

        pygame.draw.line(surface, color, (start_x, start_y), (end_x, end_y), line_width)
