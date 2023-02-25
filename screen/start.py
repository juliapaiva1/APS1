import pygame

class Start:
    def __init__(self, status, screen):
        self.background = pygame.image.load('assets/Astrobirds.png')
        self.status = status
        self.screen = screen
        self.playBtn = pygame.Rect((345, 450), (505,60))
        self.instructionBtn = pygame.Rect((435, 510), (330,60))

    def run(self, window):
        self.draw()
        self.getEvents()

    def getEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.status["running"] = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.status["current"] = "game"
                self.status["gameDuration"] = pygame.time.get_ticks()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if self.playBtn.collidepoint(mouse):
                    self.status["current"] = "game"
                    self.status["gameDuration"] = pygame.time.get_ticks()
                if self.instructionBtn.collidepoint(mouse):
                    self.status["current"] = "instructions"
    
    def draw(self):
        self.screen.blit(self.background, (0,0))

