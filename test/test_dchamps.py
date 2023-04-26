import unittest
import random

from problem.dchamps import *


class MyTestCase(unittest.TestCase):
    # def test_example1(self):
    #     input_data = {
    #         'N': 10,
    #         'A': [70, 45, 63, 69, 77, 81, 33, 100, 75, 10]
    #     }
    #
    #     output_data = "BCBBAACABC"
    #
    #     self.assertEqual(output_data, solution(**input_data))
    #
    # def test_example2(self):
    #     input_data = {
    #         'N': 7,
    #         'A': [1, 3, 4, 7, 6, 5, 2]
    #     }
    #
    #     output_data = "CBBAABC"
    #
    #     self.assertEqual(output_data, solution(**input_data))
    #
    # def test_example3(self):
    #     input_data = {
    #         'N': 6,
    #         'A': [100, 70, 80, 80, 55, 60]
    #     }
    #
    #     output_data = "ABBBCC"
    #
    #     self.assertEqual(output_data, solution(**input_data))

    # def test_example4(self):
    #     input_data = {
    #         'N': 7,
    #         'A': [70,45,63,69,77,81,33]
    #
    #     }
    #
    #     output_data = "BCCBAAC"
    #
    #     self.assertEqual(output_data, solution(**input_data))
    #
    # def test_example5(self):
    #     input_data = {
    #         'N': 9,
    #         'A': [98, 65, 45, 34, 23, 13, 15, 57, 55]
    #     }
    #
    #     output_data = "AABBCCCAB"
    #
    #     self.assertEqual(output_data, solution(**input_data))

    def test_example6(self):
        input_data = {
            'N': 7,
            'A': [70, 45, 69, 69, 77, 81, 33]
        }

        output_data = "BCCCAAC"

        self.assertEqual(output_data, solution(**input_data))


if __name__ == '__main__':
    unittest.main()
