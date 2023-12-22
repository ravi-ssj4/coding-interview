class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode() # root node does not have any values

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children: # cur.children is a hashMap {'a': TrieNode(), 'b': TrieNode()...}
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True # marking the end of the word

    def search(self, word: str) -> bool:

        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]
                
                if c == '.':
                    for child in cur.children.values(): # values are the TrieNodes ie. the actual children of different keys('a' to 'z')
                        if dfs(i + 1, child):
                            return True
                    return False # if none of the branches returned true, then only return false
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.word

        return dfs(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)