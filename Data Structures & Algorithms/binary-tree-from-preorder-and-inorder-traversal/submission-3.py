class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
            
        result = TreeNode(preorder[0])

        mid = inorder.index(preorder[0])
        result.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        result.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return result