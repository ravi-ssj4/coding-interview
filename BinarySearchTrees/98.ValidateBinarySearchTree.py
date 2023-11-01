# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, leftLimit, rightLimit):
            # base case
            if node == None:
                return True
            
            # current node processing
            isCurrentValid = leftLimit < node.val and node.val < rightLimit

            # calling left and right subtrees
            return isCurrentValid and dfs(node.left, leftLimit, node.val) and dfs(node.right, node.val, rightLimit)
        
        return dfs(root, float("-inf"), float("inf"))
    
