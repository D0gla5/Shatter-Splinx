from shapes import Shape
from random import randint, choice

class ShatterSplinx:
    def __init__(self, screenWidth, screenHeight):
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight

        self.shapePairs = []

    def update(self):
        for pair in self.shapePairs:
            pair[0].move()
            pair[1].move()

    def draw(self, surface):
        for pair in self.shapePairs:
            pair[0].show(surface)
            pair[1].show(surface)

    def addNewShapePair(self):
        self.shapePairs.append(self.makeRandomShapes())

    def makeRandomShapes(self):
        availablePosition = [0,1,2,3]
        shapes = []

        x = randint(150,self.screenWidth-150)
        y = randint(150,self.screenHeight-150)

        color = (randint(0,255), randint(0,255), randint(0,255))

        speed = randint(8,10)

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
