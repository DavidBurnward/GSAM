from units import scale, SIZE
from screen import screen
import pygame
from pygame.locals import *
from pics import heart, eheart

class health(object):

    def __init__(self):
        self.img = pygame.Surface((massx, massy))
        self.position(0,0)
        self.hp = 20
        self.health = heart
        self.e_health = eheart
        self.set = 0
        self.update(0,0)

    def update(self, health, score):
        if health == 1:
            self.hp -= 1
        graphrect = self.health.get_rect()
        for x in xrange(self.hp):
            if x == 0:
                graphrect = graphrect.move(0, self.set*scale)
                self.img.blit(self.health, graphrect)
                graphrect = graphrect.move([graphrect.width, 0])
            elif x < 19 and x > 0:
                self.img.blit(self.health, graphrect)
                graphrect = graphrect.move([graphrect.width, 0])
            else:
                self.img.blit(self.health, graphrect)
        Graphrect = self.e_health.get_rect()
        for x in xrange(20):
            if x == 0:a
                Graphrect = Graphrect.move(0, self.set*scale)
                self.img.blit(self.e_health, Graphrect)
                Graphrect = Graphrect.move([Graphrect.width, 0])
            elif x < 19 and x > 0:
                self.img.blit(self.e_health, Graphrect)
                Graphrect = Graphrect.move([Graphrect.width, 0])
            else:
                self.img.blit(self.e_health, Graphrect)
        if self.hp <= 0:
            self.img.blit(end, (0, 0))
            font = pygame.font.Font(None, 28)
            text = font.render(str(score), True, (0,
255, 255), (0, 0, 0))

    def get_health(self):
        return self.hp

    def setset(self, num):
        self.set = num












