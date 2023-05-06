import unittest
from problem.p83_remove_duplicates_from_sorted_list import *

class MyTestCase(unittest.TestCase):
    def test_example1(self):
        input_data = ListNode().from_list([1, 1, 2])
        output_data = ListNode().from_list([1, 2])

        self.assertEqual(output_data.to_list(), Solution().deleteDuplicates(input_data).to_list())

    def test_example2(self):
        input_data = ListNode().from_list([1, 1, 2, 3, 3])
        output_data = ListNode().from_list([1, 2, 3])

        self.assertEqual(output_data.to_list(), Solution().deleteDuplicates(input_data).to_list())


if __name__ == '__main__':
    unittest.main()
