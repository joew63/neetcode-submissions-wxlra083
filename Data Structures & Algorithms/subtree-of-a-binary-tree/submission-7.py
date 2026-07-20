# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        flag = False
        if root == None:
            return False
        if root.val == subRoot.val:
            checking = self.check(root, subRoot)
            if checking == True:
                flag = True
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)
        if left == True or right == True:
            flag = True
        return flag

    def check(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if (root == None and subRoot != None) or (root != None and subRoot == None):
            print("1")
            return False
        else:
            if root != None and subRoot != None:
                if root.val != subRoot.val:
                    print("2")
                    return False
                else:
                    left = self.check(root.left, subRoot.left)
                    right = self.check(root.right, subRoot.right)
                    if left != True or right != True:
                        print("3")
                        return False
        return True
        