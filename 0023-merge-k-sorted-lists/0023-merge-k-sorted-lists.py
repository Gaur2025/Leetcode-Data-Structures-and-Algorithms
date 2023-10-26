# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:     # Base Case
            return None

        while len(lists) > 1:                # until only 1 list is present in the given list
            mergedLists = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None    # VERY IMP EDGE CASE

                mergedLists.append(self.mergeList(l1, l2))

            lists = mergedLists

        # at last we return the first element of the lists
        return lists[0]
   
    
    def mergeList(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        This function is responsible for merging 2 sorted lists.
        We create a dummy so that dummy.next will be returned as the head of the merged list.
        """
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = ListNode(l1.val)
                l1 = l1.next
            else:
                tail.next = ListNode(l2.val)
                l2 = l2.next

            # in all cases we need to move our tail to next
            tail = tail.next

        if l1:
            tail.next = l1
        else:
            tail.next = l2

        # at this point both the sorted lists are merged into single sorted lists
        return dummy.next

        