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

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        newnode = None
        # l1 = self.reverseLL(l1)
        # l2 = self.reverseLL(l2)
        while l1 and l2:
            addition = str(l1.val + l2.val+ carry) 
            # print(addition)
            add = int(addition[-1])
            # print(add)
            if addition[:-1] != "":
                carry = int(addition[:-1])
            else:
                carry = 0
            tempnode = ListNode(add)
            tempnode.next = newnode
            newnode = tempnode
            l1 = l1.next
            l2 = l2.next

        while l1:
            addition = str(l1.val + carry)
            add = int(addition[-1])
            if addition[:-1] != "":
                carry = int(addition[:-1])
            else:
                carry = 0
            tempnode = ListNode(add)
            tempnode.next = newnode
            newnode = tempnode
            l1 = l1.next
        while l2:
            addition = str(l2.val + carry)
            add = int(addition[-1])
            if addition[:-1] != "":
                carry = int(addition[:-1])
            else:
                carry = 0
            tempnode = ListNode(add)
            tempnode.next = newnode
            newnode = tempnode
            l2 = l2.next
        print(newnode.val)
        newnode = self.reverseLL(newnode) 
        l3 = newnode
        print(carry)

        if carry != 0:
            while newnode.next:
                print(newnode.val)
                newnode = newnode.next
            newnode.next = ListNode(carry)
        return l3
        

        