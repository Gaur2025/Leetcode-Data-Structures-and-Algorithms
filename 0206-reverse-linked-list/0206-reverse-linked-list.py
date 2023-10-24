# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Iterative solution : 2 - pointer approach
            a. start with a prev node pointing at None, and a curr node pointing at head.
            b. iterate through the whole LL. At each iteration swap the adjacent nodes.
            c. at last prev node will be pointing to the resulting head
        """
        curr, prev = head, None

        while curr:
            temp = curr.next    # as this will be assigned to curr node
            curr.next = prev
            prev = curr
            curr = temp

        # at last we will be having prev pointed to new LL (reverse LL of original)
        return prev
