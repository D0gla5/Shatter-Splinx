import pygame

class Shape:
    def __init__(self, x, y, xSpeed, ySpeed, color):
        self.x = x
        self.y = y
        self.xSpeed = xSpeed
        self.ySpeed = ySpeed
        self.color = color

    def move(self):
        self.x = self.x + self.xSpeed
        self.y = self.y + self.ySpeed

    def show(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), 50)

    def getDistance(self, otherShape):
        return ((self.x - otherShape.x)**2 + (self.y - otherShape.y)**2)**.5

    def getDistanceFromPoint(self, x, y):
        return ((self.x - x)**2 + (self.y - y)**2)**.5

    def isOutOfBounds(self, width, height):
        outOfBounds = False
        if self.x < 0 and self.xSpeed < 0:
            outOfBounds = True
        if self.y < 0 and self.ySpeed < 0:
            outOfBounds = True
        if self.x > width and self.xSpeed > 0:
            outOfBounds = True
        if self.y > height and self.ySpeed > 0:
            outOfBounds = True

        return outOfBounds