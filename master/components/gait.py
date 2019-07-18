

import math


'''
    class Gait

        Determines how each group of legs should move
'''


#TODO try to finish this tonight or tomorrow
class Gait:

    def __init__(self, groupSize, tickPerStep):
        self.numLegs = 6
        self.steps = 12.0
        self.groupSize = groupSize
        self.ticksPerStepCycle = ticksPerStep * (self.numLegs / groupSize)
        self.gait = None
    
    def changeGroup(self, groupSize):
        self.groupSize = groupSize

    def selectGroup(self, groupSize):
        p = self.ticksPerStepCycle / self.steps
        
        '''
            Two at a time (three groups)

            |1|2|3|4|5|6|7|8|9|0|1|2|
            |-2-|---4---|---4---|-2-|
                ^       ^       ^
                2       6       0
        '''
        if (self.groupSize == 2):
            a = p * 2
            b = p * 6
            c = p * 10
            self.gait = { 
                0: a, #FL
                1: b, #FR
                2: a, #MR
                3: c, #BR
                4: b, #BL
                5: c  #ML
            }

        '''
            Three at a time (two groups)

            |1|2|3|4|5|6|7|8|9|0|1|2|
            |--3--|-----6-----|--3--|
                  ^           ^
                  3           9

        '''
        elif (self.groupSize == 3):
            a = p * 3
            b = p * 9
            self.gait = { 
                0: a, #FL
                1: b, #FR
                2: a, #MR
                3: b, #BR
                4: a, #BL
                5: b  #ML
            }

        '''
            Move one leg at a time (six groups)

            |1|2|3|4|5|6|7|8|9|0|1|2|
            |1|1|1|1|1|1|1|1|1|1|1|1|
              ^   ^   ^   ^   ^   ^
              1   3   5   7   9   1

        '''
        else:
            self.gait = { 
                0: p * 1,
                1: p * 3,
                2: p * 5,
                3: p * 7,
                4: p * 9,
                5: p * 11
            }

            

