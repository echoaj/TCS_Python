import json
import pygame as pg


def get_level(num):
    directory = f"./levels/lvl{num}.json"
    with open(directory, "r") as file:
        data = json.load(file)
    return data["tile_map"]


def get_image(path, size):
    img = pg.image.load(path)
    img = pg.transform.scale(img, (size, size))
    return img