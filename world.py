from path import path
from pics import rock, grass, wood, map1, dirt, dtg1, dtg2
from tile import tile
from units import massx, massy, chunk_size, scale
import pygame
from pygame.locals import *

composition = []
size = [map1.get_height(), map1.get_width()]
for y in xrange(size[0]):
    for x in xrange(size[1]):
        c = map1.get_at((x,y))
        if c == (0, 255, 42, 255):
            composition.append(tile(x, y, grass, False))
        elif c == (181, 100, 34, 255):
            composition.append(tile(x, y, wood, False))
        elif c == (159,159,159,255):
            composition.append(tile(x, y, grass, False))
            composition.append(tile(x, y, rock, True))
        elif c == (255, 114, 0, 255):
            composition.append(tile(x, y, dirt, False))
        elif c == (55, 114, 0, 255):
            composition.append(tile(x, y, dtg1, False))
        elif c == (85, 142, 29, 255):
            composition.append(tile(x, y, dtg2, False))

world1 = (size, composition)











