class Solution:
    '''
    method: binary search modified(quite complicated) on the smaller array
    algo:
        1. initialize nums1 and nums2 as A and B
        2. make the smaller array as A (we are going to do binary search only in this)
        3. calculate total and half lengths of both arrays combined
        4. initialize l, r = 0, len(A) - 1
        5. while True (since we are guaranteed to find the median, can run an infinite loop)
            5.1. i = (l + r) // 2 (middle element in the array A)
            5.2. j = half - i - 2 (middle element in the array B)
            5.3. ALeft = A[i] if i >= 0 else float("-inf")
            5.4. ARight = A[i + 1] if (i + 1) < len(A) else float("inf")
            5.5. same thing for BLeft
            5.6. same thing for BRight
            5.7. if the partition is correct (ALeft <= BRight and BLeft <= ARight)
                    5.7.1. if odd:
                        return min(ARight, BRight)
                    5.7.2. if even:
                        return (max(ALeft, BLeft), min(ARight, BRight)) / 2 (decimal division) 
                 elif ALeft > BRight 
                    (meaning we have extra elements in left partition of A -> 
                    reduce the size of A's left partition) -> make r = i - 1
                 else 
                    (meaning BLeft > ARight -> have extra elements in left partition of B -> 
                    reduce these elements from left partition of B -> increase elements in 
                    left partition of A) -> make l = i + 1

    time: O(log(min(m, n)))
    space: O(1)

    '''
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A
        
        l, r = 0, len(A) - 1

        while True:
            # calculate markers for left partition of both arrays via indices i and j
            i = (l + r) // 2
            j = half - (i + 2) # for 0 idx in both arrays
            
            # calculate the 4 extreme values that matter
            ALeft = A[i] if i >= 0 else float("-inf")
            ARight = A[i + 1] if (i + 1) < len(A) else float("inf")
            BLeft = B[j] if j >= 0 else float("-inf")
            BRight = B[j + 1] if (j + 1) < len(B) else float("inf")

            # check for parition correctness
            if ALeft <= BRight and BLeft <= ARight:
                # calculate median in case of even length
                if total % 2 == 0:
                    return (max(ALeft, BLeft) + min(ARight, BRight)) / 2
                # calculate median in case of odd length
                return min(ARight, BRight)
            elif ALeft > BRight:
                r = i - 1
            else:
                l = i + 1