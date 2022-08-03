import pygame as pg
import random


class Spark:
    def __init__(self):
        self.x = 250
        self.y = 250
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
WIDTH = 500
HEIGHT = 500
FPS = 60
screen = pg.display.set_mode([WIDTH, HEIGHT])
clock = pg.time.Clock()


spark = Spark()
spark.y = HEIGHT
spark.speedy = -5
spark.speedx = 0

spark_list = [Spark() for i in range(15)]


def main():
    run = True
    while run:
        screen.fill((0, 0, 0))

        if spark.y > 250:
            spark.display()
            spark.move()
        else:
            for s in spark_list:
                s.display()
                s.move()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

        pg.display.update()
        clock.tick(FPS)
    pg.quit()


if __name__ == '__main__':
    main()
