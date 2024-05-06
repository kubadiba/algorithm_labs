import unittest
from src.calculating_number_islands import IslandCounter


class TestIslandCounter(unittest.TestCase):
    def test_count_islands(self):

        grid2 = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        island_counter2 = IslandCounter(len(grid2), len(grid2[0]), grid2)
        self.assertEqual(island_counter2.count_islands(), 0)
        grid2 = [
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1]
        ]
        island_counter2 = IslandCounter(len(grid2), len(grid2[0]), grid2)
        self.assertEqual(island_counter2.count_islands(), 1)


if __name__ == '__main__':
    unittest.main()
