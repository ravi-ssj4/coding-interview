class Solution:
    '''
    method 1: brute force: O(max(piles) * len(p))
    algo:
        1. from k = 1 to max(piles) check for every k if koko is able to eat in <= h hours or not

    method 2: binary search for correct value of k where k (1, 2, 3, .. max(piles)) for which hours <= h(given)
    algo:
        1. initialize left, right = 1, max(piles) and output = float("inf")
        2. while left <= right
            2.1. k = (left + right) // 2
            2.2. hours = 0
            2.3. iterate over all values of piles
                2.3.1. hours += math.ceil(piles[i] / k)
            2.4. if hours <= k:
                    output = min(output, k)
                    r = k - 1
                else
                    l = k + 1
        3. return output
    '''
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles) # -> O(n)

        output = float("inf")

        while l <= r:
            k = (l + r) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)
            
            if hours <= h:
                output = min(output, k)
                r = k - 1
            else:
                l = k + 1
        return output