"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:

        res = []

        # creating a queue
        q = collections.deque()

        # adding root into the queue
        q.append(root)

        while q:
            lenQ = len(q)
            level = []

            # iterating over q to get all the level nodes
            for i in range(lenQ):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    # adding node's children to the q
                    for child in node.children:
                        q.append(child)

            if level:
                res.append(level)

        return res
        