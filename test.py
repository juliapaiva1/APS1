import pygame
import numpy as np
from classes.meteoro import Meteoro
from classes.raios import Raios
from classes.planeta import Planet
from screen.game import Game
from screen.start import Start

pygame.init()

# Tamanho da tela e definição do FPS
pos = np.array([1200,720])
screen = pygame.display.set_mode((pos))
clock = pygame.time.Clock()
FPS = 60  # Frames per Second

screens = {
    "start": Start(),
    "game": Game()
}

status = {
    "current": "start",
    "running": True,
}

while status["running"]:
    clock.tick(FPS)
    screens[status["current"]].run(screen,status)
    pygame.display.update()

# Terminar tela
pygame.quit()