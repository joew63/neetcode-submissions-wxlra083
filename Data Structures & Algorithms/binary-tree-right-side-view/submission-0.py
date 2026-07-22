# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        level = 0
        result = list()
        self.check(root, level, result)
        return result

    def check(self, curr, num, res):
        if curr != None:
            if len(res) == num:
                res.append(curr.val)
            self.check(curr.right, num + 1, res)
            self.check(curr.left, num + 1, res)
            
        