import numpy as np
import pygame
import random

class Meteoro:
    all = []

    def __init__(self):
        pos = random.randint(1,2)
        self.s = Meteoro.setPos(self, pos)
        self.v = Meteoro.setSpeed(self, pos)
        self.radius = 8
        Meteoro.all.append(self)

    @classmethod
    def draw(cls, screen):
        for met in Meteoro.all:
            pygame.draw.circle(screen, "green", met.s, met.radius, met.radius)
    
    def setPos(self, pos):
        match pos:
            case 1: return np.array([random.randint(-200,0), random.randint(0,720)]) 
            case 2: return np.array([random.randint(1200,1400), random.randint(0,720)]) 
    
    def setSpeed(self, pos):
        match pos:
            case 1: return np.array([50, 20])
            case 2: return np.array([-50, 20])

    def resetPos(self):
        pos = random.randint(1,2)
        self.s = Meteoro.setPos(self, pos)
        self.v = Meteoro.setSpeed(self, pos)

    def update(self, aceleracao):
        self.v = self.v + aceleracao
        self.s = self.s + 0.01 * self.v

    def checkCollision(self, particula):
        for part in particula:
            if np.linalg.norm(self.s - part.s) <= part.radius + self.radius:
                self.resetPos()