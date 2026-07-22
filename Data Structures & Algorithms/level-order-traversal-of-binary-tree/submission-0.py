# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = list()
        num = 0
        self.check(root, num, res)
        return res
    
    def check(self, curr, count, result):
        if curr != None:
            if len(result) == count:
                result.append(list())
            result[count].append(curr.val)
            self.check(curr.left, count + 1, result)
            self.check(curr.right, count + 1, result)
        
