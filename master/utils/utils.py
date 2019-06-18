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

    def __init__(self, roll=0, pitch=0, yaw=0):
        self.roll = roll
        self.pitch = pitch
        self.yaw = yaw

    def toString(self):
        print(' ')
        print("roll: " + str(self.roll))
        print("pitch: " + str(self.pitch))
        print("yaw: " + str(self.yaw))
        print(' ')

#constructor
def makeSingularEulerAngle(rotation, angle):
    ea = Euler()

    if (rotation == 0):
        ea.roll = angle
    elif (rotation == 1):
        ea.pitch = angle
    elif (rotation == 2):
        ea.yaw = angle

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

    def subtract(self, vv):
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

    def distance(self, vv):
        result = Vector3()

        result.x = math.sqrt((self.x - vv.x)**2)
        result.y = math.sqrt((self.y - vv.y)**2)
        result.z = math.sqrt((self.z - vv.z)**2)

        return result

    def unit(self):
        result = Vector3()
        m = self.magnitude()
        if (m != 0):
            result.x = self.x / m
            result.y = self.y / m
            result.z = self.z / m
        return result


    def magnitude(self):
        return math.sqrt((self.x*self.x) + (self.y * self.y) + (self.z * self.z))
    
    def multiplyMatrix44(self, m):
        result = Vector3()

        result.x = (self.x * m.m11) + (self.y * m.m21) + (self.z * m.m31) + m.m41
        result.y = (self.x * m.m12) + (self.y * m.m22) + (self.z * m.m32) + m.m42
        result.z = (self.x * m.m13) + (self.y * m.m23) + (self.z * m.m33) + m.m43

        return result

    def toString(self):
        print("X: " + str(self.x))
        print("Y: " + str(self.y))
        print("Z: " + str(self.z))

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
	cy = math.cos(ea.roll)
	sy = math.sin(ea.roll)
	cx = math.cos(ea.pitch)
	sx = math.sin(ea.pitch)
	cz = math.cos(ea.yaw)
	sz = math.sin(ea.yaw)

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
	self.m41 = v.x
	self.m42 = v.y
	self.m43 = v.z

    def toString(self):
        print('')
        print(str(self.m11) + ' ' + str(self.m12) + ' ' + str(self.m13) + ' ' + str(self.m14))
        print(str(self.m21) + ' ' + str(self.m22) + ' ' + str(self.m23) + ' ' + str(self.m24))
        print(str(self.m31) + ' ' + str(self.m32) + ' ' + str(self.m33) + ' ' + str(self.m34))
        print(str(self.m41) + ' ' + str(self.m42) + ' ' + str(self.m43) + ' ' + str(self.m44))
        print('')



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
