import pygame, sys
import random
import time
pygame.init()
pygame.font.init()
pygame.mixer.init()

game_active = True

pygame.display.set_caption("Reflex Game")

#music
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.set_volume(0.7)
pygame.mixer.music.play(loops=True)

points_gained = 0


font = pygame.font.Font("font.ttf", 80)
text = font.render(str(points_gained), False, (255,255,255))
textRect = text.get_rect()
textRect.center = (500, 50)


cell_size = 20
screen_size = (cell_size*50, cell_size*40)
screen = pygame.display.set_mode((screen_size))

clock = pygame.time.Clock()

point = pygame.Rect(random.randint(1, 49) * cell_size, random.randint(1, 39) * cell_size, cell_size, cell_size)
touching = True

counter_start = time.time()
while True:
    if game_active:

        counter = time.time()
        time_left = round(counter - counter_start, 2)

        if int(time_left) == 10:
            game_active = False
            print(counter_start, "----------", counter)

        mouse_x, mouse_y = pygame.mouse.get_pos()
        if mouse_x in range(point.x, point.x + 20) and mouse_y in range(point.y, point.y + 20):
            touching = True
        else:
            touching = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if touching:
                    point = pygame.Rect(random.randint(1, 49) * cell_size, random.randint(1, 39) * cell_size, cell_size,cell_size)
                    points_gained += 1
                    text = font.render(str(points_gained), True, (255, 255, 255))
                    textRect = text.get_rect()
                    textRect.center = (500, 50)

        screen.fill('black')
        screen.blit(text, textRect)
        point_surface = pygame.draw.rect(screen, 'red', point)
        pygame.display.update()


    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                game_active = True
                pygame.mixer.music.unpause()
                print(pygame.mixer.music.get_busy())
                pygame.mixer.music.set_volume(0.7)
                points_gained = 0
                text = font.render(str(points_gained), True, (255, 255, 255))
                textRect = text.get_rect()
                textRect.center = (500, 50)
                point = pygame.Rect(random.randint(1, 49) * cell_size, random.randint(1, 39) * cell_size, cell_size,cell_size)
                counter_start = time.time()


        screen.fill('Red')
        pygame.mixer.music.pause()
        pygame.display.update()

    clock.tick(60)
