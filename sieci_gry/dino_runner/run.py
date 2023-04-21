import pygame, time,sys,random
pygame.init()
from pygame.locals import *

screen = pygame.display.set_mode((1000,800),RESIZABLE)
clock = pygame.time.Clock()
background = pygame.image.load('bg.png')
backgroundRect = background.get_rect()
move_bg = 1150
player_pos_x = 48
player_pos_y = 483

class Player:
    def __init__(self):
        pass

    def draw_player(self):
        player_frames = [pygame.image.load('dino/dino1.png').convert_alpha(), pygame.image.load('dino/dino2.png').convert_alpha(), pygame.image.load('dino/dino3.png').convert_alpha()]
        player_surf = player_frames[int(player_index)]
        player_surf_rect = player_surf.get_rect()
        player_surf_rect.center = ((player_pos_x,player_pos_y))
        screen.blit(player_surf,player_surf_rect)

    def draw_player_crouch(self):
        player_frames = [pygame.image.load('dino/dinoc1.png').convert_alpha(), pygame.image.load('dino/dinoc2.png').convert_alpha()]
        player_surf = player_frames[int(crouch_index)]
        player_surf_rect = player_surf.get_rect()
        player_surf_rect.center = ((player_pos_x,player_pos_y+13))
        screen.blit(player_surf,player_surf_rect)


class Obstacles:
    pass

player = Player()
global player_index
global crouch_index
player_index = 0
crouch_index = 0
gravity = 1

while True:
    player_index += 0.1
    crouch_index += 0.1
    gravity += 1
    player_pos_y += gravity


    if player_index > 3:
        player_index = 0

    if crouch_index > 2:
        crouch_index = 0

    move_bg -= 5
    if move_bg < 6:
        move_bg = 1200

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


    if player_pos_y >= 483:
        player_pos_y = 483

    if player_pos_y == 483:
        if pygame.key.get_pressed()[K_SPACE]:
            gravity = -20
        elif pygame.key.get_pressed()[K_UP]:
            gravity = -20

    backgroundRect.center = (move_bg, 550)
    screen.fill('white')
    screen.blit(background, backgroundRect)
    if pygame.key.get_pressed()[K_DOWN]:
        print('dowsn')
        player.draw_player_crouch()
    else:
        player.draw_player()
    pygame.display.flip()
    clock.tick(60)

