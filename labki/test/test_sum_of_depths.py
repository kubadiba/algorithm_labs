import unittest
from src.sum_of_depths import sum_of_depths, TreeNode


class TestSumOfDepths(unittest.TestCase):

    def test_single_node(self):
        root = TreeNode(1)
        self.assertEqual(sum_of_depths(root, 0), 0)

    def test_two_levels(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        self.assertEqual(sum_of_depths(root, 0), 2)

    def test_three_levels(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        self.assertEqual(sum_of_depths(root, 0), 8)

    def test_unbalanced_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.left.left = TreeNode(4)
        self.assertEqual(sum_of_depths(root, 0), 6)

    def test_null_root(self):
        self.assertEqual(sum_of_depths(None, 0), 0)

if __name__ == '__main__':
    unittest.main()
