import unittest
from src.FloatNumber import FloatNumber



class TestFloatNumber(unittest.TestCase):
    def test_add(self):
        self.assertEqual(FloatNumber(3.124)+FloatNumber(5.2), FloatNumber(8.324))

    def test_sub(self):
        self.assertEqual(FloatNumber(3.124)-FloatNumber(5.2), FloatNumber(-2.076))

    def test_mult(self):
        self.assertEqual(FloatNumber(3.124)*FloatNumber(5.2), FloatNumber(16.2448))
    
    def test_div(self):
        self.assertEqual(FloatNumber(3.124)/FloatNumber(5.2), FloatNumber(0.6007692307692307))

if __name__ == '__main__':
    unittest.main()
