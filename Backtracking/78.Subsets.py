class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        # i = idx in [1, 2, 3]
        def dfs(i):
            # base case
            if i >= len(nums):
                # deep copy is mandatory since subset list is being altered all the time
                res.append(subset.copy()) 
                return

            # left side of the decision tree (including the element)
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop() # bringing back to original state

            # right side of the decision Tree (not including the element)
            dfs(i + 1)

        dfs(0)
        return res