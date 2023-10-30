# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # max depth function
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        This function is responsible for evaluating the length of a given BT
        Length ⇒ max(maxDepth(left child), maxDepth(right child)) + 1 root node
        """
        if not root:
            return 0

        depth = max(self.maxDepth(root.left), self.maxDepth(root.right))

        return (depth + 1)

        