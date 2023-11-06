# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        res = []
        q = collections.deque()

        # adding root to the queue
        q.append(root)

        while q:
            lenQ = len(q)
            level = []

            # for each node in q
            for i in range(lenQ):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    # adding children of node to q
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)

            if level:
                res.append(level)

        return res
        