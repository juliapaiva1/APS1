import pygame
import numpy as np
from classes.meteoro import Meteoro
from classes.raios import Raios
from classes.planeta import Planet

class Game:
    def __init__(self, status, screen):
        Meteoro.all = []
        Planet.all = []
        Raios.all = []
        self.qtdMeteoro = 10
        for i in range(self.qtdMeteoro):
            Meteoro()
        self.font = pygame.font.Font(None, 50)
        self.font1 = pygame.font.Font(None, 30)
        self.galaxy = pygame.transform.scale(pygame.image.load('assets/galaxy5.jpg'), (1200,720))
        self.earth = Planet(np.array([600, 360]), 50, 105000, "earth", pygame.transform.scale(pygame.image.load('assets/earth.png'), (140,140)), 70)
        self.moon = Planet(np.array([900, 320]), 15, -15000, "moon", pygame.transform.scale(pygame.image.load('assets/moon.png'), (42,42)), 20)
        self.currentTime = 0
        self.lastWaveStart = 0
        self.status = status
        self.screen = screen
        self.vida = pygame.transform.scale(pygame.image.load('assets/vidas.png'), (50, 50))

    def run(self, window):
        self.wave()        
        self.checkgame()
        self.getEvents()
        self.updatePos()
        self.screen.fill((0,0,0))
        Meteoro.draw(self.screen)            
        Raios.draw(self.screen)
        Planet.draw(self.screen)
        self.draw()
    
    def getEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.status["running"] = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                Raios(pygame.mouse.get_pos())

    def updatePos(self):
        for met in Meteoro.all:
            ac_earth = self.earth.gravity(met)
            ac_moon = self.moon.gravity(met)
            ac = ac_earth + ac_moon
            met.update(ac)
            met.checkCollisionR(Raios.all, self.status)
            met.checkCollisionP(Planet.all, self.status)
        
        for raio in Raios.all:
            ac_moon = self.moon.gravity(raio)
            ac = ac_moon
            raio.update(ac)

        for planet in [p for p in Planet.all if p.name != "earth"]:
            planet.update()
    
    def checkgame(self):
        if self.status["life"] == 0:
            self.status["current"] = "death"
            time = self.currentTime - self.status["gameDuration"]
            if time/60000 < 1:
                self.status["gameDuration"] = f'{(time/1000):.1f} segundos'
            else: 
                self.status["gameDuration"] = f'{(time/60000):.2f} minutos'

    def lives(self, x, y, lives, img):
        for i in range(lives):
            img_rect = img.get_rect()
            img_rect.x = x + 30 * i
            img_rect.y = y
            self.screen.blit(img, img_rect)
    
    def draw(self):
        destroyedMeteor = self.font.render(str(self.status["destroyedMeteor"]), False, (255,255,255))
        waveCount = self.font1.render("Wave: "+str(self.status["wave"]), False, (255,255,255))
        vidas = self.font1.render("Vidas:", False, (255,255,255))
        self.screen.blit(destroyedMeteor,(10,5))
        self.screen.blit(waveCount,(85,14))
        self.screen.blit(vidas,(340,14))
        self.lives(400, 3, self.status["life"], self.vida)

    def wave(self):
        self.currentTime = pygame.time.get_ticks()
        if self.currentTime - self.lastWaveStart > 20000:
            self.lastWaveStart = pygame.time.get_ticks()
            self.status["wave"] += 1
            for i in range(2):
                Meteoro()
    

    