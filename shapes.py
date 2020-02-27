import pygame

class Shape:
    def __init__(self, x, y, xSpeed, ySpeed):
        self.x = x
        self.y = y
        self.xSpeed = xSpeed
        self.ySpeed = ySpeed

    def move(self):
        self.x = self.x + self.xSpeed
        self.y = self.y + self.ySpeed

    def show(self, surface):
        pygame.draw.circle(surface, (255,255,255), (self.x, self.y), 10)



circle = Shape(0, 400, 10, 0)