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


'''
Test Cases
Single-digit input:
Input: "2"
Expected Output: ["a", "b", "c"]

Double-digit input with different numbers:
Input: "23"
Expected Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

Triple-digit input:
Input: "234"
Expected Output: Any combination of letters corresponding to the digits "234", such as ["adg", "adh", "adi", "aeg", ...]

Input with a digit that maps to 4 letters:
Input: "7"
Expected Output: ["p", "q", "r", "s"]

Input with repeating digits:
Input: "22"
Expected Output: ["aa", "ab", "ac", "ba", "bb", "bc", "ca", "cb", "cc"]

Input with no valid digits (1 and 0 do not map to any letters):
Input: "1"
Expected Output: []

Long input string:
Input: "23456789"
Expected Output: A list of all combinations for the corresponding letters.

Input with digits that are not between 2-9:
Input: "10"
Expected Output: [], since "1" and "0" do not map to any letters.

Non-digit input (edge case, if not already handled by the function):
Input: "2a"
Expected Output: This depends on how the function handles invalid input. It could return an empty list, throw an error, or skip the non-digit character.

Empty string input:
Input: ""
Expected Output: [], since there are no digits to map to letters.
'''