import pygame
import pygame.sysfont
from pygame.sprite import Sprite


class Scoreboard:
    def __init__(self):
        self.lives_sprites = pygame.image.load_basic("Images/Pacman.bmp")
        self.lives_sprites = pygame.transform.scale(self.lives_sprites, (23, 23))
        self.points = 0
        self.text_color = (250,250,250)
        self.font = pygame.sysfont.SysFont(None, 40)
        self.lives_text = self.font.render("Lives:", True, self.text_color)


    def blit_text(self, pacman, screen):

        delta_x = 30
        i = 1
        j = pacman.num_of_lives +1
        screen.blit(self.lives_text, (615, 10))
        for x in range(1, j):
            screen.blit(self.lives_sprites, (670 + delta_x * x, 10))
        points = self.font.render("Points: " + str(self.points), True, self.text_color)
        screen.blit(points, (615, 45))
