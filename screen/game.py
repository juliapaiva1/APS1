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
        self.galaxy = pygame.transform.scale(pygame.image.load('assets/galaxy5.jpg'), (1200,720))
        self.earth = Planet(np.array([600, 360]), 50, 105000, "earth", pygame.transform.scale(pygame.image.load('assets/earth.png'), (140,140)), 70)
        self.moon = Planet(np.array([900, 320]), 15, 30000, "moon", pygame.transform.scale(pygame.image.load('assets/moon.png'), (42,42)), 20)

    def run(self,screen,status):
        self.getEvents(status)
        self.updatePos()
        #screen.blit(self.galaxy, (0,0))
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
            ac_moon = self.moon.gravity(met)
            ac = ac_earth + ac_moon
            met.update(ac)
            met.checkCollision(Raios.all)
            met.checkCollision(Planet.all)
        
        for raio in Raios.all:
            ac_moon = self.moon.gravity(raio)
            ac = ac_moon
            raio.update(ac)
            raio.checkCollision([p for p in Planet.all if p.name != "earth"])

        for planet in [p for p in Planet.all if p.name != "earth"]:
            planet.update()

    

    