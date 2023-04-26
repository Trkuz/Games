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
cactus_timer = pygame.USEREVENT + 2
pygame.time.set_timer(cactus_timer, random.randint(1500,3000))
pygame.time.set_timer(ptero_timer, random.randint(4000,5000))

class Player:

    def draw_player(self):
        player_frames = [pygame.image.load('dino/dino1.png').convert_alpha(),
                         pygame.image.load('dino/dino2.png').convert_alpha(),
                         pygame.image.load('dino/dino3.png').convert_alpha()]
        player_surf = player_frames[int(player_index)]
        player_surf_rect = player_surf.get_rect()
        player_surf_rect.center = ((player_pos_x,player_pos_y))
        screen.blit(player_surf,player_surf_rect)

        return player_surf_rect

    def draw_player_crouch(self):
        player_frames = [pygame.image.load('dino/dinoc1.png').convert_alpha(),
                         pygame.image.load('dino/dinoc2.png').convert_alpha()]
        player_surf = player_frames[int(crouch_index)]
        player_surf_rect = player_surf.get_rect()
        player_surf_rect.center = ((player_pos_x,player_pos_y+13))
        screen.blit(player_surf,player_surf_rect)

        return player_surf_rect

class Obstacles:
    def spawn_ptero(self):
        height = [ 400,468, 500]
        ptero_y = random.choice(height)
        ptero_x = 1200
        ptero_frames = [pygame.transform.scale2x(pygame.image.load('ptero/ptero1.png').convert_alpha()),
                        pygame.transform.scale2x(pygame.image.load('ptero/ptero2.png').convert_alpha())]
        global ptero_surf
        ptero_surf = ptero_frames[int(crouch_index)]
        global ptero_surf_rect
        ptero_surf_rect = ptero_surf.get_rect(bottomright=(ptero_x, ptero_y))

    def spawn_cactus(self):
        cactus_y = 540
        cactus_x = 1200
        cactus_surf = random.choice([pygame.transform.scale(pygame.image.load('cactus/cactus1.png').convert_alpha(),(40,84)),
                                     pygame.transform.scale(pygame.image.load('cactus/cactus2.png').convert_alpha(),(80,84)),
                                     pygame.transform.scale(pygame.image.load('cactus/cactus3.png').convert_alpha(),(120,84))])

        cactus_surf_rect = cactus_surf.get_rect(bottomright = (cactus_x,cactus_y))

        return cactus_surf, cactus_surf_rect


    def move_obstacles_ptero(self, obstacle_list, rect1):
        if obstacle_list:
            for element in obstacle_list:
                element.x -= 7
                screen.blit(ptero_surf, element)
                if element.colliderect(rect1):
                    sys.exit()

            obstacle_list = [element for element in obstacle_list if element.x > -100]
            return obstacle_list
        else:
            return []

    def move_obstalces_cactus(self,obstacle_list, rect1):
        if obstacle_list:
            for (x,y) in obstacle_list:
                y.x -= 6
                screen.blit(x, y)
                if y.colliderect(rect1):
                    sys.exit()

            obstacle_list = [(x,y) for (x,y) in obstacle_list if y.right > -100]
            return obstacle_list
        else:
            return []

player = Player()
obstacles = Obstacles()
global player_index
global crouch_index
player_index = 0
crouch_index = 0
gravity = 1
obstacle_list_ptero = []
obstacle_list_cactus = []

while True:
    player_index += 0.1
    crouch_index += 0.1
    gravity += 1
    player_pos_y += gravity

    if player_index > 3:
        player_index = 0

    if crouch_index > 2:
        crouch_index = 0

    move_bg -= 6
    if move_bg < 7:
        move_bg = 1200

    obstacles.spawn_ptero()
    #obstacles.collide()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == ptero_timer:
            obstacle_list_ptero.append(ptero_surf_rect)
        if event.type == cactus_timer:
            x, y = obstacles.spawn_cactus()
            obstacle_list_cactus.append((x,y))

    if player_pos_y >= 483:
        player_pos_y = 483

    if player_pos_y == 483:
        if pygame.key.get_pressed()[K_SPACE]:
            gravity = -25
        elif pygame.key.get_pressed()[K_UP]:
            gravity = -20

    backgroundRect.center = (move_bg, 550)
    screen.fill('white')
    screen.blit(background, backgroundRect)

    if pygame.key.get_pressed()[K_DOWN]:
        rect1 = player.draw_player_crouch()
    else:
        rect1 = player.draw_player()

    obstacle_list_ptero = obstacles.move_obstacles_ptero(obstacle_list_ptero, rect1)
    obstacle_list_cactus = obstacles.move_obstalces_cactus(obstacle_list_cactus, rect1)

    pygame.display.flip()
    clock.tick(60)

