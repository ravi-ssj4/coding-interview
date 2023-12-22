class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.robHelper(nums[1:]), self.robHelper(nums[:-1]))
        
    def robHelper(self, nums):
        rob1, rob2 = 0, 0
        for n in nums:
            rob3 = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = rob3
        return rob2