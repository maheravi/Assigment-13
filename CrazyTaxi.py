import pygame
import random
import time

pygame.init()


class Color:
    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)
    blue = (0, 0, 255)
    yellow = (255, 255, 0)


class Taxi:
    def __init__(self, x, y):
        self.w = 50
        self.h = 50
        self.x = x
        self.y = y
        self.speed = 10
        self.score = 0
        self.image = pygame.transform.scale(pygame.image.load('Taxi.png'), (self.w, self.h))
        self.rect = self.image.get_rect()

    def show(self):
        Game.screen.blit(self.image, [self.x, self.y])

    def move(self, b):
        if self.y < 0:
            self.y = 0

        if self.y > Game.height - self.h:
            self.y = Game.height - self.h


class Car:
    def __init__(self):
        self.w = 30
        self.h = 50
        self.r = 10
        self.x = random.randint(10, Game.width-10)
        self.y = 10
        self.speed = 15
        self.image = pygame.transform.scale(pygame.image.load('Car.png'), (self.w, self.h))
        self.rect = self.image.get_rect()

    def show(self):
        Game.screen.blit(pygame.transform.flip(self.image, False, True), [self.x, self.y])

    def new(self):
        self.x = random.randint(0, Game.width)
        self.y = 10

    def move(self):
        self.y += self.speed


class Game:
    width = 200
    height = 700
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Crazy Taxi')
    clock = pygame.time.Clock()
    fps = 30

    @staticmethod
    def play():
        me = Taxi(Game.width / 2, Game.height - 100)
        car = Car()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEMOTION:
                    me.x = pygame.mouse.get_pos()[0]
                    if me.x > Game.width - me.w - 10:
                        me.x = Game.width - me.w - 10
                    elif me.x < 10:
                        me.x = 10
                elif event.type == pygame.QUIT:
                    pygame.quit()

            car.move()

            Game.screen.fill(Color.black)
            pygame.draw.rect(Game.screen, Color.white, [0, 0, Game.width, Game.height], 10)
            pygame.draw.aaline(Game.screen, Color.white, [Game.width / 2, 0], [Game.width / 2, Game.height])
            me.show()
            car.show()

            if car.y > Game.height:
                me.score += 1
                car.new()

            font = pygame.font.SysFont('comicsansms', 20)
            text = font.render("Score: " + str(me.score), True, Color.white)
            Game.screen.blit(text, (15, Game.height - 50))

            if pygame.Rect(me.x, me.y, me.w, me.h).colliderect(pygame.Rect(car.x, car.y, car.w, car.h)):
                print('game over')
                image = pygame.transform.scale(pygame.image.load('GameOver.jpg'), (Game.width, Game.height))
                Game.screen.blit(image, [0, 0])
                time.sleep(3)
                pygame.display.update()
                me.score = 0
                break

            pygame.display.update()

            Game.clock.tick(Game.fps)


if __name__ == "__main__":
    game = Game()
    font = pygame.font.SysFont('comicsansms', 15)
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            else:
                game.screen.fill((0, 0, 0))
                main_menu_message = font.render('Press to start the game', True, (255, 255, 255))
                font_pos = main_menu_message.get_rect(center=(game.width // 2, game.height // 2))
                game.screen.blit(main_menu_message, font_pos)
                pygame.display.update()
            if event.type == pygame.MOUSEBUTTONDOWN:
                Game.play()
