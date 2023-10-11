class Solution:
    '''
    method 1: binary search modified to find the pivot point -> ans = next element of pivot

    issue: lot of edge cases

    time: O(logn)
    space: O(1)

    method 2: binary search modified more smartly (since rotating leaves the array into 2 sorted arrays)
                * check if middle is part of the left sorted array or right sorted array
                * if its part of left sorted array, search on the right (left elements are eliminated)
                * if its part of right sorted array, search on its left(right elements eliminated)
    algo:
        1. initialize l, r = 0, len(nums) - 1, res = nums[0]
        2. while l <= r:
            2.1. if the array from l to r is totally sorted,
                update res = min(res, nums[l])
            2.2. mid = (l + r) // 2
            2.3. again update res = min(res, nums[mid])
            2.4. if nums[mid] >= nums[l] (means middle element is part of the left sorted array)
                    search on the right
                else
                    search on the left
        3. return res
                
    '''
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        res = nums[0]
    
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            mid = (l + r) // 2

            res = min(res, nums[mid])
            
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
            
        return res
            















