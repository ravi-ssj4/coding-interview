class Solution:
    '''
    method 1: O(n^3): check for all possible subarrays
    algo:
        for i in range(n-1) - (to keep track of beginning of subarray)
            for j in range(n) - (to keep track of end of subarray)
                for k in range(i, j + 1) - (for calculating sum)
                
    method 2: O(n^2): 2 for loops + prefix Sum per subarray
    algo:
        for i in range(n-1) - (to keep track of beginning of subarray)
            curSum = 0
            for j in range(n) - (to keep track of end of subarray)
                curSum += nums[j]


    method 3: if curSum becomes -ve, make it 0 and restart (Kadane's algo)
    '''
    def maxSubArray(self, nums: List[int]) -> int:
        
        curSum = 0
        maxSub = nums[0]

        for num in nums:
            if curSum < 0:
                curSum = 0
            curSum += num
            maxSub = max(maxSub, curSum)
        
        return maxSub