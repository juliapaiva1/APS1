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

earth = Planet(np.array([600, 360]), 50, "blue", 100000, "earth")
mars = Planet(np.array([1000, 220]), 15, "red", 10000, "mars")

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
        ac_earth = earth.gravity(met)
        ac_mars = mars.gravity(met)
        ac = ac_earth + ac_mars
        met.update(ac)
        met.checkCollision(Raios.all)
        met.checkCollision(Planet.all)
    
    for raio in Raios.all:
        ac_mars = mars.gravity(raio)
        ac = ac_mars
        raio.update(ac)
        raio.checkCollision([p for p in Planet.all if p.name != "earth"])

    for planet in Planet.all:
        planet.update()

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