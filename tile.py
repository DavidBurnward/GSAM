from units import scale
from screen import screen
import pygame

class tile(object):

    def __init__(self,x,y,item,solid):
        self.img = item
        self.rect = self.img.get_rect(topleft=(x*scale,y*scale))
        self.hard = solid
        self.player = False
        self.x = x*scale
        self.y = y*scale
        self.position = (self.x, self.y)

    def c_test(self, thing):
        if self.rect.colliderect(thing.rect):
            return True
        else:
            return False

    def updatex(self,xmove):
        self.x -= xmove
        self.rect.x = self.x

    def updatey(self,xmove):
        self.y -= xmove
        self.rect.y = self.y



    

