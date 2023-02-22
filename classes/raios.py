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

    @classmethod
    def draw(cls, screen):
        for raio in Raios.all:
            pygame.draw.circle(screen, "red", raio.s, raio.radius, raio.radius)
    
    def update(self, aceleracao):
        v0 = self.direction - self.s
        v0 = v0 / np.linalg.norm(v0) * 100
        v0 = v0 + 3 * np.random.randn(2)
        self.v = v0
        self.s = self.s + 0.1 * self.v + aceleracao
    
    def checkCollision(self, planets):
        for planet in planets:
            if np.linalg.norm(self.s - planet.s) <= planet.radius + self.radius:
                Raios.all.remove(self)
    