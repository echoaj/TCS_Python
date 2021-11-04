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
        bottom = self.y < y2 + h2
        top = self.y + self.h > y2
        return right and left and bottom and top


class Mario(Sprite):
    def __init__(self):
        self.width = 100
        self.height = 100
        super().__init__(x=100, y=480, image='Images/mario.png', w=self.width, h=self.height+30)
        self.direction = "right"
        self.mariojump = pg.mixer.Sound('Sounds/mario_jump.wav')
        self.mario_jump = pg.image.load('Images/mario_jump2.png')
        self.mario_jump = pg.transform.scale(self.mario_jump, (self.width, self.height))
        self.big_mario = pg.image.load('Images/big_mario.png')
        self.big_mario = pg.transform.scale(self.big_mario, (self.width, self.height))
        self.velocity = 50
        self.state = {"in_air":False, "on_top_of_pipe":False}
        self.in_air = False

    def display(self):
        if self.in_air:
            window.blit(self.mario_jump, (self.x, self.y))
        else:
            super().display()

    def jump(self):
        if self.velocity == 50:
            pg.mixer.Sound.play(self.mariojump)
            self.state["in_air"] = True

    def gravity(self, on):
        if on:
            if self.state["in_air"]:
                self.y -= self.velocity
                self.velocity -= 5
        else:
            if self.state["in_air"]:
                self.state["in_air"] = False
                self.state["on_top_of_pipe"] = True
                self.velocity = 50

    def stand_on_top(self, constant=False):
        if constant:
            if self.y + self.h > constant:
                self.gravity(False)
        # if platform:
        #     if platform.x < self.x + self.w and self.x < platform.x + platform.w:
        #         self.gravity(False)
        #     elif not self.state["in_air"]:
        #         self.gravity(True)

    def orient_image(self, speedX):
        if self.direction == "right" and speedX < 0:
            super().flip()
            self.mario_jump = pg.transform.flip(self.mario_jump, True, False)
            self.direction = "left"
        elif self.direction == "left" and speedX > 0:
            super().flip()
            self.mario_jump = pg.transform.flip(self.mario_jump, True, False)
            self.direction = "right"

    def move(self, speedX):
        self.orient_image(speedX)
        self.x += speedX

    def set_last_pos(self):
        self.last_pos = (self.x, self.y)

    def backup(self):
        self.x, self.y = self.last_pos

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

        super().__init__(470, 440, 'Images/pipe2.png', 170, 170)


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
    window.blit(mario_background, (0, 0))
    pipe_obj.display()
    mush_obj.display()
    Qblock_obj.display()
    koopa_obj.display()

    key = pg.key.get_pressed()

    mario_obj.set_last_pos()
    if key[pg.K_LEFT]:
        mario_obj.move(-10)
    if key[pg.K_RIGHT]:
        mario_obj.move(10)
    if key[pg.K_UP]:
        mario_obj.jump()

    mario_obj.gravity(True)

    if mario_obj.touching(pipe_obj):
        mario_obj.gravity(False)
        mario_obj.backup()

    mario_obj.stand_on_top(constant=600)
    if mario_obj.touching(goomba_obj) and mario_obj.velocity <= -1:
        goomba_obj.stomp()
    else:
        goomba_obj.display()
    mario_obj.touching(koopa_obj)

    if mario_obj.touching(mush_obj):
        print('power up!')
        mario_obj.mushroom()
    # pg.draw.rect(window, (0,0,0), (300, 600, 40, 40))
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
