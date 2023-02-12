import unittest
from problem.p20_valid_parentheses import Solution


class MyTestCase(unittest.TestCase):
    def test_example1(self):
        input_data = {
            's': "()"
        }

        output_data = True

        self.assertEqual(output_data, Solution().isValid(**input_data))

    def test_example2(self):
        input_data = {
            's': "()[]{}"
        }

        output_data = True

        self.assertEqual(output_data, Solution().isValid(**input_data))

    def test_example3(self):
        input_data = {
            's': "(]"
        }

        output_data = False

        self.assertEqual(output_data, Solution().isValid(**input_data))


    def test_example4(self):
        input_data = {
            's': "([)]"
        }

        output_data = False

        self.assertEqual(output_data, Solution().isValid(**input_data))

    def test_example5(self):
        input_data = {
            's': "{[]}"
        }

        output_data = True

        self.assertEqual(output_data, Solution().isValid(**input_data))


if __name__ == '__main__':
    unittest.main()
