from helper_functions import*


def background(rgb):
    pg.draw.rect(screen, rgb, (0, 0, WIDTH, HEIGHT))
    x = y = 0
    for row in game_map:
        for i in row:
            if i == 1:
                screen.blit(ground, (x, y))
            x += TILE_SIZE
        x = 0
        y += TILE_SIZE


pg.init()
WIDTH, HEIGHT = 800, 600
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Super Mario Game")
clock = pg.time.Clock()


TILE_SIZE = 25
ground = get_image("./images/ground.png", TILE_SIZE)
mario = get_image("./images/mario.png", TILE_SIZE)
game_map = get_level(1)
tile_rects = get_rectangles(game_map, TILE_SIZE)
# plr = Player2(mario, tile_rects)


while True:
    background((0,0,0))
    # plr.display(screen)
    # plr.set_movement()
    # plr.gravity(True)
    # plr.move()

    for event in pg.event.get():        # event loop
        if event.type == QUIT:          # check for window quit
            pg.quit()                   # stop pygame
            exit()                      # stop script
        # plr.move_control(event)

    pg.display.update()
    clock.tick(60)
