import unittest
from src.heap_based_priority_queue import MaxHeap, PriorityNode

class TestMaxHeap(unittest.TestCase):

    def test_insert(self):
        heap = MaxHeap()
        heap.insert((3, 'a'))
        heap.insert((5, 'b'))
        heap.insert((1, 'c'))
        heap.insert((4, 'd'))
        self.assertEqual(heap.heap, [(5, 'b'), (4, 'd'), (1, 'c'), (3, 'a')])

    def test_remove(self):
        heap = MaxHeap()
        heap.insert((3, 'a'))
        heap.insert((5, 'b'))
        heap.insert((1, 'c'))
        heap.insert((4, 'd'))
        self.assertEqual(heap.remove(), (5, 'b'))
        self.assertEqual(heap.remove(), (4, 'd'))
        self.assertEqual(heap.remove(), (3, 'a'))
        self.assertEqual(heap.remove(), (1, 'c'))
        self.assertEqual(heap.remove(), None)

    def test_heapify_up(self):
        heap = MaxHeap()
        heap.insert((1, 'a'))
        heap.insert((2, 'b'))
        heap.insert((3, 'c'))
        self.assertEqual(heap.heap, [(3, 'c'), (1, 'a'), (2, 'b')])

    def test_heapify_down(self):
        heap = MaxHeap()
        heap.insert((10, 'a'))
        heap.insert((20, 'b'))
        heap.insert((5, 'c'))
        heap.insert((1, 'd'))
        heap.insert((25, 'e'))
        self.assertEqual(heap.remove(), (25, 'e'))
        self.assertEqual(heap.remove(), (20, 'b'))
        self.assertEqual(heap.remove(), (10, 'a'))
        self.assertEqual(heap.remove(), (5, 'c'))
        self.assertEqual(heap.remove(), (1, 'd'))

class TestPriorityNode(unittest.TestCase):

    def test_insert(self):
        priority_node = PriorityNode()
        priority_node.insert('task1', 1)
        priority_node.insert('task2', 3)
        priority_node.insert('task3', 2)
        self.assertEqual(priority_node.heap.heap, [(3, 'task2'), (1, 'task1'), (2, 'task3')])


if __name__ == '__main__':
    unittest.main()
