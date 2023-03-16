import pygame
import sys,time,random
pygame.init()

grit_size = 20

screen_width = 25
screen_height = 35

screen = pygame.display.set_mode((screen_width*grit_size,screen_height*grit_size))

game_active = True

clock = pygame.time.Clock()

class Nodes:
    def __init__(self):
        pass

    single_node = pygame.Rect(12 * grit_size, 0, grit_size, grit_size)
    node_velocity_x = grit_size
    node_velocity_y = grit_size

    def draw_single(self):
        pygame.draw.rect(screen,(255,0,0) , self.single_node)

    def move_node(self):
        if self.single_node.bottom < screen_height * grit_size:
            self.single_node.y  += self.node_velocity_y

nodes = Nodes()

while game_active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


    screen.fill('black')
    nodes.draw_single()
    nodes.move_node()
    pygame.display.update()
    clock.tick(3)

