from path import path as path
import player
#import health
#import Terranada
#import enemy
#import gun
from pics import rock as rock, grass as grass
from tile import tile
from units import massx, massy, chunk, scale
import pygame
from pygame.locals import *

player1 = player.player(chunk/2,chunk/2)
#sams_health = health.health()

#terranada = Terranada.Terranada()
#terras_health = health.health()
#terras_health.setset(1)

world1 = []
for y in xrange(chunk):
    for x in xrange(chunk):
        world1.append(tile(x, y, grass, False))

world1.append(tile(20, 20, rock, True))
world1.append(player1)

class chunk1(object):

    def __init__(self):
        self.img = pygame.Surface((chunk*scale,chunk*scale))
        for i in world1:
            self.img.blit(i.img,i.position)
        self.position = (0,0)
        self.p_pos = (-player1.position[0]+massx/2, -player1.position[1]+massy/2)

    def update(self,xmove,ymove):
        self.p_pos = (self.p_pos[0] - xmove, self.p_pos[1] - ymove)
        for i in world1:
            if i.player:
                player1.position = (i.position[0]+xmove, i.position[1]+ymove)
        self.img.fill(Color('black'))
        for i in world1:
            self.img.blit(i.img,i.position)
            
























