import numpy as np
import pygame

class Planet:
    all = []

    def __init__(self, pos, radius, color, gravConstant, name):
        self.s = pos
        self.radius = radius
        self.color = color
        self.gravConstant = gravConstant
        self.name = name
        Planet.all.append(self)
    
    @classmethod
    def draw(cls, screen):
        for pla in Planet.all:
            pygame.draw.circle(screen, pla.color, pla.s, pla.radius, pla.radius)

    def gravity(self, particula):
        direcao_a = self.s - particula.s
        d = np.linalg.norm(direcao_a)
        direcao_a = direcao_a / d
        mag_a = self.gravConstant / d**2
        a = direcao_a * mag_a
        return a

    def update(self):
        pass

