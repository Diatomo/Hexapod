
import subprocess

'''

    Class Input

    opens an input stream to a switch pro controller

'''

#open file
path = '../../venv/lib/python3.6/site-packages/HID-Joy-Con-Whispering/uinputdriver/uinputdriver'
proc = subprocess.Popen([path], stdout=subprocess.PIPE)

class Input:

    '''
        init bytes to get from controller
    '''
    def __init__(self):
        self.lenInput = 30
        self.input = [x for x in range(self.lenInput)] #define input array
        self.right = 13 #13th short encodes right side of controller (buttons right triggs)
        self.left = 15 #15th hex byte encodes left side of controller (dpad left triggs)
        self.joyLeft = [16,17,18]
        self.joyRight = [19,20,21]
        self.line = ""

    '''
        begin input stream
    '''
    def inputStream(self):

        #read controller stream
        #while True:
        #print("inputs")
        #get line
        line = proc.stdout.readline()
        #if not line:
         #   break
        #format line
        line = str(line.rstrip())
        output = line.split(' ')
        output = output[3:]

        #cheap hack for IndexException error
        try:
            print(output[self.right] + ' ' + output[self.left] + ' ' + output[self.joyLeft[2]] + ' ' + output[self.joyRight[2]])
        except:
            pass

    '''
        report values
    '''
    def poll(self):
        self.inputStream()
        if (self.line):
            output = {'left' : 0, 'right' : 0, 'joyLeft' : [0,0,0], 'joyRight' : [0,0,0]}
            output['left'] = self.line[self.left]
            output['right'] = self.line[self.right]
            for value in range(len(self.joyLeft)):
                output['joyLeft'][value] = self.line[self.joyLeft[value]]
                output['joyRight'][value] = self.line[self.joyRight[value]]
        #return output

    #TODO map byte values into directions
    def direction(self):
        pass
