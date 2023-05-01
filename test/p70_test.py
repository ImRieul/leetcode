import unittest
from problem.p70_climbing_stairs import *


class TestCase(unittest.TestCase):
    def test_example1(self):
        input_data = 2
        expected = 2
        self.assertEqual(Solution().climbStairs(input_data), expected)

    def test_example2(self):
        input_data = 3
        expected = 3
        self.assertEqual(Solution().climbStairs(input_data), expected)

    def test_example3(self):
        input_data = 4
        expected = 5
        self.assertEqual(Solution().climbStairs(input_data), expected)

    def test_example4(self):
        input_data = 5
        expected = 8
        self.assertEqual(Solution().climbStairs(input_data), expected)

    def test_example5(self):
        input_data = 1
        expected = 1
        self.assertEqual(Solution().climbStairs(input_data), expected)

    def test_example6(self):
        input_data = 6
        expected = 13
        self.assertEqual(Solution().climbStairs(input_data), expected)

if __name__ == '__main__':
    unittest.main()