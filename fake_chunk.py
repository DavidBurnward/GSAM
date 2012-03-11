import pygame
from pygame.locals import *
from units import chunk_size, scale

class fake_chunk(object):
    
    def __init__(self, (X, Y)):
        self.img = pygame.Surface((chunk_size * scale, chunk_size * scale))
        x, y = (X, Y)
        x -= 1
        x = x * scale * chunk_size
        y -= 1
        y = y * scale * chunk_size
        self.p_pos = (x, y)
        print self.p_pos

    def update(self, xmove, ymove, run, dash, plane):
        x, y =self.p_pos
        if run:
            x -= xmove * 2
            y -= ymove * 2
        if dash:
            x -= xmove * 10
            y -= ymove * 10
        else:
            x -= xmove  
            y -= ymove
        for i in plane:
            self.img.blit(i.img,i.position)
        self.p_pos = (x,y)









