
from utils import *
import unittest

roll = 0
pitch = 1
yaw = 2


class testVector3(unittest.TestCase):

    def testVector3(self):
        vv = Vector3()
        self.assertEqual(vv.x, 0, "vv x did not construct correctly")
        self.assertEqual(vv.y, 0, "vv y did not construct correctly")
        self.assertEqual(vv.z, 0, "vv z did not construct correctly")

    def testVector3Values(self):
        vv = Vector3(2, 2, 2)
        self.assertEqual(vv.x, 2, "vv x did not value correctly")
        self.assertEqual(vv.y, 2, "vv y did not value correctly")
        self.assertEqual(vv.z, 2, "vv z did not value correctly")

    def testVector3Make(self):
        vv = makeVector3(2, 2, 2)
        self.assertEqual(vv.x, 2, "vv x did not make correctly")
        self.assertEqual(vv.y, 2, "vv y did not make correctly")
        self.assertEqual(vv.z, 2, "vv z did not make correctly")

    def testVector3Add(self):
        vx = makeVector3(1,1,1)
        vy = makeVector3(1,1,1)
        vv = vx.add(vy)
        self.assertEqual(vv.x, 2, "vv x did not add correctly")
        self.assertEqual(vv.y, 2, "vv y did not add correctly")
        self.assertEqual(vv.z, 2, "vv z did not add correctly")

    def testVector3Sub(self):
        vx = makeVector3(4,4,4)
        vy = makeVector3(2,2,2)
        vv = vx.subtract(vy)
        self.assertEqual(vv.x, 2, "vv x did not sub correctly")
        self.assertEqual(vv.y, 2, "vv y did not sub correctly")
        self.assertEqual(vv.z, 2, "vv z did not sub correctly")

    def testMultScalar(self):
        vx = makeVector3(1,1,1)
        vv = vx.multScalar(2) 
        self.assertEqual(vv.x, 2, "vv x did not scale correctly")
        self.assertEqual(vv.y, 2, "vv y did not scale correctly")
        self.assertEqual(vv.z, 2, "vv z did not scale correctly")


if __name__ == '__main__':
    unittest.main()
