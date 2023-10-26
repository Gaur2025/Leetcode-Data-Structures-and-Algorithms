# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        # we need to create a ListNode to store the new LL
        dummy = ListNode()
        curr = dummy

        carry = 0
        # we need to add till l1 or l2 or if carry remains (CARRY is VERY IMPORTANT)
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # new digit by adding
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10

            # add the new node with this val 
            curr.next = ListNode(val)

            # update the pointers
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        # at last return dummy.next
        return dummy.next

        