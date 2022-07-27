import pygame as pg


def triggerEvent():
    pg.event.post(pg.event.Event(custom_event, message="Out of Screen"))


pg.init()

# Setup the screen window
width = 500
height = 500
FPS = 60
screen = pg.display.set_mode([width, height])
clock = pg.time.Clock()

# Images
CAR_IMG = pg.image.load('blue_car.png')
CAR_IMG = pg.transform.scale(CAR_IMG, (150, 80))

# Define a font
font = pg.font.SysFont('Arial', 25)

# create custom event
custom_event = pg.USEREVENT + 1

rect2 = pg.Rect(20, 400, 40, 40)

x = 50
y = 50

run = True
while run:
    # When user hits the close button of the window
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == custom_event:
            print(event.message)
            x = 0

    # Fill in the background of the window
    screen.fill((0, 255, 0))

    # Draw a solid blue circle in the center
    pg.draw.circle(screen, (0, 0, 255), (x, y), 25)
    pg.draw.rect(screen, (255, 0, 0), (100, 200, 40, 120))
    x += 1

    if x > width:
        triggerEvent()

    pg.draw.rect(screen, (255, 255, 0), rect2)

    # Draw the car image
    screen.blit(CAR_IMG, (250, 300))

    # Draw the text
    text = font.render("Car", True, (255, 0, 255))
    screen.blit(text, (380, 250))

    # Flip the display
    pg.display.update()
    clock.tick(FPS)


# Done! Time to quit.
pg.quit()
