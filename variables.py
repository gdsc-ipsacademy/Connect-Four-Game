# Connect four board has dimentions 6*7
ROW_COUNT = 6
COLUMN_COUNT = 7

# Global variables for pygame
SQUARESIZE = 100

width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT + 1) * SQUARESIZE
size = (width, height)

RADIUS = int(SQUARESIZE / 2 - 5)

# Dictionary for colors
colors = {
    "VERDIGRIS": (23, 190, 187),
    "CHARCOAL": (47, 72, 88),
    "CERISE": (236, 64, 103),
    "ICTERINE": (248, 242, 114),
    "MISTYROSE": (250, 216, 214),
}

# Values for player and AI turns
PLAYER = 0
AI = 1

# Values for player and AI piece
PLAYER_PIECE = 1
AI_PIECE = 2

WINDOW_LENGTH = 4
EMPTY = 0
