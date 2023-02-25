import pygame
from classes.default import defaultStatus

class Death:
    def __init__(self, status, screen):
        self.font = pygame.font.Font(None, 50)
        self.font1 = pygame.font.Font(None, 30)
        self.background = pygame.image.load('assets/gameOver.png')
        self.title, self.score, self.wave = "", "", ""
        self.playBtn = pygame.Rect((345, 600), (505,60))
        self.status = status
        self.screen = screen

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
                self.status["current"] = "start" 
                defaultStatus(self.status)
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if self.playBtn.collidepoint(mouse):
                    self.status["current"] = "start" 
                    defaultStatus(self.status)
                           
    def draw(self):
        '''Desenha na tela os indicadores de game status.'''
        self.textRender()
        self.screen.blit(self.background,(0,0))
        self.screen.blit(self.wave,(815,543))
        self.screen.blit(self.score,(765,443))
        self.screen.blit(self.time,(700,494))
    
    def textRender(self):
        '''Renderiza o titulo e indicadores de pontuacao e tempo.'''
        self.score = self.font.render(str(self.status["destroyedMeteor"]), False, (255, 255, 255))
        self.time = self.font.render(str(self.status["gameDuration"]), False, (255, 255, 255))
        self.wave = self.font.render(str(self.status["wave"]), False, (255, 255, 255))