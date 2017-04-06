# Sprites
import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((30, 40))
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10

    def move_with_mouse(self):
        self.mouse_location = pygame.mouse.get_pos()
        self.rect.centerx = self.mouse_location[0]
        self.rect.centery = self.mouse_location[1]

    def update(self):
        pass
