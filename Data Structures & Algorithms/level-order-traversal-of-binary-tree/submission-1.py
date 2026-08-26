# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # if root == None:
        #     return []
        
        def recur(root, level, result):
            if root != None:
                if len(result) == level:
                    result.append([])
                result[level].append(root.val)
                recur(root.left, level + 1, result)
                recur(root.right, level + 1, result)

        result = []
        recur(root, 0, result)
        return result