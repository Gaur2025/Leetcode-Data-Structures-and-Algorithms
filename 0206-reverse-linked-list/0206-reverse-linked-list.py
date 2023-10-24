# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     """
    #     Iterative solution : 2 - pointer approach
    #         a. start with a prev node pointing at None, and a curr node pointing at head.
    #         b. iterate through the whole LL. At each iteration swap the adjacent nodes.
    #         c. at last prev node will be pointing to the resulting head
    #     TC = O(n), SC = O(1)
    #     """
    #     curr, prev = head, None

    #     while curr:
    #         temp = curr.next    # as this will be assigned to curr node
    #         curr.next = prev
    #         prev = curr
    #         curr = temp

    #     # at last we will be having prev pointed to new LL (reverse LL of original)
    #     return prev

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Recursive solution: 
            a. call recursive calls on part of the given input
            b. attach this reversed sub list with the remaining part of given LL
        """
        if (head is None or head.next is None):    # base case 
            return head

        # calling the recursive function
        smallAns = self.reverseList(head.next)


        # attach head to the last node of smallAns
        temp = smallAns

        # traverse on temp to reach its last node
        while temp.next:
            temp = temp.next

        # now we are at last node of smallAns. so we need to attach head to it
        temp.next = head
        head.next = None

        return smallAns

