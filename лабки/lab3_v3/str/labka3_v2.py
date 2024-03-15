class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def sum_of_depths(root, d):
    if root is None:
        return 0
    return (d + sum_of_depths(root.left, d + 1) +
            sum_of_depths(root.right, d + 1))

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.right.right = TreeNode(4)
root.left.right.left = TreeNode(6)
print(sum_of_depths(root, 0))