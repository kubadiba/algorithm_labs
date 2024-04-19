import unittest
from src.monotone_array import monoton

class TestMonoton(unittest.TestCase):
    """
    Test case for the monotone function.
    """

    def test_monoton(self):
        """
        Test case for the monotone function.
        """

        self.assertTrue(monoton([1, 2, 3, 4, 5]))
        self.assertTrue(monoton([5, 4, 3, 2, 1]))
        self.assertFalse(monoton([1, 3, 2, 4, 5]))
        self.assertTrue(monoton([2]))
        self.assertTrue(monoton([]))

if __name__ == '__main__':
    unittest.main()