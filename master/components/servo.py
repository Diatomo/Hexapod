
from sys import path

path.append("../dynamixel/ax12")
from ax12 import Ax12 #TODO update to python3
s = Ax12()

'''

    Class Servo

Description:
    Contains ax12 api calls to configue servo parameters,
    ping servo information and rotate the servo

'''

class Servo:

    #init servo with ID
    def __init__(self, idx):
        self.id = idx
        self.slowSpeed = 512
        self.fastSpeed = 1023

    #startup (may not be needed)
    def startup(self):
        try:
            s.ping(self.id)
            self.setLed(True)
        except:
            print("Error, The motor is not active")

    #shutdown might need to limit torque
    def shutdown(self):
        self.setLed(False)

    def move(self, position):
        s.move(self.id, position)

    '''
        setters
    '''
    def setMovementSpeed(self, speed):
        s.moveSpeed(self.id, s.readPosition(self.id), speed)

    def setLed(self, status):
        s.setLedStatus(self.id, status)

    def setTorque(self, torque):
        s.setTorqueLimit(self.id, torque)

    def setAngle(self, cwLimit, ccwLimit):
        s.setAngleLimit(self.id, cwLimit, ccwLimit)
    
    '''
        getters
    '''
    def ping(self):
        return s.ping(self.id)

    def getPosition(self):
        return s.readPosition(self.id)

    def getSpeed(self):
        return s.readSpeed(self.id)
    
    def getMovingStatus(self):
        return s.readMovingStatus(self.id)

