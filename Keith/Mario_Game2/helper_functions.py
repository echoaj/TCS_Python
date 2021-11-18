import json
import pygame as pg
from pygame.locals import *


def get_rectangles(game_map, ts):
    tiles = []
    x = y = 0
    for row in game_map:
        for i in row:
            if i != 0:
                rect = pg.Rect(x,y,ts,ts)
                tiles.append(rect)
            x += ts
        x = 0
        y += ts
    return tiles


def get_level(num):
    directory = f"./levels/lvl{num}.json"
    with open(directory, "r") as file:
        data = json.load(file)
    return data["tile_map"]


def get_image(path, size):
    img = pg.image.load(path)
    img = pg.transform.scale(img, (size, size))
    return img























class Player2:
    def __init__(self, img, tiles):
        self.plr = pg.Rect(50, 50, img.get_width(), img.get_height())   # 1
        self.img = img
        self.tiles = tiles
        self.moving_right = False
        self.moving_left = False
        self.player_y_momentum = 0
        self.movement = [0, 0]
        self.air_time = 0

    def display(self, screen):                                          # 1
        screen.blit(self.img, (self.plr.x, self.plr.y))

    def set_movement(self):                                             # 2
        self.movement = [0, 0]
        if self.moving_right:
            self.movement[0] += 3  # move right
        if self.moving_left:
            self.movement[0] -= 3  # move left

    def move(self):
        collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}
        # collision left and right
        self.plr.x += self.movement[0]                # move left       # 3
        self.collision(collision_types, "horizontal")
        # collision up and down
        self.plr.y += self.movement[1]                # move right      # 3
        self.collision(collision_types, "vertical")
        # stop falling if on top of platform
        if collision_types['bottom']:
            self.gravity(False)
            self.air_time = 0
        else:
            self.air_time += 1

    def gravity(self, on):
        if on:
            self.movement[1] += self.player_y_momentum * 1.5  # increase fall speed
            self.player_y_momentum += 0.2
        else:
            self.player_y_momentum = 0

    def collision(self, collision_types, type):
        for tile in self.tiles:
            if self.plr.colliderect(tile):
                if type == "horizontal":
                    if self.movement[0] > 0:  # check if moving right
                        self.plr.right = tile.left  # set the right side of the player to left side of tile
                        collision_types['right'] = True
                    elif self.movement[0] < 0:  # check if moving left
                        self.plr.left = tile.right  # set the left side of the player to right side of tile
                        collision_types['left'] = True
                if type == "vertical":
                    if self.movement[1] > 0:  # check if moving down
                        self.plr.bottom = tile.top  # set the bottom side of player to top side of tile
                        collision_types['bottom'] = True
                    elif self.movement[1] < 0:  # check if moving up
                        self.plr.top = tile.bottom  # set the top side of player to bottom side of tile
                        collision_types['top'] = True

    def move_control(self, event):                                  # 2
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                self.moving_right = True
            if event.key == K_LEFT:
                self.moving_left = True
            if event.key == K_UP:
                if self.air_time < 6:
                    self.player_y_momentum = -5
        if event.type == KEYUP:
            if event.key == K_RIGHT:
                self.moving_right = False
            if event.key == K_LEFT:
                self.moving_left = False








