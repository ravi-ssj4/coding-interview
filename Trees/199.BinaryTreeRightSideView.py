# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    method: level-order traversal(BFS) and keep on adding the rightmost at each level to the result
    time: O(n)
    space: O(n)
    '''
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = collections.deque()
        q.append(root)
        res = []

        while q:
            rightSide = None
            qLen = len(q)
            for _ in range(qLen):
                node = q.popleft()
                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)
            if rightSide:
                res.append(rightSide.val)

        return res