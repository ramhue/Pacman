import pygame
from pygame.sprite import Sprite

class Shield(Sprite):
    def __init__(self, screen):
        super(Shield, self).__init__()
        self.screen = screen
        self.color = (255, 0, 0)
        self.rect = pygame.Rect(50, 50, 8, 8)

    def blitme(self):
        pygame.draw.rect(self.screen, self.color, self.rect)