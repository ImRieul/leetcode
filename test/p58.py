import unittest
from problem.p58_legnth_of_last_word import *


class MyTestCase(unittest.TestCase):
    def test_example1(self):
        input_data = {
            's': "Hello World"
        }

        output_data = {
            'k': 5
        }

        self.assertEqual(output_data['k'], Solution().lengthOfLastWord(**input_data))

    def test_example2(self):
        input_data = {
            's': "   fly me   to   the moon  "
        }

        output_data = {
            'k': 4
        }

        self.assertEqual(output_data['k'], Solution().lengthOfLastWord(**input_data))

    def test_example3(self):
        input_data = {
            's': "luffy is still joyboy"
        }

        output_data = {
            'k': 6
        }

        self.assertEqual(output_data['k'], Solution().lengthOfLastWord(**input_data))


if __name__ == '__main__':
    unittest.main()
