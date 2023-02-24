import pygame

class Start:
    def __init__(self, status, screen):
        self.my_font = pygame.font.Font(None, 100)
        self.status = status
        self.screen = screen

    def run(self, window):
        self.update()
        self.getEvents()

    def getEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.status["running"] = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.status["current"] = "game"
                self.status["gameDuration"] = pygame.time.get_ticks()
    
    def update(self):
        self.screen.fill((0,0,0))
        title = self.my_font.render('AstroBirds', False, (255, 255, 255))
        play = self.my_font.render('Clique para jogar!', False, (255, 255, 255))
        self.screen.blit(title,(300,360))
        self.screen.blit(play,(300,450))