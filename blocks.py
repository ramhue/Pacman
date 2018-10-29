import pygame
from pygame.sprite import Sprite

class Blocks(Sprite):
    def __init__(self, screen):
        super(Blocks, self).__init__()
        self.screen = screen
        self.color = (0, 51, 255)
        self.rect = pygame.Rect(50, 50, 13, 13)


    def drawBlocks(self):
        pygame.draw.rect(self.screen, self.color, self.rect)