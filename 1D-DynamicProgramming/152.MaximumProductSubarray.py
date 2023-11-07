class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax, curMin = 1, 1
        res = max(nums) # in case num = [-1], res = -1 and not 0

        for n in nums:
            if n == 0:
                curMax, curMin = 1, 1
                continue
            
            temp = n * curMax
            curMax = max(n * curMax, n * curMin, n) # [-1, 8], curMax = curMin = -1 -> -1 * 8 = -8, hence just take n ie. 8
            curMin = min(temp, n * curMin, n) # [-1, -8], curMax = curMin = -1 -> -1 * -8 = 8, hence just take n ie. -8
            res = max(curMax, res)

        return res