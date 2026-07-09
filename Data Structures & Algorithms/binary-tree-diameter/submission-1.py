# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxdep = 0
        def maxdepth(root):
            nonlocal maxdep
            if not root:
                return 0
            left = maxdepth(root.left)
            right =  maxdepth(root.right)
            maxdep = max(maxdep, left + right)
            return 1 + max(left, right)
        maxdepth(root)
        return maxdep
        

        