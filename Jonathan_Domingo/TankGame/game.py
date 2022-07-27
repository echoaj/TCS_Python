import pygame as pg


pg.init()
WIDTH = 500
HEIGHT = 500
FPS = 60
screen = pg.display.set_mode([WIDTH, HEIGHT])
clock = pg.time.Clock()


def main():
    run = True
    while run:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

        pg.display.update()
        clock.tick(FPS)
    pg.quit()


if __name__ == '__main__':
    main()
