"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ans = []
        def inorder(root):
            if not root:
                return
            for i in root.children:
                inorder(i)
            ans.append(root.val)
        inorder(root)
        return ans
        