class Solution:
    # method 1
    # def isValid(self, s: str) -> bool:
    #     stack = []
    #     for char in s:
    #         if char in "({[":
    #             stack.append(char)
    #         else:
    #             if not stack or \
    #                 (char == ')' and stack[-1] != '(') or \
    #                 (char == '}' and stack[-1] != '{') or \
    #                 (char == ']' and stack[-1] != '['):
    #                 return False
    #             stack.pop()
    #     return not stack

    '''
    method 2: use a stack that contains open brackets
    algo:
        1. initialize a stack
        2. create a closeToOpen hashMap -> {")": "(", "}": "{", "]": "["}
        3. iterate over all chars of s
        4. if char in closeToOpen,
                check if stack is not empty and its value matches the stack top, 
                if so, match it (means pop one element from the stack since this 
                    open bracket is now matched and we need to continue testing for previous open brackets)
                else 
                    return False
        5. stack.append(char) # we are sure that we can only get open brackets if we are here

    time: O(n)
    space: O(n)
    '''
    def isValid(self, s):
        stack = []
        openToClose = {")": "(", "}": "{", "]": "["}
        for c in s:
            if c in openToClose:
                if stack and stack[-1] == openToClose[c]:
                    stack.pop()
                else: # (either stack is empty or the brackets did not match)
                    return False
            else:
                stack.append(c)
        return True if len(stack) == 0 else False