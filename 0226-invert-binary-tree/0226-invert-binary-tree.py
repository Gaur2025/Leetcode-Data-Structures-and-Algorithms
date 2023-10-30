# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Optional[TreeNode] is a type that can either be a TreeNode or None.
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        This function is responsible for inverting a given BT
        Inversion means ⇒ node.left, node.right = node.right, node.left (this needs to be implemented)
        """
        if not root:
            return None

        # swap nodes function
        def swapNodes(node):
            if not node:
                return None
        
            node.left, node.right = node.right, node.left

            # if one of the left or right node is present
            if node.left:
                swapNodes(node.left)
            if node.right:
                swapNodes(node.right)

            return node

        swapNodes(root)

        return root

    # TC = O(height of the given BT)  (Worst Case)
    # SC = O(1)  

        