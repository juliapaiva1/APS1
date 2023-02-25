import numpy as np
import pygame
import math

class Planet:
    all = []
    def __init__(self, pos, radius, gravConstant, name, img, imgPosDiscount):
        self.s = pos
        self.radius = radius
        self.gravConstant = gravConstant
        self.name = name
        self.angle = 0
        self.img = img
        self.blitPos = self.s - imgPosDiscount
        self.imgPosDiscount = imgPosDiscount
        Planet.all.append(self)
    
    @classmethod
    def draw(cls, screen):
        for pla in Planet.all:
            screen.blit(pla.img, pla.blitPos)
    
    @classmethod
    def clear(cls):
        cls.all = []

    def gravity(self, particle):
        '''Utiliza o recurso Distancia entre pontos do Numpy para calcular 
        o vetor resultante de aceleração entre particula e planeta.
        '''
        direction_a = self.s - particle.s
        d = np.linalg.norm(direction_a)
        direction_a = direction_a / d
        mag_a = self.gravConstant / d**2
        a = direction_a * mag_a
        return a

    def update(self):
        '''Calcula a posicao do planeta utilizando Trigonometria'''
        self.s[0] = math.cos(self.angle) * 400 + 600
        self.s[1] = math.sin(self.angle) * 300 + 360
        self.blitPos = self.s - self.imgPosDiscount
        self.angle += 0.0025