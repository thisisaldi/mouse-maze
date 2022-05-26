import pygame
from config import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos: tuple, groups):
        super().__init__(groups)
        self.image = pygame.image.load('assets/tile.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, TILE_SIZE)
        self.rect = self.image.get_rect(topleft = pos)
          
class Checkpoint(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.image = pygame.image.load('assets/tile.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, TILE_SIZE)
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft = pos)
     
class Startpoint(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.image = pygame.image.load('assets/tile.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, TILE_SIZE)
        self.image.fill('yellow')
        self.rect = self.image.get_rect(topleft = pos)
        