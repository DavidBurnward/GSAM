import pygame
from pygame.locals import *
from units import chunk_size, scale, massx, massy

class fake_chunk(object):
    
    def __init__(self, (X, Y)):
        self.img = pygame.Surface((chunk_size * scale, chunk_size * scale))
        self.X, self.Y = (X,Y)
        x, y = (X, Y)
        x -= 1
        x = x * (chunk_size * scale) + (massx / 2) - scale / 2 - chunk_size * scale / 2
        y -= 1
        y = y * (chunk_size * scale) + (massy / 2) - scale / 2 - chunk_size * scale / 2
        self.p_pos = (x, y)

    def update(self, pos, plane):
        self.x = self.X * chunk_size * scale + pos[0] - chunk_size * scale
        self.y = self.Y * chunk_size * scale + pos[1] - chunk_size * scale
        for i in plane:
            self.img.blit(i.img,i.position)
        print self.x, self.y
        self.p_pos = (self.x,self.y)









