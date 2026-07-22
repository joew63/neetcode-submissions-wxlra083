# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.check(root, -1001, 1001)
    
    def check(self, curr, min_val, max_val):
        if curr != None:
            if not min_val < curr.val < max_val:
                return False
            return self.check(curr.left, min_val, curr.val) and self.check(curr.right, curr.val, max_val)
        return True

        