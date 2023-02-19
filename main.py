import pygame
import math

x = 1200
y = 720

fundo = pygame.image.load('6789.jpg')
terra = pygame.image.load('terra.png')
canhao = pygame.image.load('5332.png')
canhao = pygame.transform.scale(canhao, (200, 200))

pygame.display.set_caption('Astrobirds')

win = pygame.display.set_mode((x, y))

clock = pygame.time.Clock()

gameover = False

class Terra(object):
    def __init__(self):
        self.img_terra = terra
        self.largura = self.img_terra.get_width()
        self.altura = self.img_terra.get_height()
        self.x_terra = 80
        self.y_terra = 450

    def desenha_terra(self):
        win.blit(self.img_terra, [self.x_terra, self.y_terra, self.largura, self.altura])
        pygame.display.update()

class Atirador(object):
    def __init__(self):
        self.img = canhao
        self.largura = self.img.get_width()
        self.altura = self.img.get_height()
        self.x_canhao = 80
        self.y_canhao = 450
        self.angulo = 0
        self.rotacao_superficie = pygame.transform.rotate(self.img, self.angulo) 
        self.rotacao_retangulo = self.rotacao_superficie.get_rect()
        self.rotacao_retangulo.center = (self.x_canhao, self.y_canhao) 
        self.cosseno = math.cos(math.radians(self.angulo + 45))
        self.seno = math.sin(math.radians(self.angulo + 45))
        self.direcao_tiro = (self.x_canhao + self.cosseno * self.largura//2, self.y_canhao - self.seno * self.altura//2)

    def terra(self):
        self.img_terra = terra
        self.largura_terra = self.img_terra.get_width()
        self.altura_terra = self.img_terra.get_height()
        self.x_terra = 80
        self.y_terra = 450

    def desenha(self, win):
        #win.blit(terra.img_terra, [terra.x_terra, terra.y_terra, terra.largura, terra.altura])
        #Terra.desenha_terra(self)
        win.blit(self.img, [self.x_canhao, self.y_canhao, self.largura, self.altura])
        win.blit(fundo, (0, 0))
        win.blit(self.rotacao_superficie, self.rotacao_retangulo)
        #win.blit(terra.img_terra, [terra.x_terra, terra.y_terra, terra.largura, terra.altura])

    def gira_esquerda(self):
        if self.angulo <55:
            self.angulo += 5 
        self.rotacao_superficie = pygame.transform.rotate(self.img, self.angulo)
        self.rotacao_retangulo = self.rotacao_superficie.get_rect()
        self.rotacao_retangulo.center = (self.x_canhao, self.y_canhao)
        self.cosseno = math.cos(math.radians(self.angulo + 45))
        self.seno = math.sin(math.radians(self.angulo + 45))
        self.direcao_tiro = (self.x_canhao + self.cosseno * self.largura//2, self.y_canhao - self.seno * self.altura//2)

    def gira_direita(self):
        if self.angulo >-60:
            self.angulo -= 5 
        self.rotacao_superficie = pygame.transform.rotate(self.img, self.angulo)
        self.rotacao_retangulo = self.rotacao_superficie.get_rect()
        self.rotacao_retangulo.center = (self.x_canhao, self.y_canhao)
        self.cosseno = math.cos(math.radians(self.angulo + 45))
        self.seno = math.sin(math.radians(self.angulo + 45))
        self.direcao_tiro = (self.x_canhao + self.cosseno * self.largura//2, self.y_canhao - self.seno * self.altura//2)

class Raios(object):
    def __init__(self):
        self.mira = atirador.direcao_tiro
        self.x, self.y = self.mira
        self.w = 50
        self.h = 5
        self.cos = atirador.cosseno
        self.sen = atirador.seno
        self.velocidade_x = self.cos * 10
        self.velocidade_y = self.sen * 10

    def percurso(self):
        self.x += self.velocidade_x
        self.y -= self.velocidade_y

    def desenha_raio(self, win):
        pygame.draw.rect(win, (178, 34, 34), [self.x, self.y, self.w, self.h])





def redesenha_tela():
    win.blit(fundo, (0,0))
    atirador.desenha(win)
    for raio in raios:
        raio.desenha_raio(win)
    pygame.display.update()

atirador = Atirador()
raios = []
run = True
while run:
    clock.tick(60)
    if not gameover:
        for raio in raios:
            raio.percurso()



        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]:
            atirador.gira_esquerda()
        if teclas[pygame.K_RIGHT]:
            atirador.gira_direita()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not gameover:
                    raios.append(Raios())

    redesenha_tela()

pygame.quit()