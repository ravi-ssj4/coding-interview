# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []

        def dfs(node):
            if node == None:
                res.append("N")
                return
            
            res.append(str(node.val))

            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return ",".join(res) # "1, 2, N, ..."
            

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        values = data.split(",") # ["1", "2", "N", ...]
        self.i = 0
    
        def dfs():
            if values[self.i] == "N":
                self.i += 1
                return None
            
            tree = TreeNode(values[self.i])
            self.i += 1
        
            tree.left = dfs()
            tree.right = dfs()
            return tree
            
        return dfs()
     

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))