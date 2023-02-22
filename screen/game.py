import pygame
import numpy as np
from classes.meteoro import Meteoro
from classes.raios import Raios
from classes.planeta import Planet

class Game:
    def __init__(self):
        self.qtdMeteoro = 10
        for i in range(self.qtdMeteoro):
            Meteoro()
        self.earth = Planet(np.array([600, 360]), 50, "blue", 100000, "earth")
        self.mars = Planet(np.array([1000, 220]), 15, "red", 10000, "mars")

    def run(self,screen,status):
        self.getEvents(status)
        self.updatePos()
        screen.fill((0,0,0))
        Meteoro.draw(screen)            
        Raios.draw(screen)
        Planet.draw(screen)
    
    def getEvents(self,status):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                status["running"] = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                Raios(pygame.mouse.get_pos())

    def updatePos(self):
        for met in Meteoro.all:
            ac_earth = self.earth.gravity(met)
            ac_mars = self.mars.gravity(met)
            ac = ac_earth + ac_mars
            met.update(ac)
            met.checkCollision(Raios.all)
            met.checkCollision(Planet.all)
        
        for raio in Raios.all:
            ac_mars = self.mars.gravity(raio)
            ac = ac_mars
            raio.update(ac)
            raio.checkCollision([p for p in Planet.all if p.name != "earth"])

        for planet in Planet.all:
            planet.update()

    

    