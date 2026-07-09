# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = fast = head
        count = 0
        while fast and count < n:
            count += 1
            fast = fast.next
        if not fast:
            head = slow.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        # print(slow.val)
        if slow and slow.next:
            slow.next = slow.next.next
        return head
        