import pygame
import sys
import GameFunc as gf
from pygame.sprite import Group
from PacSprite import PacSprite
from Ghost import Ghost
from Scoreboard import Scoreboard
from Portal import Portal
from pygame.sprite import Sprite
from blocks import Blocks


def run_game():

    pygame.init()
    pygame.display.set_caption("Portal Pacman")

    screen = pygame.display.set_mode((800, 700))
    clock = pygame.time.Clock()
    settings = ["Images/red_ghost.bmp",
                "Images/orange_ghost.bmp",
                "Images/pink_ghost.bmp",
                "Images/cyan_ghost.bmp"]

    maze = Group()
    AllDots = Group()
    myShield = Group()
    ghosts = Group()
    pac = PacSprite(screen)
    score = Scoreboard()
    bullets = Group()
    portal = Portal(screen, pac)


    gf.makeMap(screen, maze, myShield)
    gf.makeFood(screen, AllDots)
    gf.create_Ghost(screen, ghosts, settings)
    red_ghost = Ghost(screen, settings[0])
    orange_ghost = Ghost(screen, settings[1])
    orange_ghost.rect.x += 30
    pink_ghost = Ghost(screen, settings[2])
    pink_ghost.rect.x += 60
    cyan_ghost = Ghost(screen, settings[3])
    cyan_ghost.rect.x += 90

    timer = 0
    gf.mainMenu(screen)
    while True:
        clock.tick(120)

        if not AllDots:
            gf.makeFood(screen, AllDots)
            pac.reset()
        screen.fill((0, 0, 0))
        gf.check_events(screen, pac, bullets, portal)
        pac.update()
        gf.collision_check(pac, maze, AllDots, ghosts, score, myShield, bullets, portal)


        for block in maze:
            block.drawBlocks()
        for dot in AllDots:
            dot.draw_Dots()
        for Shield in myShield:
            Shield.blitme()
        # for ghost in ghosts:
        #   ghost.blitme()

        for bullet in bullets:
            bullet.update()
            bullet.draw_bullet(portal)
        if timer % 10 == 0:
            red_ghost.update()
        else:
            red_ghost.rect = 250, 300
        red_ghost.blitme()
        orange_ghost.blitme()
        pink_ghost.blitme()
        cyan_ghost.blitme()
        pac.blitme()
        score.blit_text(pac, screen)
        pygame.display.flip()
        timer += 1

run_game()
