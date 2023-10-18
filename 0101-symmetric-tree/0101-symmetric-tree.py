# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def dfs(leftRoot, rightRoot):
            # if both are None
            if not leftRoot and not rightRoot:
                return True

            # if one of them is None
            if not leftRoot or not rightRoot:
                return False

            # if nodes dont have the same value
            if (leftRoot.val != rightRoot.val):
                return False

            # Now for mirror images
            return dfs(leftRoot.left, rightRoot.right) and dfs(leftRoot.right, rightRoot.left)

        return dfs(root.left, root.right)
            

            

        
        