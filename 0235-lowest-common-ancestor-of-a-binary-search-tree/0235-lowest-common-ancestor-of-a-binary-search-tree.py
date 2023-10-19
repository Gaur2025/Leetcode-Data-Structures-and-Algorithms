# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root

        while curr:
            if (p.val > curr.val and q.val > curr.val):
                # It means LCA will surely exist in right subtree
                curr = curr.right
            elif (p.val < curr.val and q.val < curr.val):
                # It means LCA will surely exist in left subtree
                curr = curr.left
            else:
                # LCA will be at split coz p and q are at other ends of the root
                return curr
        