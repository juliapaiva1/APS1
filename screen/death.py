import pygame
from screen.game import Game
from classes.default import defaultStatus

class Death:
    def __init__(self, status, screen):
        self.font = pygame.font.Font(None, 100)
        self.font1 = pygame.font.Font(None, 30)
        self.status = status
        self.screen = screen
        self.title = ""
        self.score = ""
        self.time = ""

    def run(self, window):
        '''Faz a chamada de todas as funcoes necessarias para renderizar a essa tela.'''
        self.draw()
        self.getEvents(window)

    def getEvents(self, window):
        '''Recebe inputs do jogador. Reinicia o status e tela Game para iniciar um novo jogo.'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.status["running"] = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                defaultStatus(self.status)
                window["game"] = Game(self.status, self.screen) 
        
    def draw(self):
        '''Desenha na tela os indicadores de game status.'''
        self.textRender()
        self.screen.fill((0,0,0))
        self.screen.blit(self.title,(300,360))
        self.screen.blit(self.score,(300,450))
        self.screen.blit(self.time,(300,560))
    
    def textRender(self):
        '''Renderiza o titulo e indicadores de pontuacao e tempo.'''
        self.title = self.font.render('AstroBirds', False, (255, 255, 255))
        self.score = self.font1.render(f'Seu score foi: {self.status["destroyedMeteor"]}', False, (255, 255, 255))
        self.time = self.font1.render(str(self.status["gameDuration"]), False, (255, 255, 255))