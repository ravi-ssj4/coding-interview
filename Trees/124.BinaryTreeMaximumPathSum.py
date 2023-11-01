# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [float("-inf")]

        def dfs(node):
            if node == None:
                return 0

            maxLeftPath = dfs(node.left)
            maxRightPath = dfs(node.right)

            maxWithSplit = max(node.val + maxLeftPath + maxRightPath, node.val)
            maxWithoutSplit = max(maxLeftPath, maxRightPath, 0) + node.val

            res[0] = max(res[0], maxWithSplit, maxWithoutSplit)

            return maxWithoutSplit
        
        dfs(root)

        return res[0]




#     def maxPathSum(self, root: Optional[TreeNode]) -> int:
#         return self.maxPathSumHelper(root).maxSum

#     def maxPathSumHelper(tree):
#         if tree is None:
#             return TreeInfo(0, float("-inf"))

#         lti = self.maxPathSumHelper(tree.left)
#         rti = self.maxPathSumHelper(tree.right)

#         maxBranchSumViaSubtrees = max(lti.maxBranchSum, rti.maxBranchSum) 
        
#         # the above could be a negative number, hence adding this to the root value will give a lower value
#         # hence its better to not even include these values in the currentMaxSumViaBranch
#         currentMaxBranchSum = max(maxBranchSumViaSubtrees + tree.value, tree.value) 

#         maxSumThroughCurrentNode = max(tree.value + lti.maxBranchSum + rti.maxBranchSum, currentMaxBranchSum)
#         maxSumInSubrees = max(lti.maxSum, rti.maxSum)
#         currentMaxSum = max(maxSumThroughCurrentNode, maxSumInSubrees)

#         return TreeInfo(currentMaxBranchSum, currentMaxSum)


# class TreeInfo:
#     def __init__(self, maxBranchSum, maxSum):
#         self.maxBranchSum = maxBranchSum
#         self.maxSum = maxSum
