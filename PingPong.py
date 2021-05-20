import pygame
import random

pygame.init()


class Color:
    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)
    blue = (0, 0, 255)
    yellow = (255, 255, 0)


class Rocket:
    def __init__(self, x, y, color):
        self.w = 10
        self.h = 50
        self.x = x
        self.y = y
        self.color = color
        self.speed = 10
        self.score = 0
        self.area = pygame.draw.rect(Game.screen, self.color, [self.x, self.y, self.w, self.h])

    def show(self):
        self.area = pygame.draw.rect(Game.screen, self.color, [self.x, self.y, self.w, self.h])

    def move(self, b):
        # if self.y < -1:
        #     self.y -= self.speed
        # elif b.x_dir == 1:
        #     self.y += self.speed
        if self.y < b.y:
            self.y += self.speed
        if self.y > b.y:
            self.y -= self.speed
        #limitation
        if self.y < 0:
            self.y = 0

        if self.y > Game.height - self.h:
            self.y = Game.height - self.h

    def cp_speed(self):
        self.speed = random.randint(5, 15)


class Ball:
    def __init__(self):
        self.r = 10
        self.x = Game.width/2
        self.y = Game.height/2
        self.color = Color.yellow
        self.x_dir = -1
        self.y_dir = +1
        self.speed = 5
        self.area = pygame.draw.circle(Game.screen, self.color, [self.x, self.y], self.r)

    def show(self):
        self.area = pygame.draw.circle(Game.screen, self.color, [self.x, self.y], self.r)

    def new(self):
        self.x = Game.width / 2
        self.y = Game.height / 2
        self.x_dir = random.choice([-1, 1])
        self.y_dir = random.choice([-1, 1])

    def move(self):
        self.x += self.speed * self.x_dir
        self.y += self.speed * self.y_dir
        if self.y == Game.height-10 or self.y < 10:
            self.y_dir *= -1


class Game:
    width = 700
    height = 400
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('ping pong')
    clock = pygame.time.Clock()
    fps = 30

    @staticmethod
    def play():
        me = Rocket(20, Game.height / 2, Color.red)
        computer = Rocket(Game.width - 30, Game.height / 2, Color.blue)
        computer.cp_speed()
        ball = Ball()
        while True:

            for event in pygame.event.get():
                if event.type == pygame.MOUSEMOTION:
                    me.y = pygame.mouse.get_pos()[1]
                    if me.y > Game.height - me.h:
                        me.y = Game.height - me.h
                elif event.type == pygame.QUIT:
                    pygame.quit()

            ball.move()

            Game.screen.fill(Color.black)
            pygame.draw.rect(Game.screen, Color.white, [0, 0, Game.width, Game.height], 10)
            pygame.draw.aaline(Game.screen, Color.white, [Game.width / 2, 0], [Game.width / 2, Game.height])
            me.show()
            computer.show()
            computer.move(ball)
            ball.show()
            if ball.x < 0:
                computer.score += 1
                ball.new()
                computer.cp_speed()
            elif ball.x > Game.width:
                me.score += 1
                ball.new()
                computer.cp_speed()

            if me.area.colliderect(ball.area) or computer.area.colliderect(ball.area):
                ball.x_dir *= -1

            font = pygame.font.SysFont('comicsansms', 20)
            text = font.render("Score: " + str(me.score), True, Color.white)
            Game.screen.blit(text, (15, Game.height - 50))
            text = font.render("Score: " + str(computer.score), True, Color.white)
            Game.screen.blit(text, (Game.width - 100, Game.height - 50))
            pygame.display.update()
            Game.clock.tick(Game.fps)


if __name__ == "__main__":
    # game = Game()
    # game.play()

    Game.play()
