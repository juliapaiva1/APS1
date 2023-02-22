import numpy as np
import pygame

class Planet:
    all = []

    def __init__(self, pos, radius):
        self.s = pos
        self.radius = radius
        Planet.all.append(self)
    
    @classmethod
    def draw(cls, screen):
        for pla in Planet.all:
            pygame.draw.circle(screen, "red", pla.s, pla.radius, pla.radius)

    def gravity(self, constante, particula):
        direcao_a = self.s - particula.s
        d = np.linalg.norm(direcao_a)
        direcao_a = direcao_a / d
        mag_a = constante / d**2
        a = direcao_a * mag_a
        return a


