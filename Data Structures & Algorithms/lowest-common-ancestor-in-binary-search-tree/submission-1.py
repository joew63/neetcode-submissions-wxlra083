# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root

        small = min(p.val, q.val)
        large = max(p.val, q.val)

       
        while True:
            if small <= curr.val <= large:
                return curr
            elif curr.val > large:
                curr = curr.left
            elif curr.val < small:
                curr = curr.right