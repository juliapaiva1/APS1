import numpy as np
import pygame
import math

class Planet:
    all = []

    def __init__(self, pos, radius, gravConstant, name, sprite, posDiscount):
        self.s = pos
        self.radius = radius
        self.gravConstant = gravConstant
        self.name = name
        self.angle = 0
        self.sprite = sprite
        self.blitPos = self.s - posDiscount
        self.posDiscount = posDiscount
        Planet.all.append(self)
    
    @classmethod
    def draw(cls, screen):
        for pla in Planet.all:
            screen.blit(pla.sprite, pla.blitPos)

    def gravity(self, particle):
        direction_a = self.s - particle.s
        d = np.linalg.norm(direction_a)
        direction_a = direction_a / d
        mag_a = self.gravConstant / d**2
        a = direction_a * mag_a
        return a

    def update(self):
        self.s[0] = math.cos(self.angle) * 400 + 600
        self.s[1] = math.sin(self.angle) * 300 + 360
        self.blitPos = self.s - self.posDiscount
        self.angle += 0.0025