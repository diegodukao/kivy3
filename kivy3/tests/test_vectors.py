
import unittest
from kivy3 import Vector3


class Vector3Test(unittest.TestCase):
    
    def test_create(self):
        v = Vector3(1, 2, 3)
        self.assertEquals(v[0], 1)
        self.assertEquals(v[1], 2)
        self.assertEquals(v[2], 3)
        v = Vector3([4, 5, 6])
        self.assertEquals(v[0], 4)
        self.assertEquals(v[1], 5)
        self.assertEquals(v[2], 6)
        try:
            Vector3(1, 2, 3, 4)
            assert False, "This shold not reached"
        except:
            pass
        try:
            Vector3([3, 4, 2, 1])
            assert False, "This shold not reached"
        except:
            pass
    
    def test_add(self):
        v1 = Vector3(1, 2, 3)
        v2 = Vector3(4, 5, 6)
        v = v1 + v2
        self.assertEqual(v, [5, 7, 9])
        v1.add(v2)
        self.assertEqual(v1, [5, 7, 9])
        self.assertEqual(v + 2, [7, 9, 11])


if __name__ == '__main__':
    unittest.main()