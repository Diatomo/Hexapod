

'''
    Hexapod.py

    Author :: Charles C. Stevenson
    Date 12.22.18

    **Place holder
    just going to be an interface for now

'''



class Hexapod:

    def __init__(self):

        sDefault = ""
        sStandUp = "sStandUp"
        sSitDown = "sSitDown"
        sStepping = "sStepping"

        moveSpeedSlow = 512
        torqueLimitSlow = 256

        moveSpeedFast = 1023
        torqueLimitFast = 1023

        yMoveSpeed = 1
        bankMoveSpeed = 0.5
        pitchMoveSpeed = 0.5

        stepRadius = 240.0

        baseTicksPerStep = 20

        minTicksPerStep = 4

        maxTicksPerStep = 80

        stepHeight = 40.0

        minStepDistance = 20.0

        minTurnDistance = 5.0

        maxStepDistance = 90.0

    #TODO fill in math depending on states

    def clamp(self,min,max,v):
        value = v
        if (v < min):
            value = min
        elif (v > max):
            value = max
        return value
