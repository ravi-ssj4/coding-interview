# method 1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.isBalancedHelper(root).isBalanced
    
    def isBalancedHelper(self, root):
        # base case's height and isBalanced
        if root is None:
            return TreeInfo(0, True)
        # get height and isBalanced of lst and rst
        leftTreeInfo = self.isBalancedHelper(root.left)
        rightTreeInfo = self.isBalancedHelper(root.right)
        # if lst is balanced and rst is balanced and abs diff
        # of height of lst and rst of current root node <= 1 
        # then current tree at root is also balanced
        isBalanced = leftTreeInfo.isBalanced and rightTreeInfo.isBalanced and abs(leftTreeInfo.height - rightTreeInfo.height) <= 1

        # current height = max height of lst and rst + 1
        height = 1 + max(leftTreeInfo.height, rightTreeInfo.height)
    
        return TreeInfo(height, isBalanced)

    
class TreeInfo:
    def __init__(self, height, isBalanced):
        self.height = height
        self.isBalanced = isBalanced


# method 2
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if root is None:
                return [True, 0]
            
            left, right = dfs(root.left), dfs(root.right)

            isBalanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1

            return [isBalanced, 1 + max(left[1], right[1])]
        
        return dfs(root)[0]