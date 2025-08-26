import pygame

class Doorway:
    def __init__(self, room1, room2, color=(200, 200, 100), width=16):
        """
        Initializes a doorway between two rooms.

        Args:
            room1, room2: Room objects with x, y, width, height attributes.
            color: RGB tuple for the doorway color.
            width: The width of the doorway rectangle.
        """
        self.room1 = room1
        self.room2 = room2
        self.color = color
        self.width = width

        # Calculate doorway position and orientation
        x1 = room1.x + room1.width // 2
        y1 = room1.y + room1.height // 2
        x2 = room2.x + room2.width // 2
        y2 = room2.y + room2.height // 2

        if x1 == x2:
            # Vertical passage
            self.rect = pygame.Rect(
                x1 - width // 2,
                min(y1, y2),
                width,
                abs(y2 - y1)
            )
            self.is_rect = True
        elif y1 == y2:
            # Horizontal passage
            self.rect = pygame.Rect(
                min(x1, x2),
                y1 - width // 2,
                abs(x2 - x1),
                width
            )
            self.is_rect = True
        else:
            # Diagonal or non-adjacent, use a line
            self.line = ((x1, y1), (x2, y2))
            self.is_rect = False

    def draw(self, screen):
        if self.is_rect:
            pygame.draw.rect(screen, self.color, self.rect)
        else:
            pygame.draw.line(screen, self.color, self.line[0], self.line[1], self.width)
