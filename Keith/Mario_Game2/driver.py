from helper_functions import*

pg.init()
width = 800
height = 600
screen = pg.display.set_mode((width, height))
pg.display.set_caption("Super Mario Game")
clock = pg.time.Clock()


def background():
    x = y = 0
    for row in game_map:
        for i in row:
            if i == 1:
                screen.blit(ground, (x, y))
            x += TILE_SIZE
        x = 0
        y += TILE_SIZE


TILE_SIZE = 25
ground = get_image("./images/ground.png", TILE_SIZE)
game_map = get_level(1)

while True:
    background()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

    pg.display.update()
    clock.tick(60)
