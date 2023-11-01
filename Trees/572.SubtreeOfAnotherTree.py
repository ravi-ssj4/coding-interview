# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        s, t = root, subRoot
        if t == None: return True
        if s == None: return False # (we know that t is not none if we are here so no need to check explicitly)

        if self.isSameTree(s, t):
            return True
        
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
    
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
            
        # p.val == q.val for sure

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)