# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        stack = []
        cur = root

        while cur or stack:
            # go left
            while cur:
                stack.append(cur)
                cur = cur.left
            
            # process
            cur = stack.pop()
            n += 1
            if n == k:
                return cur.val
            
            # go right
            cur = cur.right

# Follow up question:
# Design an efficient data structure to insert/delete and search in the BST

'''
BST + doubly LinkedList
* kth smallest: 
    -> doubly linked list contains the inorder traversal of the BST 
    -> For searching of kth smallest, just traverse the doubly linked list from left to right
    -> O(k) to search for kth smallest
* insert/delete:
    -> BST insert/delete + linkedlist insert/delete
    -> O(H)/O(H) + O(1) = O(H); H: (logn) in case of Balanced BST otherwise (n)
'''

#     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
#         treeInfo = TreeInfo(0, 1)
#         self.dfs(root, k, treeInfo)
#         return treeInfo.lastVisited


#     def dfs(self, node, k, treeInfo):
#         if node == None or treeInfo.numVisited >= k:
#             return
        
#         # go left
#         self.dfs(node.left, k, treeInfo)

#         # process
#         if treeInfo.numVisited < k:
#             treeInfo.numVisited += 1
#             treeInfo.lastVisited = node.val

#             # go right
#             self.dfs(node.right, k, treeInfo)

# class TreeInfo:
#     def __init__(self, numVisited, lastVisited):
#         self.numVisited = numVisited
#         self.lastVisited = lastVisited