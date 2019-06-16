'''
    Utils

    These are utility functions to help with other scripts.
'''

import math



'''
    class : Euler class

    This is a class to hold a container for euler angles
'''
class Euler:

    def __init__(self, heading=0, pitch=0, bank=0):
        self.heading = heading
        self.pitch = pitch
        self.bank = bank

    def toString(self):
        print("heading: " + self.heading)
        print("pitch: " + self.pitch)
        print("bank: " + self.bank)

#constructor
def makeSingularEulerAngle(rotation, angle):
    ea = Euler()

    if (rotation == 0):
        ea.heading = angle
    elif (rotation == 1):
        ea.pitch = angle
    elif (rotation == 2):
        ea.bank = angle

    return ea

'''
    class Vector3

    Stores operators and coordinates for a 3 dimensional vector
'''
class Vector3:

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def add(self, vv):
        result = Vector3()

        result.x = self.x + vv.x
        result.y = self.y + vv.y
        result.z = self.z + vv.z

        return result

    def subtract(self. vv):
        result = Vector3()

        result.x = self.x - vv.x
        result.y = self.y - vv.y
        result.z = self.z - vv.z

        return result

    def multScalar(self, s):
        result = Vector3()

        result.x = self.x * s
        result.y = self.y * s
        result.z = self.z * s

        return result

    def toString(self):
        print("X: " + self.x)
        print("Y: " + self.y)
        print("Z: " + self.z)

    #TODO Distance()
    #TODO Magnitude()
    #TODO MultMatrix44()

#constructor
def makeVector3(x,y,z):
    v = Vector3(x,y,z)
    return v



#Util Functions
def degree(rads):
    return rads / (math.pi / 180.0)

def radians(deg):
    return (math.pi / 180.0) * deg




'''

    Framing!

    Not quite sure what this does
    However;; there is a lot of framing information
    for how fast servos can update and be called

'''
