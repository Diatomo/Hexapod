

from sys import path
path.append("../utils")
from utils import *
import time
from leg import Leg


'''
    class Legs

        collection class being utilized as a data class
        resembling a struct
'''
class Legs:

    def __init__(self):
        
        '''
            Legs
        '''
        self.leg1 = Leg(1, Vector3(-61.167, 24, 98), 300)
        self.leg2 = Leg(2, Vector3(61.167, 24, 98), 60)
        self.leg3 = Let(3, Vector3(81, 24, 0), 0)
        self.leg4 = Leg(4, Vector3(61.167, 24, -98), 120)
        self.leg5 = Leg(5, Vector3(-61.167, 24, -98), 240)
        self.leg6 = Leg(6, Vector3(-81, 24, 0), 270)
        
        #leg collection
        self.legs = { 
                "FL" : self.leg1,  
                "FR" : self.leg2, 
                "MR" : self.leg3, 
                "BR" : self.leg4, 
                "BL" : self.leg5, 
                "ML" : self.leg6
        }

        '''
            Feets
        '''
        self.foot1 = self.homeFootPosition(Vector3(), leg1, Pose())
        self.foot2 = self.homeFootPosition(Vector3(), leg2, Pose())
        self.foot3 = self.homeFootPosition(Vector3(), leg3, Pose())
        self.foot4 = self.homeFootPosition(Vector3(), leg4, Pose())
        self.foot5 = self.homeFootPosition(Vector3(), leg5, Pose())
        self.foot6 = self.homeFootPosition(Vector3(), leg6, Pose())
        
        #feet collection
        self.feet = {
                "FL" : self.foot1, 
                "FR" : self.foot2, 
                "MR" : self.foot3,
                "BR" : self.foot4,
                "BL" : self.foot5,
                "ML" : self.foot6
        }

        '''
            Poses 
        '''
        self.target = Pose()
        self.lastPose = Pose()
        self.lastFeet = []
        self.nextFeet = []

'''
    class Hexapod

        a State machine to route action to the legs
'''
class Hexapod:

    def __init__(self):
        #states
        state = ""
        stateCounter = 0

        #boot slow config
        self.moveSpeedSlow = 512
        self.torqueLimitSlow = 256

        #boot fast config
        self.moveSpeedFast = 1023
        self.torqueLimitFast = 1023

	# The distance (in mm) to adjust the Y position to meet the Y target each
	# tick. This mostly controls the time it takes to stand up and sit down.
        self.yMoveSpeed = 1
        self.yawMoveSpeed = 0.5
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

        #leg && feet collection
        self.legs = Legs()

    def start(self):

        #TODO start pose
        #TODO start state
        pass

    
    #TODO test this math.
    def homeFootPosition(self, vv, leg, pose):
        hyp = math.Sqrt((leg.Origin.X * leg.Origin.X) + (leg.Origin.Z * leg.Origin.Z))
        v = pose.add(Pose(vv, 0, 0, 0)).add(Pose(Vector3(0,0,10),0,0,0))
        v = pose.add(Pose(leg.origin, leg.angles, 0, 0)).add(Pose(Vector3(0, 0, self.stepRadius - hyp),0,0,0))
        v.position
        v.y = 0.0
        return v

    '''
        Helper Functions
            Routine mathematical protocols
    '''
    def distanceFromHome(self):
        td = 0.0

        for key, leg in self.legs:
            pv = leg.presentPosition()
            td += pv.distance(self.legs.feet[key]) #TODO check index syntax
    
    def setState(self, s):
        self.stateCounter = 0
        self.stateTime = time.time()
        self.state = s

    def clamp(self, minimum, maximum, v):
        if (v < minimum):
            return minimum
        elif (v > maximum):
            return maximum
        return v

    def diffPoseY(self):
        return (self.legs.target.pos.y - self.pos.legs.lastPose.pos.y)

   def diffRoll(self):
       return (self.legs.target.roll - self.pose.roll)

    def waitForReady(self):
        pass


    '''
        boot functions
            sets moving speed
            sets torque limit
    '''
    def bootSlow(self):
        for (_, leg in self.legs):
            for (servo in leg):
                servo.setMovingSpeed(self.moveSpeedSlow)
                servo.setTorqueLimit(self.torqueLimitSlow)

    def bootFast(self):
        for (_, leg in self.legs):
            for (servo in leg):
                servo.setMovingSpeed(self.moveSpeedFast)
                servo.setTorqueLimit(self.torqueLimitFast)

    '''
        States for State Machine
    '''
    def default(self):
        self.bootFast()
        self.state = "standup"

    def standup(self):
        yOffset = self.diffRoll()
        if (math.abs(yOffset) < 1):
            self.state = "stepping"

    def sitDown(self):
        yOffset = self.diffPoseY()
        if (math.abs(yOffset) < 1):
            self.ready = False

    def stepping(self):

        if (stateCounter == 1):
            self.legs.lastPose = self.pose
            for key, foot in self.legs.feet: #TODO check iteration
                legs.lastFeet[key] = legs.feet[key]

            xzPosePos = state.Pose.pos
            xzTargetPos = state.target.pos
            xzPosePos.y = 0
            xzTargetPos.y = 0

            vecToGoal = xzTargetPos.subtract(xzPosePos)
            distToGoal = vecToGoal.magnitude()

            distToStep = min(distToGoal, self.maxStepDistance)
            if (distToStep < self.minStepDistance and math.abs(self.diffRoll()) < minTurnDistance):
                    self.legs.target = self.legs.lastPose
                    if (self.legs.shutdown == True):
                        self.setState("sitdown")
                    else:
                        self.setState("stepping")
        
        #TODO generate a gait
         
        #TODO calculate the target position for the origin

        #TODO calculate target position for each foot.
   
        #TODO move continuously toward target

        #TODO Ignore Y axis

        #TODO check state counter with gait
        #if so get ready for next cycle

        #TODO error checking

        #endif

        #TODO adjust clearence.
        #for y, x and z axis.

        #TODO update the goal of each leg

    def tick(self, cTime):
        if (self.state == "default"):
            self.default()
        elif (self.state == "standup"):
            self.standup()
        elif (self.state == "sitDown"):
            self.sitDown()
        elif (self.state == "stepping"):
            pass#TODO

    def makeGait(self):
        pass




