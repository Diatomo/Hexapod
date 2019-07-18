

from sys import path
path.append("../utils")
from utils import *




#TODO
'''
    Description of pose here
'''
class Pose:

    '''
        constructor
            param: ea = euler angles
            @param: v = vector3
    '''
    def __init__(self, ea, v):
        self.angles = ea
        self.pos = v

    '''
        fxn: add
            adds two poses together
    '''
    def add(self, pose):
        pose.multiplyByMatrix44(self.pos.toWorld())
        self.angles.roll = self.angles.roll + pose.angles.roll
        self.angles.pitch = self.angles.pitch + pose.angles.pitch
        self.angles.yaw = self.angles.yaw + pose.angles.yaw

    '''
        fxn: toWorld
            converts pose into its world coordinates
    '''
    def toWorld(self):
        return makeMatrix(self.pos, self.angles)
    
    '''
        fxn :: toLocal
            turns pose into its local coordinates
    '''
    def toLocal(self):
        return makeMatrix(self.pos, self.angles)

    
    #TODO
    def out(self, pp):
        pass

    #TODO
    def eulerAngles(self):
        pass


    '''
        fxn :: toString
            outputs pose in string format
    '''
    def toString(self):
        print("position x: " + self.pos.x)
        print("position y: " + self.pos.y)
        print("position z: " + self.pos.z)
        print("euler roll: " + self.angles.roll)
        print("euler pitch: " + self.angles.pitch)
        print("euler yaw: " + self.angles.yaw)

