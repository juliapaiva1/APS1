import numpy as np
import pygame
import math

class Planet:
    all = []

    def __init__(self, pos, radius, color, gravConstant, name):
        self.s = pos
        self.radius = radius
        self.color = color
        self.gravConstant = gravConstant
        self.name = name
        self.angle = 0
        Planet.all.append(self)
    
    @classmethod
    def draw(cls, screen):
        for pla in Planet.all:
            pygame.draw.circle(screen, pla.color, pla.s, pla.radius, pla.radius)

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
        self.angle += 0.0025