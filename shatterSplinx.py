from shapes import Shape
import random

class ShatterSplinx:
    def __init__(self, screenWidth, screenHeight):
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight

        self.circle, self.circle2 = self.makeRandomShapes()

    def update(self):
        self.circle.move()
        self.circle2.move()

    def draw(self, surface):
        self.circle.show(surface)
        self.circle2.show(surface)

    def makeRandomShapes(self):
        availablePosition = [0,1,2,3]
        shapes = []

        speed = random.randint(2,8)

        for i in range(2):
            randomNum = random.choice(availablePosition)
            availablePosition.remove(randomNum)
            if randomNum == 0:
                shape = Shape(self.screenWidth/2, 0, 0, speed)
            if randomNum == 1:
                shape = Shape(self.screenWidth, self.screenHeight/2, -speed, 0)
            if randomNum == 2:
                shape = Shape(self.screenWidth/2, self.screenHeight, 0, -speed)
            if randomNum == 3:
                shape = Shape(0, self.screenHeight/2, speed, 0)

            shapes.append(shape)

        return shapes
