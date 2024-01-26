from typing import Optional, List

import collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bottomView(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        q = collections.deque()
        q.append([root, 0])
        distanceMap = collections.defaultdict(int)
        res = []
        while q:
            node, dist = q.popleft()

            distanceMap[dist] = node.val # will retain the values of hd seen last
            
            if node.left:
                q.append([node.left, dist - 1])
            if node.right:
                q.append([node.right, dist + 1])
        
        min_hd = min(distanceMap.keys())
        max_hd = max(distanceMap.keys())

        res = [distanceMap[hd] for hd in range(min_hd, max_hd + 1)]
        
        return res
    
# Driver code
# Set up the binary tree
# The tree looks like this:
#          1
#        /   \
#       2     3
#      / \   / \
#     4   5 6   7
# Tree Diagram:
#     1
#    / \
#   2   3
#  /|   |\
# 4 5   6 7
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# Create a Solution object
solution = Solution()

# Get the top view
top_view = solution.bottomView(root)

# Print the top view
print("Top view of the binary tree is:", top_view)
            