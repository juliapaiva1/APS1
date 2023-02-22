import pygame

class Start:
    def __init__(self):
        self.my_font = pygame.font.Font(None, 100)

    def run(self,screen,status):
        self.update(screen)
        self.getEvents(status)

    def getEvents(self,status):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                status["running"] = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                status["current"] = "game"
    
    def update(self, screen):
        screen.fill((0,0,0))
        title = self.my_font.render('AstroBirds', False, (255, 255, 255))
        play = self.my_font.render('Clique para jogar!', False, (255, 255, 255))
        screen.blit(title,(300,360))
        screen.blit(play,(300,450))