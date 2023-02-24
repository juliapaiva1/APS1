import pygame

class Start:
    def __init__(self, status, screen):
        self.my_font = pygame.font.Font(None, 100)
        self.background = pygame.image.load('assets/AStrobirds.png')
        self.status = status
        self.screen = screen

    def run(self, window):
        self.draw()
        self.getEvents()

    def getEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.status["running"] = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.status["current"] = "game"
                self.status["gameDuration"] = pygame.time.get_ticks()
    
    def draw(self):
        self.screen.blit(self.background, (0,0))