import unittest
from src.RationalNumber import RationalNumber



class TestRationalNumber(unittest.TestCase):
    def test_add(self):
        self.assertEqual(RationalNumber(3,4)+RationalNumber(5,2), RationalNumber(13,4))

    def test_sub(self):
        self.assertEqual(RationalNumber(3,4)-RationalNumber(5,2), RationalNumber(-7,4))

    def test_mult(self):
        self.assertEqual(RationalNumber(3,4)*RationalNumber(5,2), RationalNumber(15,8))
    
    def test_div(self):
        self.assertEqual(RationalNumber(3,4)/RationalNumber(5,2), RationalNumber(3,10))
if __name__ == '__main__':
    unittest.main()