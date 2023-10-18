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
    "GREEN": (51, 255, 51),
    "LIGHT_GREEN": (153, 255, 51),
    "YELLOW": (255, 255, 51),
    "ORANGE": (255, 153, 51),
    "RED": (255, 51, 51),
    "BLACK": (0, 0, 0),
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