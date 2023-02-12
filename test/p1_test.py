import unittest
from problem.p1_two_sum import Solution


class MyTestCase(unittest.TestCase):
    def test_example1(self):
        input_data = {
            'nums': [2, 7, 11, 15],
            'target': 9
        }

        output_data = [0, 1]

        self.assertEqual(output_data, Solution().twoSum(**input_data))

    def test_example2(self):
        input_data = {
            'nums': [3, 2, 4],
            'target': 6
        }

        output_data = [1, 2]

        self.assertEqual(output_data, Solution().twoSum(**input_data))

    def test_example3(self):
        input_data = {
            'nums': [3, 3],
            'target': 6
        }

        output_data = [0, 1]

        self.assertEqual(output_data, Solution().twoSum(**input_data))


if __name__ == '__main__':
    unittest.main()
