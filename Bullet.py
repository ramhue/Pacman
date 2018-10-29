import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, screen, pacman, portal):
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 10, 10)
        self.num_of_bullets = 0
        self.blue = (0, 250, 255)
        self.orange = (255, 155, 0)
        self.rect.x = pacman.rect.x
        self.rect.y = pacman.rect.y + 8
        self.pac_direction = pacman.direction

    def draw_bullet (self, portal):
        if portal.Portal_color == "Blue":
            pygame.draw.ellipse(self.screen, self.blue, self.rect)
        elif portal.Portal_color == "Orange":
            pygame.draw.ellipse(self.screen, self.orange, self.rect)

    def update(self):
        if self.pac_direction == "Right":
            self.rect.x += 1
        elif self.pac_direction == "Left":
            self.rect.x -= 1
        elif self.pac_direction == "Up":
            self.rect.y -= 1
        elif self.pac_direction == "Down":
            self.rect.y += 1