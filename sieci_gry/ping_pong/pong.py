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

        player = pygame.Rect(10, 250, 10, 50)

        def draw_player(self):
            pygame.draw.rect(screen, 'white', self.player)


    class Player2:
        def __init__(self, name):
            self.name = name

        player = pygame.Rect(680, 250, 10, 50)

        def draw_player(self):
            pygame.draw.rect(screen, 'white', self.player)



    class Ball:
        def __init__(self):
            pass

        size = 20
        starting_direction = random.choice([1,1,1,1])
        ball = pygame.Rect(350, 200, size, size)

        velocity_x = 3
        velocity_y = 3

        def draw_ball(self):
            pygame.draw.rect(screen, (0, 255, 0), self.ball)


        def move_ball(self):

            #print("top: ", self.ball.top,"bottom: ", self.ball.bottom, "right: ", self.ball.right, "left: ",self.ball.left, end="\n")
            print(self.ball.x,":::::::", self.ball.y)
            print(self.starting_direction)
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

            #print(self.ball.x, "----------", self.y)




    def game_active(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        player1 = Game.Player1('Josh')
        player2 = Game.Player2('Marcin')
        ball = Game.Ball()

        screen.fill('black')


        player1.draw_player()
        player2.draw_player()
        self.move_player()

        ball.move_ball()
        ball.draw_ball()



        pygame.display.update()
        Clock.tick(60)

    def game_over(self):
        pass

    def move_player(self):
        if self.Player1.player.bottom < 500:
            if pygame.key.get_pressed()[pygame.K_x]:
                self.Player1.player.y += 4
        if self.Player1.player.top > 0:
            if pygame.key.get_pressed()[pygame.K_w]:
                self.Player1.player.y -= 4

        if self.Player2.player.top > 0:
            if pygame.key.get_pressed()[pygame.K_UP]:
                self.Player2.player.y -= 4
        if self.Player2.player.bottom < 500:
            if pygame.key.get_pressed()[pygame.K_DOWN]:
                self.Player2.player.y += 4

    def movement(self):
        pass

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

game = Game()
while True:
    if game_active:
        game.game_active()
        game.event_loop()

    else:
        pass
