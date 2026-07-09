# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        maxnode = float('-inf')
        def inorder(node):
            nonlocal maxnode
            if not node:
                return True
            
            left = inorder(node.left)
            if not left:
                return False
            if node.val <= maxnode:
                return False
            maxnode = node.val
               
            return inorder(node.right)
        return inorder(root)


        