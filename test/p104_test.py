import unittest
from problem.p104_maximum_depth_of_binary_tree import *


class MyTestCase(unittest.TestCase):
    def test_example1(self):
        input_data = {
            'root': TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        }

        output_data = 3

        self.assertEqual(output_data, Solution().maxDepth(input_data['root']))

    def test_example2(self):
        input_data = {
            'root': TreeNode(1, None, TreeNode(2))
        }

        output_data = 2

        self.assertEqual(output_data, Solution().maxDepth(input_data['root']))


if __name__ == '__main__':
    unittest.main()