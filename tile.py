from units import scale
from screen import screen
import pygame

class tile(pygame.sprite.Sprite):

    def __init__(self,x,y,item,solid):
        pygame.sprite.Sprite.__init__(self)
        self.img = item
        self.rect = self.img.get_rect()
        self.area = (x*scale,y*scale)
        self.x,self.y = self.area
        self.hard = solid


    

