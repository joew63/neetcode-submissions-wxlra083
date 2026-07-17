# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        return self.maxD(0, root)

    def maxD(self, count: int, root: Optional[TreeNode]) -> int:
        curr = root
        if curr == None:
            return count
        count += 1

        left = self.maxD(count, curr.left)
        right = self.maxD(count, curr.right)

        return max(left, right)