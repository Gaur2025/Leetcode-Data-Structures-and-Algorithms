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
        q = collections.deque()

        q.append(root)

        while q:
            lenQ = len(q)
            level = []
            
            for i in range(lenQ):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    # adding all children to the level
                    for child in node.children:
                        q.append(child)
                    
            if level:
                res.append(level)
                    
        return res
         


        