import pygame
from pygame.locals import *
from units import chunk_size, scale

class fake_chunk(object):
    
    def __init__(self, (x, y)):
        self.img = pygame.Surface((chunk_size * scale, chunk_size * scale))
        self.p_pos = (x, y)
        for i in self.p_pos:
            i -= 1
            i = i * scale * chunk_size

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









