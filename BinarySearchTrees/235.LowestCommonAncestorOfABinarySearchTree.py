# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    '''
    method : Binary search way recursion based on condtiions:
            * if both nodes have values greater than current root, go right
            * elif both nodes have values less than the current root, go left
            * else
                * both nodes are in different subtrees, basically a split has occured
                * or one of the nodes has become equal to the current root

    time: O(logn)
    space: O(1)
    '''
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root
        while cur:
            if p.val < cur.val and q.val < cur.val:
                cur = cur.left
            elif p.val > cur.val and q.val > cur.val:
                cur = cur.right
            else:
                return cur