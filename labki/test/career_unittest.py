import unittest
from src.career import max_experience


class TestMaxExperience(unittest.TestCase):
    def test_max_experience(self):
        hierarchy = [[4], [3, 1], [2, 1, 5], [1, 3, 2, 1]]
        expected_max_experience = 12

        actual_max_experience = max_experience(hierarchy)

        self.assertEqual(actual_max_experience, expected_max_experience)


if __name__ == "__main__":
    unittest.main()
