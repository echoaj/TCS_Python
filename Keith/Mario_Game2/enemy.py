import pygame as pg


class Enemy:
    def __init__(self, img, stompedImg, tile_rects):
        self.enm = pg.Rect(200, 125, img.get_width(), img.get_height())
        self.img = img
        self.stompedImg = stompedImg
        self.tile_rects = tile_rects
        self.movement = [0, 0]
        self.moving_left = False
        self.moving_right = False
        self.velocityY = 0
        self.facing = "right"
        self.moveDirection = "right"
        self.speed = 2
        self.timer = 0
        self.state = {"stomped":False}

    def display(self, screen):
        if self.timer % 10 == 0:
            self.img = self.flip(self.img)
        screen.blit(self.img, (self.enm.x, self.enm.y))         # regular mario

    def flip(self, img):
        return pg.transform.flip(img, True, False)

    def set_movement(self):
        self.movement = [0, 0]
        if self.moving_right:
            self.movement[0] += self.speed  # move right
            self.moveDirection = "right"
        if self.moving_left:
            self.movement[0] -= self.speed  # move left
            self.moveDirection = "left"

    def move(self):
        collision_types = {"right": False, "left": False, "up": False, "down": False}
        self.enm.x += self.movement[0]  # move left or right
        self.collision(collision_types, "horizontal")  # check for a collision left or right
        self.enm.y += self.movement[1]  # move up or down
        self.collision(collision_types, "vertical")
        if collision_types["down"]:
            self.gravity(False)

    def collision(self, collision_types, type):
        for tile in self.tile_rects:
            # check if you collide with something
            if self.enm.colliderect(tile):
                if type == "horizontal":  # checks if moving right or left
                    if self.movement[0] > 0:  # check if moving right
                        self.enm.right = tile.left
                        collision_types["right"] = True
                    if self.movement[0] < 0:  # check if moving left
                        self.enm.left = tile.right
                        collision_types["left"] = True
                if type == "vertical" and not self.state["stomped"]:  # checks if moving right or left
                    if self.movement[1] > 0:  # check if moving down
                        self.enm.bottom = tile.top
                        collision_types["down"] = True
                    if self.movement[1] < 0:  # check if moving up
                        self.enm.top = tile.bottom
                        collision_types["up"] = True

    def gravity(self, on):
        if on:
            self.movement[1] += self.velocityY
            self.velocityY += 0.2
        else:
            self.velocityY = 0

    def side_movement(self):
        if not self.state["stomped"]:
            if self.timer < 101:
                self.moving_right = True
                self.moving_left = False
                self.facing = "right"
            elif 101 <= self.timer < 200:
                self.moving_left = True
                self.moving_right = False
                self.facing = "left"
            else:
                self.timer = 0
            self.timer += 1
        else:
            self.moving_right = False
            self.moving_left = False

    def stateMachine(self):
        if self.state["stomped"]:
            self.death()

    def death(self):
        self.img = self.stompedImg