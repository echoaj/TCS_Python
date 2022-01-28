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

    def checkTouchMushtoom(self):
        if self.plrRect.colliderect(self.mshRect):
            print("Touching")