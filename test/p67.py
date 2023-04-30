import unittest
from problem.p67_add_binary import *


class TestCase(unittest.TestCase):
    def test_example1(self):
        input_data = ['11', '1']
        expected = '100'
        self.assertEqual(Solution().addBinary(*input_data), expected)

    def test_example2(self):
        input_data = ['1010', '1011']
        expected = '10101'
        self.assertEqual(Solution().addBinary(*input_data), expected)

    def test_example3(self):
        input_data = ['0', '0']
        expected = '0'
        self.assertEqual(Solution().addBinary(*input_data), expected)
        

if __name__ == '__main__':
    unittest.main()
