from path import path as path
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

composition = []
size = 30
for y in xrange(chunk_size):
    for x in xrange(chunk_size):
        composition.append(tile(x, y, grass, False))

composition = composition + wall1 + wall3
world1 = (size, composition)

world2 = []
for y in xrange(chunk_size):
    for x in xrange(chunk_size):
        world2.append(tile(x, y, grass, False))

world2 = world2 + wall1 + wall3











