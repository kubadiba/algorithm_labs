import unittest
import os

from problem_about_experience import max_experience


class TestMaxExperience(unittest.TestCase):
    def test_max_experience(self):
        test_data_folder = "path/to/test/data/folder"
        input_file = os.path.join(test_data_folder, "career.in")
        output_file = os.path.join(test_data_folder, "career.out")

        with open(output_file, "r") as f:
            expected_max_experience = int(f.read().strip())

        with open(input_file, "r") as f:
            L = int(f.readline())
            hierarchy = []
            for _ in range(L):
                hierarchy.append(list(map(int, f.readline().split())))

        actual_max_experience = max_experience(hierarchy)
        self.assertEqual(actual_max_experience, expected_max_experience)


if __name__ == "__main__":
    unittest.main()
