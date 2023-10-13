import pygame
import sys
import math
import random

from variables import ROW_COUNT, COLUMN_COUNT, SQUARESIZE, size, RADIUS, colors, height, width, PLAYER, AI, \
    PLAYER_PIECE, AI_PIECE
from functions import create_board, is_valid_location, get_next_open_row, drop_piece, game_over_check, draw_board, \
    board, screen
from score_ai import pick_best_move
from minmax_ai import minimax
from ui_components import Button 
from ui_components import ai_move, self_move, ai_wins_sound, player_wins_sound 

class ConnectFour:
    def __init__(self):
        pygame.init()
        pygame.mixer.init() #added to initialize sound 
        self.game_over = False
        self.turn = random.randint(PLAYER, AI)
        self.board = create_board()
        self.myfont = pygame.font.SysFont("monospace", 80)
        button_width = 250
        button_height = 100
        padding = 20
        restart_button_y = height // 2
        quit_button_y = restart_button_y + button_height + padding
        center_x = width // 2 - button_width // 2
        self.quit_button = Button((255, 0, 0), center_x, quit_button_y, button_width, button_height, 'Quit')
        self.restart_button = Button((0, 255, 0), center_x, restart_button_y, button_width, button_height, 'Restart')
        pygame.display.set_caption("Connect Four")
        draw_board(self.board)
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
            if is_valid_location(self.board, col):
                self._extracted_from_ai_move_7(col, PLAYER_PIECE, "You win!! ^_^")
                self.turn ^= 1
                self_move.play()
                self.render_thinking("Thinking...")
                draw_board(self.board)
        if self.game_over:
            if self.quit_button.is_over((posx, event.pos[1])):
                sys.exit()
            elif self.restart_button.is_over((posx, event.pos[1])):
                self.__init__()

    def ai_move(self):
        col, minimax_score = minimax(self.board, 6, -math.inf, math.inf, True)
        if is_valid_location(self.board, col):
            self.clear_label()
            self._extracted_from_ai_move_7(col, AI_PIECE, "AI wins!! :[")
            draw_board(self.board)
            self.turn ^= 1
            ai_move.play()


    # TODO Rename this here and in `handle_mouse_button_down` and `ai_move`
    def _extracted_from_ai_move_7(self, col, arg1, arg2):
        row = get_next_open_row(self.board, col)
        drop_piece(self.board, row, col, arg1)
        if game_over_check(self.board, arg1):
            self.display_winner(arg2)

    def display_winner(self, message):
        if message == "AI wins!! :[":
            ai_wins_sound.play()
        elif message == "You win!! ^_^":
            player_wins_sound.play()
        label = self.myfont.render(message, 1, colors["MISTYROSE"])
        screen.blit(label, (40, 10))
        self.game_over = True

    def handle_game_over(self):
        while self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    posx, posy = event.pos
                    if self.quit_button.is_over((posx, posy)):
                        sys.exit()
                    elif self.restart_button.is_over((posx, posy)):
                        self.__init__()
                        self.game_start()  # You need to call game_start again to restart the game loop

            self.quit_button.draw(screen, (0, 0, 0))
            self.restart_button.draw(screen, (0, 0, 0))
            pygame.display.update()

    def game_start(self):
        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEMOTION:
                    self.handle_mouse_motion(event)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_mouse_button_down(event)
            if self.turn == AI and not self.game_over:
                self.ai_move()
            if self.game_over:
                self.handle_game_over()
    
    def clear_label(self):
        pygame.draw.rect(screen, colors["CHARCOAL"], (0, 0, width, SQUARESIZE))


    def render_thinking(self, text):
        self.clear_label()
        label = pygame.font.SysFont("monospace", 60).render(text, 1, colors["MISTYROSE"])
        screen.blit(label, (40, 10))

if __name__ == "__main__":
    game = ConnectFour()
    game.game_start()


# TODO Complete the game and make a downloadable file for the game. Use pybag to take the game to the web.