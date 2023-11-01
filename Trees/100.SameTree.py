# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        # here we are sure that p.val and q.val are equal and hence
        # now just need to make sure that subtrees are equal
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))