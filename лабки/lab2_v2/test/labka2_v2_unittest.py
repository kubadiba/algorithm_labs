import unittest
from labka2_v2 import max_value

class TestMaxValueFunction(unittest.TestCase):

    def test_max_value(self):
        K = 2
        T = 5
        L = [10, 15, 10, 5, 10, 15, 20, 20, 15]
        result = max_value(K, T, L)
        self.assertEqual(result, 325)

if __name__ == '__main__':
    unittest.main()
