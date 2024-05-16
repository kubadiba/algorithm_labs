import unittest
from src.optimizing_communication_network_during_blackouts import Graph, kruskal_minimum_spanning_tree

class TestGraphMethods(unittest.TestCase):

    def test_add_edge(self):
        g = Graph(5)
        g.add_edge(0, 1, 2)
        g.add_edge(1, 2, 3)
        self.assertEqual(len(g.edges), 2)
        self.assertEqual(g.edges[0], [0, 1, 2])
        self.assertEqual(g.edges[1], [1, 2, 3])

    def test_find(self):
        g = Graph(5)
        parent = [0, 1, 2, 3, 4]
        self.assertEqual(g.find(parent, 3), 3)
        parent[3] = 2
        self.assertEqual(g.find(parent, 3), 2)

    def test_union(self):
        g = Graph(5)
        parent = [0, 1, 2, 3, 4]
        rank = [0, 0, 0, 0, 0]
        g.union(parent, rank, 1, 2)
        self.assertEqual(parent, [0, 1, 1, 3, 4])
        g.union(parent, rank, 0, 3)
        self.assertEqual(parent, [0, 1, 1, 0, 4])

if __name__ == '__main__':
    unittest.main()
