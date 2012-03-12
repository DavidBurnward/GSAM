from path import path as path
import player
#import health
#import Terranada
#import enemy
#import gun
from pics import rock, grass, wood
from tile import tile
from units import massx, massy, scale
import pygame
from pygame.locals import *
from borders import wall1, wall2, wall3, wall4
from world import world1

player1 = player.player(world1[0][0] / 2, world1[0][1] / 2)
#sams_health = health.health()
#world1.append(tile(4, 4, rock, True))

#terranada = Terranada.Terranada()
#terras_health = health.health()
#terras_health.setset(1)


class chunk(object):

    def __init__(self, world):
        self.img = pygame.Surface((world[0][0] * scale, world[0][1] * scale))
        world[1].append(player1)
        for i in world[1]:
            self.img.blit(i.img,i.position)
        self.p_pos = ( - player1.position[0] + massx / 2 - scale / 2, - player1.position[1] + massy / 2 - scale / 2 )
        self.player = True

    def update(self, xmove, ymove, run, dash, world):
        if self.player:
            player1.updatex(xmove, run, dash, world)
            player1.updatey(ymove, run, dash, world)
            self.p_pos = ( - player1.position[0] + massx / 2 - scale / 2 - xmove, - player1.position[1] + massy / 2 - scale / 2 - ymove)
            for i in world[1]:
                if i.player:
                    player1.position = (i.position[0]+xmove, i.position[1]+ymove)
        self.img.fill(Color('black'))
        for i in world[1]:
#            self.img.blit(i.img,i.position)
            if i.position[0] >= player1.position[0] - (massx / 2 + scale * 3):
                if i.position[0] <= player1.position[0] + (massx / 2 + scale * 3):
                    if i.position[1] >= player1.position[1] - (massx / 2 + scale * 3):
                        if i.position[1] <= player1.position[1] + (massx / 2 + scale * 3):
                            self.img.blit(i.img,i.position)
            
























