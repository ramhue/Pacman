import pygame
import sys
from pygame.sprite import Sprite

from blocks import Blocks
from dot import Dot
from Shield import Shield
from Ghost import Ghost
from Bullet import Bullet
from PacSprite import PacSprite

def mainMenu (screen):
    title_Image = pygame.image.load_basic("Images/Pac-Man-Ghosts.bmp")
    text_color = (250, 250, 250)
    font = pygame.sysfont.SysFont(None, 40)
    start_text = font.render("Press any key to Start!", True, text_color)

    while True:
        screen.fill((0, 0, 0))
        screen.blit(title_Image, (0, 0))
        screen.blit(start_text, (250, 500))
        pygame.display.flip()
        if check_menu_events() == False:
            break

def makeMap(screen, maze, MyShield):

    line = ""
    allLines = []
    deltaX = 0
    deltaY =0
    file = open("pacmanportalmaze.txt", "r")

    if file.mode == 'r':
        contents = file.read()
    for chars in contents:
        if chars != '\n':
            line += chars
        else:
            allLines.append(line)
            line = ""
    for line in allLines:
        for char in line:
            if char == 'X':
                newBlock = Blocks(screen)
                newBlock.rect.x, newBlock.rect.y = deltaX, deltaY
                maze.add(newBlock)
            elif char == 'o':
                newShield = Shield(screen)
                newShield.rect.x, newShield.rect.y = deltaX, (deltaY )
                MyShield.add(newShield)

            deltaX += 13
        deltaX = 0
        deltaY += 13
def makeFood(screen, Alldots):

    line = ""
    allLines = []
    deltaX = 0
    deltaY =0
    file = open("pacmanportalmaze.txt", "r")
    if file.mode == 'r':
        contents = file.read()
    for chars in contents:
        if chars != '\n':
            line += chars
        else:
            allLines.append(line)
            line = ""
    for line in allLines:
        for char in line:
            if char == 'd':
                newDot = Dot(screen)
                newDot.rect.x, newDot.rect.y = deltaX, deltaY
                Alldots.add(newDot)

            deltaX += 13
        deltaX = 0
        deltaY += 13

def check_events(screen, pac_sprite, Bullets, portal):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_KEYDOWN_events(event, pac_sprite, screen, Bullets, portal)
        elif event.type == pygame.KEYUP:
            check_KEYUP_events(event, pac_sprite)

def check_menu_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            return False


def create_Ghost(screen, group, list_of_names):
    deltaX = 0
    for path_name in list_of_names:
        newGhost = Ghost(screen, path_name)
        newGhost.rect.x += deltaX

        group.add(newGhost)
        deltaX += 30
def check_KEYDOWN_events(event, pac_sprite, screen, Bullets, portal):
    if event.key == pygame.K_UP:
        pac_sprite.moving_up = True
        pac_sprite.idle = False
    elif event.key == pygame.K_DOWN:
        pac_sprite.moving_down = True
        pac_sprite.idle = False
    elif event.key == pygame.K_LEFT:
        pac_sprite.moving_left = True
        pac_sprite.idle = False
    elif event.key == pygame.K_RIGHT:
        pac_sprite.moving_right = True
        pac_sprite.idle = False
    elif event.key == pygame.K_SPACE:
        fire_bullet(screen, pac_sprite, Bullets, portal)
    elif event.key == pygame.K_q:
        sys.exit()

def check_KEYUP_events(event, pac_sprite):
    if event.key == pygame.K_UP:
        pac_sprite.moving_up = False
        pac_sprite.idle = True
    elif event.key == pygame.K_DOWN:
        pac_sprite.moving_down = False
        pac_sprite.idle = True
    elif event.key == pygame.K_LEFT:
        pac_sprite.moving_left = False
        pac_sprite.idle = True
    elif event.key == pygame.K_RIGHT:
        pac_sprite.moving_right = False
        pac_sprite.idle = True

def check_pacman_direction(Pacmand, block):

    up_dir = False
    down_dir = False
    left_dir = False
    right_dir = False

def fire_bullet(screen, pacman, bullets, portal):
    # Create a new bullet and add it to the bullets group.
    if len(bullets) < 1:
        new_bullet = Bullet(screen, pacman, portal)
        bullets.add(new_bullet)


def collision_check(pacman, blocks, dots, ghosts, scoreboard, myShield, bullets, portal):
    for block in blocks:
        if pygame.sprite.collide_rect(pacman, block):
            if pacman.direction == "Left":
                pacman.rect.x += 1
            elif pacman.direction == "Right":
                pacman.rect.x -= 1
            if pacman.direction == "Up":
                pacman.rect.y += 1
            elif pacman.direction == "Down":
                pacman.rect.y -= 1
    for bullet in bullets:
        for block in blocks:
            if pygame.sprite.collide_rect(bullet, block):
                if portal.Portal_color == "Blue":
                    portal.Portal_color = "Orange"
                elif portal.Portal_color == "Orange":
                    portal.Portal_color = "Blue"
                bullet.remove(bullets)
    for dot in dots:
        if pygame.sprite.collide_rect(pacman, dot):
            dot.remove(dots)
            scoreboard.points += 10
    for ghost in ghosts:
        if pygame.sprite.collide_rect(pacman, ghost):
            pacman.reset()