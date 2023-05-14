import unittest
from problem.p100_same_tree import *
from library.node import TreeNode

class MyTestCase(unittest.TestCase):
    def test_example1(self):
        input_data = {
            'p': TreeNode(1, TreeNode(2), TreeNode(3)),
            'q': TreeNode(1, TreeNode(2), TreeNode(3))
        }

        output_data = True

        self.assertEqual(output_data, Solution().isSameTree(**input_data))

    def test_example2(self):
        input_data = {
            'p': TreeNode(1, TreeNode(2)),
            'q': TreeNode(1, None, TreeNode(2))
        }

        output_data = False

        self.assertEqual(output_data, Solution().isSameTree(**input_data))

    def test_example3(self):
        input_data = {
            'p': TreeNode(1, TreeNode(2), TreeNode(1)),
            'q': TreeNode(1, TreeNode(1), TreeNode(2))
        }

        output_data = False

        self.assertEqual(output_data, Solution().isSameTree(**input_data))

    def test_example4(self):
        input_data = {
            'p': TreeNode(1, TreeNode(1)),
            'q': TreeNode(1, None, TreeNode(1))
        }

        output_data = False

        self.assertEqual(output_data, Solution().isSameTree(**input_data))


if __name__ == '__main__':
    unittest.main()
