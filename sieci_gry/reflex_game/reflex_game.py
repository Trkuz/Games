import pygame, sys
import random
import time
pygame.init()
pygame.font.init()
pygame.mixer.init()

#music
pygame.mixer.music.load("muzyka1.mp3")
pygame.mixer.music.set_volume(0.7)
pygame.mixer.music.play(loops=True)

#grit and screen init
cell_size = 20
screen_size = (cell_size*50, cell_size*40)
screen = pygame.display.set_mode((screen_size))

clock = pygame.time.Clock()
#drawing point
point = pygame.Rect(random.randint(1, 49) * cell_size, random.randint(1, 39) * cell_size, cell_size, cell_size)
touching = True

points_gained = 0


counter_start = time.time()
while True:
    counter = time.time()
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if mouse_x in range(point.x, point.x + 20) and mouse_y in range(point.y, point.y + 20):
        touching = True
    else:
        touching = False

    time_left = round(counter - counter_start,2)

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if touching is True:
                point = pygame.Rect(random.randint(1, 49) * cell_size, random.randint(1, 39) * cell_size, cell_size,cell_size)
                points_gained += 1


    if int(time_left) == 60:
        print(points_gained)
        sys.exit()

    screen.fill('black')
    pygame.draw.rect(screen, 'red', point)
    pygame.display.update()

    clock.tick(60)