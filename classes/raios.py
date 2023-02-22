import numpy as np
import pygame

class Raios():
    all = []

    def __init__(self, mouse):
        self.s = np.array([600,360])
        self.v = np.array([10,10])
        self.direction = mouse
        self.radius = 5
        Raios.all.append(self)
    
    def update(self):
        v0 = self.direction - self.s
        v0 = v0 / np.linalg.norm(v0) * 100
        v0 = v0 + 3 * np.random.randn(2)
        self.v = v0
        self.s = self.s + 0.1 * self.v

    @classmethod
    def draw(cls, screen):
        for raio in Raios.all:
            pygame.draw.circle(screen, "red", raio.s, raio.radius, raio.radius)

    