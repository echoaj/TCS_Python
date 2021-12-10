import pygame as pg
from pygame.locals import *


class Player:
    def __init__(self, img, tile_rects):
        self.plr = pg.Rect(50, 50, img.get_width(), img.get_height())
        self.img = img
        self.tile_rects = tile_rects
        self.movement = [0, 0]
        self.moving_left = False
        self.moving_right = False
        self.velocityY = 0
        self.air_time = 0

    def display(self, screen):
        screen.blit(self.img, (self.plr.x, self.plr.y))

    def set_movement(self):
        self.movement = [0, 0]
        if self.moving_right:
            self.movement[0] += 3  # move right
        if self.moving_left:
            self.movement[0] -= 3  # move left

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
                if type == "vertical":         # checks if moving right or left
                    if self.movement[1] > 0:    # check if moving right
                        self.plr.bottom = tile.top
                        collision_types["down"] = True
                    if self.movement[1] < 0:    # check if moving left
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
            if event.key == K_LEFT:
                self.moving_left = True
            if event.key == K_UP:
                if self.air_time < 6:
                    self.velocityY = -5
        if event.type == KEYUP:
            if event.key == K_RIGHT:
                self.moving_right = False
            if event.key == K_LEFT:
                self.moving_left = False