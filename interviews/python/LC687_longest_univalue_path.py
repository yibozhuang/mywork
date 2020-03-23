class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    longest = 0

    def traverse(self, node, parent_val):
        if not node:
            return 0

        left = self.traverse(node.left, node.val)
        right = self.traverse(node.right, node.val)

        self.longest = max(self.longest, left + right)

        path = 0
        if node.val == parent_val:
            path = 1 + max(left, right)

        return path

    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.traverse(root, None)
        return self.longest

