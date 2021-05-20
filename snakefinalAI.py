import sys
import pygame
import random

pygame.init()


class Apple:
    def __init__(self):
        self.w = 10
        self.h = 10
        self.x = random.randrange(40, width - 40, 10)
        self.y = random.randrange(40, height - 40, 10)
        self.color = (138, 43, 226)

    def show(self):
        pygame.draw.rect(d, self.color, [self.x, self.y, self.w, self.h])


class Snake:
    def __init__(self):
        self.w = 10
        self.h = 10
        self.x = width / 2
        self.y = height / 2
        self.pos = [self.x, self.y]
        self.name = "mohammad ali"
        self.color = (0, 127, 0)
        self.speed = 10
        self.score = 0
        self.x_change = 0
        self.y_change = 0
        # self.body = [[self.pos[0], self.pos[1]], [self.pos[0] - 10, self.pos[1]], [self.pos[0] - (2 * 10), self.pos[1]]]
        self.body = [[self.pos[0] - 20, self.pos[1]], [self.pos[0] - 10, self.pos[1]], [self.pos[0], self.pos[1]]]

    def eat(self):
        if apple.x - apple.w <= self.pos[0] <= apple.x + apple.w and apple.y - apple.h <= self.pos[1] <= apple.y + apple.h:
            self.score += 1
            self.body.append(self.pos)
            return True
        else:
            return False

    def show(self):
        pygame.draw.rect(d, self.color, [self.pos[0], self.pos[1], self.w, self.h])
        for item in self.body:
            pygame.draw.rect(d, self.color, [item[0], item[1], self.w, self.h])

    def move(self):
        if self.x_change == -1:
            self.pos[0] -= self.speed
        elif self.x_change == 1:
            self.pos[0] += self.speed
        elif self.y_change == -1:
            self.pos[1] -= self.speed
        elif self.y_change == 1:
            self.pos[1] += self.speed
        self.body.append(list(self.pos))
        self.body.pop(0)

    def Body(self):
        self.body.append(self.pos)

    def Screen(self):
        if self.pos[0] == width:
            self.pos[0] = 0
        elif self.pos[0] == 0:
            self.pos[0] = width
        if self.pos[1] == height:
            self.pos[1] = 0
        elif self.pos[1] == 0:
            self.pos[1] = height

    # def Collide(self):
    #     if len(self.body) > 3:
    #         for i in range(1, len(self.body)-2):
    #             if self.pos[0] == self.body[i][0] and self.pos[1] == self.body[i][1]:
    #                 pygame.quit()


if __name__ == "__main__":
    width = 800
    height = 600

    d = pygame.display.set_mode((width, height))
    pygame.display.set_caption('snake game')
    font = pygame.font.SysFont('comicsansms', 30)
    clock = pygame.time.Clock()

    snake = Snake()
    apple = Apple()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            else:
                d.fill((0, 0, 0))
                main_menu_message = font.render('Press anywhere to start the game', True, (255, 255, 255))
                font_pos = main_menu_message.get_rect(center=(width // 2, height // 2))
                d.blit(main_menu_message, font_pos)
                pygame.display.update()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    while True:
                        if snake.pos[0] < apple.x:
                            if snake.x_change == -1:
                                snake.x_change = -1
                            else:
                                snake.x_change = 1
                                snake.y_change = 0
                        elif snake.pos[0] > apple.x:
                            if snake.x_change == 1:
                                snake.x_change = 1
                            else:
                                snake.x_change = -1
                                snake.y_change = 0
                        elif snake.pos[0] == apple.x:
                            if snake.pos[1] > apple.y:
                                if snake.y_change == 1:
                                    snake.y_change = 1
                                else:
                                    snake.y_change = -1
                                    snake.x_change = 0
                            elif snake.pos[1] < apple.y:
                                if snake.y_change == -1:
                                    snake.y_change = -1
                                else:
                                    snake.y_change = 1
                                    snake.x_change = 0

                        snake.move()
                        snake.Screen()
                        # snake.Collide()

                        if snake.eat():
                            snake.Body()
                            apple = Apple()

                        d.fill((0, 0, 0))

                        snake.show()
                        apple.show()

                        score_font = font.render("Score: "+str(snake.score), True, (255, 255, 0))
                        font_pos = score_font.get_rect(center=(80, height - 50))
                        d.blit(score_font, font_pos)
                        pygame.display.update()
                        clock.tick(30)

                elif event.type == pygame.QUIT:
                    pygame.quit()
