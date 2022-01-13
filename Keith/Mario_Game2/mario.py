import pygame as pg
from pygame.locals import *


class Player:
    def __init__(self, img, img_jump, img_dead, tile_rects, x, y):
        self.plr = pg.Rect(x, y, img.get_width(), img.get_height())
        self.img = img
        self.img_jump = img_jump
        self.img_dead = img_dead
        self.tile_rects = tile_rects
        self.movement = [0, 0]
        self.moving_left = False
        self.moving_right = False
        self.velocityY = 0
        self.air_time = 0
        self.facing = "right"
        self.moveDirection = "right"
        self.state = {"dead":False}

    def display(self, screen):
        # If facing right but moving left
        if self.facing == "right" and self.moveDirection == "left":
            self.img = self.flip(self.img)
            self.img_jump = self.flip(self.img_jump)
        # If facing left but moving right
        if self.facing == "left" and self.moveDirection == "right":
            self.img = self.flip(self.img)
            self.img_jump = self.flip(self.img_jump)
        if self.air_time < 6:
            screen.blit(self.img, (self.plr.x, self.plr.y))         # regular mario
        else:
            screen.blit(self.img_jump, (self.plr.x, self.plr.y))    # jump mario

    def flip(self, img):
        return pg.transform.flip(img, True, False)

    def set_movement(self):
        self.movement = [0, 0]
        if self.moving_right:
            self.movement[0] += 3  # move right
            self.moveDirection = "right"
        if self.moving_left:
            self.movement[0] -= 3  # move left
            self.moveDirection = "left"

    def move(self):
        collision_types = {"right": False, "left": False, "up": False, "down": False}
        self.plr.x += self.movement[0]      # move left or right
        self.collision(collision_types, "horizontal")   # check for a collision left or right
        self.plr.y += self.movement[1]      # move up or down
        self.collision(collision_types, "vertical")
        if collision_types["down"]:
            self.gravity(False)
            self.air_time = 0
        else:
            self.air_time += 1

    def collision(self, collision_types, type):
        if not self.state["dead"]:
            for tile in self.tile_rects:
                # check if you collide with something
                if self.plr.colliderect(tile):
                    if type == "horizontal":       # checks if moving right or left
                        if self.movement[0] > 0:    # check if moving right
                            self.plr.right = tile.left
                            collision_types["right"] = True
                        if self.movement[0] < 0:    # check if moving left
                            self.plr.left = tile.right
                            collision_types["left"] = True
                    if type == "vertical":         # checks if moving up or down
                        if self.movement[1] > 0:    # check if moving down
                            self.plr.bottom = tile.top
                            collision_types["down"] = True
                        if self.movement[1] < 0:    # check if moving up
                            self.plr.top = tile.bottom
                            collision_types["up"] = True

    def gravity(self, on):
        if on:
            self.movement[1] += self.velocityY
            self.velocityY += 0.2
        else:
            self.velocityY = 0

    def move_control(self, event):
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                self.moving_right = True
                self.facing = "right"
            if event.key == K_LEFT:
                self.moving_left = True
                self.facing = "left"
            if event.key == K_UP:
                if self.air_time < 6:
                    self.velocityY = -5
        if event.type == KEYUP:
            if event.key == K_RIGHT:
                self.moving_right = False
            if event.key == K_LEFT:
                self.moving_left = False

    def stateMachine(self):
        if self.state["dead"]:
            self.death()

    def death(self):
        self.img = self.img_dead
        self.img_jump = self.img_dead
        self.moving_left = False
        self.moving_right = False
        self.plr.y -= 5     # Jump animation
