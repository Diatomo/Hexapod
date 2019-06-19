

from leg import Leg

class Hexapod:

    def __init__(self):
        self.moveSpeedSlow = 512
        self.torqueLimitSlow = 256

        self.moveSpeedFast = 1023
        self.torqueLimitFast = 1023

	# The distance (in mm) to adjust the Y position to meet the Y target each
	# tick. This mostly controls the time it takes to stand up and sit down.
        self.yMoveSpeed = 1

        self.bankMoveSpeed = 0.5
        self.pitchMoveSpeed = 0.5

	# Distance (on the X/Z axis) from the origin to the point at which the feet
	# should be positioned. This isn't adjustable at runtime, because there are
	# very few valid settings.
        self.stepRadius = 240.0
        
	# The number of ticks per step, i.e. a single foot is lifted, moved to its
	# new position, and put down.
        self.baseTicksPerStep = 20

	# The minimum number of ticks allowed per step.
        self.minTicksPerStep = 4

	# The maximum number of ticks allowed per step.
        self.maxTicksPerStep = 80

	# The offset (on the Y axis) which feet should be moved to on the up step,
	# relative to the origin.
        self.stepHeight = 40.0

	# Minimum distance which the desired foot position should be from its
	# actual position before a step should be taken to correct it.
        self.minStepDistance = 20.0
        self.minTurnDistance = 5.0

	# The distance (in mm) which the hex can move per step cycle. This should
	# be determined experimentally; too high and the legs get tangled up.
        self.maxStepDistance = 90.0

        self.leg1 = Leg(1, Vector3(-61.167, 24, 98), 300)
        self.leg2 = Leg(2, Vector3(61.167, 24, 98), 60)
        self.leg3 = Let(3, Vector3(81, 24, 0), 0)
        self.leg4 = Leg(4, Vector3(61.167, 24, -98), 120)
        self.leg5 = Leg(5, Vector3(-61.167, 24, -98), 240)
        self.leg6 = Leg(6, Vector3(-81, 24, 0), 270)
        self.legs = { 
                "FL" : self.leg1,  
                "FR" : self.leg2, 
                "MR" : self.leg3, 
                "BR" : self.leg4, 
                "BL" : self.leg5, 
                "ML" :self.leg6
        }

    def start(self):

        #TODO start pose
        #TODO start state
        pass

    def makeGait(self):
        pass




