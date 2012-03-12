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
from world import world1

player1 = player.player(chunk_size/2,chunk_size/2)
#sams_health = health.health()
#world1.append(tile(4, 4, rock, True))

#terranada = Terranada.Terranada()
#terras_health = health.health()
#terras_health.setset(1)


world1.append(player1)

class chunk(object):

    def __init__(self):
        self.img = pygame.Surface((chunk_size*scale,chunk_size*scale))
        for i in world1:
            self.img.blit(i.img,i.position)
        self.p_pos = (-player1.position[0]+massx/2-scale/2, -player1.position[1]+massy/2-scale/2)
        self.player = True

    def update(self, xmove, ymove, run, dash, world1):
        if self.player:
            player1.updatex(xmove, run, dash, world1)
            player1.updatey(ymove, run, dash, world1)
            self.p_pos = ( - player1.position[0] + massx / 2 - scale / 2 - xmove, - player1.position[1] + massy / 2 - scale / 2 - ymove)
            for i in world1:
                if i.player:
                    player1.position = (i.position[0]+xmove, i.position[1]+ymove)
        self.img.fill(Color('black'))
        for i in world1:
#            self.img.blit(i.img,i.position)
            if i.position[0] >= player1.position[0]-(massx/2+scale*3):
                if i.position[0] <= player1.position[0]+(massx/2+scale*3):
                    if i.position[1] >= player1.position[1]-(massx/2+scale*3):
                        if i.position[1] <player1.position[1]+(massx/2+scale*3):
                            self.img.blit(i.img,i.position)
            
























