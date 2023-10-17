# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if root is None:
            return res

        queue = [root]   # creating a queue with root in it 
        leftToRight = True
        while queue:
            size = len(queue)
            level = [0 for _ in range(size)]
            for i in range(size):
                node = queue[0]
                queue.pop(0)

                # check if left or right of node exists. If exists, append it to queue.
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                # index to insert value in level list  (THIS IS IMPORTANT)
                index = i if leftToRight else (size - 1 - i)
                level[index] = node.val
            
            # change the flag value
            leftToRight = not leftToRight
            res.append(level)
    
        return res

        