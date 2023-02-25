import pygame
import numpy as np
from classes.meteoro import Meteoro
from classes.raios import Raios
from classes.planeta import Planet

class Game:
    ''' Classe que renderiza a tela de jogo.'''

    def __init__(self, status, screen):
        '''Gera os meteoros e planetas, carrega os assets, e inicia as variaveis necessarias.'''
        Meteoro.clear()
        Planet.clear()
        Raios.clear()
        self.qtdMeteoro = 8
        for i in range(self.qtdMeteoro):
            Meteoro()
        self.font, self.font1 = pygame.font.Font(None, 50), pygame.font.Font(None, 30)
        self.vida = pygame.transform.scale(pygame.image.load('assets/vidas.png'), (50, 50))
        self.earth = Planet(np.array([600, 360]), 50, 24000, "earth", pygame.transform.scale(pygame.image.load('assets/earth.png'), (140,140)), 70)
        self.moon = Planet(np.array([900, 320]), 15, -5000, "moon", pygame.transform.scale(pygame.image.load('assets/moon.png'), (42,42)), 20)
        self.currentTime, self.lastWaveStart = 0, status["gameStart"]
        self.textDestroyedMeteor, self.textWaveCount, self.textVidas = '','',''
        self.status = status
        self.screen = screen

    def run(self, window):
        '''Faz a chamada de todas as funcoes necessarias para renderizar a essa tela.'''
        self.wave()        
        self.checkgame()
        self.getEvents()
        self.updatePos()
        self.draw()
        Meteoro.draw(self.screen)            
        Raios.draw(self.screen)
        Planet.draw(self.screen)
    
    def getEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.status["running"] = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                Raios(pygame.mouse.get_pos())

    def updatePos(self):
        ''' Passa por todas as particulas renderizadas: 
        Atualiza a resultante de aceleração e verifica colisões entre objetos.
        '''
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
            raio.checkPosition()

        for planet in [p for p in Planet.all if p.name != "earth"]:
            planet.update()
    
    def checkgame(self):
        '''Verifica se o player ficou sem vidas. 
        Aponta o status para a tela seguinte e calcula o tempo de jogo.
        '''
        if self.status["life"] == 0:
            self.status["current"] = "death"
            time = self.currentTime - self.status["gameStart"]
            if time/60000 < 1:
                self.status["gameDuration"] = f'{(time/1000):.1f} segundos'
            else: 
                self.status["gameDuration"] = f'{(time/60000):.2f} minutos'
    
    def draw(self):
        '''Desenha na tela os indicadores de game status.'''
        self.textRender()
        self.screen.fill((0,0,0))
        self.screen.blit(self.textDestroyedMeteor,(10,5))
        self.screen.blit(self.textWaveCount,(85,14))
        self.screen.blit(self.textVidas,(340,14))
        self.lives(400, 3)
    
    def textRender(self):
        '''Renderiza os indicadores de quantidade de meteoros destruidos, wave atual e vidas.'''
        self.textDestroyedMeteor = self.font.render(str(self.status["destroyedMeteor"]), False, (255,255,255))
        self.textWaveCount = self.font1.render("Wave: "+str(self.status["wave"]), False, (255,255,255))
        self.textVidas = self.font1.render("Vidas:", False, (255,255,255))

    def lives(self, x, y):
        '''De acordo com a quantidade de vidas, renderiza os coracoes na tela.'''
        for i in range(self.status["life"]):
            img_rect = self.vida.get_rect()
            img_rect.x = x + 30 * i
            img_rect.y = y
            self.screen.blit(self.vida, img_rect)

    def wave(self):
        '''Calcula delta de tempo entre waves para atualizar a quantidade de asteroides na tela.'''
        self.currentTime = pygame.time.get_ticks()
        if self.currentTime - self.lastWaveStart > 20000:
            self.lastWaveStart = pygame.time.get_ticks()
            self.status["wave"] += 1
            for i in range(2):
                Meteoro()
    

    