import pygame

class Room:
    def __init__(self, x, y, width, height, color=(200, 200, 200), border_color=(0, 0, 0), border_width=2):
        """
        Initialize a Room object.

        Args:
            x (int): The x-coordinate of the top-left corner.
            y (int): The y-coordinate of the top-left corner.
            width (int): The width of the room.
            height (int): The height of the room.
            color (tuple): The fill color of the room (R, G, B).
            border_color (tuple): The border color of the room (R, G, B).
            border_width (int): The width of the border.
        """
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.border_color = border_color
        self.border_width = border_width

    def draw(self, surface):
        """
        Draw the room on the given surface.

        Args:
            surface (pygame.Surface): The surface to draw the room on.
        """
        pygame.draw.rect(surface, (200, 200, 200), self.rect)
        pygame.draw.rect(surface, self.border_color, self.rect, self.border_width)