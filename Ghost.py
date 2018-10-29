import pygame
from pygame.sprite import Sprite

class Ghost(Sprite):
    def __init__(self, screen, color):
        super(Ghost, self).__init__()
        self.screen = screen
        self.image = pygame.image.load_basic(color)
        self.image = pygame.transform.scale(self.image, (25, 25))
        self.rect = self.image.get_rect()
        self.rect.x = 250
        self.rect.y = 300
        #self.center = (254, 300)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.rect = 250, 301