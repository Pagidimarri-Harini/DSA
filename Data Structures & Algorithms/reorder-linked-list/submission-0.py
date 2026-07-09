# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseLL(self, node):
        if not node or not node.next:
            return node
        newnode = self.reverseLL(node.next)
        node.next.next = node
        node.next = None
        return newnode
        
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        rhead = self.reverseLL(slow.next)
        slow.next = None
        lhead = head
        while lhead and rhead:
            tmp1, tmp2 = lhead.next, rhead.next
            lhead.next = rhead
            rhead.next = tmp1
            lhead, rhead = tmp1, tmp2


    
        

            


        