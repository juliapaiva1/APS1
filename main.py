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


class Atirador(object):
    def __init__(self):
        self.img = canhao
        self.largura = self.img.get_width()
        self.altura = self.img.get_height()
        self.x_canhao = 0
        self.y_canhao = 350
        self.angulo = 0
        self.rotacao_superficie = pygame.transform.rotate(self.img, self.angulo) 
        self.rotacao_retangulo = self.rotacao_superficie.get_rect()
        self.rotacao_retangulo.center = (self.x_canhao, self.y_canhao)
        self.cosseno = math.cos(math.radians(self.angulo + 45))
        self.seno = math.sin(math.radians(self.angulo + 45))
        self.direcao_tiro = (self.x_canhao + self.cosseno * self.largura//2, self.y_canhao - self.seno * self.altura//2)

    def desenha(self, win):
        win.blit(self.img, [self.x_canhao, self.y_canhao, self.largura, self.altura])
        win.blit(self.rotacao_superficie, self.rotacao_retangulo)

    def gira_esquerda(self):
        self.angulo += 5
        self.rotacao_superficie = pygame.transform.rotate(self.img, self.angulo)
        self.rotacao_retangulo = self.rotacao_superficie.get_rect()
        self.rotacao_retangulo.center = (self.x_canhao, self.y_canhao)
        self.cosseno = math.cos(math.radians(self.angulo + 45))
        self.seno = math.sin(math.radians(self.angulo + 45))
        self.direcao_tiro = (self.x_canhao + self.cosseno * self.largura//2, self.y_canhao - self.seno * self.altura//2)

    def gira_direita(self):
        self.angulo -= 5
        self.rotacao_superficie = pygame.transform.rotate(self.img, self.angulo)
        self.rotacao_retangulo = self.rotacao_superficie.get_rect()
        self.rotacao_retangulo.center = (self.x_canhao, self.y_canhao)
        self.cosseno = math.cos(math.radians(self.angulo + 45))
        self.seno = math.sin(math.radians(self.angulo + 45))
        self.direcao_tiro = (self.x_canhao + self.cosseno * self.largura//2, self.y_canhao - self.seno * self.altura//2)



def redesenha_tela():
    win.blit(fundo, (0,0))
    atirador.desenha(win)
    pygame.display.update()

atirador = Atirador()
run = True
while run:
    clock.tick(60)
    if not gameover:
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]:
            atirador.gira_esquerda()
        if teclas[pygame.K_RIGHT]:
            atirador.gira_direita()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    redesenha_tela()

pygame.quit()