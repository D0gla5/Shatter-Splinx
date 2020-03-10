from shapes import Shape
from random import randint, choice
import pygame

import sys

class ShatterSplinx:
    def __init__(self, screenWidth, screenHeight):
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight

        self.shapePairs = []
        self.mousePos = (0,0)

        self.score = 0
        self.health = 100

        self.cursorColor = (255,255,255)
        self.timeSinceColorChange = 0
        self.timer = 0;

        self.scoreBoard = pygame.font.SysFont("Courier New", 24)

    def setMousePos(self, mPos):
        self.mousePos = mPos

    def update(self, dt):
        self.timeSinceColorChange += dt

        if self.timeSinceColorChange > .25:
            self.cursorColor = (255,255,255)

        for pair in self.shapePairs:

            if pair[0].isOutOfBounds(self.screenWidth, self.screenHeight) and pair[1].isOutOfBounds(self.screenWidth, self.screenHeight):
                self.missedShapes()
                self.deleteShapes(pair)

            pair[0].move()
            pair[1].move()
            
    def drawScoreBoard(self, surface, x, y):
        text_object = self.scoreBoard.render(str(self.score), False, (255,255,255))
        text_rect = text_object.get_rect( )
        text_rect.center = (x, y)
        surface.blit( text_object, text_rect )

    def draw(self, surface):
        for pair in self.shapePairs:
            pair[0].show(surface)
            pair[1].show(surface)


        #draw the mouse cursor
        pygame.draw.circle(surface, self.cursorColor, self.mousePos, 5)
        pygame.draw.circle(surface, self.cursorColor, self.mousePos, 25, 2)


        #Draw the health bar
        pygame.draw.rect(surface, (255,100,100), (100,50,600,10))
        pygame.draw.rect(surface, (100,255,100), (100, 50, self.health*6, 10))

        #draw the score
        self.drawScoreBoard(surface, self.screenWidth/2, 25)

    def addNewShapePair(self):
        self.shapePairs.append(self.makeRandomShapes())

    def checkIfClickedShapes(self, x, y):
        clickedOnPair = None

        for pair in self.shapePairs:
                s1 = pair[0]
                s2 = pair[1]

                if s1.getDistance(s2) < 100 and s1.getDistanceFromPoint(x,y) < 75:
                    clickedOnPair = pair
        
        if clickedOnPair:
            self.clickedOnShapes(clickedOnPair)
        else:
            self.missedShapes()

    def clickedOnShapes(self, pair):
        self.cursorColor = (100,255,100)
        self.timeSinceColorChange = 0

        self.score += 1
        self.health += 1
        if self.health > 100:
            self.health = 100


        print(self.score)
        self.deleteShapes(pair)

    def missedShapes(self):
        self.cursorColor = (255,100,100)
        self.timeSinceColorChange = 0

        self.health -= 25
        if self.health < 0:
            sys.exit()

    def deleteShapes(self, shapes):
        self.shapePairs.remove(shapes)

    def makeRandomShapes(self):
        availablePosition = [0,1,2,3]
        shapes = []

        safeZone = 150

        x = randint(safeZone,self.screenWidth-safeZone)
        y = randint(safeZone,self.screenHeight-safeZone)

        color = (randint(0,255), randint(0,255), randint(0,255))

        speed = randint(6,6)

        distanceFromSides = [x,y,self.screenWidth-x, self.screenHeight-y]
        distance = max(distanceFromSides)

        for i in range(2):
            randomNum = choice(availablePosition)
            availablePosition.remove(randomNum)

            if randomNum == 0:
                shape = Shape(x-distance, y, speed, 0, color)
            if randomNum == 1:
                shape = Shape(x, y-distance, 0, speed, color)
            if randomNum == 2:
                shape = Shape(x+distance, y, -speed, 0, color)
            if randomNum == 3:
                shape = Shape(x, y+distance, 0, -speed, color)

            shapes.append(shape)

        return shapes
