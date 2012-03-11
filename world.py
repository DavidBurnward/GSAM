from path import path as path
import player
#import health
#import Terranada
#import enemy
#import gun
from pics import rock as rock, grass as grass
from tile import tile
from units import massx, massy, chunk_size, scale
import pygame
from pygame.locals import *
from borders import wall1, wall2, wall3, wall4

#sams_health = health.health()

#terranada = Terranada.Terranada()
#terras_health = health.health()
#terras_health.setset(1)

world1 = []
for y in xrange(chunk_size):
    for x in xrange(chunk_size):
        world1.append(tile(x, y, grass, False))

world1.append(tile(4, 4, rock, True))
#world1 = world1 + wall1 + wall2 + wall3 + wall4
















