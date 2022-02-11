from TCS_Python.Keith.Mario_Game2.mario import Player
from interactions import *
from helper_functions import*
from enemy import*
from mushroom import *


def background(rgb):
    pg.draw.rect(screen, rgb, (0, 0, WIDTH, HEIGHT))
    x = y = 0
    for row in game_map:
        for i in row:
            if i != 0:
                screen.blit(bg_tiles[i-1], (x, y))
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
brick = get_image("./images/brick.png", TILE_SIZE)
pipeTL = get_image("./images/pipeTL.png", TILE_SIZE)
pipeTR = get_image("./images/pipeTR.png", TILE_SIZE)
pipeBR = get_image("./images/pipeBR.png", TILE_SIZE)
pipeBL = get_image("./images/pipeBL.png", TILE_SIZE)
bg_tiles = [ground, brick, pipeTL, pipeTR, pipeBR, pipeBL]

mario = get_image("./images/mario.png", TILE_SIZE+20)
marioJump = get_image("./images/mario_jump.png", TILE_SIZE+20)
marioBig = get_image("./images/mario_big.png", TILE_SIZE+20)
mariodead = get_image("./images/mario_dead.png", TILE_SIZE+20)
goomba = get_image(("./images/goomba.png"), TILE_SIZE+20)
goomba_stomped = get_image("./images/goomba_stomped.png", TILE_SIZE+10)
mushroom = get_image("./images/mushroom.png", TILE_SIZE)
game_map = get_level(1)
tile_rects = get_rectangles(game_map, TILE_SIZE)


# pg.mixer.music.load('./music/supermariobros.mp3')
# pg.mixer.music.play(-1)

plr = Player(mario, marioJump, mariodead, marioBig, tile_rects, 50, 100)
gmb = Enemy(goomba, goomba_stomped, tile_rects)
msr = Mushroom(mushroom, tile_rects, 410, 125)


reaction = Interaction(plr, gmb, msr)


# after change picture when jumping

while True:

    background((135,180,255))
    plr.orient()
    plr.display(screen)
    plr.set_movement()
    plr.gravity(True)
    plr.move()
    plr.stateMachine()

    reaction.checkTouchGombaSide()
    reaction.checkGoombaStomped()
    reaction.checkTouchMushroom()

    gmb.display(screen)
    gmb.set_movement()
    gmb.gravity(True)
    gmb.move()
    gmb.side_movement()
    gmb.stateMachine()

    msr.display(screen)
    msr.set_movement()
    msr.gravity(True)
    msr.move()
    msr.side_movement()

    for event in pg.event.get():        # event loop
        if event.type == QUIT:          # check for window quit
            pg.quit()                   # stop pygame
            exit()                      # stop script
        plr.move_control(event)

    pg.display.update()
    clock.tick(60)
