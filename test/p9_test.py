import unittest
from p9_palindrome_number import Solution


class MyTestCase(unittest.TestCase):
    def test_example1(self):
        input_data = {
            "x": 121
        }

        output_data = True

        self.assertEqual(output_data, Solution().isPalindrome(**input_data))

    def test_example2(self):
        input_data = {
            "x": -121
        }

        output_data = False

        self.assertEqual(output_data, Solution().isPalindrome(**input_data))

    def test_example3(self):
        input_data = {
            "x": 10
        }

        output_data = False

        self.assertEqual(output_data, Solution().isPalindrome(**input_data))

    def test_example4(self):
        input_data = {
            'x': 1000021
        }

        output_data = False

        self.assertEqual(output_data, Solution().isPalindrome(**input_data))

    def test_example5(self):
        input_data = {
            'x': 11
        }

        output_data = True

        self.assertEqual(output_data, Solution().isPalindrome(**input_data))


if __name__ == '__main__':
    unittest.main()
