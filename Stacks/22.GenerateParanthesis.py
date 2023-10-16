class Solution:
    # # Method 1: brute force
    # # time : O(2^2n * n)
    # # space : O(4^n / n * sqrt(n))
    # def isValid(self, string):
    #     leftCount = 0
    #     for char in string:
    #         if char == "(":
    #             leftCount += 1
    #         else:
    #             leftCount -= 1
    #         if leftCount < 0:
    #             return False
    #     return leftCount == 0

    # def generateParenthesis(self, n: int) -> List[str]:
    #     queue = [""]
    #     result = []
    #     while len(queue) > 0:
    #         curStr = queue.pop(0)
    #         if len(curStr) == 2 * n:
    #             if self.isValid(curStr):
    #                 result.append(curStr)
    #             continue
    #         queue.append(curStr + "(")
    #         queue.append(curStr + ")")

    #     return result

    # Method 2: Backtracking
    # time = 
    # space = 

    # def generateParenthesis(self, n: int) -> List[str]:
    #     result = []
    #     self.genParUtil(n, result, [], 0, 0)
    #     return result

    # def genParUtil(self, n, result, currString, leftCount, rightCount):
    #     if len(currString) == 2 * n:
    #         result.append("".join(currString))
    #         return
        
    #     if leftCount < n:
    #         currString.append("(")
    #         self.genParUtil(n, result, currString, leftCount + 1, rightCount)
    #         currString.pop()
        
    #     if leftCount > rightCount:
    #         currString.append(")")
    #         self.genParUtil(n, result, currString, leftCount, rightCount + 1)
    #         currString.pop()

    '''
    method: backtracking (simpler code)
    logic: 1. only add "(" if openN < n
            2. only add ")" if closedN < openN
            3. only add to result if openN == closedN == n
    example: n = 2 -> do it on paper

    time: O(4^n / sqrt(n))
    space: O(n) for the stack to keep running paranthesis list

    '''        
    def generateParenthesis(self, n: int) -> List[str]:

        res = []
        stack = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()
        
        backtrack(0, 0)

        return res


