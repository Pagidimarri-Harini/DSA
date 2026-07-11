"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        visited = {}
        def clone(node):
            if node in visited:
                return visited[node]
            copy = Node(node.val)
            visited[node] = copy
            for i in node.neighbors:
                copy.neighbors.append(clone(i)) 
            return copy
        return clone(node)
        

        
        
        