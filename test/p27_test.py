import unittest
from problem.p27_remove_element import *


class MyTestCase(unittest.TestCase):
    def test_example1(self):
        input_data = {
            'nums': [3, 2, 2, 3],
            'val': 3
        }

        output_data = {
            'k': 2,
            'nums': [2, 2]
        }

        self.assertEqual(output_data['k'], Solution().remove_element(**input_data))
        self.assertEqual(output_data['nums'], input_data['nums'])

    def test_example2(self):
        input_data = {
            'nums': [0, 1, 2, 2, 3, 0, 4, 2],
            'val': 2
        }

        output_data = {
            'k': 3,
            'nums': [0, 1, 3, 0, 4]
        }

        self.assertEqual(output_data['k'], Solution().remove_element(**input_data))
        self.assertEqual(output_data['nums'], input_data['nums'])


if __name__ == '__main__':
    unittest.main()
