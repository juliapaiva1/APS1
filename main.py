import pygame
import numpy as np
from classes.default import defaultStatus
from screens.game import Game
from screens.start import Start
from screens.death import Death
from screens.instructions import Instructions

pygame.init()

size = np.array([1200,720])
screen = pygame.display.set_mode((size))
clock = pygame.time.Clock()
FPS = 120  # Frames per Second

# Definicoes para basicas para o jogo
status = defaultStatus({})

# Hub para as telas 
window = {
    "start": Start(status,screen),
    "instructions": Instructions(status, screen),
    "game": Game(status,screen),
    "death": Death(status,screen)
}  

while status["running"]:
    clock.tick(FPS)
    window[status["current"]].run(window)
    pygame.display.update()

pygame.quit()