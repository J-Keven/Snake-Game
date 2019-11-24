import pygame
from pygame.locals import *
import random
import time

CIMA = 0
DIREITO  = 1
BAIXO = 2
ESQUERDA= 3
__LINHAS__ = 840
__COLUNAS__ = 620

def alinhamento():
    x = random.randint(0,830)
    y = random.randint(0,610)
    return ((x // 10 * 10, y // 10 * 10))

def colisao(c1,c2):
    
    if c1[0] == c2[0] and c1[1] == c2[1]:
        return True
    else:
        return False

def ColisaoBordas(snake):
    for i in range(len(snake)):
        snake[i][0] %= __LINHAS__
        snake[i][1] %= __COLUNAS__
            
def Mordida(snake):
    for index,i in enumerate(snake):
        if index > 0 and (snake[0][0] == i[0] ) and (snake[0][1] == i[1]):
            return True
        
    return False
    
pygame.init()

tela = pygame.display.set_mode((__LINHAS__, __COLUNAS__))

snake = [[20,10], [530,10],[0,10]]
snake_bloco = pygame.Surface([10,10])
snake_bloco.fill([255,0,255])

pos_maca = alinhamento()
maca = pygame.Surface([10,10])
maca.fill([255,0,0])

Pos_bloquinho = alinhamento()
bloquinho = pygame.Surface([50,50])
bloquinho.fill([0,0,0])

_Veloc = 10
pontos = 0
__Const__ = 10
velocidade = pygame.time.Clock()
direcao = ESQUERDA

Tabre = open("Record.txt","r")

record = Tabre.readlines()[-1]
Tabre.close()
py_active = True

while py_active: 
    
    velocidade.tick(_Veloc)
    pygame.display.set_caption('Snake' + 5 *' ' + 'Pontos: ' + str(pontos) + 4 * ' ' + 'Record: ' + str(record))
    
    ColisaoBordas(snake)
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.QUIT
            py_active = False
            
        elif evento.type == pygame.KEYDOWN:
            
            if evento.key == pygame.K_w and direcao != BAIXO:
                direcao = CIMA
    
            elif evento.key == pygame.K_a and direcao != DIREITO:
                direcao = ESQUERDA
    
            elif evento.key == pygame.K_s and direcao != CIMA: 
                direcao = BAIXO
    
            elif evento.key == pygame.K_d and direcao != ESQUERDA:
                direcao = DIREITO
      
    if colisao(snake[0], pos_maca):
        pos_maca = alinhamento()
        snake.append([0,0])
        pontos += 1
        _Veloc *= 1.005
        
    if colisao(snake[0],Pos_bloquinho):
        py_active = False
        pygame.QUIT
        
    for i in range(len(snake) - 1, 0, -1):
        snake[i] = [snake[i - 1][0], snake[i - 1][1]]
            
    if direcao == CIMA:
        snake[0] = [snake[0][0], snake[0][1] - 10]
        
    if direcao == BAIXO:
        snake[0] = [snake[0][0], snake[0][1] + 10]
            
    if direcao == ESQUERDA:
        snake[0] = [snake[0][0] - 10, snake[0][1]]
        
    if direcao == DIREITO:
        snake[0] = [snake[0][0] + 10, snake[0][1]]
        
    if Mordida(snake): 
        py_active = False
        time.sleep(5)
        pygame.QUIT
         
        
    tela.fill([255,255,255])
        
    tela.blit(maca,pos_maca)
    #tela.blit(bloquinho,Pos_bloquinho)
    
    for pos in snake:
        tela.blit(snake_bloco,pos)

    pygame.display.update()
    
if pontos > int(record):
    Tabre = open("Record.txt","w")
    Tabre.write(str(pontos))
    Tabre.close()

