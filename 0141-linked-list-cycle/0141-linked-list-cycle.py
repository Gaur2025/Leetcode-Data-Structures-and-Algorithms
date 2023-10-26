# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        """
        This function is responsible for detecting a cycle in a given Linked List
        Approach: Slow and Fast pointer.
            We define slow and a fast pointer at pointing at the head of the LL. we move slow by 1 step
            and fast by 2 steps. It is sure that if a cycle exist in a Linked List, slow and fast pointer
            will meet for sure at a specific node. 
            And this will happen in O(n) TC. 
        """
        if not head:
            return False


        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # if at any point of iteration
            if slow == fast:
                return True


        # if the pointers do not meet then cycle does not exist in the given Linked List.
        return False

        