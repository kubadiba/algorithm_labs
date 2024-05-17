import unittest
from src.career import max_experience


class TestMaxExperience(unittest.TestCase):
    def test_max_experience(self):
        # Test case 1
        hierarchy1 = [
            [3],
            [7, 4],
            [2, 4, 6],
            [8, 5, 9, 3]
        ]
        self.assertEqual(max_experience(hierarchy1), 23)

        # Test case 2
        hierarchy2 = [
            [1],
            [2, 3],
            [4, 5, 6],
            [7, 8, 9, 10]
        ]
        self.assertEqual(max_experience(hierarchy2), 22)


if __name__ == '__main__':
    unittest.main()
