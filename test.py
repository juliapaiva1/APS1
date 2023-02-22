import pygame
import numpy as np
from classes.meteoro import Meteoro
from classes.raios import Raios
from classes.planeta import Planet
pygame.init()

# Tamanho da tela e definição do FPS
pos = np.array([1200,720])
screen = pygame.display.set_mode((pos))
clock = pygame.time.Clock()
FPS = 60  # Frames per Second

qtdMeteoros = 10
for i in range(qtdMeteoros):
    Meteoro()

earth = Planet(np.array([600, 360]), 50)

rodando = True
while rodando:
    # Capturar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            Raios(pygame.mouse.get_pos())

    # Controlar frame rate
    clock.tick(FPS)

    # Processar posicoes
    for met in Meteoro.all:
        ac_earth = earth.gravity(100000, met)
        ac = ac_earth
        met.update(ac)
        met.checkCollision(Raios.all)
        met.checkCollision(Planet.all)
    
    for raio in Raios.all:
        raio.update()

    # Desenhar fundo
    screen.fill((0,0,0))

    # Desenhar personagem
    Meteoro.draw(screen)            
    Raios.draw(screen)
    Planet.draw(screen)

    # Update!
    pygame.display.update()

# Terminar tela
pygame.quit()