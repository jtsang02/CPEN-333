from demo import Arithmetic

import unittest # import test framework

class Test(unittest.TestCase):
    
    def test_add1(self):
        a, b = 25.6, -97.0
        arithmetic = Arithmetic()
        self.assertEqual(arithmetic.add(a, b), a + b)
    
    def test_add2(self):
        a, b = 0.0, 0.0
        arithmetic = Arithmetic()
        self.assertEqual(arithmetic.add(a, b), a + b)
    
    def test_subtract1(self):
        a, b = 34.0, 16.55
        arithmetic = Arithmetic()
        self.assertEqual(arithmetic.subtract(a, b), a - b)
    
    def test_subtract2(self):
        a, b = -91.0, -88.8
        arithmetic = Arithmetic()
        self.assertEqual(arithmetic.subtract(a, b), a - b)

if __name__ == '__main__':
    unittest.main()


