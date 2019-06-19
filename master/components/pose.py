

from sys import path
path.append("../utils")
from utils import *


class Pose:

    def __init__(self, ea, v):
        self.angles = ea
        self.pos = v

    def add(self, pose):
        pose.multiplyByMatrix44(self.pos.toWorld())
        self.angles.roll = self.angles.roll + pose.angles.roll
        self.angles.pitch = self.angles.pitch + pose.angles.pitch
        self.angles.yaw = self.angles.yaw + pose.angles.yaw

    def toWorld(self):
        return makeMatrix(self.pos, self.angles)

    #TODO perhaps inverse this?
    def toLocal(self):
        return makeMatrix(self.pos, self.angles)

