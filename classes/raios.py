import numpy as np
import pygame

class Raios():
    '''Classe que gera os disparos utilizados para destruir asteroides'''

    all = []
    def __init__(self, mouse):
        self.s = np.array([600,360])
        self.v = np.array([10,10])
        self.direction = (mouse - self.s) / np.linalg.norm(mouse - self.s) * 100
        self.radius = 5
        Raios.all.append(self)

    @classmethod
    def draw(cls, screen):
        for raio in Raios.all:
            pygame.draw.circle(screen, "red", raio.s, raio.radius, raio.radius)

    @classmethod
    def clear(cls):
        cls.all = []
    
    def update(self, aceleracao):
        '''Atualiza a posicao da particula utilizando uma resultante gravitacional como aceleracao'''
        self.v = self.direction
        self.s = self.s + 0.07 * self.v + aceleracao
    
    def checkPosition(self):
        '''Verifica se a particula esta fora da tela, em seguida, a exclui.'''
        if self.s[0] < 0 or self.s[0] > 1200 or self.s[1] < 0 or self.s[1] > 720:
            Raios.all.remove(self)
    
        
        