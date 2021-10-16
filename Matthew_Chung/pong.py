import pygame as pg

pg.init()

width = 700
height = 700

screen = pg.display.set_mode((width, height))
clock = pg.time.Clock()

# Ball Variables
bx = 350
by = 350
bcolor = (0,255,0)
speed_x = 3
speed_y = 2


while True:
    screen.fill((50, 50, 50))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

    # Draw Ball
    pg.draw.circle(screen, bcolor, (bx,by), 25)
    # Move Ball
    bx += speed_x
    by += speed_y
    # Bounce of Walls
    if bx+25 > width:
        speed_x *= -1

    pg.display.update()
    clock.tick(60)
