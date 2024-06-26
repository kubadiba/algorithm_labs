import unittest
from src.sum_of_depths import sum_of_depths, TreeNode


class TestSum(unittest.TestCase):
    def test_sum(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        result = sum_of_depths(root)
        self.assertEqual(result, 5)

    def test_sum_two(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.left.right.right = TreeNode(4)
        root.left.right.left = TreeNode(6)
        result = sum_of_depths(root)
        self.assertEqual(result, 9)
