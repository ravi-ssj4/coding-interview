class Solution:
    '''
    method : backtracking + sorting (duplicate avoidance)
    algo:

    time: O(n.logn) + O(n.2^n) = O(n.2^n)
    space: O(n)
    '''
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []

        nums.sort() # to keep duplicates together

        def backtrack(i, subset):
            # base case
            if i == len(nums):
                res.append(subset[::])
                return
            
            # get all subsets after including nums[i]
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop() # bringing back to original state

            # get all subsets if nums[i] is never included
            # to make sure of this, skip all duplicates of nums[i]
            # nums = [1, 2, 2, 3], i = 1
            while (i + 1) < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            # i = 2 at this point
            backtrack(i + 1, subset) # backtrack called with i = 3(all 2s not considered)

        backtrack(0, [])
    
        return res