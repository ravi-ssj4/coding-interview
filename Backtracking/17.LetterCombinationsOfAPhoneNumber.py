class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        # Strings are mutable, hence a new string is created if we try to mutate it
        # wasting space

        # technique 1: using a list of chars instead of string directly
        # def backtrack(i, curStr):
        #     # base case
        #     if len(curStr) == len(digits):
        #         res.append("".join(curStr))
        #         return
            
        #     for c in digitToChar[digits[i]]:
        #         curStr.append(c)
        #         backtrack(i + 1, curStr)
        #         curStr.pop()

        # technique 2: actually appending the char to the string and then removing it
        # wasteful!
        # def backtrack(i, curStr):
        #     # base case
        #     if len(curStr) == len(digits):
        #         res.append(curStr)
        #         return
            
        #     for c in digitToChar[digits[i]]:
        #         curStr = curStr + c
        #         backtrack(i + 1, curStr)
        #         curStr = curStr[:-1]
        
        # technique 3: best technique as we are not touching(no need to append and then remove) 
                     # the string in the current function
                     # we are just passing a new string to backtracking function called
        def backtrack(i, curStr):
            # base case
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            
            for c in digitToChar[digits[i]]:
                backtrack(i + 1, curStr + c)
            
        if digits:
            backtrack(0, "")
        
        return res