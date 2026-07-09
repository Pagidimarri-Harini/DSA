# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            n = len(stack)
            for i in range(n):
                top = stack.pop(0)
                if top.left:
                    stack.append(top.left)
                if top.right:
                    stack.append(top.right)
            res.append(top.val)
        return res




        