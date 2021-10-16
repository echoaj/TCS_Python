import pygame as pg

pg.init()

width = 700
height = 700

screen = pg.display.set_mode((width, height))
clock = pg.time.Clock()

riffle = pg.image.load("electric riffle.png")
riffle = pg.transform.flip(riffle, True, False)
riffle = pg.transform.scale(riffle, (40, 60))

rect_x = 300
rect_y = 300
speed_x = 3
speed_y = 1.5
rate_x = 0.05
rate_y = 0.05


while True:
    screen.fill((0, 255, 0))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

    pg.draw.rect(screen, (150,150,150), (rect_x,rect_y,100,70))
    screen.blit(riffle, (50, 100))

    # Move Block
    # move left
    rect_x -= speed_x
    speed_x += rate_x
    if speed_x < -3 or speed_x > 3:
        rate_x *= -1

    # move up
    rect_y += speed_y
    if speed_x > -0.001 and speed_x < 0.001:
        speed_y *= -1

    print(speed_x)

    pg.display.update()
    clock.tick(60)
