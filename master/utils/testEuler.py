


from utils import *
import unittest

roll = 0
pitch = 1
yaw = 2


class testEuler(unittest.TestCase):

    def testEuler(self):
        ea = Euler()
        self.assertEqual(ea.roll, 0, "ea roll did not construct correctly")
        self.assertEqual(ea.pitch, 0, "ea pitch did not construct correctly")
        self.assertEqual(ea.yaw, 0, "ea yaw did not construct correctly")

    def testSingularEuler(self):
        ea = makeSingularEulerAngle(roll, 180)
        self.assertEqual(ea.roll, 180, "ea roll did not set correctly")
        self.assertEqual(ea.pitch, 0, "ea pitch did not set correctly")
        self.assertEqual(ea.yaw, 0, "ea yaw did not set correctly")

        ea = makeSingularEulerAngle(pitch, 180)
        self.assertEqual(ea.roll, 0, "ea roll did not set correctly")
        self.assertEqual(ea.pitch, 180, "ea pitch did not set correctly")
        self.assertEqual(ea.yaw, 0, "ea yaw did not set correctly")
        
        ea = makeSingularEulerAngle(yaw, 180)
        self.assertEqual(ea.roll, 0, "ea roll did not set correctly")
        self.assertEqual(ea.pitch, 0, "ea pitch did not set correctly")
        self.assertEqual(ea.yaw, 180, "ea yaw did not set correctly")
        
        ea = makeSingularEulerAngle(4, 180)
        self.assertEqual(ea.roll, 0, "ea roll did not set correctly")
        self.assertEqual(ea.pitch, 0, "ea pitch did not set correctly")
        self.assertEqual(ea.yaw, 0, "ea yaw did not set correctly")



if __name__ == '__main__':
    unittest.main()
