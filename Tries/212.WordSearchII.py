class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

    def addWord(self, word):
        cur = self

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        # get the words list into the trie data structure
        root = TrieNode()
        for word in words:
            root.addWord(word)

        ROWS, COLS = len(board), len(board[0])

        res, visited = set(), set()

        def dfs(r, c, word, node):
            # the below fails because we are returning as soon as we find
            # a valid word till this path in the trie, but we don't continue further
            # if we did however, we could have found more words, hence we need to continue
            # the trie path until possible
            # eg: app and apple both will be on the same path
            # if we stop after finding app, we won't be able to find apple!
            # if node.endOfWord == True:
            #     res.add(word)
            #     return
            
            
            # 1. all invalid cases: return
            if (r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                (r, c) in visited or
                board[r][c] not in node.children):
                return
            
            # 2. visit the board[r][c] and update the state of word and node
            visited.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.endOfWord:
                res.add(word)
            
            # 3. call recursive function on neighbors
            dfs(r + 1, c, word, node)
            dfs(r - 1, c, word, node)
            dfs(r, c + 1, word, node)
            dfs(r, c - 1, word, node)

            # 4. backtrack: unvisit the (r, c) position
            # Note: no need to reset word and node as they are local vars to the rec function
            visited.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, "", root)
        
        return list(res)


'''
Time Complexity:
O(w.m.n.4^(m.n))
'''

'''
Time Complexity:
1. Building the Trie: 
    The time complexity of building the Trie is  ( )O(M), where  Mis the total number of characters in all words.
2. Searching with DFS: 
    For each cell in the board, we perform a DFS search. If we denote  Nas the total number of cells in the board (i.e., ROWS * COLS), then in the worst case, we might have to explore 4 4Lpaths (4 possible directions at each step) where  Lis the maximum length of a word. However, the search is greatly reduced by the Trie, as we only explore paths that are prefixes of words in the Trie.
The worst-case time complexity for the DFS part can be estimated as  ( ⋅4 )O(N⋅4L). However, it's important to note that the Trie reduces the actual number of paths explored, so the effective complexity will often be much less.

Space Complexity:
1. Trie Storage: 
    The space used by the Trie is  ( )O(M), where  Mis the total number of characters in all words.
2. DFS Stack Space: 
    In the worst case, the maximum depth of the recursive call stack would be  ( )O(L)where  Lis the maximum length of a word.
3. Visited Set: 
    The visited set could potentially hold all cells in the worst case, adding  ( )O(N)to the space complexity.
4. Result Set: 
    The space for the res set is  ( )O(W), where  Wis the number of unique words found. In the worst case, this could be all the words we're looking for.

Combining these, the total space complexity is  ( + + + )O(M+L+N+W). In most cases,  M,  L, and  Ware much smaller than  N, so we might approximate this as  ( )O(N)for simplicity, but this is a loose upper bound.

In summary, the time complexity is  ( ⋅4 )O(N⋅4L), and the space complexity is  ( + + + )O(M+L+N+W), where  Nis the number of cells on the board,  Mis the total number of characters in all words,  Lis the maximum length of a word, and  Wis the number of unique words found.
'''

