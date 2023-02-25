import pygame
import numpy as np
from classes.default import defaultStatus
from screen.game import Game
from screen.start import Start
from screen.death import Death
from screen.instructions import Instructions

pygame.init()

# Tamanho da tela e definição do FPS
size = np.array([1200,720])
screen = pygame.display.set_mode((size))
clock = pygame.time.Clock()
FPS = 120  # Frames per Second

status = defaultStatus({})

window = {
    "start": Start(status,screen),
    "game": Game(status,screen),
    "death": Death(status,screen),
    "instructions": Instructions(status, screen)
}  

while status["running"]:
    clock.tick(FPS)
    window[status["current"]].run(window)
    pygame.display.update()

# Terminar tela
pygame.quit()