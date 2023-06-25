import pygame, sys
import random
import time
pygame.init()
pygame.font.init()
pygame.mixer.init()
pygame.mixer.music.load("muzyka1.mp3")
pygame.mixer.music.set_volume(0.7)
pygame.mixer.music.play(loops = True)

class Game:
    def __init__(self):
        self.game_active = True
        self.points = 0
        self.cell_size = 20
        self.touching = True
        self.screen = pygame.display.set_mode((self.cell_size*50, self.cell_size*40))
        self.clock = pygame.time.Clock()
        self.timer = 10
        self.counter_start = time.time()
        self.font1 = pygame.font.Font("font.ttf", 80)
        self.font2 = pygame.font.Font("font.ttf", 120)
        self.font3 = pygame.font.Font("font.ttf", 50)
        self.point = pygame.Rect(random.randint(1, 49) * self.cell_size, random.randint(1, 39) * self.cell_size,
                                 self.cell_size, self.cell_size)

    def spawn(self):
        self.point = pygame.Rect(random.randint(1, 49) * self.cell_size, random.randint(1, 39) * self.cell_size,
                                 self.cell_size, self.cell_size)

        pygame.draw.rect(self.screen, 'red', self.point)

    def time(self):
        counter = time.time()
        time_left = round(counter - self.counter_start, 2)
        display_time = round(self.timer - time_left, 1)
        text3 = self.font1.render(f"Time left: {display_time}", False, (255, 255, 255))
        textRect3 = text3.get_rect()
        textRect3.center = (600, 50)
        self.screen.blit(text3,textRect3)
        print(display_time)
        if display_time != 0.0:
            pygame.draw.rect(self.screen, 'red', self.point)
        if display_time == 0.0:
            pygame.mixer.music.pause()
            self.game_active = False

    def display_points(self,):
        text1 = self.font1.render(str(self.points), False, (72, 251, 0))
        textRect1 = text1.get_rect()
        textRect1.center = (100, 50)
        self.screen.blit(text1, textRect1)

    def collide(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if mouse_x in range(self.point.x, self.point.x + 20) and mouse_y in range(self.point.y, self.point.y + 20):
            self.touching = True
        else:
            self.touching = False

    def game_over(self):

        text2 = self.font2.render("GAME OVER", False, (255, 0, 0))
        textRect2 = text2.get_rect()
        textRect2.center = (500, 300)

        text4 = self.font2.render(f"score: {str(self.points)}", False, (72, 251, 0))
        textRect4 = text4.get_rect()
        textRect4.center = (500, 400)

        text5 = self.font3.render("PRESS SPACE TO PLAY AGAIN", False, (0, 0, 255))
        textRect5 = text5.get_rect()
        textRect5.center = (500, 500)

        self.screen.blit(text2, textRect2)
        self.screen.blit(text4, textRect4)
        self.screen.blit(text5, textRect5)
        pygame.display.update()

game = Game()
while True:
    if game.game_active:
        game.collide()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if game.touching:
                    game.points += 1
                    game.spawn()

        game.screen.fill('black')
        game.time()
        game.display_points()
        pygame.display.update()
    else:
        game.game_over()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                game.game_active = True
                pygame.mixer.music.play()
                game.points = 0
                game.spawn()
                game.counter_start = time.time()

    game.clock.tick(60)
