

from leg import Leg

class Hexapod:

    def __init__(self):
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

        self.Leg1 = Leg(1)
        self.Leg2 = Leg(2)
        self.Leg3 = Let(3)
        self.Leg4 = Leg(4)
        self.Leg5 = Leg(5)
        self.Leg6 = Leg(6)


