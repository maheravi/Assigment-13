import pygame
import sys
pygame.init()


class Color:
    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)
    blue = (0, 0, 255)
    yellow = (255, 255, 0)
    red1 = (255, 51, 51)
    purple = (255, 0, 255)
    fiz = (0, 255, 255)
    lgreen = (0, 255, 0)
    yellow1 = (255, 255, 51)


class Block:
    def __init__(self, x, y, color):
        self.w = 25
        self.h = 10
        self.x = x
        self.y = y
        self.color = color
        self.area = pygame.draw.rect(Game.screen, self.color, [self.x, self.y, self.w - 20, self.h])

    def show(self):
        pygame.draw.rect(Game.screen, self.color, [self.x, self.y, self.w, self.h])


class Rocket:
    def __init__(self, x, y, color):
        self.w = 40
        self.h = 10
        self.x = x
        self.y = y
        self.color = color
        self.speed = 10
        self.score = 0
        self.area = pygame.draw.rect(Game.screen, self.color, [self.x, self.y, self.w, self.h])

    def show(self):
        self.area = pygame.draw.rect(Game.screen, self.color, [self.x, self.y, self.w, self.h])


class Ball:
    def __init__(self):
        self.r = 10
        self.x = Game.width/2
        self.y = Game.height/2
        self.color = Color.yellow
        self.x_dir = -1
        self.y_dir = +1
        self.speed = 5
        self.no = 3
        self.area = pygame.draw.circle(Game.screen, self.color, [self.x, self.y], self.r)

    def show(self):
        self.area = pygame.draw.circle(Game.screen, self.color, [self.x, self.y], self.r)

    def new(self):
        self.x = Game.width / 2
        self.y = Game.height / 2

    def move(self):
        self.x += self.speed * self.x_dir
        self.y += self.speed * self.y_dir
        if self.y < 10:
            self.y_dir *= -1
        if self.x == Game.width-10 or self.x < 10:
            self.x_dir *= -1


class Game:
    width = 700
    height = 400
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Break Out')
    clock = pygame.time.Clock()
    fps = 30

    @staticmethod
    def play():
        global color
        me = Rocket(Game.width / 2, Game.height - 20, Color.red)
        ball = Ball()
        blk = []
        for x in range(10, Game.width - 5, 30):
            for y in range(50, 150, 20):
                color = [Color.blue, Color.fiz, Color.lgreen, Color.yellow1, Color.red1]
                a = int((y - 50) / 20)
                block = Block(x, y, color[a-1])
                block.show()
                blk.append(block)

        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                else:
                    Game.screen.fill((0, 0, 0))
                    font = pygame.font.SysFont('comicsansms', 20)
                    main_menu_message = font.render('Press anywhere to start the game', True, (255, 255, 255))
                    font_pos = main_menu_message.get_rect(center=(Game.width // 2, Game.height // 2))
                    Game.screen.blit(main_menu_message, font_pos)
                    pygame.display.update()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        while True:
                            for event in pygame.event.get():
                                if event.type == pygame.MOUSEMOTION:
                                    me.x = pygame.mouse.get_pos()[0]
                                    if me.y > Game.height - me.h:
                                        me.y = Game.height - me.h
                                elif event.type == pygame.QUIT:
                                    pygame.quit()

                            ball.move()
                            Game.screen.fill(Color.black)
                            pygame.draw.rect(Game.screen, Color.white, [0, 0, Game.width, Game.height], 10)
                            me.show()
                            ball.show()

                            if ball.y > Game.height:
                                ball.no -= 1
                                ball.new()

                            if me.area.colliderect(ball.area):
                                ball.y_dir *= -1

                            for b in blk:
                                b.show()
                                if ball.area.colliderect(b.area):
                                    me.score += 1
                                    ball.y_dir *= -1
                                    blk.remove(b)

                            font = pygame.font.SysFont('comicsansms', 20)
                            text = font.render("Score: " + str(me.score), True, Color.yellow)
                            Game.screen.blit(text, (15, 5))
                            text = font.render("Balls: " + str(ball.no), True, Color.yellow)
                            Game.screen.blit(text, (Game.width - 85, 5))
                            pygame.display.update()
                            Game.clock.tick(Game.fps)


if __name__ == "__main__":
    # game = Game()
    # game.play()

    Game.play()
