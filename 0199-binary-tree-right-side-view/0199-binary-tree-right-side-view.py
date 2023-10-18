# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.recursion(0, root, res)
        return res

    def recursion(self, level: int, root: Optional[TreeNode], res: List[int]):
        if root is None:
            return

        if (len(res) == level):
            res.append(root.val)
        
        self.recursion(level + 1, root.right, res)
        self.recursion(level + 1, root.left, res)
        