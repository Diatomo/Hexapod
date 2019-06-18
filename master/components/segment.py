

from sys import path
path.append("../utils")
from utils import *

'''
    class: Segment
        Collection of data and objects within an ik chain
'''
class Segment:

    '''
        fxn :: init ; constructor
            name := name of object
            parent := point to parent object
            child := point to child object
            angles := euler angle object contains roll, pitch, yaw
            vector := contains homogenous vector information {x/w, y/w, z/w, w} where w != 0
    '''
    def __init__(self, name="", parent=None, child=None, angles=None, vector=None):
        self.name = name
        self.parent = parent
        self.child = child
        self.angles = angles
        self.vector = vector

    '''
        fxn :: makeSegment
            alternative constructor to the Segment Class
    '''
    def makeSegment(self, name, parent, child, angles, vector):
        s = Segment(name, parent, child, angles, vector)
        if (parent != None):
            s.parent.child = s
        return s

    '''
        fxn :: makeRootSegment
            Creates a root segment; the parent of the ik chain
    '''
    def makeRootSegment(self, vv):
        ea = Euler()
        s = Segment(name, None, None, ea, vv)
        return s

    '''
        fxn :: start
            returns a vector3 of the start of this segment, in the world coordinates
    '''
    def start(self):
        v = Vector3()
        return s.project(v)

    '''
        fxn :: end
            returns a vector3 at the end of this segment, in world coordinate space
    '''
    def end(self, vv):
        return s.project(vv)

    '''
        fxn :: worldMatrix
            returns a M44 that can be applied to a vector in this segment's coord space
            to convert it to the world space
    '''
    def worldMatrix(self):

        if (self.parent != None):
            m = makeMatrix44(self.parent.vector, self.angles)
            return m.multiplyMatrices(s.parent.worldMatrix())
        else:
            v = Vector3()
            return makeMatrix44(v, self.angles)
    
    '''
        fxn :: project
            transforms a local vec3 to a world vec3
    '''
    def project(self, vv):
        return vv.multiplyMatrix44(s.worldMatrix())

    '''
        fxn :: toString
            outputs object methods to strings
    '''
    def toString(self):
        print('')
        print('name: ' + str(self.name))
        self.angles.toString()
        self.vector.toString()
