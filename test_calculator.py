import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        # Add the following test methods to the TestCalculator class:
        self.assertEqual(self.calc.add(3.7, -98), -94.3)
        self.assertEqual(self.calc.add(1.4,3.1), 4.5)
        
    def test_sub(self):
        self.assertEqual(self.calc.subtract(1, 2), -1)
        self.assertEqual(self.calc.subtract(-98, 3.7), -101.7)
        self.assertEqual(self.calc.subtract(3.1,1.1), 2)

    def test_mul(self):
        self.assertEqual(self.calc.multiply(1, 2), 2)
        self.assertEqual(self.calc.multiply(2, -30), -60)

    def test_div(self):
        self.assertEqual(self.calc.divide(4, 2), 2)
        self.assertEqual(self.calc.divide(100, 10), 10)

    def test_mod(self):
        self.assertEqual(self.calc.modulo(5, 2), 1)
        self.assertEqual(self.calc.modulo(100, 12), 4)

if __name__ == '__main__':
    unittest.main()