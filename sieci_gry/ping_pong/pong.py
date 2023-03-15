import pygame
import time,sys
import random

pygame.init()
pygame.mixer.init()
pygame.font.init()

Clock = pygame.time.Clock()
game_active = True
screen = pygame.display.set_mode((700,500))


class Player1:
        def __init__(self, name):
            self.name = name
            self.points = 0

        player = pygame.Rect(10, 250, 10, 50)

        def draw_player(self):
            pygame.draw.rect(screen, 'white', self.player)


class Player2:
        def __init__(self, name):
            self.name = name
            self.points = 0

        player = pygame.Rect(680, 250, 10, 50)

        def draw_player(self):
            pygame.draw.rect(screen, 'white', self.player)



class Ball:
    def __init__(self):
            pass

    size = 20
    starting_direction = random.choice([1,1,1,1])
    ball = pygame.Rect(350, 200, size, size)

    velocity_x = 5
    velocity_y = 5

    def draw_ball(self):
        pygame.draw.rect(screen, (0, 255, 0), self.ball)

    def move_ball(self,):
        if self.starting_direction == 1:
            self.ball.x -= self.velocity_x
            self.ball.y -= self.velocity_y
        if self.starting_direction == 2:
            self.ball.x -= self.velocity_x
            self.ball.y += self.velocity_y
        if self.starting_direction == 3:
            self.ball.x += self.velocity_x
            self.ball.y -= self.velocity_y
        if self.starting_direction == 4:
            self.ball.x += self.velocity_x
            self.ball.y += self.velocity_y

        if self.ball.top <=0 or self.ball.bottom >= 500 :
            self.velocity_y *= -1
        if self.ball.colliderect(player1.player) or self.ball.colliderect(player2.player):
            self.velocity_x *= -1

        if self.ball.right >= 700:
            player1.points +=1
            game_active = False
            #print('dsa')
            return game_active

        if self.ball.left <= 0:
            player2.points +=1
            game_active = False
            #print('asd')
            return game_active

#-------------------------------------------------------------------
player1 = Player1('Josh')
player2 = Player2('Marcin')
ball = Ball()

while True:
    print(game_active)
    if game_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        if Player1.player.bottom < 500:
            if pygame.key.get_pressed()[pygame.K_x]:
                Player1.player.y += 4
        if Player1.player.top > 0:
            if pygame.key.get_pressed()[pygame.K_w]:
                Player1.player.y -= 4

        if Player2.player.top > 0:
            if pygame.key.get_pressed()[pygame.K_UP]:
                Player2.player.y -= 4
        if Player2.player.bottom < 500:
            if pygame.key.get_pressed()[pygame.K_DOWN]:
                Player2.player.y += 4

        screen.fill('black')
        player1.draw_player()
        player2.draw_player()
        print(game_active)
        ball.move_ball()
        ball.draw_ball()
        pygame.display.update()
        Clock.tick(60)
    else:
        time.sleep(2)
        game_active = True
