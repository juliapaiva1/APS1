import pygame
from classes.default import *

class Death:
    def __init__(self, status, screen):
        self.my_font = pygame.font.Font(None, 100)
        self.status = status
        self.screen = screen

    def run(self, window):
        self.update()
        self.getEvents(window)

    def getEvents(self, window):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.status["running"] = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.status["current"] = "start"
                self.status["life"] = 3
                self.status["destroyedMeteor"] = 0
                #window["game"] = Game(status, screen) 
    
    def update(self):
        self.screen.fill((0,0,0))
        title = self.my_font.render('AstroBirds', False, (255, 255, 255))
        score = self.my_font.render(f'Seu score foi: {self.status["destroyedMeteor"]}', False, (255, 255, 255))
        self.screen.blit(title,(300,360))
        self.screen.blit(score,(300,450))
