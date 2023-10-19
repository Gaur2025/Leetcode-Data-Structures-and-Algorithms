# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
            This function is responsible for:
        1.	To check whether left and right nodes of the root exist.
        2.	Then dfs at each node, and swap its left and right nodes
        """
        def swapNodes(node):
            if not node:
                return 
            
            # Swap the left and right child
            node.left, node.right = node.right, node.left

            if node.left:
                swapNodes(node.left)
            if node.right:
                swapNodes(node.right)

            return node

        return swapNodes(root)

        return root

        
