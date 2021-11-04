import pygame as pg

pg.init()

width = 700
height = 700

screen = pg.display.set_mode((width, height))
clock = pg.time.Clock()

# Ball Variables
bx = 350
by = 350
br = 25
bcolor = (0, 255, 0)
speed_x = -3
speed_y = 0

# Paddle Left
pad_left_x = 25
pad_left_y = 300
pad_width = 15
pad_height = 100
pl_color = (255, 0, 0)

# Paddle Right
pad_right_x = width - 40
pad_right_y = 300
pr_color = (0, 0, 255)

while True:
    screen.fill((50, 50, 50))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

    key = pg.key.get_pressed()
    if key[pg.K_UP]:
        pad_right_y -= 5
    if key[pg.K_DOWN]:
        pad_right_y += 5
    if key[pg.K_w]:
        pad_left_y -= 5
    if key[pg.K_s]:
        pad_left_y += 5

    # Draw Ball
    pg.draw.circle(screen, bcolor, (bx, by), br)
    # Move Ball
    bx += speed_x
    by += speed_y
    # Bounce of Walls
    # if bx+br > width or bx-br < 0:
    #     speed_x *= -1

    # Bounce off left paddle
    if pad_left_x + 10 > bx - br > pad_left_x and pad_left_y < by < pad_left_y + pad_height:
        speed_x *= -1
    # Bounce off right paddle
    if pad_right_x < bx + br < pad_right_x + 10 and pad_right_y < by < pad_right_y + pad_height:
        speed_x *= -1

    if by + br > height or by - br < 0:
        speed_y *= -1

    # Draw left paddle
    pg.draw.rect(screen, pl_color, (pad_left_x, pad_left_y, pad_width, pad_height))

    # Draw right paddle
    pg.draw.rect(screen, pr_color, (pad_right_x, pad_right_y, pad_width, pad_height))

    pg.display.update()
    clock.tick(60)
