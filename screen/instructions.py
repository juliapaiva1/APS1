import pygame

class Instructions:
    '''Classe para renderizar tela de Instruções. Redireciona para tela Game.'''

    def __init__(self, status, screen):
        self.status = status
        self.screen = screen
        self.background = pygame.image.load("assets/instrucoes.png")
        self.playBtn = pygame.Rect((450, 550), (270,60))

    def run(self, window):
        '''Faz a chamada de todas as funcoes necessarias para renderizar a essa tela.'''
        self.draw()
        self.getEvents()
    
    def getEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.status["running"] = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if self.playBtn.collidepoint(mouse):
                    self.status["current"] = "game"
                    self.status["gameDuration"] = pygame.time.get_ticks()
        
    def draw(self):
        self.screen.blit(self.background, (0,0))
        


