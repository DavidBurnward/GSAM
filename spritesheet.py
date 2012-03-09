from pygame import Rect, Surface
import pygame
from path import *
import os
from units import *

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((massx,massy),0,32)

spritesheet = pygame.transform.scale(pygame.image.load(path +  os.path.join('res','spritesheet.png')).convert_alpha(),(SIZE*256,SIZE*256))

sprites = []
for x in xrange(spritesheet.get_width()/scale):
    list1 = []
    for y in xrange(spritesheet.get_height()/scale):
        list1.append(spritesheet.subsurface(Rect(x*scale,y*scale,scale,scale)))
    sprites.append(list1)
