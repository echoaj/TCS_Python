import pygame as pg


pg.init()

# Setup the screen window
width = 500
height = 500
screen = pg.display.set_mode([width, height])

x = 50
y = 50

while True:
    # When user hits the close button of the window
    for event in pg.event.get():
        if event.type == pg.QUIT:
            break

    # Fill in the background of the window
    screen.fill((0, 255, 0))

    # Draw a solid blue circle in the center
    pg.draw.circle(screen, (0, 0, 255), (x, y), 25)
    pg.draw.rect(screen, (255, 0, 0), (100, 200, 40, 120))
    x += 1
    # Flip the display
    pg.display.flip()

# Done! Time to quit.
pg.quit()
