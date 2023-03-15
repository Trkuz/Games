import pygame
import time,sys
import random

pygame.init()
pygame.mixer.init()
pygame.font.init()

Clock = pygame.time.Clock()
screen = pygame.display.set_mode((700,500))

font1 = pygame.font.Font('font.ttf', 80)
font2 = pygame.font.Font('font.ttf', 80)



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

    game_active = True
    size = 20
    starting_direction = random.choice([1,2,3,4])
    ball = pygame.Rect(350, 200, size, size)

    velocity_x = 3
    velocity_y = 3

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
            screen.fill((0, 0, 0))
            display_points()
            pygame.display.update()
            time.sleep(2)
            ball.ball.x = 350
            ball.ball.y = 250

        if self.ball.left <= 0:
            player2.points +=1
            screen.fill((0, 0, 0))
            display_points()
            pygame.display.update()
            time.sleep(2)
            ball.ball.x = 350
            ball.ball.y = 250

player1 = Player1('Josh')
player2 = Player2('Marcin')
ball = Ball()

def draw_net():
    net = []
    j = 0
    for i in range(0,50):
        element = pygame.Rect(350, 2 + j, 7, 12)
        net.append(element)
        j += 22

    for element in net:
        pygame.draw.rect(screen, 'white', element)


def display_points():
    player1_points_display = font1.render(str(player1.points), False, (0,0,255))
    player2_points_display = font1.render(str(player2.points), False, (255,0,0))
    player1_pointsRect = player1_points_display.get_rect()
    player2_pointsRect = player2_points_display.get_rect()
    player1_pointsRect.center = (200,200)
    player2_pointsRect.center = (500,200)
    screen.blit(player1_points_display, player1_pointsRect)
    screen.blit(player2_points_display, player2_pointsRect)

def game_over():
    screen.fill('black')
    if player1.points == 5:
        player_won = font2.render(f"Player1({player1.name})  won!", False, (155,0,179))
    if player2.points == 5:
        player_won = font2.render(f"Player2({player2.name}) won!", False, (155,0,179))

    player_wonRect = player_won.get_rect()
    player_wonRect.center = (350, 50)
    screen.blit(player_won, player_wonRect)

    press_space = font1.render("Press space", False, (0,255,0))
    press_spaceRect = press_space.get_rect()
    press_spaceRect.center = (350,150)
    screen.blit(press_space, press_spaceRect)

    again = font1.render("to play again", False, (0, 255, 0))
    againRect = again.get_rect()
    againRect.center = (350, 250)
    screen.blit(again, againRect)
    pygame.display.update()

while True:
    if ball.game_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        player_velocity = 5
        if player1.points == 5 or player2.points == 5:
            ball.game_active = False

        if Player1.player.bottom < 500:
            if pygame.key.get_pressed()[pygame.K_x]:
                Player1.player.y += player_velocity
        if Player1.player.top > 0:
            if pygame.key.get_pressed()[pygame.K_w]:
                Player1.player.y -= player_velocity

        if Player2.player.top > 0:
            if pygame.key.get_pressed()[pygame.K_UP]:
                Player2.player.y -= player_velocity
        if Player2.player.bottom < 500:
            if pygame.key.get_pressed()[pygame.K_DOWN]:
                Player2.player.y += player_velocity

        screen.fill('black')
        draw_net()
        player1.draw_player()
        player2.draw_player()
        ball.move_ball()
        ball.draw_ball()
        pygame.display.update()
        Clock.tick(60)
    else:
        game_over()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed() [pygame.K_SPACE]:
                    player1.points = 0
                    player2.points = 0
                    ball.ball.x = 350
                    ball.ball.y = 350
                    ball.game_active = True

        pygame.display.update()

