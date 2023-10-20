#!/usr/bin/env python3
import pygame
import os


class Button:
    def __init__(self, color, x, y, width,
                 height, text='', font_size=35,
                 text_color=(0,0,0), radius=50):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.font_size = font_size
        self.text_color = text_color
        self.radius = radius

        try:
            script_dir = os.path.dirname(os.path.realpath(__file__))
            fonts_path = os.path.join(script_dir, '../assets/fonts')
            self.font = pygame.font.Font(f'{fonts_path}/Gabarito-SemiBold.ttf', self.font_size)
        except pygame.error:
            print("Failed to find font, using comicsans.")
            self.font = pygame.font.SysFont('comicsans', self.font_size)

    def draw(self, win, outline_color=None, outline_width=3):
        self._draw_button(win)
        if outline_color:
            self._draw_outline(win, outline_color, outline_width)
        if self.text:
            self._draw_text(win)

    def _draw_outline(self, win, color, width):
        pygame.draw.rect(win, color, (self.x-2, self.y-2, self.width+4, self.height+4), width, self.radius)

    def _draw_button(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0, self.radius)

    def _draw_text(self, win):
        text = self.font.render(self.text, 1, self.text_color)
        win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def is_over(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if self.x < pos[0] < self.x + self.width and self.y < pos[1] < self.y + self.height:
            return True

pygame.mixer.init()

script_dir = os.path.dirname(os.path.realpath(__file__))
sound_path = os.path.join(script_dir, '../assets/sound')

ai_move_sound = pygame.mixer.Sound(os.path.join(sound_path, 'AI_sound.ogg'))
self_move_sound = pygame.mixer.Sound(os.path.join(sound_path,'self_sound.ogg'))
ai_wins_sound = pygame.mixer.Sound(os.path.join(sound_path,"looser.ogg"))
player_wins_sound = pygame.mixer.Sound(os.path.join(sound_path,"winner.ogg"))
