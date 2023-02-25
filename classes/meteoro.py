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
        self.imgPosDiscount = 11
        self.blitPos = self.s - self.imgPosDiscount
        Meteoro.all.append(self)

    @classmethod
    def draw(cls, screen):
        for met in Meteoro.all:
            pygame.draw.circle(screen, "green", met.s, met.radius, met.radius)
            screen.blit(met.sprite, met.blitPos)
    
    @classmethod
    def clear(cls):
        cls.all = []
    
    def setPos(self, pos):
        '''Gerador randomico de posicao.'''
        match pos:
            case 1: return np.array([random.randint(-200,0), random.randint(0,720)]) 
            case 2: return np.array([random.randint(1200,1400), random.randint(0,720)]) 
    
    def setSpeed(self, pos):
        '''Gerador randomico de velocidade'''
        match pos:
            case 1: return np.array([20, 10])
            case 2: return np.array([-20, 10])

    def resetPos(self):
        '''Gera nova velocidade e posicao para particula'''
        pos = random.randint(1,2)
        self.s = Meteoro.setPos(self, pos)
        self.v = Meteoro.setSpeed(self, pos)

    def update(self, aceleracao):
        '''Atualiza a posicao da particula utilizando uma resultante gravitacional como aceleracao'''
        self.v = self.v + aceleracao
        self.s = self.s + 0.01 * self.v
        self.blitPos = self.s - self.imgPosDiscount

    def checkCollisionP(self, particula, status):
        '''Verifica colisao entre meteoro e planetas. Reduz a vida caso a colisão tenha ocorrido com a Terra.'''
        for part in particula:
            if np.linalg.norm(self.s - part.s) <= part.radius + self.radius:
                self.resetPos()
                if part.name == "earth":
                    status["life"] -= 1
    
    def checkCollisionR(self, raios, status):
        '''Verifica colisao entre meteoro e raios'''
        for raio in raios:
            if np.linalg.norm(self.s - raio.s) <= raio.radius + self.radius:
                self.resetPos()
                status["destroyedMeteor"] += 1
