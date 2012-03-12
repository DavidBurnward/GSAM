from units import scale, SIZE
from screen import screen
import pygame
from pygame.locals import *

class Ally(object):
    
    def __init__(self, x, y, bunch):
        self.ani_speed_init = 5
        self.ani_speed = self.ani_speed_init
        self.anidown = bunch[0]
        self.aniup = bunch[1]
        self.anileft = bunch[2]
        self.aniright = bunch[3]
        self.anidown_pos = 0
        self.aniup_pos = 0
        self.anileft_pos = 0
        self.aniright_pos = 0
        self.anidown_max = len(self.anidown) - 1
        self.aniup_max = len(self.aniup) - 1
        self.anileft_max = len(self.anileft) - 1
        self.aniright_max = len(self.aniright) - 1
        self.img = self.anidown[0]
        self.hurting_init = 200
        self.hurting = self.hurting_init
        self.rect = self.img.get_rect()
        self.face = 1
        self.x = x * scale
        self.y = y * scale
        self.position = (self.x, self.y)
        self.size = (scale, scale)
        self.player = False
        self.hard = True

    def update(self,















