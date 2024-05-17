import unittest
from src.painting_billboard_distribution import max_value


class TestMaxValueFunction(unittest.TestCase):

    def test_max_value(self):
        k = 2
        t = 5
        l = [10, 15, 10, 5, 10, 15, 20, 20, 15]
        result = max_value(k, t, l)
        self.assertEqual(result, 325)


if __name__ == '__main__':
    unittest.main()
