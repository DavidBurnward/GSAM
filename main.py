#!/usr/bin/env python

#This program written in comic sans

import os,sys,pygame
from pygame.locals import *
from path import path
from screen import clock, screen
from pics import rock
from units import massx, massy

#getting the world
from chunk import chunk
from fake_chunk import fake_chunk
from world import world1
import time
real = chunk()
chunks = []
for x in xrange(3):
    list = []
    for y in xrange(3):
        if (x,y) == (1,1):
            list.append(real)
            print 'true'
        else:
            list.append(fake_chunk((x, y)))
    chunks.append(list)

screen_rect = screen.get_rect()
camera = screen_rect.copy()

dx = dy = 0
black = Color('black')
xback = 0
yback = 0
run = False
dash = False

#starting the loop
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_q:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_UP:
            dy = -1
        elif event.type == KEYDOWN and event.key == K_DOWN:
            dy = 1
        elif event.type == KEYDOWN and event.key == K_LEFT:
            dx = -1
        elif event.type == KEYDOWN and event.key == K_RIGHT:
            dx = 1
        elif event.type == KEYUP and event.key == K_UP:
            dy = 0
        elif event.type == KEYUP and event.key == K_DOWN:
            dy = 0
        elif event.type == KEYUP and event.key == K_LEFT:
            dx = 0
        elif event.type == KEYUP and event.key == K_RIGHT:
            dx = 0
        elif event.type == KEYDOWN and event.key == K_r:
            run = True
        elif event.type == KEYUP and event.key == K_r:
            run = False
        elif event.type == KEYDOWN and event.key == K_t:
            dash = True
        elif event.type == KEYUP and event.key == K_t:
            dash = False

    dx = dx
    dy = dy
    screen.fill(black)
    for x in chunks:
        for y in x:
            if y == real:
                y.update(dx, dy, run, dash, world1)
            else:
                y.update(dx, dy, run, dash, world1)
    
    for x in chunks:
        for y in x:
            screen.blit(y.img, y.p_pos)

    pygame.display.update()















