import pygame
from screen.game import Game
from classes.default import defaultStatus

class Death:
    def __init__(self, status, screen):
        self.font = pygame.font.Font(None, 100)
        self.font1 = pygame.font.Font(None, 30)
        self.status = status
        self.screen = screen

    def run(self, window):
        self.update()
        self.getEvents(window)

    def getEvents(self, window):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.status["running"] = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                defaultStatus(self.status)
                window["game"] = Game(self.status, self.screen) 
    
    def update(self):
        self.screen.fill((0,0,0))
        title = self.font.render('AstroBirds', False, (255, 255, 255))
        score = self.font1.render(f'Seu score foi: {self.status["destroyedMeteor"]}', False, (255, 255, 255))
        time = self.font1.render(str(self.status["gameDuration"]), False, (255, 255, 255))
        self.screen.blit(title,(300,360))
        self.screen.blit(score,(300,450))
        self.screen.blit(time,(300,560))