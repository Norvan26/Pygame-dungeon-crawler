import pygame


class Button:
    def __init__(self, width, height, x, y, image, display):
        self.image = image
        self.display = display
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        

    def run(self):
        self.display.blit(self.image, (self.x, self.y))
        self.pos = pygame.mouse.get_pos()

        if (self.pos[0] > self.x and self.pos[0] < self.x+self.width) and (self.pos[1] > self.y and self.pos[1] < self.y+self.height):
            return 1
        else:
            return 0

        


