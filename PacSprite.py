import pygame
import sys
from pygame.sprite import Sprite


class PacSprite(Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.Images = []
        self.image = pygame.image.load_basic("Images/Pacman.bmp")
        self.image2 = pygame.image.load_basic("Images/Pacman2.bmp")
        self.image = pygame.transform.scale(self.image, (25, 25))
        self.image2 = pygame.transform.scale(self.image, (25, 25))

        self.rect = self.image.get_rect()
        self.rect.x = 295
        self.rect.y = 490
        self.currentFrame = 0
        self.direction = "Right"
        self.idle = True
        self.num_of_lives = 3
        # self.rect.centerx = (273, 400)
       # self.rect.bottom = 503


        #movement fo pacman test
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False

    def reset(self):
        self.rect.x = 295
        self.rect.y = 490
        self.direction = "Right"
        self.image = pygame.image.load_basic("Images/Pacman.bmp")
        self.image = pygame.transform.scale(self.image, (23, 23))
        self.num_of_lives -= 1
        self.currentFrame = 0
        if self.num_of_lives == 0:
            sys.exit()


    def update(self):
        if self.moving_up == True:
            if self.direction == "Right":
                self.image = pygame.transform.rotate(self.image, 90)

            elif self.direction == "Left":
                self.image = pygame.transform.rotate(self.image, -90)

            elif self.direction == "Down":
                self.image = pygame.transform.flip(self.image, False, True)
            self.direction = "Up"
            self.rect.y -= 1

        elif self.moving_down == True:
            if self.direction == "Up":
                self.image = pygame.transform.flip(self.image, False, True)
            elif self.direction == "Right":
                self.image = pygame.transform.rotate(self.image, -90)
            elif self.direction == "Left":
                self.image = pygame.transform.rotate(self.image, 90)
            self.direction = "Down"
            self.rect.y += 1
        elif self.moving_left == True:
            if self.direction == "Right":
                self.image = pygame.transform.flip(self.image, True, False)
            elif self.direction == "Up":
                self.image = pygame.transform.rotate(self.image, 90)
            elif self.direction == "Down":
                self.image = pygame.transform.rotate(self.image, -90)
            self.rect.x -= 1
            self.direction = "Left"
        elif self.moving_right == True:
            if self.direction == "Left":
                self.image = pygame.transform.flip(self.image, True, False)
            elif self.direction == "Up":
                self.image = pygame.transform.rotate(self.image, -90)
            elif self.direction == "Down":
                self.image = pygame.transform.rotate(self.image, 90)
            self.rect.x += 1
            self.direction = "Right"


    def blitme(self):
            self.screen.blit(self.image, self.rect)
