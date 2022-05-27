import pygame
from path import Tile, Checkpoint, Startpoint
from config import *

class Level:
    def __init__(self):
        self.display = pygame.display.get_surface()
        self.path = pygame.sprite.Group()
        self.checkpoint = pygame.sprite.Group()
        self.startpoint = pygame.sprite.Group()
        self.levels = 1
        self.map = MAP[self.levels - 1]
        self.create_map()
        self.tutorial = True
        self.onpath = True
        self.finished = False
        self.started = False
        self.game_over = False
        
        self.font = pygame.font.SysFont('Helvetica', FONT_SIZE)
        self.tutorial_text = self.font.render('Drag the Mouse to the Yellow Area To start playing', True, (240, 240, 240))
        self.tutorial_text_rect = self.tutorial_text.get_rect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
        
        self.game_over_text = self.font.render('Game over! Drag the Mouse to the Yellow Area to start playing again', True, (240, 240, 240))
        self.game_over_text_rect = self.game_over_text.get_rect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
        
    def create_map(self):
        for row_index, row in enumerate(self.map):
            for col_index, col in enumerate(row):
                x = col_index * TILE_DIMENSION
                y = row_index * TILE_DIMENSION
                if col == 1:
                    Tile((x, y), [self.path])
                elif col == 2:
                    Checkpoint((x, y), [self.checkpoint, self.path])
                elif col == 3:
                    Startpoint((x, y), [self.startpoint, self.path])

    def player_out(self):
        if self.started and not self.onpath:
            self.started = False
            self.onpath = True

    def mouse_collide(self):
        if self.started:
            self.onpath = False
            self.finished = False
            self.tutorial = False
            for path in self.path:
                if path.rect.collidepoint(pygame.mouse.get_pos()):
                    self.onpath = True
            for checkpoint in self.checkpoint:
                if checkpoint.rect.collidepoint(pygame.mouse.get_pos()):
                    self.finished = True
        for startpoint in self.startpoint:
            if startpoint.rect.collidepoint(pygame.mouse.get_pos()):
                self.started = True
                self.game_over = False   
    
    def level_finish(self):
        if self.finished:
            self.started = False
            self.onpath = True
            self.finished = False
            self.levels += 1
            if self.levels - 1 >= len(MAP):
                self.game_over = True
                self.levels = 1
            self.map = MAP[self.levels - 1]
            self.path.empty()
            self.checkpoint.empty()
            self.startpoint.empty()
            self.create_map()
                
    def run(self):
        if self.tutorial:
            self.display.blit(self.tutorial_text, self.tutorial_text_rect)
        if self.game_over:
            self.display.blit(self.game_over_text, self.game_over_text_rect)
            
        self.mouse_collide()
        self.level_finish()
        self.player_out()
        if self.started:
            self.checkpoint.draw(self.display)
            self.path.draw(self.display)
            
        self.startpoint.draw(self.display)
        
        self.path.update()
        self.checkpoint.update()
        self.startpoint.update()
        