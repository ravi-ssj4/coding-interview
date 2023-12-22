class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                # if the string is long enough, compare
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)] # since current string already matched, check for the subproblem dp[i + len(w)]
                if dp[i] == True: # no need to continue further checking with remaining words in the dict
                    break
        return dp[0]
            