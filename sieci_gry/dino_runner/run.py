import pygame, time,sys,random
pygame.init()
from pygame.locals import *

screen = pygame.display.set_mode((1000,800),RESIZABLE)
clock = pygame.time.Clock()
background = pygame.image.load('bg.png')
backgroundRect = background.get_rect()
move_bg = 1150
class Player:
    def __init__(self):
        pass

    def draw_player(self):
        player_frames = [pygame.image.load('dino/dino1.png'), pygame.image.load('dino/dino2.png'), pygame.image.load('dino/dino3.png')]
        for i in player_frames:
            player = i
            playerRect = player.get_rect()
            playerRect.center = ((48,482))
            screen.blit(player, playerRect)

class Obstacles:
    pass

player = Player()

while True:
    move_bg -= 5
    if move_bg < 6:
        move_bg = 1200
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    backgroundRect.center = (move_bg, 550)
    screen.fill('white')
    screen.blit(background, backgroundRect)
    player.draw_player()
    pygame.display.flip()
    clock.tick(60)

