import numpy as np
import pygame
import random

class Meteoro:
    all = []
    
    def __init__(self):
        part = random.randint(1,2)
        self.s = Meteoro.setPos(self, part)
        self.v = Meteoro.setSpeed(self, part)
        self.radius = 8
        Meteoro.all.append(self)

    @classmethod
    def draw(cls, screen):
        for met in Meteoro.all:
            pygame.draw.circle(screen, "green", met.s, met.radius, met.radius)
    
    def setPos(self, part):
        match part:
            case 1: return np.array([random.randint(-400,0), random.randint(0,720)]) 
            case 2: return np.array([random.randint(1200,1800), random.randint(0,720)]) 
    
    def setSpeed(self, part):
        match part:
            case 1: return np.array([50, 20])
            case 2: return np.array([-50, 20])

    def resetPos(self):
        part = random.randint(1,2)
        self.s = Meteoro.setPos(self, part)
        self.v = Meteoro.setSpeed(self, part)

    def update(self, aceleracao):
        self.v = self.v + aceleracao
        self.s = self.s + 0.01 * self.v

    def checkCollision(self, particula):
        for part in particula:
            if np.linalg.norm(self.s - part.s) <= part.radius + self.radius:
                self.resetPos()