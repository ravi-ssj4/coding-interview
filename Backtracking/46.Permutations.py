class Solution:
    # def permute(self, nums: List[int]) -> List[List[int]]:
    #     permutations = []
    #     self.permuteUtil(nums, [], permutations)
    #     return permutations
    
    # def permuteUtil(self, array, permutation, permutations):
    #     if len(array) == 0:
    #         permutations.append(permutation)
    #     else:
    #         for i in range(len(array)):
    #             newArray = array[:i] + array[i+1:]
    #             newPermutation = permutation + [array[i]]
    #             self.permuteUtil(newArray, newPermutation, permutations)

    '''
    method 2: backtracking with minimal code
        # remove the first element in the current list
        # find perms of remaining (perms)
        # include the removed element to all the permutations of perms
        # add the removed element back to the nums array
        # add these newly formed permutations to the result
    '''
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        # base case
        if len(nums) == 1:
            return [[nums[0]]]

        for i in range(len(nums)):
            # remove
            removed = nums.pop(0)
            
            perms = self.permute(nums)
            for perm in perms:
                perm.append(removed)
            
            # add back
            nums.append(removed)
            
            result.extend(perms)
        
        return result


            