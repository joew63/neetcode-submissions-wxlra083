# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        def valid(root, subRoot):
            if not root and not subRoot:
                return True
            if root and subRoot and root.val == subRoot.val:
                return valid(root.left, subRoot.left) and valid(root.right, subRoot.right)
            return False

        if root.val == subRoot.val:
            result = valid(root, subRoot)
            if result:
                return result
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


        