# Connect four board has dimentions 6*7
ROW_COUNT = 6
COLUMN_COUNT = 7

# Global variables for pygame
SQUARESIZE = 100

width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT + 1) * SQUARESIZE

size = (width, height)

RADIUS = int(SQUARESIZE/2 - 5)

# Dictionary for colors
colors = {
"BLUE" : (0, 0, 204),
"BLACK" : (0, 0, 0),
"RED" : (204, 0, 0),
"YELLOW": (204, 204, 0),
}