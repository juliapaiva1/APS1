import pygame
from classes.default import *

class Death:
    def __init__(self):
        self.my_font = pygame.font.Font(None, 100)

    def run(self,screen,status, window):
        self.update(screen, status)
        self.getEvents(status, window)

    def getEvents(self, status, window):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                status["running"] = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                status["current"] = "start"
                status["life"] = 3
                status["destroyedMeteor"] = 0
    
    def update(self, screen, status):
        screen.fill((0,0,0))
        title = self.my_font.render('AstroBirds', False, (255, 255, 255))
        score = self.my_font.render(f'Seu score foi: {status["destroyedMeteor"]}', False, (255, 255, 255))
        screen.blit(title,(300,360))
        screen.blit(score,(300,450))
