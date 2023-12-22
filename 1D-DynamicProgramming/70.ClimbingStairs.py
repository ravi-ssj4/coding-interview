class Solution:
    # method 1 : memoization
    # def climbStairs(self, n: int) -> int:
    #     return self.csHelper(n, {0: 1, 1: 1})

    # def csHelper(self, n, memoize):
    #     if n in memoize:
    #         return memoize[n]
    #     memoize[n] = self.csHelper(n-1, memoize) + self.csHelper(n-2, memoize)
    #     return memoize[n]

    # method 2 : its actually fibonacci nummbers !! 
    def climbStairs(self, n):
        one = 1
        two = 1
        for i in range(n - 1):
            three = one + two
            two = one
            one = three
        return one