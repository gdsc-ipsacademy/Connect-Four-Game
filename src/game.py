import pygame
import sys
import math
import random
import time

from enum import Enum
from variables import ROW_COUNT, COLUMN_COUNT, SQUARESIZE, size, RADIUS, colors, height, width, PLAYER, AI, \
    PLAYER_PIECE, AI_PIECE
from functions import createBoard, isValidLocation, getNextOpenRow, dropPiece, gameOverCheck, drawBoard, \
    board, screen
from scoreAI import pickBestMove
from minmaxAI import minimax
from ui_components import Button

class Difficulty(Enum):
    EASY = 1
    INTERMEDIATE = 2
    HARD = 3
    IMPOSSIBLE = 4
    GODMODE = 5

class ConnectFour:
    def __init__(self):
        pygame.init()
        self.gameOver = False
        self.turn = random.randint(PLAYER, AI)
        self.board = createBoard()
        self.myfont = pygame.font.SysFont("monospace", 80)
        button_width = 250
        button_height = 100
        padding = 20
        restart_button_y = height // 2
        quit_button_y = restart_button_y + button_height + padding
        self.center_x = width // 2 - button_width // 2
        self.quit_button = Button((255, 0, 0), self.center_x, quit_button_y, button_width, button_height, 'Quit')
        self.restart_button = Button((0, 255, 0), self.center_x, restart_button_y, button_width, button_height, 'Restart')
        pygame.display.set_caption("Connect Four")
        self.difficulty = self.choose_difficulty()
        drawBoard(self.board)
        pygame.display.update()

    def handle_mouse_motion(self, event):
        pygame.draw.rect(screen, colors["CHARCOAL"], (0, 0, width, SQUARESIZE))
        posx = event.pos[0]
        if self.turn == PLAYER:
            pygame.draw.circle(screen, colors["CERISE"], (posx, int(SQUARESIZE / 2)), RADIUS)
        pygame.display.update()

    def handle_mouse_button_down(self, event):
        pygame.draw.rect(screen, colors["CHARCOAL"], (0, 0, width, SQUARESIZE))
        posx = event.pos[0]
        if self.turn == PLAYER:
            col = int(math.floor(posx / SQUARESIZE))
            if isValidLocation(self.board, col):
                row = getNextOpenRow(self.board, col)
                dropPiece(self.board, row, col, PLAYER_PIECE)
                if gameOverCheck(self.board, PLAYER_PIECE):
                    self.display_winner("You win!! ^_^")
                self.turn ^= 1
                drawBoard(self.board)
        if self.gameOver:
            if self.quit_button.isOver((posx, event.pos[1])):
                sys.exit()
            elif self.restart_button.isOver((posx, event.pos[1])):
                self.__init__()


    def ai_move(self):
        thinking_time = 1
        if self.difficulty == Difficulty.EASY:
            col = random.randint(0, COLUMN_COUNT-1)
            time.sleep(thinking_time)
        if self.difficulty == Difficulty.INTERMEDIATE:
            col = pickBestMove(self.board,
                         AI_PIECE,
                         directions=tuple(1 if i in random.sample(range(4), 2) else 0 for i in range(4)))
        if self.difficulty == Difficulty.HARD:
            col = pickBestMove(self.board, AI_PIECE)
        if self.difficulty == Difficulty.IMPOSSIBLE:
            col, minimaxScore = minimax(self.board, 6, -math.inf, math.inf, True)
        if self.difficulty == Difficulty.GODMODE:
            col, minimaxScore = minimax(self.board, 7, -math.inf, math.inf, True)
        if isValidLocation(self.board, col):
            row = getNextOpenRow(self.board, col)
            dropPiece(self.board, row, col, AI_PIECE)
            if gameOverCheck(self.board, AI_PIECE):
                self.display_winner("AI wins!! :[")
                self.gameOver = True
            self.turn ^= 1
            drawBoard(self.board)

    def display_winner(self, message):
        label = self.myfont.render(message, 1, colors["MISTYROSE"])
        screen.blit(label, (40, 10))

    def handle_game_over(self):
        self.quit_button.draw(screen, (0, 0, 0))
        self.restart_button.draw(screen, (0, 0, 0))
        pygame.display.update()
        while self.gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    posx, posy = event.pos
                    if self.quit_button.isOver((posx, posy)):
                        sys.exit()
                    elif self.restart_button.isOver((posx, posy)):
                        self.__init__()
                        return self.game_start()


    def choose_difficulty(self):
        print("ENTERING DIFFICULTY CHOICE")
        btn_height = 50
        btn_y = [i * (btn_height + 5) + height/2 for i in range(-3,3)]
        self.easy = Button((0, 255, 0), self.center_x, btn_y[0], 250, btn_height, 'Easy')
        self.intermediate = Button((0, 255, 0), self.center_x, btn_y[1], 250, btn_height, 'Intermediate')
        self.hard = Button((255, 255, 0), self.center_x, btn_y[2], 250, btn_height, 'Hard')
        self.impossible = Button((255, 255, 0), self.center_x, btn_y[3], 250, btn_height, 'Impossible')
        self.godmode = Button((255, 0, 0), self.center_x, btn_y[4], 250, btn_height, 'God Mode')

        screen.fill((0,0,0))
        self.easy.draw(screen, (0, 0, 0))
        self.intermediate.draw(screen, (0, 0, 0))
        self.hard.draw(screen, (0, 0, 0))
        self.impossible.draw(screen, (0, 0, 0))
        self.godmode.draw(screen, (0, 0, 0))
        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    posx, posy = event.pos
                    if self.easy.isOver((posx, posy)):
                        return Difficulty.EASY
                    elif self.intermediate.isOver((posx, posy)):
                        return Difficulty.INTERMEDIATE
                    elif self.hard.isOver((posx, posy)):
                        return Difficulty.HARD
                    elif self.impossible.isOver((posx, posy)):
                        return Difficulty.IMPOSSIBLE
                    elif self.godmode.isOver((posx, posy)):
                        return Difficulty.GODMODE


    def game_start(self):
        while not self.gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEMOTION:
                    self.handle_mouse_motion(event)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_mouse_button_down(event)
            if self.turn == AI and not self.gameOver:
                self.ai_move()
            if self.gameOver:
                self.handle_game_over()

            pygame.display.update()

if __name__ == "__main__":
    game = ConnectFour()
    game.game_start()
