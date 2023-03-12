import pygame, sys
import random
import time
pygame.init()
pygame.font.init()
pygame.mixer.init()
game_active = True

pygame.display.set_caption("Reflex Game")

pygame.mixer.music.load("muzyka1.mp3")
pygame.mixer.music.set_volume(0.7)
pygame.mixer.music.play(loops=True)

points_gained = 0

font1 = pygame.font.Font("font.ttf", 80)
text1 = font1.render(str(points_gained), False, (72,251,0))
textRect1 = text1.get_rect()
textRect1.center = (100, 50)

font2 = pygame.font.Font("font.ttf", 120)
text2 = font2.render("GAME OVER", False, (255,0,0))
textRect2 = text2.get_rect()
font3 = pygame.font.Font("font.ttf", 50)
text5 = font3.render("PRESS SPACE TO PLAY AGAIN", False, (0,0,255))
textRect5 = text5.get_rect()



cell_size = 20
screen_size = (cell_size*50, cell_size*40)
screen = pygame.display.set_mode((screen_size))
clock = pygame.time.Clock()
point = pygame.Rect(random.randint(1, 49) * cell_size, random.randint(1, 39) * cell_size, cell_size, cell_size)
touching = True
timer = 10

counter_start = time.time()
while True:

    if game_active:

        counter = time.time()
        time_left = round(counter - counter_start, 2)
        display_time = round(timer-time_left, 1)
        text3 = font1.render(f"Time left: {display_time}", False, (255,255,255))
        textRect3 = text3.get_rect()
        textRect3.center = (600, 50)

        if int(time_left) == 10:
            pygame.mixer.music.pause()
            game_active = False

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
                    text1 = font1.render(str(points_gained), True, (72,251,0))
                    textRect1 = text1.get_rect()
                    textRect1.center = (100, 50)

        screen.fill('black')
        screen.blit(text1, textRect1)
        screen.blit(text3, textRect3)
        point_surface = pygame.draw.rect(screen, 'red', point)
        pygame.display.update()

    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                game_active = True
                pygame.mixer.music.play()
                points_gained = 0
                text1 = font1.render(str(points_gained), True, (72,251,0))
                textRect1 = text1.get_rect()
                textRect1.center = (100, 50)
                point = pygame.Rect(random.randint(1, 49) * cell_size, random.randint(1, 39) * cell_size, cell_size,cell_size)
                counter_start = time.time()


        screen.fill('black')
        text4 = font2.render(f"score: {str(points_gained)}", False, (72,251,0))
        textRect4 = text4.get_rect()
        textRect2.center = (500, 300)
        textRect4.center = (500,400)
        textRect5.center = (500,500)
        screen.blit(text2, textRect2)
        screen.blit(text4, textRect4)
        screen.blit(text5, textRect5)
        pygame.display.update()

    clock.tick(60)
