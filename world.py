from path import path
from pics import rock, grass, wood, map1, map2, dirt, dtg1, dtg2, portal
from tile import tile
from units import massx, massy, chunk_size, scale
import pygame
from pygame.locals import *

def mapmaker(area):
    composition = []
    size = [area.get_width(), area.get_height()]
    for x in xrange(size[0]):
        for y in xrange(size[1]):
            c = area.get_at((x,y))
            if c == (0, 255, 42, 255):
                composition.append(tile(x, y, grass, False, False))
            elif c == (181, 100, 34, 255):
                composition.append(tile(x, y, wood, False, False))
            elif c == (159,159,159,255):
                composition.append(tile(x, y, grass, False, False))
                composition.append(tile(x, y, rock, True, False))
            elif c == (255, 114, 0, 255):
                composition.append(tile(x, y, dirt, False, False))
            elif c == (55, 114, 0, 255):
                composition.append(tile(x, y, dirt, False, False))
                composition.append(tile(x, y, rock, True, False))
            elif c == (85, 142, 29, 255):
                composition.append(tile(x, y, dtg2, False, False))
            elif c == (0, 0, 0, 255):
                composition.append(tile(x, y, portal, False, True))
    return (size, composition)

world1 = (mapmaker(map1))
world2 = (mapmaker(map2))

worlds = []
worlds.append(world1)
worlds.append(world2)










