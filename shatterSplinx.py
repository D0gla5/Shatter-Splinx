from shapes import Shape

class ShatterSplinx:
    def __init__(self):
        self.circle = Shape(0, 400, 10, 0)

    def update(self):
        self.circle.move()

    def draw(self, surface):
        self.circle.show(surface)