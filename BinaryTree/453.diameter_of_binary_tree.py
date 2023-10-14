# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    method 1: doing postorder dfs because we want values from bottom to top(only 1 value ie. height in this case)
    problem scoping:
        * we don't need to pass diameter through each node as well because we are dynamically calculating that
          and updating the maxDiam list[0]
        
    time: O(n)
    space: O(n)

    '''
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # In Python, function arguments are passed by object reference. 
        # For immutable objects (like integers, strings, and tuples), 
        # any changes you make to the passed object inside the function 
        # do not affect the original object. However, for mutable objects 
        # (like lists, dictionaries, and sets), any changes made inside 
        # the function are reflected outside, because both the function 
        # parameter and the original variable refer to the same object in memory.
        maxDiam = [0]

        def postOrder(root):
            if root is None:
                return -1
            
            leftHeight = postOrder(root.left)
            rightHeight = postOrder(root.right)

            diameter = leftHeight + rightHeight + 2
            maxDiam[0] = max(maxDiam[0], diameter)

            height = max(leftHeight, rightHeight) + 1
            return height
        
        postOrder(root)
    
        return maxDiam[0]

#     '''
#     method 2: TreeInfo object: has 2 values(height, diameter) that it returns bottom up
#     '''

#     def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
#         return self.diameterBTHelper(root).diameter
    
#     def diameterBTHelper(self, root):
#         if root == None:
#             return TreeInfo(0, 0)
        
#         leftTreeInfo = self.diameterBTHelper(root.left)
#         rightTreeInfo = self.diameterBTHelper(root.right)

    
#         maxDiamInSubtrees = max(leftTreeInfo.diameter, rightTreeInfo.diameter)

#         diamThroughRoot = leftTreeInfo.height + rightTreeInfo.height

#         currentHeight = 1 + max(leftTreeInfo.height, rightTreeInfo.height)
#         currentDiameter = max(maxDiamInSubtrees, diamThroughRoot)

#         return TreeInfo(currentHeight, currentDiameter)
        
# class TreeInfo:
#     def __init__(self, height, diameter):
#         self.height = height
#         self.diameter = diameter

