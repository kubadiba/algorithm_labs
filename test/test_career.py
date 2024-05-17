import unittest
from src.career import bfs


class TestBFS(unittest.TestCase):

    def test_case_1(self):
        hierarchy = [
            [3],
            [7, 4],
            [2, 4, 6]
        ]
        expected = 14
        result = bfs(hierarchy)
        self.assertEqual(result, expected)

    def test_case_2(self):
        hierarchy = [
            [1],
            [2, 3],
            [4, 5, 6],
            [7, 8, 9, 10]
        ]
        expected = 20
        result = bfs(hierarchy)
        self.assertEqual(result, expected)



if __name__ == '__main__':
    unittest.main()