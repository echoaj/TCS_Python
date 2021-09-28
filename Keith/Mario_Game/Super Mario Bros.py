import pygame as pg


# Classes
class Sprite:
    def __init__(self, x, y, image, w, h, onscreen=True):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.onscreen = onscreen
        self.image = pg.image.load(image)
        self.image = pg.transform.scale(self.image, (self.w, self.h))

    def display(self):
        if self.onscreen:
            window.blit(self.image, (self.x, self.y))

    def flip(self):
        self.image = pg.transform.flip(self.image, True, False)

    def get_y(self):
        return self.y

    def set_y(self, y):
        self.y = y

    def get_x(self):
        return self.x

    def set_x(self, x):
        self.x = x

    def set_onscreen(self, onscreen):
        self.onscreen = onscreen

    def get_xywh(self):
        return self.x, self.y, self.w, self.h

    def touching(self, sprite1, above=True):
        (x2, y2, w2, h2) = sprite1.get_xywh()
        right = self.x < x2 + w2            #   | | <-
        left = self.x + self.w > x2         # ->| |
        bottom = self.y < y2 + self.h
        top = h2 + self.y > y2
        return right and left and bottom and top


class Mario(Sprite):
    def __init__(self):
        self.width = 100
        self.height = 100
        self.speedX = 0
        self.last_pos = 0
        super().__init__(x=100, y=480, image='Images/mario.png', w=self.width, h=self.height+30)
        self.direction = "right"
        self.mariojump = pg.mixer.Sound('Sounds/mario_jump.wav')
        self.mario_jump = pg.image.load('Images/mario_jump2.png')
        self.mario_jump = pg.transform.scale(self.mario_jump, (self.width, self.height))
        self.big_mario = pg.image.load('Images/big_mario.png')
        self.big_mario = pg.transform.scale(self.big_mario, (self.width, self.height))
        self.velocity = 50
        self.in_air = False

    def display(self):
        if self.in_air:
            window.blit(self.mario_jump, (self.x, self.y))
        else:
            super().display()

    def jump(self):
        key = pg.key.get_pressed()
        if self.velocity == 50 and key[pg.K_UP]:
            y = super().get_y()
            # super().set_y(y - self.velocity)
            pg.mixer.Sound.play(self.mariojump)
            self.in_air = True

        if self.in_air:
            y = super().get_y()
            super().set_y(y - self.velocity)
            self.velocity -= 5

        if super().get_y() >= 480 and self.in_air:
            self.in_air = False
            self.velocity = 50
            print(super().get_y())

        if key[pg.K_DOWN]:
            print(super().get_y())

    def orient_image(self, speedX):
        if self.direction == "right" and speedX < 0:
            super().flip()
            self.mario_jump = pg.transform.flip(self.mario_jump, True, False)
            self.direction = "left"
        elif self.direction == "left" and speedX > 0:
            super().flip()
            self.mario_jump = pg.transform.flip(self.mario_jump, True, False)
            self.direction = "right"

    def set_speedX(self, speedX):
        self.orient_image(speedX)
        self.speedX = speedX

    def move(self):
        self.last_pos = self.x
        self.x += self.speedX

    def backup(self):
        self.x = self.last_pos

    def get_direction(self):
        return self.direction

    def mushroom(self):
        window.blit(self.big_mario, (self.x, self.y))

    def pipetouch(self, x, y):
        self.set_x(x)
        self.set_y(y)


class Goomba(Sprite):
    def __init__(self):
        super().__init__(650, 480, 'Gifs/goomba.gif', 130, 130)
        self.goombastomped = pg.mixer.Sound('Sounds/stomp_enemy.wav')
        self.stomped = pg.image.load('Images/goomba_stomped.png')
        self.stomped = pg.transform.scale(self.stomped, (130, 48))
        self.count = 0

    def display(self):
        super().flip()
        super().display()

    def stomp(self):
        if self.onscreen:
            window.blit(self.stomped, (self.x, self.y + 75))
            self.count += 1
            if self.count > 10:
                super().set_onscreen(False)
                self.count = 0


class Pipe(Sprite):
    def __init__(self):
        super().__init__(500, 434, 'Images/pipe.png', 170, 170)


class Mushroom(Sprite):
    def __init__(self):
        super().__init__(25, 350, 'Images/super_mushroom.png', 130, 130)


class QuestionMarkBlock(Sprite):
    def __init__(self):
        super().__init__(240, 260, 'Gifs/QuestionMarkBlock.gif', 130, 145)


class KoopaTroopa(Sprite):
    def __init__(self):
        super().__init__(300, 450, 'Images/koopa.png', 130, 175)


# RGB color variables to use
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

pg.mixer.init()
window = pg.display.set_mode((1000, 700))

# mariomusic = pg.mixer.music.load('supermariobros.mp3')
# pg.mixer.music.play(-1)
mario_obj = Mario()
pipe_obj = Pipe()
goomba_obj = Goomba()
mush_obj = Mushroom()
koopa_obj = KoopaTroopa()
Qblock_obj = QuestionMarkBlock()
mario_background = pg.image.load('Images/mario_background.jpg')
mario_background = pg.transform.scale(mario_background, (1000, 700))

# Game loop

while True:
    pg.time.delay(60)

    # Check all possible pg events (inputs)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

    # Your game code goes here...
    print(mario_obj.velocity)
    window.blit(mario_background, (0, 0))
    pipe_obj.display()
    mush_obj.display()
    Qblock_obj.display()
    koopa_obj.display()

    key = pg.key.get_pressed()

    if key[pg.K_LEFT]:
        mario_obj.set_speedX(-10)
    elif key[pg.K_RIGHT]:
        mario_obj.set_speedX(10)
    else:
        mario_obj.set_speedX(0)

    if mario_obj.touching(pipe_obj):
        mario_obj.set_speedX(0)
        mario_obj.backup()

    mario_obj.move()

    mario_obj.jump()
    mario_obj.touching(Qblock_obj)
    if mario_obj.touching(goomba_obj) and mario_obj.velocity <= -1:
        goomba_obj.stomp()
    else:
        goomba_obj.display()
    mario_obj.touching(koopa_obj)

    if mario_obj.touching(mush_obj):
        print('power up!')
        mario_obj.mushroom()

    mario_obj.display()
    pg.display.update()

    '''WORLD 1-1
  place 2 pipes in the middle
  place a goomba in between the pipes
  15 blocks later remove ground for gap
  put 2 brick blocks and a ? block in between
  mushroom inside ? block
  place koopa troopa
  place blocks like a triangle but inside of it is a gap
  place pipe that you can go down
  place 2 blocks above 2 goombas and place another ? block with a coin
  place pipe where you come out
  place stairs + flagpole'''
