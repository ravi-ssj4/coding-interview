class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            # odd length
            res += self.countPalin(s, i, i)
            # even length
            res += self.countPalin(s, i, i + 1)
        return res
    
    def countPalin(self, s, l, r):
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
        return res