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

        expected = 20
        result = bfs(hierarchy)
        self.assertEqual(result, expected)



if __name__ == '__main__':
    unittest.main()
=======
        self.assertEqual(max_experience(hierarchy2), 22)


if __name__ == '__main__':
    unittest.main()

