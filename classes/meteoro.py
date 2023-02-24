import numpy as np
import pygame
import random

class Meteoro():
    all = []

    def __init__(self):
        pos = random.randint(1,2)
        self.s = Meteoro.setPos(self, pos)
        self.v = Meteoro.setSpeed(self, pos)
        self.radius = 8
        self.sprite = pygame.transform.scale(pygame.image.load('assets/asteroide.png'), (20,20))
        self.posDiscount = 11
        self.blitPos = self.s - self.posDiscount
        Meteoro.all.append(self)

    @classmethod
    def draw(cls, screen):
        for met in Meteoro.all:
            pygame.draw.circle(screen, "green", met.s, met.radius, met.radius)
            screen.blit(met.sprite, met.blitPos)
    
    def setPos(self, pos):
        match pos:
            case 1: return np.array([random.randint(-200,0), random.randint(0,720)]) 
            case 2: return np.array([random.randint(1200,1400), random.randint(0,720)]) 
    
    def setSpeed(self, pos):
        match pos:
            case 1: return np.array([20, 10])
            case 2: return np.array([-20, 10])

    def resetPos(self):
        pos = random.randint(1,2)
        self.s = Meteoro.setPos(self, pos)
        self.v = Meteoro.setSpeed(self, pos)

    def update(self, aceleracao):
        self.v = self.v + aceleracao
        self.s = self.s + 0.01 * self.v
        self.blitPos = self.s - self.posDiscount

    def checkCollisionP(self, particula, status):
        for part in particula:
            if np.linalg.norm(self.s - part.s) <= part.radius + self.radius:
                self.resetPos()
                if part.name == "earth":
                    status["life"] -= 1
    
    def checkCollisionR(self, raios, status):
        for raio in raios:
            if np.linalg.norm(self.s - raio.s) <= raio.radius + self.radius:
                self.resetPos()
                status["destroyedMeteor"] += 1
