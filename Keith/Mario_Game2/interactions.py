import pygame as pg

class Interaction:
    def __init__(self, plr, gmb):
        self.plr = plr
        self.gmb = gmb
        self.plrRect = plr.plr
        self.gmbRect = gmb.enm

    def checkGoombaStomped(self):
        if not self.plr.state["dead"]:
            if self.plrRect.colliderect(self.gmbRect):
                if self.plr.movement[1] > 1:
                    self.gmb.state["stomped"] = True

    def checkTouchGombaSide(self):
        if not self.gmb.state["stomped"]:
            if self.plrRect.colliderect(self.gmbRect):
                if self.plr.movement[1] < 1:
                    self.plr.state["dead"] = True