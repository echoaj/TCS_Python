import pygame as pg
import random


class Firework:
    def __init__(self, amount, y_pos):
        x_pos = random.randint(0, WIDTH)
        self.y_pos = y_pos
        self.spark = Spark(x_pos, y_pos)
        self.spark.y = HEIGHT
        self.spark.speedy = -5
        self.spark.speedx = 0
        self.spark_list = [Spark(x_pos, y_pos) for i in range(amount)]

    def display(self):
        if self.spark.y > self.y_pos:
            self.spark.display()
            self.spark.move()
        else:
            for s in self.spark_list:
                s.display()
                s.move()


class Spark:
    def __init__(self, x_pos, y_pos):
        self.x = x_pos
        self.y = y_pos
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.radius = 5
        self.speedx = random.choice([-6, -5, -4, -3, 3, 4, 5, 6])
        self.speedy = random.choice([-6, -5, -4, -3, 3, 4, 5, 6])

    def display(self):
        pg.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.speedx
        self.y += self.speedy


pg.init()
WIDTH = 800
HEIGHT = 800
FPS = 60
screen = pg.display.set_mode([WIDTH, HEIGHT])
clock = pg.time.Clock()


firework_list = []


def main():
    timer = 0
    run = True
    while run:
        screen.fill((0, 0, 0))

        if timer == 120:
            spark_amount = random.randint(8, 30)
            y_pos = random.randint(100, WIDTH//2)
            # create a new firework
            new_firework = Firework(spark_amount, y_pos)
            # add it to the firework list
            firework_list.append(new_firework)
            timer = random.randint(0, 100)

        for f in firework_list:
            f.display()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

        pg.display.update()
        clock.tick(FPS)
        timer += 1

    pg.quit()


if __name__ == '__main__':
    main()
