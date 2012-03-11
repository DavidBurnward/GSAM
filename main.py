#!/usr/bin/env python

#This program written in comic sans

import os,sys,pygame
from pygame.locals import *
from path import path
from screen import clock, screen
from pics import rock
from units import massx, massy

#getting the world
from world import chunk1
import time

chunk1 = chunk1()

screen_rect = screen.get_rect()
camera = screen_rect.copy()

dx = dy = 0
black = Color('black')
xback = 0
yback = 0

#starting the loop
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_RIGHT: dx = 1
            elif event.key == K_LEFT: dx = -1
            elif event.key == K_DOWN: dy = 1
            elif event.key == K_UP: dy = -1
            elif event.key == K_ESCAPE: quit()
        elif event.type == KEYUP:
            if event.key in (K_RIGHT,K_LEFT): dx = 0
            elif event.key in (K_DOWN,K_UP): dy = 0

    screen.fill(black)
    chunk1.update(dx,dy)
    screen.blit(chunk1.img,chunk1.p_pos)

    pygame.display.update()















