import pygame 
import sys
import os
import random
import math
from components.playerGui import Gui
from components.room import Room
from components.linking import Doorway


clock = pygame.time.Clock()

class Level:
    def __init__(self, display):
        self.display = display
        self.gui = Gui(self.display)
        self.room1 = Room(self.display, 'dummy', 200, 200, 16) 

        #self.door = Doorway(self.room1, self.room2)

    def run(self):
        clock.tick(60)
        self.display.fill((0,22,22,255))
        self.pos = pygame.mouse.get_pos()
        #-------------------------------------------------------------------------------------------------------------------
        keys = pygame.key.get_pressed()
        self.room1.run()
        #self.door.draw(self.display)
        self.gui.run()
        
        