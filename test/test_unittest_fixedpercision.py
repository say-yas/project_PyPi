import unittest
from src.FixedPrecision import FixedPrecision



class TestFixedPrecision(unittest.TestCase):
    def test_add(self):
        self.assertEqual(FixedPrecision(3.124)+FixedPrecision(5.2), FixedPrecision(8.324))

    def test_sub(self):
        self.assertEqual(FixedPrecision(3.124)-FixedPrecision(5.2), FixedPrecision(-2.076))

    def test_mult(self):
        self.assertEqual(FixedPrecision(3.124)*FixedPrecision(5.2), FixedPrecision(16.12,2))
    
    def test_div(self):
        self.assertEqual(FixedPrecision(3.124)/FixedPrecision(5.2), FixedPrecision(0.6007692307692307))

if __name__ == '__main__':
    unittest.main()