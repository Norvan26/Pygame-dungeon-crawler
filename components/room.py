import pygame
from data.layout import roomLayout

class Room:
    def __init__(self, display, tile_map, x, y, size):
        self.display = display
        self.tile_map = tile_map
        self.size = size
        self.x = x
        self.y = y
        self.height = 0
        self.width = -32 #offset to fix first tile placement beacuse fuck ass thing kept skipping drawing the first tile
        self.TILE_SIZE = 16
        self.width = len(tile_map[0]) * self.TILE_SIZE
        self.floor = pygame.image.load("assets/floor.png").convert_alpha()
        self.wall = pygame.image.load("assets/wall.png").convert_alpha()
        self.foundation = pygame.Surface((self.size*self.TILE_SIZE, self.size*self.TILE_SIZE), pygame.SRCALPHA)
        self.foundation.fill((255, 0, 0))
        self.i = 0
        
        for i in roomLayout:
            for j in i:
                print(self.width-16)
                print(j)
                if j == 'W':
                    self.foundation.blit(self.wall, (self.width, self.height))

                else:
                    self.foundation.blit(self.floor, (self.width, self.height))

                self.width += self.TILE_SIZE
                self.i += 1
                print(self.width, self.height)
            self.width = 0
            self.height += self.TILE_SIZE
            

        
    def run(self):
        self.display.blit(self.foundation, (self.x, self.y))
