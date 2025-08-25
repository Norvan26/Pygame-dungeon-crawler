import pygame 
import sys
import os
import random
import math
from components.playerGui import Gui
from components.room import Room

clock = pygame.time.Clock()

class Level:
    def __init__(self, display):
        self.display = display
        self.gui = Gui(self.display)
        self.room = Room(0, 0, 512, 100, self.display) 

    def run(self):
        clock.tick(60)
        self.display.fill((0,22,22,255))
        self.pos = pygame.mouse.get_pos()
        #-------------------------------------------------------------------------------------------------------------------
        keys = pygame.key.get_pressed()
        self.room.draw(self.display)
        self.gui.run()
        
        