import pygame
from config import *

class Teclas:
    def __init__(self, seta, window, dados_teclas):                         
        self.window = window
        self.dados_teclas = dados_teclas
        self.seta = dados_teclas[seta][0]              
        self.posi = dados_teclas[seta][1]             
        self.tecla = dados_teclas[seta][2]            
        self.radius = 5

class Notes(pygame.sprite.Sprite):
    def __init__(self, seta, assets, dados_teclas):
        pygame.sprite.Sprite.__init__(self)
        self.dados_teclas = dados_teclas
        self.nome = seta
        self.color = (dados_teclas[seta][0])
        self.image = pygame.transform.scale((assets['notas'][seta]), (90,90))
        self.radius = 45
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = dados_teclas[seta][1][0] - self.radius
        self.rect.y = height + self.radius
        self.speed_y = -90                
    
    def update(self):
        self.rect.y += self.speed_y
    
    def remove(self):
        self.image.fill(transparente)
        self.kill()