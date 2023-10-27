"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        We need to create a deep copy of the given Random List.
        Approach: 
            1. We can create clones of each node by first passing through the given Random List.
            2. We can store each of the cloned nodes, into a hashmap. Initially we need not to do any mapping.
            3. In another pass we can get the pointers and make mapping in the new deep copy.
        """

        # creating the hashmap
        nodesMap = {None:None}    # initializing with None, as any node can also point to None

        # Making the first pass (cloning each node)
        curr = head
        while curr:
            copy = Node(curr.val)
            # storing the clones into our hashmap
            nodesMap[curr] = copy
            # move to next node
            curr = curr.next

        # Making another pass, mapping to be done now
        curr = head
        while curr:
            copy = nodesMap[curr]
            copy.next = nodesMap[curr.next]
            copy.random = nodesMap[curr.random]
            curr = curr.next


        return nodesMap[head]

        