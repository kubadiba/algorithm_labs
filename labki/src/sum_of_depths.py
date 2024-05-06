class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def sum_of_depths(root, d):
    if root is None:
        return 0
    return d + sum_of_depths(root.left, d + 1) + sum_of_depths(root.right, d + 1)
