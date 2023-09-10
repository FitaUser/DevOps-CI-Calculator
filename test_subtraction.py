import unittest
from Calculator import subtraction

class TestCalculator(unittest.TestCase):

    def test_subtraction(self):
        self.assertEqual(subtraction(2, 3), -1)
        self.assertEqual(subtraction(-2, 3), -5)
        self.assertEqual(subtraction(-2, -3), 1)

if __name__ == '__main__':
    unittest.main()