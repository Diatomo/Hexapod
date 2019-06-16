
'''
    config.py

    This script is to practice and set the config
    of the ax-12 servos.


    Packet Structure
        +   2 start bytes (255 or 0xff)
        +   Next Byte = ID
        +   Next Byte = Length of the Packet
        +   Next Byte = Instruction to Carry Out == Ping,Read,Write,SyncWrite
        +   Next Byte(s) = parameters
        +   Last Byte = checksum
'''

import serial

AX_WRITE_DATA = 3
AX_READ_DATA = 4

s = serial.Serial()
s.baudrate = 1000000
s.port = "/dev/ttyUSB0"
s.open()


'''
example::
'''

def setReg(ID,reg,values):
    length = 3 + len(values)
    checksum = 255 - ((index + length + AX_WRITE_DATA + reg + sum(values))%256)
    s.write(chr(startByte) + chr(startByte) + chr(ID) + chr(length) + chr(AX_WRITE_DATA) + chr(reg))
    for val in values:
        s.write(chr(val))
    s.write(chr(checksum))


def protocol(ID):
    startByteA = 0xff
    startByteB = 0xff


