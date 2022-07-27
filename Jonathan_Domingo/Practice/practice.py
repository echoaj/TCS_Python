import pygame as pg
import pygame.event

pg.init()
FPS = 60
WIDTH = 500
HEIGHT = 500
screen = pg.display.set_mode([WIDTH, HEIGHT])
pg.display.set_caption("Practice")
clock = pg.time.Clock()

custom_font = pg.font.SysFont("Arial", 30)

SPACE_SHIP_IMG = pg.image.load("spaceship.png")
SPACE_SHIP_IMG = pg.transform.scale(SPACE_SHIP_IMG, (40, 70))

custom_event = pg.USEREVENT + 1

pygame.event.post(pg.event.Event(custom_event, message="Hello"))

platRect = pg.Rect(200, 200, 100, 40)

x = 50
y = 50

run = True
while run:
    screen.fill((0, 255, 0))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            print("User quit")
            run = False
        elif event.type == custom_event:
            print(event.message)

    pg.draw.circle(screen, (0, 0, 255), (x, y), 25)
    pg.draw.rect(screen, (255, 0, 0), (100, 200, 40, 120))
    x += 1

    # Display Image Surface
    screen.blit(SPACE_SHIP_IMG, (300, 100))
    # Display platRect
    pg.draw.rect(screen, (0, 0, 255), platRect)
    platRect.x += 1

    # Display Text
    text = custom_font.render("Hello World", True, (255, 0, 0))
    screen.blit(text, (100, 100))

    pg.display.update()
    clock.tick(FPS)


pg.quit()
