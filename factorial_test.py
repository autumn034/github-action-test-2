import unittest
from factorial import factorial

class TestSampleMethods(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(-5), "Please enter a positive number.")
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(8), 40320)
        self.assertEqual(factorial(12), 479001600)
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(7), 5040)
        self.assertEqual(factorial(-8), "Please enter a positive number.")
        self.assertEqual(factorial(-2), "Please enter a positive number.")
        self.assertEqual(factorial(10), 3628800)
        self.assertEqual(factorial(2), 2)
        self.assertEqual(factorial(1), 1)

if __name__ == '__main__':
    unittest.main()