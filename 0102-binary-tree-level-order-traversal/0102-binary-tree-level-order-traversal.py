# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Approach 1: BFS (FIFO)
    # a. Create a queue to store level. Create a res list to store the final result.
    # b. Insert root into this queue.
    # c. Now we need to keep inserting children of each node and maintain specific lists for each level.
    # d. Append each level list to the result list.
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = []
        q = collections.deque()   # as we need to perform FIFO operations
        # add root to the queue.
        q.append(root)

        while q:
            lenQ = len(q)
            level = []

            for i in range(lenQ):
                # pop left elements from the queue and add their respective levels.
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)

            if level:
                res.append(level)

        return res


    # TC = O(n), n = number of nodes in the given BT
    # SC = O(n) (Recursive Stack)

        