class Solution:
    '''
    method: binary search modified(very important to visualize on paper this one)
    algo:
        1. initialize l, r = 0, len(nums) - 1
        2. iterate until l <= r
            2.1. find middle
            2.2. if middle == target: return middle
            2.3. if middle is in the left sorted portion (nums[l] <= nums[mid])
                2.3.1. if target > nums[mid] or target < nums[l]:
                            search in the right (l = mid + 1)
                        else (target is in between nums[l] and nums[mid])
                            search in the left ( r = mid - 1)
            2.4. if middle is in the right sorted portion (nums[l] > nums[mid])
                2.4.1. if target < nums[mid] or target nums[r]:
                            search in the left (r = mid - 1)
                        else:
                            search in the right (l = mid + 1)
            2.5. return -1

    example: [4, 5, 6, 7, 0, 1, 2], target = 0
    iteration 1: 
        * middle = 2, nums[middle] = 6 (in the left sorted portion)
        * target < nums[l] (leftmost element ie. 4), so search in the right, l = mid + 1
    iteration 2: [x, x, x, x, 0, 1, 2]
        * middle = 5, nums[middle] = 1 (in the left sorted portion)
        * target >= nums[l] (else case, ie. we search in the left portion, ie. r = mid - 1)
    iteration 3: [x, x, x, x, 0, x, x]
        * middle = 4, nums[middle] = 0 == target

    time: O(logn)
    space: O(1)
    '''
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
    
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            
            if nums[l] <= nums[mid]:
                # left sorted portion
                if target > nums[mid] or target < nums[l]:
                    # search right
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                # right sorted portion
                if target < nums[mid] or target > nums[r]:
                    # search in the left
                    r = mid - 1
                else:
                    l = mid + 1
        return -1