import pygame as pg
import pygame.freetype as pf

pg.init()
width = 1000
height = 800

font = pf.SysFont("Times", 50)
screen = pg.display.set_mode((width, height))
pg.display.set_caption("Pong Game")
clock = pg.time.Clock()

# BAll
bx = width/2
by = height/2
speedx = 5
speedy = 2
ball_size = 40
ball_color = (0,200,0)

# Paddle
px1 = 20
py1 = height/2 - 50
px2 = width - 40
py2 = height/2 - 50
pad1_color = (200,0,0)
pad2_color = (0,0,200)

# Score
pad1_score = 0
pad2_score = 0

run = True
while run:
    screen.fill((0,0,0))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    # Ball
    pg.draw.ellipse(screen, ball_color, (int(bx),int(by),ball_size,ball_size))
    # Ball Movement
    bx += speedx
    by += speedy
    # Bounce top & bottom
    if by+ball_size > height or by < 0:
        speedy *= -1
    # Change Score left & right
    if bx > width:
        pad1_score += 1
        bx, by = width/2, height/2
    elif bx+ball_size < 0:
        pad2_score += 1
        bx, by = width/2, height/2
    # Score Display
    font.render_to(screen, (50, 50), str(pad1_score), pad1_color)
    font.render_to(screen, (width-100, 50), str(pad2_score), pad2_color)
    # Paddle Display
    pg.draw.rect(screen, pad1_color, (int(px1), int(py1), 20, 100))
    pg.draw.rect(screen, pad2_color, (int(px2), int(py2), 20, 100))
    # Paddle Movement
    key = pg.key.get_pressed()
    if key[pg.K_w]:
        py1 -= 5
    if key[pg.K_s]:
        py1 += 5
    if key[pg.K_UP]:
        py2 -= 5
    if key[pg.K_DOWN]:
        py2 += 5
    # Paddle Ball Bounce
    if px1+20 > bx > px1 and by > py1 and by+20 < py1+100:
        speedx *= -1
    if px2 < bx+40 < px2+20 and by > py2 and by+20 < py2+100:
        speedx *= -1

    pg.display.update()
    clock.tick(60)
