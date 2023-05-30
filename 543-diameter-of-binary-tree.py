class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.max_diameter = 0

        def dfs(node):
            if not node:
                return 0

            # Recursively compute the height of the left and right subtrees
            left_height = dfs(node.left)
            right_height = dfs(node.right)

            # Update the maximum diameter seen so far
            self.max_diameter = max(
                self.max_diameter, left_height + right_height
            )

            # Return the height of the current node's subtree
            return max(left_height, right_height) + 1

        dfs(root)

        return self.max_diameter
