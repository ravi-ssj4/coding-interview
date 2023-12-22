class Solution:
    '''
    method 1: O(n^n) -> Brute force: checking all possible solutions
    method 2: O(n^2) -> DP: using memoization
    method 3: O(n) -> setting a goal post and shrinking it while going from right to left
    '''
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
            
        return goal == 0