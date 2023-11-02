# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    method: construct the tree in preorder style, first the root and then the lst and rst recursively
    logic:
        * once we fix the root of the tree to preorder[0] and find its index in the inorder = mid
        * this index mid = number of elements to the left of the root in the inorder array
        * ie. these number of elements need to be present in the left subtree and hence we need to
        * count these many elements in the preorder array as well and slice them and call the function
        * recursively to build the left subtree
            -> (1: mid + 1)
        * hence the remaining elements will be part of right subtree
            -> (mid + 1:)
    '''
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return
        
        root = TreeNode(preorder[0])

        mid = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        
        return root