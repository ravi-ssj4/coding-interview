class Solution:
    '''
    method 1: Memoization
    '''
    # def numDecodings(self, s: str) -> int:
    #     dp = {len(s): 1} # if s = "", ans = 1

    #     def dfs(i):
    #         # memoization base case
    #         if i in dp:
    #             return dp[i]


    #         if s[i] == "0":
    #             return 0
    #         res = dfs(i + 1) # 1st digit only considered (we are sure that its not 0)

    #         if (i + 1) < len(s) and 
    #             (s[i] == "1" or 
    #             (s[i] == "2" and (s[i + 1] in "0123456"))):
    #             res += dfs(i + 2) # 1st 2 digits considered (we are sure that they are either 10-19 or 20-26)
            
    #         dp[i] = res
    #         return res
        
    #     return dfs(0)

    '''
    method 2: bottom-up dp
    '''
    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1}

        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]
            if (    
                (i + 1) < len(s) and 
                ((s[i] == "1") or 
                (s[i] == "2" and s[i + 1] in "0123456"))
                ):
                dp[i] += dp[i + 2]
        return dp[0]

            