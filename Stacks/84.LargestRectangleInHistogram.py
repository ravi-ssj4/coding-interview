class Solution:
    '''
    method : stack that stores a pair of (startIdx, height). why?
                -> because we need to keep track of startIdx 
                    for a particular height as well along with the height
    problem scoping:
        * the constant or reference point we can take as the height
            ie. for height h, what's the max area it can cover
        * the rectangle at a particular height h can extend either way right or left
        * case 1: increasing heights -> 1,2,3,4,... (all can keep extending until they see a smaller value)
        * case 2: encountering a smaller value -> 1,2,3,4,2 .. (heights 4 and 3 cannot extend now)
                    -> their max areas need to be calculated and they can be removed
            lightbulb moment : we can use a stack for this!
                    -> but h = 2's rectangle can be extended backwards ( need to keep track of this )
            lightbulb moment : can keep 2 things (starting index, height) in the stack
    
    algo:
        1. initialize an empty stack
        2. enumerate over i, h for all values of heights
            2.1. start = i (for now until start needs to go backwards)
            2.2. while stack and height of bar at top of stack > current height
                2.2.1. index, height = stack.pop()
                2.2.2. update maxArea
                2.2.3. update start = index (the current rectangle goes one step backwards)
            2.3. stack.append((start, h))
        3. iterate over the stack
            3.1 update maxArea
        4. return maxArea

    time: O(n)
    space: O(n)

    dry run:
    heights = [2,1,5,6,2,3]
    stack = []
    maxArea = 
    
    '''
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            stack.append((start, h))
        
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
    
        return maxArea