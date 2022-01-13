from TCS_Python.Keith.Mario_Game2.mario import Player
from interactions import *
from helper_functions import*
from enemy import*


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
mario = get_image("./images/mario.png", TILE_SIZE+20)
marioJump = get_image("./images/mario_jump.png", TILE_SIZE+20)
mariodead = get_image("./images/mario_dead.png", TILE_SIZE+20)
goomba = get_image(("./images/goomba.png"), TILE_SIZE+20)
goomba_stomped = get_image("./images/goomba_stomped.png", TILE_SIZE+10)
game_map = get_level(1)
tile_rects = get_rectangles(game_map, TILE_SIZE)
# plr = Player2(mario, tile_rects)


plr = Player(mario, marioJump, mariodead, tile_rects, 50, 100)
gmb = Enemy(goomba, goomba_stomped, tile_rects)


reaction = Interaction(plr, gmb)


# after change picture when jumping

while True:


    background((135,180,255))
    plr.display(screen)
    plr.set_movement()
    plr.gravity(True)
    plr.move()
    plr.stateMachine()

    reaction.checkTouchGombaSide()
    reaction.checkGoombaStomped()

    gmb.display(screen)
    gmb.set_movement()
    gmb.gravity(True)
    gmb.move()
    gmb.side_movement()
    gmb.stateMachine()

    for event in pg.event.get():        # event loop
        if event.type == QUIT:          # check for window quit
            pg.quit()                   # stop pygame
            exit()                      # stop script
        plr.move_control(event)

    pg.display.update()
    clock.tick(60)
