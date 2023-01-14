import pygame
from pygame.math import Vector2


class Grid:
    def __init__(self):
        self.position = Vector2()

        self.cell_size = 32
        self.width = 20
        self.height = 15
        self.cells = []
        for y in range(self.height):
            self.cells.append([])
            for x in range(self.width):
                self.cells[y].append(0)

    def draw(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                rect = pygame.Rect(self.position.x + x * self.cell_size, self.position.y + y * self.cell_size, self.cell_size, self.cell_size)
                pygame.draw.rect(screen, (0, 0, 0), rect, 1)
