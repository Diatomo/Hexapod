
'''
    Prototype script to build out a controller for the hexapod robot
'''

from input import *
import pygame
import math
import time

white = (220,220,220)
black = (0,0,0)
coral = (255,114,111)

pygame.init()

counter = 0
nVALS = 100
incre = (2 * math.pi) / nVALS
print(str(incre))

class inputGUI:

    def __init__(self):
        #size of screen
        self.height = 600
        self.width = 800
        
        #screen aliases
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.center = (int(self.width / 2), int(self.height / 2))
        self.apos = (int(self.center[0]), int(self.center[1] - 100))

        #center dot
        self.bb = Circle(self.screen, self.center, self.center, 100, 5)

        #rotation circle
        self.rot = Circle(self.screen, self.apos, self.center, 10, 0, coral)
        self.cursor = Circle(self.screen, self.center, self.center, 5)
        self.myFont = pygame.font.Font(None, 18)
        self.controller = Input() 

        #testing
        self.tally = incre
    
    def pollInput(self):
        pass
    

    def test_key(self):
        direction = -1
        keys_pressed = pygame.event.get()
        for event in keys_pressed:
            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_UP):
                    direction = 1
                elif (event.key == pygame.K_DOWN):
                    direction = 2
                elif (event.key == pygame.K_LEFT):
                    direction = -4
                elif (event.key == pygame.K_RIGHT):
                    direction = 4
            if (event.type == pygame.KEYUP):
                direction = 0
        return direction

    def test_rotate(self):
        if (time.time() - prevTime > alarm):
            self.rot.outskirt(incre)
            prevTime = time.time()

    def loop(self):
        prevTime = time.time()
        alarm = 0.1
        counter = 0
        while True:

            self.controller.poll()
            event = pygame.event.poll()
            if (event.type == pygame.QUIT):
                pygame.quit()

            #fill with background color
            self.screen.fill(white)

            #interactive logic
            direction = self.test_key()
            self.rot.outskirt(direction)

            #draw sprites
            self.bb.draw()
            self.cursor.draw()
            self.rot.draw()

            #update screen
            self.text(self.rot.pos[0], self.rot.pos[1])
            pygame.display.update()

    def text(self, x, y):
        posX = self.myFont.render("Position X: " + str(x), True, black)
        posY = self.myFont.render("Position Y: " + str(y), True, black)
        inc = self.myFont.render("increment: " + str(self.tally), True, black)
        self.tally = (self.tally + incre)
        self.screen.blit(posX, (20,20))
        self.screen.blit(posY, (20,40))
        self.screen.blit(inc, (20,60))

class Circle:

    def __init__(self, surface, pos, center, radius, width=0, color=black):
        self.surface = surface
        self.pos = pos
        self.rot = pos
        self.center = center
        self.color = color
        self.radius = radius
        self.width = width

    def outskirt(self, rot):

        if (rot != 0 and rot != -1):
            rot = 2 * math.pi / rot
            xrot = (math.cos(rot) * (self.pos[0] - self.center[0])) 
            xrot = round(xrot - (math.sin(rot) * (self.pos[1] - self.center[1])) + self.center[0])
            yrot = (math.sin(rot) * (self.pos[0] - self.center[0])) 
            yrot = round(yrot +(math.cos(rot) * (self.pos[1] - self.center[1])) + self.center[1])
            self.rot = (xrot, yrot)
        elif (rot == 0):
            xrot = self.center[0]
            yrot = self.center[1]
            self.rot = (xrot, yrot)

    def draw(self):
        pygame.draw.circle(self.surface, self.color, self.rot, self.radius, self.width)


x = inputGUI()
x.loop()
