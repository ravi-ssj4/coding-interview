# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, maxVal):
            # base case
            if node == None:
                return 0
            
            # processing
            count = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)

            # recursively calling children
            return count + dfs(node.left, maxVal) + dfs(node.right, maxVal)
        
        return dfs(root, root.val) # could have passed float("-inf") as well