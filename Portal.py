import pygame
from pygame.sprite import Sprite

class Portal(Sprite):
    def __init__(self, screen, pacman):
        super().__init__()
        self.Portal_color = "Blue"

        self.Blue_image = pygame.image.load_basic("Images/blue_portal.bmp")
        self.Blue_image = pygame.transform.scale(self.Blue_image, (23, 23))

        self.orange_image = pygame.image.load_basic("Images/orange_portal.bmp")
        self.orange_image = pygame.transform.scale(self.orange_image, (23, 23))

        self.screen = screen

    def blitme(self, x, y):
        if self.Portal_color == "Blue":
            self.screen.blit(self.Blue_image, (x, y))
        if self.Portal_color == "Orange":
            self.screen.blit(self.orange_image, (x, y))


