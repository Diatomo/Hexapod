
from servo import Servo
import time


coxaOffsetY = -12.0
coxaOffsetZ = 39.0

femurLength = 100.0
tibiaLength = 85.0
tarsusLength = 80.5


class Leg:

    #TODO give these servos Identifications
    def __init__(self, baseId):
        self.coxa = Servo(baseId * numJoints + 1)
        self.femur = Servo(baseId * numJoints + 2)
        self.tibia = Servo(baseId * numJoints + 3)
        self.tarsus = Servo(baseId * numJoints + 4)
        self.joints = [self.coxa, self.femur, self.tibia, self.tarsus]

# PresentPosition returns the actual present posion (relative to the center of
# the hexapod) of the end of this leg. This involves reading the position of
# each servo, so don't call it in the main loop.
def presentPosition():
	v = math3d.ZeroVector3

        #get angles
	coxaAngle = self.coxa.getAngle()
	femurAngle = self.femur.getAngle()
	tibiaAngle = self.tibia.getAngle()
	tarsusPos = self.tarsus.getAngle()

        #aliases
        coxaEuler = math3d.MakeSingularEulerAngle(heading, coxaAngle)
        coxaVector = math3d.makeVector3(0, coxaOffsetY, coxaOffetZ)
        femurEuler = math3d.makeSingularEulerAngle(pitch, femurAngle)
        femurVector = math3d.makeVector3(0, 0, femurLength)
        tibiaEuler = math3d.makeSingularEulerAngle(pitch, tibiaAngle)
        tibiaVector = math3d.makeSingularEulerAngle(0, 0, tibiaLength)
        tarsusEuler = math3d.makeSingularEulerAngle(pitch, tarsusAngle)
        tarsusVector = math3d.makeVector3(0, 0, tarsusLength)

	#make segments
        root = s.rootSegment()
        coxaSeg = s.makeSegment("coxa", root, coxaEuler, coxaVector)
        femurSeg = s.makeSegment("femur", coxaSeg, femurEuler, femurVector)
        tibiaSeg = s.makeSegment("tibia", femurSeg, tibiaEuler, tibiaVector)
        tarsusSeg = s.makeSegment("tarsus", tibiaSeg, tarsusEuler, tarsusVector)

	return tarsus.End()


# SetGoal sets the goal position of the leg to the given vector in the chassis
# coordinate space.
def setGoal(vt):

    '''
	 Solve the angle of the coxa by looking at the position of the target from
	 above (x,z). Note that "above" here is in the chassis space, which might
	 not be parallel to the actual ground. Fortunately, the coxa moves around
	 the Y axis in that space, so we can cheat with 2d trig.
    '''
    coxAngle = utils.degree(math.atan2(vt.X-leg.Origin.X, vt.Z-leg.Origin.Z)) - leg.Angle
    '''
	 The other joints are all on the same plane, which we know intersects vt
	 from the above. So the rest of the function can use 2d trig on the (z,y)
	 axis in the coxa space. More cheating!
    '''
    #make root segment
    root = s.rootSegment()

    #alias
    coxaEuler = math3d.MakeSingularEulerAngle(heading, coxaAngle)
    coxaVector = math3d.makeVector3(0, coxaOffsetY, coxaOffetZ)

    #make coxa segment
    coxa = s.makeSegment("coxa", root, coxaEuler, coxaVector)

    '''
	 The following points (vr,vt) and lengths (a,b,c) are known:
	
	         (?)
	         / \
	        /   \
	       a     b
	      /       \
	     /         \
	   (vr)        (?)
	                |
	                c
	                |
	              (vt)
	
    '''
    vr = coxa.End()
    a = femurLength
    b = tibiaLength
    c = tarsusLength

    # Pick a totally arbitrary point below (vr), to make more triangles.
    vp = vr.add(v.makeVector3(0,-50,0))

    # The tarsus joint should always be directly above the target. We want that
    # last segment to be perpendicular to the ground, because it looks cool.
    vq = vt.add(v.Vector3(0, tarsusLength, 0))
    
    '''
	 The leg now looks like:
	
	         (?)
	         / \
	        /   \
	       a     b
	      /       \
	     /         \
	   (vr)       (vq)
	    |           |
	   (vp)         c
	                |
	              (vt)
	
    '''
    # Calculate the length of the remaining edges.
    d = vr.Distance(vq)
    e = vr.Distance(vt)
    f = vr.Distance(vp) # always vr.Y-50?
    g = vp.Distance(vt)

    # Calculate the inner angles of the triangles using the law of cos.
    aa = sss(b, a, d)
    bb = sss(c, d, e)
    cc = sss(g, e, f)
    dd = sss(a, d, b)
    ee = sss(e, c, d)
    hh = 180 - (aa + dd)

    # Transform inner angles to servo angles. The zero angle of each servo
    # makes the leg stick directly outwards from the chassis.
    femPos := 90 - (aa + bb + cc)
    tibPos := 180 - hh
    tarPos := 180 - (dd + ee)

    # Crash if any of the angles are invalid.
    #TODO catch errors

    #move the servos
    servos.moveTo(leg.Coxa, coxPos)
    servos.moveTo(leg.Femur, femPos)
    servos.moveTo(leg.Tibia, tibPos)
    servos.moveTo(leg.Tarsus, tarPos+tarsusExtraAngle)

    return nil


    def setLed(self, status):
        for joint in joints:
            joint.setLed(status)


# sss returns the angle α, given the length of sides a, b, and c.
# See: http://en.wikipedia.org/wiki/Solution_of_triangles
def sss(a, b, c):
    return utils.degree(math.acos(((b * b) + (c * c) - (a * a)) / (2 * b * c)))

def distance(a, b):
    return math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2 + (a.z - b.z)**2)



