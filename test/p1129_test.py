import unittest
from problem.p1129_shortest_path_with_alternating_colors_230211_fail import Solution


class MyTestCase(unittest.TestCase):

    def test_example1(self):
        input_data = {
            'n': 3,
            'red_edges': [[0, 1], [1, 2]],
            'blue_edges': []
        }

        output = [0, 1, -1]

        self.assertEqual(output, Solution().shortestAlternatingPaths(**input_data))

    def test_example2(self):
        input_data = {
            'n': 3,
            'red_edges': [[0, 1]],
            'blue_edges': [[2, 1]]
        }

        output = [0, 1, -1]

        self.assertEqual(output, Solution().shortestAlternatingPaths(**input_data))

    def test_example3(self):
        input_data = {
            'n': 3,
            'red_edges': [[1, 0]],
            'blue_edges': [[2, 1]]
        }

        output = [0, -1, -1]

        self.assertEqual(output, Solution().shortestAlternatingPaths(**input_data))

    def test_example4(self):
        input_data = {
            'n': 3,
            'red_edges': [[0, 1]],
            'blue_edges': [[1, 2]]
        }

        output = [0, 1, 2]

        self.assertEqual(output, Solution().shortestAlternatingPaths(**input_data))

    def test_example5(self):
        input_data = {
            'n': 3,
            'red_edges': [[0, 1]],
            'blue_edges': [[2, 1]]
        }

        output = [0, 1, -1]

        self.assertEqual(output, Solution().shortestAlternatingPaths(**input_data))


    def test_wrong_answer1(self):
        input_data = {
            'n': 3,
            'red_edges': [[0, 1], [0, 2]],
            'blue_edges': [[1, 0]]
        }

        output = [0, 1, 1]

        self.assertEqual(output, Solution().shortestAlternatingPaths(**input_data))


if __name__ == '__main__':
    unittest.main()
