import sys
from level import Level
from config import *

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Mouse Maze')
        self.window = pygame.display.set_mode(WINDOW_SIZE)
        self.clock = pygame.time.Clock()
        self.level = Level()
        
        self.icon = pygame.image.load('assets/icon.png')
        self.icon = pygame.transform.scale(self.icon, (32, 32))
        pygame.display.set_icon(self.icon)
        
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            self.window.fill('black')
            self.level.run()
            pygame.display.update()
            
            