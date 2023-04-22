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
ptero_timer = pygame.USEREVENT + 1
pygame.time.set_timer(ptero_timer, random.randint(2000,5000))

class Player:

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
    def spawn_ptero(self):
        height = [ 400,468, 500]
        ptero_y = random.choice(height)
        ptero_x = 1200
        ptero_frames = [pygame.transform.scale2x(pygame.image.load('ptero/ptero1.png').convert_alpha()),pygame.transform.scale2x(pygame.image.load('ptero/ptero2.png').convert_alpha())]
        global ptero_surf
        ptero_surf = ptero_frames[int(crouch_index)]
        global ptero_surf_rect
        ptero_surf_rect = ptero_surf.get_rect(bottomright=(ptero_x, ptero_y))

    def move_obstacles(self, obstacle_list):
        if obstacle_list:
            for element in obstacle_list:
                element.x -= 7
                screen.blit(ptero_surf, element)

            obstacle_list = [element for element in obstacle_list if element.x > -50]
            return obstacle_list
        else:
            return []


    def draw_cactus(self):
        pass

    def collide(self):
        pass



player = Player()
obstacles = Obstacles()
global player_index
global crouch_index
player_index = 0
crouch_index = 0
gravity = 1
obstacle_list = []
obstacle_list = list(obstacle_list)

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

    obstacles.spawn_ptero()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == ptero_timer:
            obstacle_list.append(ptero_surf_rect)
            print(obstacle_list)



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
    obstacle_list = obstacles.move_obstacles(obstacle_list)
    if pygame.key.get_pressed()[K_DOWN]:
        player.draw_player_crouch()
    else:
        player.draw_player()


    pygame.display.flip()
    clock.tick(60)

