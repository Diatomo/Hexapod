

from input import *
import pygame
import math
import time

white = (255,255,255)
black = (0,0,0)
coral = (255,127,80)



counter = 0
incre = 2 * math.pi / 100
rotRange = []
for i in range(100):
    rotRange.append(counter)
    counter += incre



class inputGUI:

    def __init__(self):
        self.height = 600
        self.width = 800
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.center = (int(self.width / 2), int(self.height / 2))
        self.apos = (int(self.center[0]), int(self.center[1] - 100))
        self.bb = Circle(self.screen, self.center, self.center, 100, 5)
        self.rot = Circle(self.screen, self.apos, self.center, 10, 0, coral)
        self.cursor = Circle(self.screen, self.center, self.center, 5)

    def loop(self):
        currTime = time.time()
        alarm = 5
        counter = 0
        while True:
            event = pygame.event.wait()
            if (event.type == pygame.QUIT):
                pygame.quit()

            #fill with background color
            self.screen.fill(white)

            #draw sprites
            self.bb.draw()
            self.cursor.draw()
            if (time.time() - currTime >= alarm):
                print("executed")
                self.rot.outskirt(rotRange[counter])
                counter += 1
                counter = counter % 100
                currTime = time.time()
            self.rot.draw()

            #update screen
            pygame.display.update()


class Circle:

    def __init__(self, surface, pos, center, radius, width=0, color=black):
        self.surface = surface
        self.pos = pos
        self.center = center
        self.color = color
        self.radius = radius
        self.width = width

    def outskirt(self, rot):
        xrot = int((math.cos(rot) * (self.pos[0] - self.center[0])) - (math.sin(rot) * (self.pos[1] - self.center[1])) + self.center[0])
        yrot = int((math.sin(rot) * (self.pos[0] - self.center[0])) + (math.cos(rot) * (self.pos[1] - self.center[1])) + self.center[1])
        self.pos = (xrot, yrot)

    def draw(self):
        pygame.draw.circle(self.surface, self.color, self.pos, self.radius, self.width)




x = inputGUI()
x.loop()
