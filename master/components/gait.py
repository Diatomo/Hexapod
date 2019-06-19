

import math


'''
    class Gait

        Determines how each group of legs should move
'''


#TODO try to finish this tonight or tomorrow
class Gait:

    def __init__(self, groupSize, tickPerStep):
        self.ticksPerStepCycle = ticksPerStep * (6 / groupSize)
        cc = curveCenters(groupSize, ticksPerStepCycle)

