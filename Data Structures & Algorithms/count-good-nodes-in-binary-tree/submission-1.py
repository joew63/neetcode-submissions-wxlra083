# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.check(root, root.val)

    def check(self, curr, biggest):
        if curr != None:
            if curr.val >= biggest:
                return 1 + int(self.check(curr.left, curr.val) + self.check(curr.right, curr.val))
            else:
                return int(self.check(curr.left, biggest) + self.check(curr.right, biggest))
        return 0

        