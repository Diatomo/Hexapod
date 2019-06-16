
from servo import Servo


servos = []

for i in range(24):
    servos.append(Servo(i+1))

def startUp():
    for servo in servos:
        servo.startup()
    print("startup pass")

def ledTest():
    for servo in servos:
        servo.setLed(True)
    print("led pass")

def shutdown():
    for servo in servos:
        servo.shutdown()
    print("shutdown pass")

def getPos():
    for servo in servos:
        print(servo.getPosition())

def getPing():
    for servo in servos:
        print(servo.ping())



startUp()
ledTest()
getPos()
getPing()
shutdown()
