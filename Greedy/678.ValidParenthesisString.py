class Solution:
    # Method 1: Brute force, time: O(3^n)
    # Method 2: DP with memoization, time: O(n^3)
    # Method 3: Greedy, time: O(n)

    # s = "(*))" -> valid!

    # wildcard can be replaced with 3 things: '(' or '' or ')'

    # if we try dp with memoization: state needed: dp(idx, leftOpenCount)

    # -> whenever a dp solution is possible, perhaps a greedy solution might be on the cards

    # -> analysing the problem further, we can keep track of leftOpenCount
    #     -> increment it if we see a '('
    #     -> decrement it if we see a ')'
    #     -> increment or decrement if we see a '*' -> need to keep 2 variables !
    #     => leftMin, leftMax: min no. of left paranthesis and max no. of left paranthesis possible!

    #     0123
    # trial: (*))

    # i = 3
    # leftMin = -1
    # leftMax = 0

    #         01234567
    # trial 2: ()(((*))

    # i = 5
    # leftMin = 0
    # leftMax = 2

    def checkValidString(self, s):
        leftMin, leftMax = 0, 0
        for c in s:
            if c == '(':
                leftMin += 1
                leftMax += 1
            elif c == ')':
                leftMin -= 1
                leftMax -= 1
            else:
                leftMin -= 1
                leftMax += 1
            if leftMax < 0:
                return False
            if leftMin < 0:
                leftMin = 0
        return leftMin == 0 or leftMax == 0
                
