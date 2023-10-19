# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # we know inorder traversal of a BST gives us a sorted list.
        # So we can just, do iorder traversal and get the k the element from res
        res = self.inorder(root)
        return res[k-1]


    def inorder(self, node: Optional[TreeNode]) -> List[int]:
        # Inorder => left -> root -> right
        if node:
            return self.inorder(node.left) + [node.val] + self.inorder(node.right)
        else:
            return []
        