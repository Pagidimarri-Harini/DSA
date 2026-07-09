# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        fast = head
        totlength = 1
        while fast.next:
            fast = fast.next
            totlength += 1
        fast.next = head
        count = 0
        while count < totlength - (k % totlength)-1:
            head = head.next
            count += 1
        slow = head.next
        head.next = None
        return slow
        

        