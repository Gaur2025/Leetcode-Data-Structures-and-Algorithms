# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # finding the middle of given LL
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next         # 1 step at a time
            fast = fast.next.next    # 2 steps at a time

        
        # Now slow.next is pointing to the start of the second LL
        # reversing the second LL
        second = slow.next
        prev = slow.next = None     # as this is going to be end of second LL
        while second:
            # reversing the LL
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # at this point prev will be pointing to head of second LL

        # merging 2 halves by breaking into components
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second     # connecting head of first with the head of second
            second.next = temp1
            first, second = temp1, temp2

        # at this point we will be havinf our reordered list

        