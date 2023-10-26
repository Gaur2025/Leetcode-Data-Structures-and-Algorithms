# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # creating a dummy node previous to head
        dummy = ListNode(0, head)
        left = dummy
        right = head

        # push the right node to its correct position i.e., at (left + n) + 1
        while n > 0 and right:
            right = right.next
            n -= 1

        # now we move 1 step ahead with both left and right. At the end left will arrive at node previous to the node that is to be removed
        while right:
            left = left.next
            right = right.next

        # now delete the required node
        left.next = left.next.next

        # at last we need to return, we can return dummy.next
        return dummy.next
        

# TC = O(n)