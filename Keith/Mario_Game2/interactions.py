import pygame as pg


class Interaction:
    def __init__(self, plr, gmb, msh):
        self.plr = plr
        self.gmb = gmb
        self.msh = msh
        self.plrRect = plr.plr
        self.gmbRect = gmb.enm
        self.mshRect = msh.msh

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

    def checkTouchMushroom(self):
        if self.plrRect.colliderect(self.mshRect):
            self.plr.img = self.plr.img_big
            self.plr.img_jump = self.plr.img_big
            self.msh.msh.x = -200