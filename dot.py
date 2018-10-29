import pygame
from pygame.sprite import Sprite

class Dot(Sprite):
    def __init__(self, screen):
        super(Dot, self).__init__()
        self.screen = screen
        self.color = (255, 255, 255)
        self.rect = pygame.Rect(50, 50, 10, 10)
    def draw_Dots(self):
        pygame.draw.ellipse(self.screen, self.color, self.rect)
