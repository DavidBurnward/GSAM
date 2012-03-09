#!/usr/bin/env python

#This program written in comic sans

import os,sys,pygame
from pygame.locals import *
from path import path
from screen import clock, screen

#getting the world
from world import world1
import time

#starting the loop
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    for i in world1:
        print 'true'
        screen.blit(i.img,(i.x,i.y))















