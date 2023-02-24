import pygame
import numpy as np
from classes.default import default

pygame.init()

# Tamanho da tela e definição do FPS
size = np.array([1200,720])
screen = pygame.display.set_mode((size))
clock = pygame.time.Clock()
FPS = 60  # Frames per Second

window, status = default(screen)

while status["running"]:
    clock.tick(FPS)
    window[status["current"]].run(window)
    pygame.display.update()

# Terminar tela
pygame.quit()