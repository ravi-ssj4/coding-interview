# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    #     stack = []
    #     if root:
    #         stack = [(1, root)]
        
    #     maxDepth = 0

    #     while stack:
    #         currentDepth, currentNode = stack.pop()
    #         if currentNode == None:
    #             continue
    #         maxDepth = max(maxDepth, currentDepth)
    #         stack.append((currentDepth + 1, currentNode.left))
    #         stack.append((currentDepth + 1, currentNode.right))
        
    #     return maxDepth