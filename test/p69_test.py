import unittest
from problem.p69_sqrt import *


class TestCase(unittest.TestCase):
    def test_example1(self):
        input_data = 4
        expected = 2
        self.assertEqual(expected, Solution().square_root(input_data))

    def test_example2(self):
        input_data = 8
        expected = 2
        self.assertEqual(expected, Solution().square_root(input_data))

    def test_example3(self):
        input_data = 9
        expected = 3
        self.assertEqual(expected, Solution().square_root(input_data))

    def test_example4(self):
        input_data = 3
        expected = 1
        self.assertEqual(expected, Solution().square_root(input_data))

if __name__ == '__main__':
    unittest.main()