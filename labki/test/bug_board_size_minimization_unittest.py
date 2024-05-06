import unittest

from src.bug_board_size_minimization import search_sq, verify_capacity


class TestFindSquare(unittest.TestCase):

    def test_find_square(self):
        self.assertEqual(search_sq(9, 2, 3), 9)

    def test_check_capacity(self):
        self.assertTrue(verify_capacity(2, 3, 9, 9))


if __name__ == '__main__':
    unittest.main()
