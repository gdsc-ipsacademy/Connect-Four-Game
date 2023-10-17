#!/usr/bin/env python3
import pygame
import os

class Button:
    def __init__(self, color, x, y, width,
                 height, text='', font_size=35,
                 text_color=(0,0,0)):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.font_size = font_size
        self.text_color = text_color

        try:
            self.font = pygame.font.Font('../assets/fonts/Monday Ramen.ttf', self.font_size)
        except pygame.error:
            print("Failed to find font, using comicsans.")
            self.font = pygame.font.SysFont('comicsans', self.font_size)

    def draw(self, win, outline_color=None, outline_width=5):
        self._draw_button(win)
        if outline_color:
            self._draw_outline(win, outline_color, outline_width)
        if self.text:
            self._draw_text(win)

    def _draw_outline(self, win, color, width):
        pygame.draw.rect(win, color, (self.x-2, self.y-2, self.width+4, self.height+4), width)

    def _draw_button(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

    def _draw_text(self, win):
        text = self.font.render(self.text, 1, self.text_color)
        win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def is_over(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if self.x < pos[0] < self.x + self.width and self.y < pos[1] < self.y + self.height:
            return True

pygame.mixer.init()

ai_move_sound = pygame.mixer.Sound(os.path.join('src','sound', 'AI_sound.ogg'))
self_move_sound = pygame.mixer.Sound(os.path.join('src','sound','self_sound.ogg'))
ai_wins_sound = pygame.mixer.Sound(os.path.join('src','sound','looser.ogg'))
player_wins_sound = pygame.mixer.Sound(os.path.join('src','sound','winner.ogg'))
