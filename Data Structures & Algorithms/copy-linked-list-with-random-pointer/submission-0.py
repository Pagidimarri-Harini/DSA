"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        node = head
        while node:
            temp = node.next
            node.next = Node(node.val)
            node.next.next = temp
            node = temp
        newnode = head
        while newnode:
            newnode.next.random = newnode.random.next if newnode.random else None
            newnode = newnode.next.next
        curr = head
        prev = Node(0)
        dummy = prev
        while curr:
            prev.next = curr.next
            curr.next = curr.next.next
            curr = curr.next
            prev = prev.next

        return dummy.next

            

        