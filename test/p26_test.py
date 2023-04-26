import unittest
from problem.p26_remove_duplicates_from_sorted_array import *


class MyTestCase(unittest.TestCase):
    def test_example1(self):
        input_data = {
            'nums': [1, 1, 2]
        }

        output_data = {
            'k': 2,
            'nums': [1, 2, 0]
        }

        self.assertEqual(output_data['k'], Solution().remove_duplicates(**input_data))
        self.assertEqual(output_data['nums'], input_data['nums'])

    def test_example2(self):
        input_data = {
            'nums': [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        }

        output_data = {
            'k': 5,
            'nums': [0, 1, 2, 3, 4, 0, 0, 0, 0, 0]
        }

        self.assertEqual(output_data['k'], Solution().remove_duplicates(**input_data))
        self.assertEqual(output_data['nums'], input_data['nums'])


if __name__ == '__main__':
    unittest.main()
