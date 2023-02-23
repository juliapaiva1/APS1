import pygame
import numpy as np
from screen.game import Game
from screen.start import Start

pygame.init()

# Tamanho da tela e definição do FPS
size = np.array([1200,720])
screen = pygame.display.set_mode((size))
clock = pygame.time.Clock()
FPS = 60  # Frames per Second

window = {
    "start": Start(),
    "game": Game(),
}

status = {
    "current": "start",
    "running": True,
    "destroyedMeteor": 0,
    "life": 3,
}

while status["running"]:
    clock.tick(FPS)
    window[status["current"]].run(screen,status)
    pygame.display.update()

# Terminar tela
pygame.quit()