class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []
        partition = []

        def dfs(i):
            # base case
            if i == len(s):
                res.append(partition[::])
            
            # checking for each possible first partition if its a palindrome
            # if it is, then recursively check for future palindromic partitions
            # reset the partition list to check for next first possible palindromic partition 
            for j in range(i, len(s)):
                if self.isPalin(s, i, j):
                    partition.append(s[i:j+1])
                    dfs(j + 1)
                    partition.pop()
                
        dfs(0)
        return res
    
    def isPalin(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

