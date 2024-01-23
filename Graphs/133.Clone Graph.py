"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    '''
    method 1: recursive dfs + hashMap(mapping of old to cloned new nodes)
    algo:
        1. initialize hashmap(mapping of old to cloned nodes)
        2. call dfs on the given node
        3. dfs:
            3.1. if given node is in the hashMap, return its clone
            3.2. otherwise clone it and then add <node, copy> to the hashMap
            3.3. also, connect all the necessary cloned nodes(ie. clones of
                all the neighbors of the current node) to this currently copied nodes
                THIS IS DONE RECURSIVELY BY CALLING DFS ON EACH NEIGHBOR OF CURRENT NODE: "node"
        
    time: O(V + E) need to go through every node and its neighbors 
    space: O(V) max depth of recursion stack
    '''
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            
            copy = Node(node.val)
            oldToNew[node] = copy
            for neighbor in node.neighbors:
                copyOfNeighbor = dfs(neighbor)
                copy.neighbors.append(copyOfNeighbor)
            return copy

        return dfs(node) if node else None