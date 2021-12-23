import pygame as pg
from pygame.locals import *

pg.init()
WIDTH, HEIGHT = 800, 600
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Super Mario Game")
clock = pg.time.Clock()




while True:


    pg.draw.rect(screen, (20,200,200), pg.Rect(30, 30, 60, 60),  0)

    for event in pg.event.get():        # event loop
        if event.type == QUIT:          # check for window quit
            pg.quit()                   # stop pygame
            exit()                      # stop script

    pg.display.update()
    clock.tick(60)