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
        if root is None:
            return []

        queue = [root]
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue[0]
                queue.pop(0)
                level.append(node.val)

                if node.children:
                    for child in node.children:
                        queue.append(child)

            res.append(level)
        
        return res
        
        
        