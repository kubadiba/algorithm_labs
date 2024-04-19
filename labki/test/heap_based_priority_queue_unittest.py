import unittest
from src.heap_based_priority_queue import MaxHeap, PriorityNode

class TestMaxHeap(unittest.TestCase):
    def test_insert_and_remove(self):
        heap = MaxHeap()
        heap.insert(5)
        heap.insert(3)
        heap.insert(8)
        self.assertEqual(heap.remove(), 8)
        self.assertEqual(heap.remove(), 5)
        self.assertEqual(heap.remove(), 3)
        self.assertIsNone(heap.remove())

class TestPriorityNode(unittest.TestCase):
    def test_insert_and_remove(self):
        priority_node = PriorityNode()
        priority_node.insert('task1', 5)
        priority_node.insert('task2', 3)
        priority_node.insert('task3', 8)
        self.assertEqual(priority_node.remove(), 'task3')
        self.assertEqual(priority_node.remove(), 'task1')
        self.assertEqual(priority_node.remove(), 'task2')
        self.assertIsNone(priority_node.remove())

if __name__ == '__main__':
    unittest.main()
