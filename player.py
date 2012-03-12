from units import scale, SIZE
from screen import screen
import pygame
from pygame.locals import *
from pics import playerdown, playerup, playerleft, playerright

class player(object):

    def __init__(self, x, y):
        self.ani_speed_init= 5
        self.ani_speed= self.ani_speed_init
        self.anidown = playerdown
        self.aniup = playerup
        self.anileft = playerleft
        self.aniright = playerright
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
        self.player = True
        self.hard = False

    def updatex(self, xmove, run, dash, world):
        if xmove > 0:
            self.ani_speed -= xmove
            if self.ani_speed <= 0:
                self.img = self.aniright[self.aniright_pos]
                self.ani_speed = self.ani_speed_init
                if self.aniright_pos == self.aniright_max:
                    self.aniright_pos = 0
                else:
                    self.aniright_pos += 1
                self.face = 2

        if xmove < 0:
            self.ani_speed += xmove
            if self.ani_speed <= 0:
                self.img = self.anileft[self.anileft_pos]
                self.ani_speed = self.ani_speed_init
                if self.anileft_pos == self.anileft_max:
                    self.anileft_pos = 0
                else:
                    self.anileft_pos += 1
                self.face = 4

        self.xback = self.x
        if run:
            self.x += xmove * 2
        if dash:
            self.x += xmove * 10
        else:
            self.x += xmove            
        self.rect = Rect(self.x, self.y, scale, scale)
        for i in world[1]:
            if i.hard:
                if self.rect.colliderect(i.rect):
                    self.x = self.xback
                    self.rect = Rect(self.x, self.y, scale, scale)
        if self.x < 0:
            self.x =world[0] * scale-scale
        elif self.x > world[0] * scale-scale:
            self.x = 0
            
        self.position = (self.x, self.y)

    def updatey(self, ymove, run, dash, world):
        if ymove > 0:
            self.ani_speed -= ymove
            if self.ani_speed <= 0:
                self.img = self.anidown[self.anidown_pos]
                self.ani_speed = self.ani_speed_init
                if self.anidown_pos == self.anidown_max:
                    self.anidown_pos = 0
                else:
                    self.anidown_pos += 1
                self.face = 1

        if ymove < 0:
            self.ani_speed += ymove
            if self.ani_speed <= 0:
                self.img = self.aniup[self.aniup_pos]
                self.ani_speed = self.ani_speed_init
                if self.aniup_pos == self.aniup_max:
                    self.aniup_pos = 0
                else:
                    self.aniup_pos += 1
                self.face = 3

        self.yback = self.y
        if run:
            self.y += ymove * 2
        if dash:
            self.y += ymove * 10
        else:
            self.y += ymove            
        self.rect = Rect(self.x, self.y, scale, scale)
        for i in world[1]:
            if i.hard:
                if self.rect.colliderect(i.rect):
                    self.y = self.yback
                    self.rect = Rect(self.x, self.y, scale, scale)
        if self.y < 0:
            self.y =world[0] * scale-scale
        elif self.y > world[0] * scale-scale:
            self.y = 0 

        self.position = (self.x, self.y)










