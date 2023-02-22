import pygame
import math

#carrega mídias utilizadas, inicializa tela e aplicação
fundo = pygame.image.load('assets/6789.jpg')
terra = pygame.image.load('assets/terra.png')
canhao = pygame.image.load('assets/5332.png')
canhao = pygame.transform.scale(canhao, (200, 200))

pygame.display.set_caption('Astrobirds')

tela = pygame.display.set_mode((1200, 720))
clock = pygame.time.Clock()

gameover = False

#classe que define o objeto Terra
class Terra(object):
    def __init__(self):
        self.img = terra
        self.largura = self.img.get_width()
        self.altura = self.img.get_height()
        self.x = 20
        self.y = 520
    
    def desenha(self):
        tela.blit(self.img, [self.x, self.y, self.largura, self.altura])

#classe que define o objeto Atirador
class Atirador(object):
    def __init__(self):
        self.img = canhao
        self.largura = self.img.get_width()
        self.altura = self.img.get_height()
        self.x_canhao = 150
        self.y_canhao = 510
        #a partir daqui, configurações que permitem a rotação da imagem do canhão
        self.angulo = 0
        self.rotacao_superficie = pygame.transform.rotate(self.img, self.angulo) 
        self.rotacao_retangulo = self.rotacao_superficie.get_rect()
        self.rotacao_retangulo.center = (self.x_canhao, self.y_canhao) 
        self.cosseno = math.cos(math.radians(self.angulo + 45))
        self.seno = math.sin(math.radians(self.angulo + 45))
        self.direcao_tiro = (self.x_canhao + self.cosseno * self.largura//2, self.y_canhao - self.seno * self.altura//2)

    def desenha(self, tela):
        #desenha tanto a Terra quanto o canhão na tela
        terra = Terra()
        tela.blit(self.img, [self.x_canhao, self.y_canhao, self.largura, self.altura])
        terra.desenha()
        tela.blit(fundo, (0, 0))
        tela.blit(self.rotacao_superficie, self.rotacao_retangulo)
        terra.desenha()

    def gira_esquerda(self):
        #função criada para limitar e redefinir a rotação do canhão na direção esquerda
        if self.angulo <55:
            self.angulo += 5 
        self.rotacao_superficie = pygame.transform.rotate(self.img, self.angulo)
        self.rotacao_retangulo = self.rotacao_superficie.get_rect()
        self.rotacao_retangulo.center = (self.x_canhao, self.y_canhao)
        self.cosseno = math.cos(math.radians(self.angulo + 45))
        self.seno = math.sin(math.radians(self.angulo + 45))
        self.direcao_tiro = (self.x_canhao + self.cosseno * self.largura//2, self.y_canhao - self.seno * self.altura//2)

    def gira_direita(self):
        #função criada para limitar e redefinir a rotação do canhão na direção direita
        if self.angulo >-60:
            self.angulo -= 5 
        self.rotacao_superficie = pygame.transform.rotate(self.img, self.angulo)
        self.rotacao_retangulo = self.rotacao_superficie.get_rect()
        self.rotacao_retangulo.center = (self.x_canhao, self.y_canhao)
        self.cosseno = math.cos(math.radians(self.angulo + 45))
        self.seno = math.sin(math.radians(self.angulo + 45))
        self.direcao_tiro = (self.x_canhao + self.cosseno * self.largura//2, self.y_canhao - self.seno * self.altura//2)


#classe que define os raios disparados pelo canhão
class Raios(object):
    def __init__(self):
        #utiliza a direção do tiro fornecida pelas funções anteriores
        self.mira = atirador.direcao_tiro
        self.x, self.y = self.mira
        self.w = 5
        self.h = 5
        self.cos = atirador.cosseno
        self.sen = atirador.seno
        self.velocidade_x = self.cos * 10
        self.velocidade_y = self.sen * 10

    def percurso(self):
        #define o percurso dos raios
        self.x += self.velocidade_x
        self.y -= self.velocidade_y

    def desenha_raio(self, win):
        pygame.draw.rect(win, (178, 34, 34), [self.x, self.y, self.w, self.h])

#desenha os raios na tela durante o jogo
def redesenha_tela():
    tela.blit(fundo, (0,0))
    atirador.desenha(tela)
    for raio in raios:
        raio.desenha_raio(tela)
    pygame.display.update()

atirador = Atirador()
raios = []
run = True
#loop principal que checa se o jogo está ativo e recebe interações do jogador
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