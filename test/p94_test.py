import unittest
from problem.p94_binary_tree_inorder_traversal import *


class TestCase(unittest.TestCase):
    def test_example1(self):
        input_data = TreeNode(1, None, TreeNode(2, TreeNode(3)))
        expected = [1, 3, 2]

        self.assertEqual(Solution().inorderTraversal(input_data), expected)

    def test_example2(self):
        input_data = TreeNode(1)
        expected = [1]

        self.assertEqual(Solution().inorderTraversal(input_data), expected)

    def test_example3(self):
        input_data = None
        expected = []

        self.assertEqual(Solution().inorderTraversal(input_data), expected)


if __name__ == '__main__':
    unittest.main()