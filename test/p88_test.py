import unittest
from problem.p88_merge_sorted_array import *

class MyTestCase(unittest.TestCase):
    def test_example1(self):
        input_data = {
            'nums1': [1, 2, 3, 0, 0, 0],
            'm': 3,
            'nums2': [2, 5, 6],
            'n': 3
        }

        output_data = [1, 2, 2, 3, 5, 6]

        Solution().merge(**input_data)
        self.assertEqual(output_data, input_data.get('nums1'))


    def test_example2(self):
        input_data = {
            'nums1': [1],
            'm': 1,
            'nums2': [],
            'n': 0
        }

        output_data = [1]

        Solution().merge(**input_data)
        self.assertEqual(output_data, input_data.get('nums1'))

    def test_example3(self):
        input_data = {
            'nums1': [0],
            'm': 0,
            'nums2': [1],
            'n': 1
        }

        output_data = [1]

        Solution().merge(**input_data)
        self.assertEqual(output_data, input_data.get('nums1'))



if __name__ == '__main__':
    unittest.main()
