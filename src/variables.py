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
    "DARKGREY": (5, 5, 5),
    "GREEN": (154, 217, 61),
    "YELLOW": (242, 191, 39),
    "RED": (242, 48, 5),
    "GREY": (42, 44, 43),
    "BLUE": (61, 104, 217)
}

# Values for player and AI turns
PLAYER = 0
AI = 1

# Values for player and AI piece
PLAYER_PIECE = 1
AI_PIECE = 2

WINDOW_LENGTH = 4
EMPTY = 0

# Time for AI to wait before moving
thinking_time = 0

# Height of buttons
level_button_height = 60
level_button_width = 250
game_end_button_width = 250
game_end_button_height = 100
