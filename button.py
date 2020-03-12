import pygame

class Button:
    def __init__(self, color, rect, text, callback):
        self.text = text
        self.callback = callback
        self.color = color
        self.rect = rect

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

        font = pygame.font.SysFont("comicsans", 60)
        text_object = font.render(self.text, 1, (0,0,0))
        text_rect = text_object.get_rect( )
        text_rect.center = (self.rect[0]+self.rect[2]/2, (self.rect[1]+self.rect[3]/2))
        surface.blit(text_object, text_rect)

    def isMouseOver(self, x, y):
        if (x > self.rect[0] and x < self.rect[0] + self.rect[2]) and (y > self.rect[1] and y < self.rect[1]+self.rect[3]):
            return True
        return False

    def checkClicked(self, x, y, clicked):
        if self.isMouseOver(x,y) and clicked:
            self.callback()

        

    

    