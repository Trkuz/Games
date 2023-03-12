import pygame
import time,sys
import random

pygame.init()
pygame.mixer.init()
pygame.font.init()

Clock = pygame.time.Clock()
game_active = True
screen = pygame.display.set_mode((700,500))

class Game:

    class Player1:
        def __init__(self, name):
            self.name = name
            self.player = pygame.Rect(10, 250, 10, 30)

        def draw_player(self):
            pygame.draw.rect(screen, 'white', self.player)

        def move_player(self):
            if pygame.key.get_pressed() [pygame.K_w]:
                self.player.y -=1
            if pygame.key.get_pressed() [pygame.K_x]:
                self.player.y +=1

    class Player2:
        def __init__(self, name):
            self.name = name
            self.player = pygame.Rect(10, 250, 10, 30)

        def draw_player(self):
            pygame.draw.rect(screen, 'white', self.player)

        def move_player(self):
            if pygame.key.get_pressed() [pygame.K_DOWN]:
                self.player.y -=1
            if pygame.key.get_pressed() [pygame.K_UP]:
                self.player.y +=1

    class Ball:
        def __init__(self):
            self.size = 20

        def draw_ball(self):
            ball = pygame.Rect(350, 250, self.size, self.size)
            pygame.draw.rect(screen, (0,255,0), ball)

        def move_ball(self):
            pass

    def game_active(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


        player1 = Game.Player1('Josh')
        player2 = Game.Player2('Marcin')
        ball = Game.Ball()

        screen.fill('black')
        ball.draw_ball()

        player1.draw_player()
        player2.draw_player()
        player1.move_player()
        player2.move_player()

        pygame.display.update()
        Clock.tick(60)

    def game_over(self):
        pass

game = Game()
while True:
    if game_active:
        game.game_active()

    else:
        pass
