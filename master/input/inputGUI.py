

from input import *
import pygame

class inputGUI:

    def __init__(self):
        self.height = 600
        self.width = 800
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.center = (int(self.width / 2), int(self.height / 2))
        self.bb = Circle(self.screen, self.center, 100, 5)
        self.cursor = Circle(self.screen, self.center, 5)

    def loop(self):
        while True:

            event = pygame.event.wait()
            if (event.type == pygame.QUIT):
                pygame.quit()
            #fill with background color
            self.screen.fill((255,255,255))

            #draw sprites
            self.bb.draw()
            self.cursor.draw()

            #update screen
            pygame.display.update()


class Circle:

    def __init__(self, surface, center, radius,  width=0):
        self.surface = surface
        self.pos = center
        self.color = (0,0,0)
        self.radius = radius
        self.width = width

    def draw(self):
        pygame.draw.circle(self.surface, self.color, self.pos, self.radius, self.width)




x = inputGUI()
x.loop()
