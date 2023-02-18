import pygame

pygame.init()

x=1200
y=720

screen = pygame.display.set_mode((x, y))
pygame.display.set_caption('Astrobirds')

fundo = pygame.image.load('6789.jpg').convert_alpha()
fundo = pygame.transform.scale(fundo, (x,y))

terra = pygame.image.load('terra.png').convert_alpha()
terra = pygame.transform.scale(terra, (300, 300))

canhao = pygame.image.load('1873.png').convert_alpha()
canhao = pygame.transform.scale(canhao, (150, 150))

pos_canhao_x = -30
pos_canhao_y = 450

pos_terra_x = -30
pos_terra_y = 500

rodando = True

angulo = 0

while rodando: 
    angulo += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

        if event.type == pygame.KEYDOWN:
            screen.blit(pygame.transform.rotate(canhao, angulo), (pos_canhao_x, pos_canhao_y))
           



    screen.blit(fundo, (0, 0))
    screen.blit(terra, (pos_terra_x, pos_terra_y))
    screen.blit(canhao, (pos_canhao_x, pos_canhao_y))
    pygame.display.flip()
    pygame.display.update()