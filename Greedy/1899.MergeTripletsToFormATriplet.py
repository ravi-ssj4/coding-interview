class Solution:
    '''
    method: no complex data structure! Just greedy approach + smart counting via set()
    approach:
        1. first, eliminate all the triplets in the triplet list 
            that have even one value > target triplet's value at that idx
        2. second, if we have a value for each of the values of target idx in any
            of the triplets combined, then we have a solution
    time: O(n)
    space: O(n)
    '''
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        goodIndices = set()

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            for i, v in enumerate(t):
                if v == target[i]:
                    goodIndices.add(i)
        # print(goodIndices)
        return len(goodIndices) == 3