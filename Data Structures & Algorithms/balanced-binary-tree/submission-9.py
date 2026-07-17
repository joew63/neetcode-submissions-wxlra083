class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced, height = self.check(root)
        return balanced

    def check(self, root: Optional[TreeNode]):
        if root is None:
            return (True, 0)

        left_balanced, left_height = self.check(root.left)
        right_balanced, right_height = self.check(root.right)

        balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1
        height = 1 + max(left_height, right_height)

        return (balanced, height)