# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        This function returns whether subRoot is a subTree of given root.
        """
        if not root: 
            return False
        if not subRoot:
            return True

        # then we check if sameTree
        if self.isSameTree(root, subRoot):
            return True

        # check for root's children (if any of the children is subTree then we return True)
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))


    # creating the isSameTree() function
    def isSameTree(self, s, t) -> bool:
        """
        This function returns whether s and t are same trees or not
        """
        if not s and not t:
            return True

        if s and t and s.val == t.val:
            return (self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right))

        # in all other cases
        return False


        