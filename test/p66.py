import unittest
from problem.p66_plus_one import *


class TestCase(unittest.TestCase):
    def test_example1(self):
        input_data = [1, 2, 3]
        expected = [1, 2, 4]

        self.assertEqual(expected, Solution().plusOne(input_data))

    def test_example2(self):
        input_data = [4, 3, 2, 1]
        expected = [4, 3, 2, 2]

        self.assertEqual(expected, Solution().plusOne(input_data))

    def test_example3(self):
        input_data = [9]
        expected = [1, 0]

        self.assertEqual(expected, Solution().plusOne(input_data))


if __name__ == '__main__':
    unittest.main()
