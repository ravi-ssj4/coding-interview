class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1: # in case of odd sum, this cannot happen
            return False

        target = sum(nums) // 2

        dp = set()
        dp.add(0) # base case

        for i in range(len(nums) - 1, -1, -1):
            tempDP = set()
            for t in dp:
                if t + nums[i] == target:
                    return True
                tempDP.add(t + nums[i]) # need to add new sums by adding previous sums with the current num
                tempDP.add(t) # need to preserve previous sums
            dp = tempDP
        return True if target in dp else False