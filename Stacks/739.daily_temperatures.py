class Solution:
    '''
    method 1: preferred over method 2 ! stack(containing indices) -> values (monotonic decreasing) traverse Left to Right
    algo:
        1. initialize empty stack
        2. initialize result list with 0s
        3. iterate over all temperatures
        4. while current temp > temp at top of stack:
            pop an element (index) from the stack
            res.append(current index - index)
        5. push the current temp's index onto the stack
        6. when out of the loop, return res
    
    time: O(n)
    space: O(n)

    dry run:
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    output = [0, 0, 0, 0, 0, 0, 0, 0]
    stack = [
    currentIdx = 0
    currentIdx - stackTop = 
    '''
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # will contain indices of temperatures
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                stackTopIdx = stack.pop()
                res[stackTopIdx] = (i - stackTopIdx)
            stack.append(i)
        return res


    '''
    method 2: stack (monotonic increasing) traverse Right to Left
    algo:
        1. initialize an empty stack
        2. initialize result list with 0s
        3. iterate over temperatures array from right to left
        3. if current temp < stack top's temp:
            res[curernt idx] = stacktop idx - currentidx
            continue
        4. while current temperature >= temperature on top of the stack
            stack.pop()
        5. stack.append(current idx)
        6. return res

    dry run:
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    output = [0, 0, 4, 2, 1, 1, 0, 0]
    stack = [6 2 1
    currentIdx = 0
    currentIdx - stackTop = 

    '''
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        
        for currentIdx in range(len(temperatures) - 1, -1, -1):
            # if stack and temperatures[currentIdx] < temperatures[stack[-1]]:
            #     res[currentIdx] = stack[-1] - currentIdx
            #     stack.append(currentIdx)
            #     continue
            # while stack and temperatures[currentIdx] >= temperatures[stack[-1]]:
            #     stack.pop()
            # if stack:
            #     res[currentIdx] = stack[-1] - currentIdx
            # stack.append(currentIdx)

            # optimized code (memorize!)
            while stack:
                if temperatures[currentIdx] >= temperatures[stack[-1]]:
                    stack.pop()
                else:
                    res[currentIdx] = stack[-1] - currentIdx
                    break
            stack.append(currentIdx)
        return res








