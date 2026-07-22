# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nerd = list()
        self.check(root, nerd)
        nerd.sort()
        return nerd[k - 1]

    def check(self, curr, result):
        if curr != None:
            result.append(curr.val)
            self.check(curr.left, result)
            self.check(curr.right, result)
        return
        