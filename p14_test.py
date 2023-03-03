import unittest
from p14_longest_common_prefix import Solution


class MyTestCase(unittest.TestCase):

    def test_example1(self):
        input_data = {
            "strs": ["flower", "flow", "flight"]
        }

        output_data = "fl"

        self.assertEqual(output_data, Solution().longestCommonPrefix(**input_data))

    def test_example2(self):
        input_data = {
            "strs": ["dog", "racecar", "car"]
        }

        output_data = ""

        self.assertEqual(output_data, Solution().longestCommonPrefix(**input_data))

    def test_example3(self):
        input_data = {
            "strs": ["dog"]
        }

        output_data = "dog"

        self.assertEqual(output_data, Solution().longestCommonPrefix(**input_data))

    def test_exemple4(self):
        input_data = {
            "strs": ["a", "b"]
        }

        output_data = ""

        self.assertEqual(output_data, Solution().longestCommonPrefix(**input_data))


if __name__ == '__main__':
    unittest.main()
