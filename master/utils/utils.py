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


class Matrix44():

    def __init__(self):
        self.m11 = 0
        self.m12 = 0
        self.m13 = 0
        self.m14 = 0
        self.m21 = 0
        self.m22 = 0
        self.m23 = 0
        self.m24 = 0
        self.m31 = 0
        self.m32 = 0
        self.m33 = 0
        self.m34 = 0
        self.m41 = 0
        self.m42 = 0
        self.m43 = 0
        self.m44 = 0


    def setRotation(self, ea):
	
        # precompute
	cy := math.cos(ea.Heading)
	sy := math.sin(ea.Heading)
	cx := math.cos(ea.Pitch)
	sx := math.sin(ea.Pitch)
	cz := math.cos(ea.Bank)
	sz := math.sin(ea.Bank)

	# perform intense snafucation
	self.m11 = cy * cz
	self.m21 = -cy * sz
	self.m31 = sy
	self.m14 = 0
	self.m12 = (cx * sz) + ((sx * cz) * sy)
	self.m22 = (cx * cz) - ((sx * sz) * sy)
	self.m32 = -sx * cy
	self.m24 = 0
	self.m13 = (sx * sz) - ((cx * cz) * sy)
	self.m23 = (sx * cz) + ((cx * sz) * sy)
	self.m33 = cx * cy
	self.m34 = 0
	self.m41 = 0
	self.m42 = 0
	self.m43 = 0
	self.m44 = 1



    def setTranslation(self, v):
	self.m41 = v.X
	self.m42 = v.Y
	self.m43 = v.Z


def makeMatrix44(v, ea):
    m = Matrix44()
    m.setRotation(ea)
    m.setTranslation(v)
    return m



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
