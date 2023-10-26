# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        This function is responsible for merging 2 given sorted linked list.
        1. We create a dummy node, which is going to be head of our new merged list.
        2. We will also maintain a tail node, which will be updated on each node attachment.
        3. We simply compare values of 2 nodes from different list and attach to the mode having smaller value to 
        the tail node.

        list1 ⇒ 1 → 2 → 3 → 4
        list2 ⇒ 1 → 2 → 3 → 4 → 5 → 6
        dummy.next ⇒ 1 → 1 → 2 → 2 → 3 → 3 → 4 → 4 → 5 → 6   

        """

        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                # move to next node in list1
                list1 = list1.next
            else:
                tail.next = list2
                # move to next node in list2
                list2 = list2.next

            # in both cases we need to update our tail node as well
            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2


        # At last we return the dummy.next node
        return dummy.next

        