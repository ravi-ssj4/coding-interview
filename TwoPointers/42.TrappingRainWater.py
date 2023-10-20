class Solution:
    '''
    method 1: using extra memory: 3 arrays (leftMax,  rightMax and min(leftMax, rightMax) arrays)
    logic: again, the minimum(max left, max right) heights is the bottleneck
    algo:
        1. create 3 arrays
        2. update leftMax -> scan left to right
        3. update rightMax -> scan right to left
        4. update min(leftMax, rightMax)
        5. calculate the amount of water that can be held at each position i
            * min(leftMax, rightMax)[i] - height[i]
            * if the above is -ve, then don't add it

    time: O(n)
    space: O(n)

    '''
    def trap(self, height: List[int]) -> int:
        leftMax = [0] * len(height)
        rightMax = [0] * len(height)
        minMaxLeftAndRight = [0] * len(height)
    
        leftMax[0] = height[0]
        rightMax[-1] = height[-1]
        
        for i in range(1, len(height)):
            leftMax[i] = max(leftMax[i - 1], height[i])
        for i in range(len(height) - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i])

        for i in range(len(height)):
            minMaxLeftAndRight[i] = min(leftMax[i], rightMax[i])
        
        areaSum = 0
        for i in range(len(height)):
            if minMaxLeftAndRight[i] - height[i] > 0:
                areaSum += minMaxLeftAndRight[i] - height[i]
        
        return areaSum

    '''
    method 2: 2 pointers(placed at extreme ends and then converge) to keep track of maxLeft and maxRight area

    algo: (complicated)
        1. initialize 2 pointers l and r at the ends of the height array
        2. out of the two pointers, whichever is pointing to smaller height, move that pointer forward
            (forward for l and backward for r)
        3. at a given position, calculate the amount of water to be held by:
            min(maxLeft, maxRight) - height[l or r], where l / r is decided based on which one was smaller
        4. keep on updating the areaSum at each position

    time: O(n)
    space: O(1)
    '''
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxLeft = height[l]
        maxRight = height[r]
        waterSum = 0
        while l < r:
            # calculate area depending upon the bottleneck:
            # note: here initially l = 0 and r = len(height) - 1
            # if we increment or decrement l / r first
            # then we are effectively calculating for the next position
            # hence, we can update maxLeft / maxRight in the end because currently
            # maxLeft and maxRight are correct for updated positions l and r respectively
            
            if maxLeft < maxRight:
                l += 1
                water = min(maxLeft, maxRight) - height[l]
                if water > 0:
                    waterSum += water
                maxLeft = max(maxLeft, height[l])
            else:
                r -= 1
                water = min(maxLeft, maxRight) - height[r]
                if water > 0:
                    waterSum += water
                maxRight = max(maxRight, height[r])
            
        return waterSum